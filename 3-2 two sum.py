nums = [2,7,11,15]
target = 9

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            d=[i,j]
print(d)

nums = [3,2,4]
target = 6

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            d=[i,j]
print(d)

#參考解法 #01
nums = [2,7,11,15], target = 9

def twoSum(nums, target):
    n = len(nums)
    # 遍歷所有可能的數字組合
    for i in range(n):
        for j in range(i+1, n):
            # 如果找到符合條件的組合，返回它們的 index
            if nums[i] + nums[j] == target:
                return [i, j]
    # 如果找不到符合條件的組合，返回空列表
    return []

d = twoSum(nums, target)
print(d) # [0,1]

#參考解法 #02
nums = [2,7,11,15], target = 9

def twoSum(nums, target):
    # 創建一個字典用於存儲已經遍歷過的數字和它們的 index
    visited = {}
    # 遍歷整個列表
    for i, num in enumerate(nums):
        # 計算與目標值的差值
        diff = target - num
        # 如果差值已經存在於 visited 中，返回差值的 index 和當前的 index
        if diff in visited:
            return [visited[diff], i]
        # 將當前數字和 index 存入 visited 中
        visited[num] = i #key=數列，value=第幾個數
    # 如果找不到符合條件的組合，返回空列表
    return []

d = twoSum(nums, target)
print(d) # [0,1] 