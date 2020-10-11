import string


def gettext(file):
    with open(file) as f:
        text = f.read().lower()
    for i in string.punctuation:
        text = text.replace(i, ' ')
    return text


def writefile(wordlist, file):
    with open(file, "w") as f:
        for i in range(100):
            print(i, wordlist[i][0], wordlist[i][1], sep='\t', file=f)


if __name__ == '__main__':
    bookText = gettext("Republic.txt")
    words = bookText.split()
    counts = {}
    for item in words:
        counts[item] = counts.get(item, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    writefile(items, "Words Frequency.txt")
