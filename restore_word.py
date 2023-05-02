# 读取文件1.txt
with open('1.txt', 'r', encoding='UTF-8') as f:
    content = f.read()

# 将大写字母转为小写
content = content.lower()

# 替换字符串
content = content.replace("hor' mxhoryiq", "horyiq mxhoryiq")
content = content.replace("hor' mxhornangx", "hornangx mxhornangx")
content = content.replace("'deih", "keoiqdeih")
content = content.replace("siur-yvnx-binh", "siurbinh")
content = content.replace("zip-gwaan-saangj", "zipsaangj")

# 划分单词
words = content.split()

# 保存修改后的结果到文件2.txt
with open('2.txt', 'w', encoding='UTF-8') as f:
    f.write('\n'.join(words))