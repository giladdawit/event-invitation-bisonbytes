class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        print(f"nums: {nums}, target: {target}")
        for i in range(len(nums)):
            difference = target - nums[i]
            print(f"i: {i}, nums[i]: {nums[i]}, difference: {difference}, hashmap: {hashmap}")
        if difference in hashmap:
            print(f"Found: difference {difference} at index {hashmap[difference]}")
            return [hashmap[difference],[i]]
        hashmap[i] = i
        print(f"Updated hashmap: {hashmap}")


          