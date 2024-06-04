#自己寫+gpt
letters = list(input()) #aabcc

lst=[]
final_lst=[]
for character in letters:
    if character not in lst:
        lst.append(character)
def permutations(lst, prefix=''):
    if len(lst) == 0:
        final_lst.append(prefix)# 如果lst列表為空(都串到prefix去了)，代表一個排列組合完成
    else:
        for i in range(len(lst)):                                       #i=0,1,2用原始lst[a,b,c]去跑
            new_prefix = prefix + lst[i]                                #取a當開頭 #取b當開頭 #取c當開頭
            new_lst = lst[:i] + lst[i+1:]                               #跳過a    #跳過b    ＃跳過c
            permutations(new_lst, new_prefix)
            #print(new_lst,new_prefix)
            #bc,a再帶入def permutations，變成for i in len(bc)
                #c,ab再帶入def permutations，變成for i in len(c)
                    #[],abc再帶入def permutations，len([])==0，print出abc
                #b,ac再帶入def permutations，變成for i in len(b)
                    #[],acb再帶入def permutations，len([])==0，print出acb
            #ac,b再帶入def permutations，變成for i in len(ac)
                #c,ba再帶入def permutations，變成for i in len(c)
                    #[],bac再帶入def permutations，len([])==0，print出bac
                #a,bc再帶入def permutations，變成for i in len(a)
                    #[],bca再帶入def permutations，len([])==0，print出bca            
            #ab,c再帶入def permutations，變成for i in len(ac)
                #b,ca再帶入def permutations，變成for i in len(c)
                    #[],cab再帶入def permutations，len([])==0，print出cab
                #a,cb再帶入def permutations，變成for i in len(a)
                    #[],cba再帶入def permutations，len([])==0，print出cba      
                        
permutations(lst) #以不重複的字母清單[a,b,c]執行排列組合
print(final_lst)

#參考解法 #01

s = input() # AB

d = []
def permute(s, i, length):
    if i == length:
        d.append("".join(s))
    else:
        for j in range(i, length): 
            s[i], s[j] = s[j], s[i] #交換 s[i] 和 s[j] 的位置，以便生成不同的排列組合。
            permute(s, i+1, length) #遞歸調用 permute() 函數，將索引 i+1 傳遞給下一層遞歸
            s[j], s[i] = s[i], s[j] #遞歸結束後，將交換的元素再次交換回來，以確保下一次循環是在原始列表的基礎上進行。

permute(list(s), 0, len(s))
print(d)

#參考解法 #02

from itertools import permutations

s = input() # AB
d = [''.join(i) for i in permutations(s)]
print(d)
print(permutations(s))