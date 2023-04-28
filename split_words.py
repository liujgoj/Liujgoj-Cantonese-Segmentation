import re

def process_word(word):
    word = word.lower()
    
    # 處理撇号
    word = re.sub(r"([a-z]+)'", r"\1", word)
    word = re.sub(r"'([a-z]+)", r"\1", word)

    # 處理動詞
    word = re.sub(r"(.*)(ganr|zor|zvh|gwo)$", r"\1", word)

    # 處理連字符
    if '-' in word:
        # 特殊處理
        if word == "mouq-zing-mouq-geoi":
            return ["mouq", "zinggeoi"]
        if word == "mouq-sih-mouq-gon":
            return ["mouq", "sihgon"]
        if word == "yauq-zungj-yauq-yih":
            return ["yauq", "zungjyih"]

        # 前綴
        word = re.sub(r"^(aa-|louq-|daaih-|sai-|siur-)", "", word)

        # 後綴
        word = re.sub(r"(-saangj|-yij|-goj|-goh|-baak|-sukj|-taair|-zair|-neoiq|-neoir|-maaj|-noengr|-gaaj|-gei|-sih|-yex|-fur|-zer|-gungj|-ciux|-satj|-wongx|-guj|-samr|-zikh|-siu)$", "", word)

        # 其他處理
        parts = word.split('-')
        n = len(parts)

        if n == 1:
            return [parts[0]]

        if parts[0] == parts[-1]:
            return [parts[0]]
        else:
            if n == 2:
                return [parts[0], parts[1]]
            else:
                return parts[:-1] + [parts[-1]]

    return [word]

def split_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        words = re.findall(r"[a-zA-Z'-]+", content)
        words = [process_word(word) for word in words]

    return words

def write_words(words, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for word_list in words:
            for word in word_list:
                file.write(word + '\n')

if __name__ == '__main__':
    input_file = 'manxginr.txt'
    output_file = 'daanjcix.txt'

    words = split_words(input_file)
    write_words(words, output_file)