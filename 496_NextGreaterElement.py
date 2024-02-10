class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2:list[int]) -> list[int]:
# Brute force:
# Defind the max_num2 list to storage the next max value
# form the specific element.
# Use a nums_dic to storage the index's element of nums1 in num2
# Interate through the element in nums1 and check the value 
# of max list. If there no greater just return -1 else return the max
        def brure_force(self, nums1: list[int], nums2:list[int]) -> list[int]:
            def max_count(nums: list[int]):
                value = [0] * len(nums)
                for i in range (0, len(nums)-1):
                    for j in range(i+1, len(nums)):
                        if nums[j] > nums[i]:
                            value[i] = nums[j]
                            break
                return value    
            nums_dic = {}
            max_nums2 = [0] * len(nums2)
            result = [0] * len(nums1)
            for i in range(0, len(nums2)):
                nums_dic[nums2[i]] = i
            max_nums2 = max_count(nums2)
            print(max_nums2, nums_dic)

            for index in range(0, len(nums1)):
                if max_nums2[nums_dic[nums1[index]]] == 0:
                    result[index] = -1
                else:
                    result[index] = max_nums2[nums_dic[nums1[index]]]
            return result
# Using stack:
# In this method we use a stack to storage the element need to find the
# next greater number. If we found it, add it to the dictionary and after 
# that remove it from the stack. 
        stack = [nums2[0]]
        result = []
        nums_dic = {}
        for i in range(1,len(nums2)):
            while stack and nums2[i] > stack[-1]:     # if stack not empty, compare it's last element with the nums2[i]
                nums_dic[stack[-1]] = nums2[i]        # if new element is greater than stack's top ele, add to the dic
                stack.pop()                           # sice we found the pair for the element in stack, remove it in stack.
            stack.append(nums2[i])                    
        for i in stack:
            nums_dic.update({i:-1})                   # if there are elements in stack mean, not have greater number, return -1
        for i in nums1:
            result.append(nums_dic[i])
        return result

nums1 = [4,1,2]
nums2 = [1,3,4,2]
s = Solution()
print(s.nextGreaterElement(nums1,nums2))