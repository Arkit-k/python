class Solution(object):
    def divideArray(self, nums):
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for count in freq.values():
            if count % 2 != 0:
                return False

        return True

        