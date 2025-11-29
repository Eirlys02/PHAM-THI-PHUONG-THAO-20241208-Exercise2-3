def load_text_file(filepath):
    with open(filepath, "r", encoding="utf-8-sig") as f:
        return f.readlines()
text_data = load_text_file("News1.txt")

def tokenize(text):
    return text.split()   

all_tokens = []
for line in text_data:
    tokens = tokenize(line)
    all_tokens.append(tokens)
print(all_tokens[0])
