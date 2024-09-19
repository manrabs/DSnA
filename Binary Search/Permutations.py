# given two arrays that are sorted and distinct, find the number of commom elements across the two
def permutations(chars1: list, chars2: list):
    count = 0
    b_start = 0
    b_end = len(chars2) - 1
    a_len = len(chars1)
    for i in range(a_len) :
        while b_start <= b_end:
            mid = b_start + (b_end - b_start) // 2 
            if chars2[mid] == chars1[i]:
                count += 1
            elif chars1[i] < chars2[mid]:
                b_end = mid - 1
            elif chars1[i] > chars2[mid]:
                b_start = mid + 1