#自己寫＋gpt
s = input().split()  

if "not" in s and "at" in s and "all" in s:
    index1= s.index("not")
    index2= s.index("at")
    index3= s.index("all")
    s[index3]=s[index2]=s[index2 - 1]=""
    s[index1]="good"
    result = " ".join(word for word in s if word != "")
print(result)

#參考解法 #01
s = input()  
# 找到字串 s 中的 'not' 子字串在 s 中的位置
c1 = s.find('not')
# 找到字串 s 中的 'at all' 子字串在 s 中的位置，再加上 6 個字元的位置，得到子字串結束的位置
c2 = s.find('at all') + 6
# 利用字串的切片（slicing）功能，取出 'not' 子字串前的字串、'at all' 子字串後的字串，並插入 'good'，組成新的字串
d = s[0:c1] + 'good' + s[c2:len(s)]
print(c1)
print(c2)
print(d)


#參考解法 #02
s = input()  
# 將字串 s 以 "not" 分割，取得分割後的第一個子字串，也就是 "not" 之前的部分
s1 = s.split('not')[0]
# 將字串 s 以 "at all" 分割，取得分割後的第二個子字串，也就是 "at all" 之後的部分
s2 = s.split('at all')[1]
# 將 s1、"good" 和 s2 結合成新的字串 d
d = f'{s1}good{s2}'
print(d)

#參考解法 #03
import re
s = input()  
# 使用 re.sub 函式來進行正規表達式取代
d = re.sub(r"not\s+.*?\s+at\s+all", "good", s)  
print(d)  