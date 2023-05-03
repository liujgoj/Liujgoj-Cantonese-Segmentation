# 读取文件1.txt
with open('1.txt', 'r', encoding='UTF-8') as f:
    content = f.read()

# 将大写字母转为小写
content = content.lower()

# 替换字符串
# 將“可唔可以”替換爲“”可以唔可以”
content = content.replace("hor' mxhoryiq", "horyiq mxhoryiq")
# 將“可唔可能”替換爲“可能唔可能”
content = content.replace("hor' mxhornangx", "hornangx mxhornangx")
# 將縮寫“'哋”替換爲“佢哋”
content = content.replace("'deih", "keoiqdeih")
# 將“小完便”替換爲“小便”
content = content.replace("siur-yvnx-binh", "siurbinh")
# 將“接慣生”替換爲“接生”
content = content.replace("zip-gwaan-saangj", "zipsaangj")

# 划分单词
words = content.split()

# 保存修改后的结果到文件2.txt
with open('2.txt', 'w', encoding='UTF-8') as f:
    f.write('\n'.join(words))


import re

# 读取文件2.txt
with open("2.txt", "r", encoding="utf-8") as file:
    content = file.read()

# 按照空格划分单词
words = content.split()

unique_words = set()  # 用于存储唯一的单词

for word in words:


    # 去掉所有的数字，去掉除了连字符“-”以外所有的标点符号
    word = re.sub(r'\d', '', word)
    word = re.sub(r'[^\w\-]', '', word)

    # 删除特定的字符串(前綴同後綴)
    word = re.sub(r'^(aa-|louq-|daaih-|sai-|siur-|feix-)', '', word)
    word = re.sub(r'(-yix|-zeh|-soex|-foj|-saangj|-yij|-goj|-goh|-baak|-sukj|-hingj|-zungr|-taair|-zair|-neoiq|-neoir|-maaj|-noengr|-gaaj|-gei|-sih|-yex|-fur|-zer|-zej|-gungj|-ciux|-satj|-wongx|-guj|-samr|-zikh|-siu)$', '', word)

    # 处理特殊情况
    # 將“冇事冇幹”等替換爲“冇 事幹”
    if re.match(r'^(mouq)-([a-z]+)-(mouq)-([a-z]+)$', word):
        word = re.sub(r'^(mouq)-', 'mouq ', word)
        word = re.sub(r'-(mouq)-', '', word)
    # 將“有忠有義”等替換爲“有 忠義”
    elif re.match(r'^(yauq)-([a-z]+)-(yauq)-([a-z]+)$', word):
        word = re.sub(r'^(yauq)-', 'yauq ', word)
        word = re.sub(r'-(yauq)-', '', word)
    # 將單詞中間嘅“ganr”等時態同埋中間插入嘅單詞刪除
    elif re.match(r'^[a-z]+(ganr|zor|zvh|gwo)(-[a-z]+)+-[a-z]+$', word):
        word = re.sub(r'(ganr|zor|zvh|gwo)(-[a-z]+)+-', '', word)
    # 將單詞中間嘅“ganr”等時態刪除
    elif re.match(r'^[a-z]+(ganr|zor|zvh|gwo)-[a-z]+$', word):
        word = re.sub(r'(ganr|zor|zvh|gwo)-', '', word)
    # 將插入單詞中間嘅音節同埋單詞刪除
    elif re.match(r'^[a-z]+(-[a-z]+)+-[a-z]+$', word) and word.count('-') >= 2:
        word = re.sub(r'(-[a-z]+)+-', '', word)

    # 删除重复的单词，只保留唯一的一个
    unique_words.add(word)

# 将处理后的单词写入文件2.txt，每行一个单词
with open("3.txt", "w", encoding="utf-8") as file:
    for unique_word in unique_words:
        file.write(unique_word + "\n")