#自己寫+gpt
s = 'Here are UPPERCASE and lowercase chars.'

d={}
for index, character in enumerate(s):
    if character in d:
        d[character].append(index+1)
    else:
        d[character]= [index+1]
        
print(d) # {'H': [1], 'n': [21], 'o': [25], 'U': [10], 'r': [3, 7, 28, 37], 'l': [24], 's': [31, 38], 'c': [29, 34], 'e': [2, 4, 8, 27, 32], 'S': [17], ' ': [5, 9, 19, 23, 33], 'a': [6, 20, 30, 36], 'R': [14], 'w': [26], '.': [39], 'h': [35], 'E': [13, 18], 'd': [22], 'P': [11, 12], 'A': [16], 'C': [15]} 

#參考解法 #01

S = 'Here are UPPERCASE and lowercase chars.'

d = {}
count = 1
for s in S:
  if s not in d:
    d[s] = []
  d[s].append(count)
  count = count + 1

print(d)
#參考解法 #02

S = 'Here are UPPERCASE and lowercase chars.'

d = {}
for i, s in enumerate(S):
  d.setdefault(s, []) #setdefault() 的目的是確保字典 d 中的每個字母都有一個對應的空列表，以便於後續迭代中添加元素。對於已經存在於字典中的字母，setdefault() 方法只是檢查它們是否已經存在，然後返回它們目前對應的值，而不會對其進行任何修改。
  d[s].append(i + 1)

print(d)

