import re

def process_word(word):
    # Step 1: Remove prefixes
    word = re.sub("^(aa-|louq-|daaih-|sai-|siur-)", "", word, flags=re.IGNORECASE)

    # Step 2: Remove suffixes
    word = re.sub("(-saangj|-yij|-goj|-goh|-baak|-sukj|-taair|-zair|-neoiq|-neoir|-maaj|-noengr|-gaaj|-gei|-sih|-yex|-fur|-zer|-zej|-gungj|-ciux|-satj|-wongx|-guj|-samr|-zikh|-siu)$", "", word)

    # Step 3: Convert uppercase letters to lowercase
    word = word.lower()

    # Step 4: Replace specified phrases
    word = word.replace("hor' mxhoryiq", "horyiq mxhoryiq").replace("hor' mxhornangx", "hornangx mxhornangx").replace("'deih", "keoiqdeih")

    # Step 5: Replace specified patterns
    word = re.sub(r"^(mouq)-([a-z]+)-(mouq)-([a-z]+)$", r"\1 \2\4", word).replace(r"^(yauq)-([a-z]+)-(yauq)-([a-z]+)$", r"\1 \2\4", word)

    return word

def process_text(text):
    # Step 6: Split words
    words = re.findall(r"[\w'-]+", text)

    # Step 7: Replace compound words
    words = [re.sub(r"^([a-z]+)ganr-([a-z]+)$", r"\1\2", w) for w in words]

    # Step 8: Keep words with single hyphen unchanged (do nothing)

    # Step 9: Replace words with multiple hyphens
    words = [re.sub(r"^([^-]+)-.*-([^-]+)$", r"\1\2", w) for w in words]

    # Step 10: Remove duplicate words
    words = sorted(set(words), key=words.index)

    # Step 11: Arrange words in separate lines
    text = "\n".join(words)

    return text

# Read input file
with open("1.txt", "r", encoding="utf-8") as input_file:
    input_text = input_file.read()

# Process content
processed_text = process_text(input_text)

# Write output file
with open("2.txt", "w", encoding="utf-8") as output_file:
    output_file.write(processed_text)