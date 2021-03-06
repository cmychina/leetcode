class Solution:
    def search(self, nums, target):
        def find_rotateindex(l, r):
            if (nums[l] < nums[r]):
                return 0
            while (l <= r):
                rotate = (l + r) // 2
                if (nums[rotate] < nums[rotate - 1]):
                    return rotate

                if (nums[rotate] > nums[r]):
                    l = rotate + 1
                else:
                    r = rotate - 1

        # print(find_rotateindex(0,len(nums)-1))
        def find(l, r):
            while (l <= r):
                mid = (l + r) // 2
                if (nums[mid] == target):
                    return mid
                if (nums[mid] > target):
                    r = mid - 1
                else:
                    l = mid + 1
            return -1

        n = len(nums)
        if (n == 0):
            return -1
        if (n == 1):
            return 0 if (nums[0] == target) else -1
        rotateindex = find_rotateindex(0, n - 1)
        if (rotateindex == 0):
            return find(0, n - 1)

        if (target >= nums[0]):
            return find(0, rotateindex)
        else:
            return find(rotateindex, n - 1)

    class Solution:
        def search(self, nums, target):
            if len(nums) == 0:
                return -1
            left, right = 0, len(nums) - 1
            while left + 1 < right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                if nums[left] < nums[mid]:
                    if nums[left] <= target and target <= nums[mid]:
                        right = mid
                    else:
                        left = mid
                else:
                    if nums[mid] <= target and target <= nums[right]:
                        left = mid
                    else:
                        right = mid
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            return -1

