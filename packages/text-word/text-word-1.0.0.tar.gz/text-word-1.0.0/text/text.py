"""
@Author: _chang_an
@Date: 2019-12-17 14:08:34
@LastEditTime: 2019-12-17 14:11:29
@LastEditors: _chang_an
@Description: 替换txt文本中的字符
@FilePath: \\text\\text.py
"""
'''from datetime import *
start = datetime.now()
list1 = []
with open("qwer.txt", 'r', encoding="utf-8") as f:   
    content = f.readlines()  #  content是列表
    for table in content:  # tabel是字符串
        rep = table.replace('章', 'star')
        list1.append(rep)
with open('圣墟目录改写.txt', 'w', encoding='utf-8') as p:
    p.writelines(list1)
    print('文件改写成功')
end = datetime.now()
print(end-start)'''
    
'''import re
from datetime import *
start = datetime.now()
p = r'章'
with open('qwer.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(len(content))
    replace_text = re.sub(p, 'star', content)
    with open('圣墟目录改写第一个.txt', 'w', encoding='utf-8') as p:
        p.write(replace_text)
        print('改写成功')
end = datetime.now()
print(end-start)'''



