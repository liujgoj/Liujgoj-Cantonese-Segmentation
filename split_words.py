import re

# 定义前缀和后缀的正则表达式
prefix_pattern = r'(?:aa|louq|daaih|sai|siur)-'
suffix_pattern = r'-[a-z]*(?:saangj|yij|goj|goh|baak|sukj|taair|zair|neoiq|neoir|maaj|noengr|gaaj|gei|sih|yex|fur|zer|zej|gungj|ciux|satj|wongx|guj|samr|zikh|siu)'

# 读取文件内容
with open('manxginr.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# 去除前缀和后缀
content = re.sub(prefix_pattern, '', content, flags=re.IGNORECASE)
content = re.sub(suffix_pattern, '', content)

# 将大写字母转为小写
content = content.lower()


# 分割单词
words = re.findall(r'[\W\S]+', content)

# 将单词写入文件
with open('1.txt', 'w') as f:
    f.write('\n'.join(words))