#參考同學解答＋gpt修改
a, b = int(input()), int(input())  # 輸入範圍的起始值和結束值 

s = []  # 用於儲存自除數的列表

# 尋找自除數
for i in range(a, b):
    remainder = 0
    zero = 0 
    for num in str(i):
        if int(num) == 0:
            zero += 1  
            continue   # 如果拆出個別數字為零，則跳過下行被除的步驟
        x = int(i) % int(num)
        remainder += x    
    if remainder == 0 and zero ==0: # 數字裡面有0就排除
        s.append(i)
print(s)

# 尋找兩個數字的最大差值
max_delta = 0
max_delta_pair = None
for x in range(len(s) - 1):
    delta = s[x + 1] - s[x]
    if delta > max_delta:
        max_delta = delta
        max_delta_pair = (s[x], s[x + 1])
print(max_delta_pair)


#參考解法 #01
def is_self_dividing(n):
    """檢查一個數字是否是自除數"""
    digits = [int(d) for d in str(n)]
    for d in digits:
      if d == 0 or n % d != 0:
        return False
    return True

def max_self_dividing_difference(left, right):
    """找出在左右邊界之間的 Self-Dividing Number 的最大差距"""
    dividings = []
    for i in range(left, right+1):
      if is_self_dividing(i):
        dividings.append(i)
  
    max_diff = 0
    max_diff_pair = None
    for i in range(len(dividings)-1):
      if dividings[i+1] - dividings[i] > max_diff:
        max_diff_pair = (dividings[i], dividings[i+1])
        max_diff = dividings[i+1] - dividings[i]     
    return max_diff_pair
        
# 範例輸入：左邊界為11，右邊界為15
left = int(input())
right = int(input())

# 呼叫函式找出最大差距
max_diff_pair = max_self_dividing_difference(left, right)
print(max_diff_pair)
# 輸出結果
print(f"差距最大的 Self-Dividing Number 是 {max_diff_pair[0]} 與 {max_diff_pair[1]}，差距為 {max_diff_pair[1] - max_diff_pair[0]}")
#上述程式中，我們定義了兩個函式 is_self_dividing 和 max_self_dividing_difference。is_self_dividing 函式用來檢查一個數字是否是自除數，max_self_dividing_difference 函式用來找出在左右邊界之間的 Self-Dividing Number 的最大差距。
#在 max_self_dividing_difference 函式中，我們使用兩個巢狀的迴圈來枚舉左右邊界之間的所有數字對。對於每一對數字，我們檢查它們是否都是自除數。如果是，我們就計算它們之間的差距，並將這個差距與目前找到的最大差距比較。如果差距比目前的最大差距還要大，我們就更新最大差距和對應的數字對。

#參考解法 #02
def is_self_dividing(n):
    """檢查一個數字是否是自除數"""
    digits = [int(d) for d in str(n)]
    for d in digits:
        if d == 0 or n % d != 0:
            return False
    return True

def max_self_dividing_difference(left, right):
  """找出在左右邊界之間的 Self-Dividing Number 的最大差距"""
  max_diff = 0
  max_diff_pair = (None, None)
  previous_dividing = None  
  for i in range(left, right+1):
    if is_self_dividing(i):
      if previous_dividing is None:  #確認i是Self-Dividing Number且previous_dividing是None時將i指派給previous_dividing
          previous_dividing = i
      if i - previous_dividing > max_diff:
        max_diff = i - previous_dividing
        max_diff_pair = (previous_dividing, i)
      previous_dividing = i
  return max_diff_pair
        
# 範例輸入：左邊界為11，右邊界為15
left = int(input())
right = int(input())

# 呼叫函式找出最大差距
max_diff_pair = max_self_dividing_difference(left, right)

# 輸出結果
print(f"差距最大的 Self-Dividing Number 是 {max_diff_pair[0]} 與 {max_diff_pair[1]}，差距為 {max_diff_pair[1] - max_diff_pair[0]}")

