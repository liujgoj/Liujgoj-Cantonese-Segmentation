import re

with open('3.txt', encoding='utf-8') as f:
    words = f.read().split()

with open('4.txt', 'w', encoding='utf-8') as f:
    for word in words:
        if re.match(r'^(mouq)-([a-z]+)-(mouq)-([a-z]+)$', word):
            word = re.sub(r'^(mouq)-', '', word)
            word = re.sub(r'-(mouq)-', '', word)
        elif re.match(r'^(yauq)-([a-z]+)-(yauq)-([a-z]+)$', word):
            word = re.sub(r'^(yauq)-', '', word)
            word = re.sub(r'-(yauq)-', '', word)
        elif re.match(r'^[a-z]+ganr(-[a-z]+)+-[a-z]+$', word):
            word = re.sub(r'ganr(-[a-z]+)+-', '', word)
        elif re.match(r'^[a-z]+zor(-[a-z]+)+-[a-z]+$', word):
            word = re.sub(r'zor(-[a-z]+)+-', '', word)
        elif re.match(r'^[a-z]+zvh(-[a-z]+)+-[a-z]+$', word):
            word = re.sub(r'zvh(-[a-z]+)+-', '', word)
        elif re.match(r'^[a-z]+gwo(-[a-z]+)+-[a-z]+$', word):
            word = re.sub(r'gwo(-[a-z]+)+-', '', word)
        elif re.match(r'^[a-z]+ganr-[a-z]+$', word):
            word = re.sub(r'ganr-', '', word)
        elif re.match(r'^[a-z]+zor-[a-z]+$', word):
            word = re.sub(r'zor-', '', word)
        elif re.match(r'^[a-z]+zvh-[a-z]+$', word):
            word = re.sub(r'zvh-', '', word)
        elif re.match(r'^[a-z]+gwo-[a-z]+$', word):
            word = re.sub(r'gwo-', '', word)    
        elif re.match(r'^[a-z]+(-[a-z]+)+-[a-z]+$', word) and word.count('-') >= 2:
            word = re.sub(r'(-[a-z]+)+-', '', word)
            
            
        f.write(word + '\n')