import re

# 读取文件1.txt
with open('1.txt', 'r', encoding='UTF-8') as f:
    content = f.read()

# 将大写字母转为小写
content = content.lower()

# 替换指定字符串
content = content.replace("hor' mxhoryiq", "horyiq mxhoryiq")
content = content.replace("hor' mxhornangx", "hornangx mxhornangx")
content = content.replace("'deih", "keoiqdeih")

# 划分单词
words = re.findall(r"[^\s\d\W\-]+", content)

# 将单词写入文件2.txt
with open('2.txt', 'w', encoding='UTF-8') as f:
    f.write("\n".join(words))