import re

# 打开文件2.txt，读取其中的内容
with open('2.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# 去掉除了连字符“-”以外的所有标点符号
text = re.sub('[^\w\s-]+', '', text)

# 根据规则处理单词
words = text.split()
for i in range(len(words)):
    word = words[i]
    # 处理最左边的字符串
    word = re.sub('^(aa-|louq-|daaih-|sai-|siur-)', '', word)
    # 处理最右边的字符串
    word = re.sub('(-saangj|-yij|-goj|-goh|-baak|-sukj|-taair|-zair|-neoiq|-neoir|-maaj|-noengr|-gaaj|-gei|-sih|-yex|-fur|-zer|-zej|-gungj|-ciux|-satj|-wongx|-guj|-samr|-zikh|-siu)$', '', word)
    words[i] = word

# 将处理后的单词列表写入文件3.txt
with open('3.txt', 'w', encoding='utf-8') as f:
    f.write(' '.join(words))