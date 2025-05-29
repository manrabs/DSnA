# every low value must be at the left of low pointer not including value at the low pointer,
# every high value must be on the right of the high pointer(not including the high value)
# sorting is complete when mid pointer goes past the high pointer

class Solution:
    def swap(self, vals: list, pos1: int, pos2: int):
        temp = vals[pos1]
        vals[pos1] = vals[pos2]
        vals [pos2] = temp
    
    def arrange(self, vals: list):
        low, mid, high = 0, 0, len(vals) - 1
        
        while (mid <= high):
            match (vals[mid]):
                case 0:
                    self.swap(vals, low, mid)
                    mid += 1
                    low += 1
                    break
                case 1:
                    mid += 1
                    break
                case 2: 
                    self.swap(vals, mid, high)
                    high -= 1
                    break
        return vals
    

if __name__ == '__main__':
    sol = Solution()
    vals = [2,0,2,1,1,0]
    print(sol.arrange(vals))


