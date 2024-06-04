#參考解法 #01
def add1(n):
  return n+1
def isPrime(n):
  return all(n % d for d in range(2, int(n**.5)+1))

def f(L, F): #利用程式實作 map 函式，map(F, L) 包含兩個參數輸入，F 是一個 function、L 是一個列表，回傳結果是一個列表
  res = []
  for e in L:
    res.append(F(e))
  return res

L = [1,2,3,4,5,6]
F = add1
print(f(L, F)) # [2,3,4,5,6,7]


L = [2,3,4,5,6,7] 
F = isPrime
print(f(L, F)) # [True,True,False,True,False,True]

#參考解法 #02

def add1(n):
  return n + 1

def isPrime(n):
  return all(n % d for d in range(2, int(n**.5)+1))

def f(L, F):
  return [ F(e) for e in L ] #列表推導式，它不需要額外建立一個空列表。列表推導式的語法是直接創建一個新的列表，然後使用迭代器遍歷原始列表 L 中的元素，對每個元素應用函數 F，並將結果添加到新列表中。這樣就不需要額外的初始化操作，而是直接將每個元素的處理結果放入列表中。

L = [1,2,3,4,5,6]
F = add1
print(f(L, F)) # [2,3,4,5,6,7]


L = [2,3,4,5,6,7] 
F = isPrime
print(f(L, F)) # [True,True,False,True,False,True]