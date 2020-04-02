# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。 
# 
#  你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。 
# 
#  示例: 
# 
#  给定 nums = [2, 7, 11, 15], target = 9
# 
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#  
#  Related Topics 数组 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 哈希表 (空间换时间) O(n)
        # 解答成功: 执行耗时:16 ms,击败了98.68% 的Python用户 内存消耗:13.6 MB,击败了5.07% 的Python用户
        mp = {}
        for i, v in enumerate(nums):
            if target - v in mp:
                return [mp[target-v], i]
            mp[v] = i
        return -1

        # # 暴力，两层遍历 O(n^2）
        # # 解答成功: 执行耗时:2976 ms,击败了31.80% 的Python用户 内存消耗:13.5 MB,击败了5.45% 的Python用户
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return -1

# leetcode submit region end(Prohibit modification and deletion)

res = Solution().twoSum([2, 7, 11, 15], 13)
print(res)
