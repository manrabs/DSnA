# MemTables: the in-memory sorted write buffer of an LSM-tree storage engine
# (LevelDB, RocksDB, Cassandra). Writes land here; when it fills up it gets
# flushed to disk as an SSTable -- a file of key/value pairs in sorted order.
#
# Requirements: O(log n) insert, O(log n) lookup, and CHEAP ORDERED ITERATION
# (so the flush doesn't have to sort). That last one rules out a hash map.
#
# Three ways to do it: skip list, red-black tree, AVL tree.

import random

# ---------------------------------------------------------------------------
# 1. SKIP LIST -- what LevelDB / RocksDB / Redis (sorted sets) actually use.
#
# A sorted linked list with randomized "express lanes" stacked on top. Each
# node gets a random height; taller nodes appear in more lanes, so search can
# skip over big chunks instead of walking one node at a time.
#
#   L2: apple ---------------------------> fig
#   L1: apple --------> cherry ----------> fig
#   L0: apple -> banana -> cherry -> date -> fig
#
# insert/search/delete: O(log n) EXPECTED (probabilistic, not guaranteed)
# space: O(n) expected -- avg 1/(1-p) = 2 pointers per node at p=0.5
#
# Why engines pick it over a balanced tree: no rotations. An insert only
# rewrites forward pointers along one path, which makes a lock-free concurrent
# version (many writers + non-blocking readers) far easier than rebalancing.
# ---------------------------------------------------------------------------
class SkipNode:
    def __init__(self, key, val, level):
        self.key = key
        self.val = val
        # forward[i] = next node at level i. len == level + 1 (this node's height)
        self.forward = [None] * (level + 1)

    def __init__(self, key, val, level):
        self.key = key
        self.val = val
        self.forward = [None] * (level + 1)

class SkipList:
    def __init__(self, max_level=16, p=0.5):
        self.max_level = max_level   # ceiling on tower height
        self.p = p                   # promotion probability per coin flip
        self.level = 0               # highest level currently in use
        # sentinel head: full height, sorts before every real key
        self.head = SkipNode(None, None, max_level)

    # coin flip until it fails -- p=0.5 means ~1/2 of nodes reach L1, 1/4 reach L2...
    def _random_level(self):
        lvl = 0
        while random.random() < self.p and lvl < self.max_level:
            lvl += 1
        return lvl

    # walk down from the top: go right while next key < target, then drop a level.
    # update[i] = the node we dropped down FROM at level i (i.e. the node whose
    # forward pointer at level i would need rewiring for an insert/delete)
    def _find_path(self, key):
        update = [self.head] * (self.max_level + 1)
        node = self.head
        for i in range(self.level, -1, -1):
            while node.forward[i] and node.forward[i].key < key:
                node = node.forward[i]
            update[i] = node
        return update, node.forward[0]   # also return the candidate match at L0

    def insert(self, key, val):
        update, candidate = self._find_path(key)

        # memtable semantics: a repeat write overwrites in place
        if candidate and candidate.key == key:
            candidate.val = val
            return

        lvl = self._random_level()
        if lvl > self.level:
            # new tallest tower -- lanes above the old top start at the head
            for i in range(self.level + 1, lvl + 1):
                update[i] = self.head
            self.level = lvl

        new_node = SkipNode(key, val, lvl)
        # splice in at every level of its tower
        for i in range(lvl + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def search(self, key):
        _, candidate = self._find_path(key)
        return candidate.val if candidate and candidate.key == key else None

    def delete(self, key):
        update, node = self._find_path(key)
        if not node or node.key != key:
            return False

        for i in range(self.level + 1):
            if update[i].forward[i] is not node:
                break    # node's tower doesn't reach this level, and won't reach higher
            update[i].forward[i] = node.forward[i]

        # drop any now-empty top lanes
        while self.level > 0 and not self.head.forward[self.level]:
            self.level -= 1
        return True

    # the flush: level 0 IS the sorted list, so this is a plain O(n) walk
    def in_order(self):
        out = []
        node = self.head.forward[0]
        while node:
            out.append((node.key, node.val))
            node = node.forward[0]
        return out

    # teaching aid: print the express lanes so you can see the towers
    def show_levels(self):
        base = [k for k, _ in self.in_order()]
        width = max((len(str(k)) for k in base), default=1) + 2
        for lvl in range(self.level, -1, -1):
            present = set()
            node = self.head.forward[lvl]
            while node:
                present.add(node.key)
                node = node.forward[lvl]
            row = "".join(
                str(k).ljust(width) if k in present else "-" * (width - 1) + " "
                for k in base
            )
            print(f"  L{lvl}: {row}")


if __name__ == "__main__":
    random.seed(7)   # deterministic tower heights so the demo is reproducible

    writes = [("banana", 1), ("apple", 2), ("cherry", 3), ("date", 4),
              ("fig", 5), ("elderberry", 6), ("grape", 7)]

    print("=== SKIP LIST ===")
    sl = SkipList()
    for k, v in writes:
        sl.insert(k, v)

    sl.show_levels()
    print("  get('cherry')  ->", sl.search("cherry"))
    print("  get('kiwi')    ->", sl.search("kiwi"))

    sl.insert("cherry", 99)          # overwrite, not a duplicate
    print("  after re-put cherry=99 ->", sl.search("cherry"))

    sl.delete("date")
    print("  flush (sorted) ->", sl.in_order())
