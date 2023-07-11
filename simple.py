import re 
import xlsxwriter

# 打开文件并读取 
with open('1.txt', encoding='utf-8') as f:
    text = f.read()

# 按照标点符号（撇號同連字符除外）和空格分割 
words = re.split('[^\w\'-]+', text)

# 全部小写
words = [word.lower() for word in words]  

# 统计单词数量 
count = len(words) 

# 统计每个单词出现的次数
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# 按出现次数排序 
word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

# 导出到excel
workbook = xlsxwriter.Workbook('2.xlsx') 
worksheet = workbook.add_worksheet()

# 第一列单词 
worksheet.write_column('A1', [x[0] for x in word_count])

# 第二列单词数量    
worksheet.write_column('B1', [x[1] for x in word_count])  

# 第三列单词频率
worksheet.write_column('C1', [x[1]/count for x in word_count])  

# 最后一行总数量 
worksheet.write('A%d' % (len(word_count)+1), 'Total')
worksheet.write('B%d' % (len(word_count)+1), count)

workbook.close()