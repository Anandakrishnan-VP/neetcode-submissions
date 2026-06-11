class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for n in range(len(numbers)):
            if target - numbers[n] in numbers:
                t = numbers.index(target-numbers[n]) + 1
                i = n + 1

                
                return list([i,t])
            
                