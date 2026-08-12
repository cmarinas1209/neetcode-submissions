class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} #initalize hashmap
        for i, n in enumerate(nums): #iterate through nums array, with index and value
            diff = target - nums[i] #value needed to add to target
            if diff in hashmap:
                if i<hashmap[diff]:
                    return [i, hashmap[diff]]
                else:
                    return [hashmap[diff], i]
            hashmap[n] = i #store value and its corresponding index
        return