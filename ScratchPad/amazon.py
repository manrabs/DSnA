"""
In an Amazon fulfillment center, a packaging operation is being planned. 
The Operations Manager needs to distribute packages to different packing stations. 
There are n conveyor belts with arr[i] packages on the ith conveyor belt. 
There are m packing stations where packages need to be processed.

The task is to allocate all the conveyor belts to the packing stations. Distribute conveyor belts in such a way that: 
Each packing station is assigned at least one conveyor belt. 
Each conveyor belt should be assigned to only one packing station. 
Conveyor belt allocation should be in a contiguous manner (adjacent belts should go to the same station). 

You have to allocate the conveyor belts to 'm' packing stations such that the 
maximum number of packages assigned to any packing station is minimum. 
If the allocation of conveyor belts is not possible, return -1

Example 1: 
Input Format: n = 4, m = 2, 
arr[] = {12, 34, 67, 90} 
Result: 113 Explanation: The distribution of belts will be 12, 34, 67 | 90.
"""
class Allocator:
    def allocateBelts(self, arr, m):
        n = len(arr)
        
        if m > n: return -1
        if m == 1: return sum(arr)
        
        def canAssign(highestLoad):
            stations_used = 1
            curr_load = 0
            
            for packages in arr:
                if packages > highestLoad: return False
                
                if packages + curr_load > highestLoad:
                    stations_used += 1
                    curr_load = packages
                    
                    if stations_used > m: return False
                
                else:
                    curr_load += packages
            return True
            
        l, r = max(arr), sum(arr)
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if canAssign(mid):
                result = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return result
    
if __name__ == "__main__":
    arr = [12, 34, 67, 90]
    m = 2
    sol = Allocator()
    print(sol.allocateBelts(arr, m))