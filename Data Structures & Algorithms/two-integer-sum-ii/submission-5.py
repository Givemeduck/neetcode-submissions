class Solution:   #two pointer
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(numbers) - 1
        summ = 0

        while l < r:
            summ = numbers[r] + numbers[l]

            if target == summ:
                return [l + 1, r + 1]
            
            if target < summ:
                r -= 1

            if target > summ:
                l += 1
