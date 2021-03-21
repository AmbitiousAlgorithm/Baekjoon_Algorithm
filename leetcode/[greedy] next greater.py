# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         answer = []
#         for num in nums1:
#             idx = nums2.index(num)
#             # 조건일 때
#             if idx != len(nums2)-1:
#                 if nums2[idx+1] > num:
#                     answer.append(nums2[idx+1])
#                 elif num > nums2[idx+1]:
#                     answer.append(-1)
#             elif idx == len(nums2)-1:
#                 answer.append(-1)
#         return answer