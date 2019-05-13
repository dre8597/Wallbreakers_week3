"""
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ...
, (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].

"""


# TODO this program asks for the max value but only accepts the min sums
#  and on some test cases requries the max at random
def arrayPairSum(nums) -> int:
    if len(nums) > 2:
        half = len(nums) // 2
        nums.sort()
        return min(nums[half:]) + min(nums[:half])
    else:
        return max(nums)
