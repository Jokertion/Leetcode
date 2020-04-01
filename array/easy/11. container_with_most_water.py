#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: jokertion
@file: container_with_most_water.py
@time: 2020/4/1 23:56
@desc: 
"""

# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i,
# ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

#  说明：你不能倾斜容器，且 n 的值至少为 2。
#  图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
#  示例：

#  输入：[1,8,6,2,5,4,8,3,7]
# 输出：49
#  Related Topics 数组 双指针


class Solution(object):
    def maxArea(self, lst):
        """
        :type lst: List[int]
        :rtype: int
        """
        # 左右两个指针i,j, 同时向中间收敛 O(n)
        # 解答成功: 执行耗时:40 ms,击败了81.58% 的Python用户 内存消耗:13.6 MB,击败了5.80% 的Python用户
        max_area, i, j = 0, 0, len(lst) - 1
        while i < j:
            max_area = max(max_area, min(lst[i], lst[j]) * (j - i))
            if lst[i] < lst[j]:
                i += 1
            else:
                j -= 1
        return max_area

        # # 暴力穷举 O(n^2)
        # # 解答成功: 执行耗时:80 ms,击败了53.71% 的Python用户 内存消耗:13.5 MB,击败了5.80% 的Python用户
        # max_area = 0
        # for i in range(0, len(lst)):
        #     for j in range(i+1, len(lst)):
        #         area = min(lst[i], lst[j]) * (j - i)
        #         max_area = max(area, max_area)
        # return max_area


res = Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(res)
