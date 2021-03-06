"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。
"""
class Solution:
    def subsets(self, nums):
        res=[]
        n=len(nums)
        def backtrack(i,tmp):
            res.append(tmp)
            for j in range(i,n):
                backtrack(j+1,tmp+[nums[j]])
        backtrack(0,[])
        return res

if __name__ == "__main__":
    s = Solution()
    nums=[1,2,3]
    print(s.subsets(nums))
