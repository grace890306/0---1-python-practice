#chatgpt
def merge_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result

dict1 = {1:10, 2:20}
dict2 = {3:30, 4:40}
dict3 = {5:50, 6:60}

d = merge_dicts(dict1, dict2, dict3)

print(d)

#參考解法 #01
# 定義三個字典 dic1、dic2、dic3
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
# 將這三個字典進行合併，先透過 list(dic.items()) 將字典轉成由 (key, value) 組成的列表
# 再透過 + 符號將三個列表連接起來
# 最後再透過 dict() 將列表轉回字典
d = dict(list(dic1.items()) + list(dic2.items()) + list(dic3.items()))
print(d)

# #參考解法 #01-2
# from collections import ChainMap

# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}

# d = dict(ChainMap(dic1, dic2, dic3))
# print(ChainMap(dic1, dic2, dic3))
# print(d)  # {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# #參考解法 #02
# # 輸出合併後的字典
# # 定義三個字典 dic1、dic2、dic3
# dic1 = {1:10, 2:20}
# dic2 = {3:30, 4:40}
# dic3 = {5:50, 6:60}
# # 使用展開字典的方式，將這三個字典合併成一個新字典 d，並指定給它。
# d = {**dic1, **dic2, **dic3}
# # 輸出合併後的字典
# print({**dic1})
# print(d) # {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


# 參考解法 #03
# # 接下來，宣告一個空的字典 d。
# d = dict()

# # 然後，使用 update() 方法將三個字典的鍵值對加到 d 中。
# d.update(dic1)
# d.update(dic2)
# d.update(dic3)

# # 輸出合併後的字典
# print(d) # {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# 參考解法 #03-2
# dic1 = {1:10, 2:20}
# dic2 = {3:30, 4:40}
# dic3 = {5:50, 6:60}
# d = {}
# for i in range(1, 4):
#     d.update(globals()[f"dic{i}"])
# print(d)