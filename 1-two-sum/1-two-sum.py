class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first_index = None
        second_index = None
        for count,number in enumerate(nums):
            rest = target - number
            print(rest)
            if rest in nums[count+1:]:
                print("Heyo")
                second_index=nums[count+1:].index(rest) + count +1
                if second_index>0:
                    first_index = count
                    return [first_index,second_index]