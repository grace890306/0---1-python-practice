#gpt協助
n=int(input())

def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a, b = 1, 2
        for i in range(3, n + 1): 
            a, b = b, a + b
            #1,2=2,3
            #2,3=3,5
            #3,5=5,8
        return b
print(f(n))

# 1=1                ->1
# 2=1+1              ->2
# 3=1+1+1=1+2=2+1    ->3
# 4=1+1+1+1=1+1+2=1+2+1=2+1+1=2+2  ->5
# 5=1+1+1+1+1=1+1+1+2=1+1+2+1=1+2+1+1=2+1+1+1=2+2+1=2+1+2=1+2+2 ->8
# 爬第 n 階樓梯的方法數」等於「爬上 n−1 階樓梯的方法數量」 + 「爬上 n−2 階樓梯的方法數量


#參考解法 #01

n = int(input())

def climbStairs(n:int) -> int: #-> int 是一種型別提示（type hinting）的語法，用於提示該函式的返回值類型應為整數。它不會影響程式碼的運行
  W = [0, 1, 2]
  if len(W) < n+1: #if輸入數字大於3，就用遞迴函數累加先前的數字，小於3就取0,1,2
      return climbStairs(n - 2) + climbStairs(n - 1);
# climbStairs(5)=climbStairs(3)+climbStairs(4)
#               =[climbStairs(1)+climbStairs(2)]+[climbStairs(2)+climbStairs(3)]
#               =1+2+2+[climbStairs(1)+climbStairs(2)]
#               =1+2+2+1+2
#               =8

  return W[n];

print(climbStairs(n)) #n=5


#參考解法 #02

#方法一採用遞迴的規則如下：
#f(n) = f(n-1) + f(n-2)
#這個題目使用遞迴會存在一個問題，就是每次計算 f(n) 之後，會去遞迴計算 f(n-1) + f(n-2)。相同的概念在計算 f(n-1) 會去計算 f(n-2) + f(n-3)、f(n-2) 會去計算 f(n-3) + f(n-4)，以這個例子來看，f(n-3) 會同時在 f(n-1) 和 f(n-2) 重複計算。這樣一來，當 n 很大的時候就會有更多的值會再遞迴過程中重複計算。
#因此這裡想法是能不能將剛剛的 f(n-3) 給記錄下來，而不用每一個遞迴過程都重複計算。所以我們想到的是將結果存在一個變數當中（而非每次都計算），將遞迴的過程暫存到一個變數中，如下：
#dp[i] = dp[i - 1] + dp[i - 2]
#接下來，用 Python 實作看看：
n = int(input())

W = [0, 1, 2]
for i in range(3, n+1): #其實一開始我有想到這句
  W.append(W[i - 2] + W[i - 1]) #但沒想到用list的方式儲存數字

# for i in range(3,6):
#   W.append(W[1]+W[2]) 第4個數用第2個數+第3個數加出來
#   W.append(W[2]+W[3]) 第5個數用第3個數+第4個數加出來
#   W.append(W[3]+W[4]) 第6個數用第4個數+第5個數加出來
print(W)
print(W[n]) #n=5


