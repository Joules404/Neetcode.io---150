from collections import defaultdict
#Top K Elements in List
'''
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Constraints:

1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.


'''

ol = [1,2,2,3,3,3]
ul = [2,1,2,3,3,3]
ol1 = [5,5,5,6,6,7]

def topKFrequent(nums, k):
        cnt = {}
        lst = [[] for i in range(len(nums)+1)]
        res = []
        for num in nums:
            cnt[num] = 1 + cnt.get(num,0)
        for i,c in cnt.items():
            lst[c].append(i)

        for i in range(len(lst)-1,0,-1):
            for n in lst[i]:
                res.append(n)
                if len(res) == k:
                    return res
topKFrequent(ol1,2)


