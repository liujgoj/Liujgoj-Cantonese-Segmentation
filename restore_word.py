with open('1.txt', 'r', encoding='utf-8') as f1, open('2.txt', 'w', encoding='utf-8') as f2:
    for line in f1:
        line = line.lower()  # 把大写字母全部转为小写
        line = line.replace("hor' mxhoryiq", "horyiq mxhoryiq")  # 替换字符串
        line = line.replace("hor' mxhornangx", "hornangx mxhornangx")
        line = line.replace("'deih", "keoiqdeih")
        words = line.split()  # 分割单词
        for word in words:
            f2.write(word)
            f2.write('\n')  # 每个单词占一行
            