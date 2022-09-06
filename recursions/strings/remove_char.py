def skip(word):
    if word == "":
        return ""
    char = word[0]
    if char == "a":
        return skip(word[1:])
    else:
        return char + skip(word[1:])


def remove_a(new_str, string):
    if not string:
        return new_str
    char = string[0]
    if char == 'a':
        return remove_a(new_str, string[1:])
    else:
        return remove_a(new_str + char, string[1:])


def skip_apple(words):
    if words == "":
        return ""
    if words.startswith("apple"):
        return skip_apple(words[5:])
    else:
        return words[0] + skip_apple(words[1:])
    

if __name__ == "__main__":
    word = "bacdaf"

    print(remove_a("", word))
    print(skip(word))
    words = "dbgapplefdfapplezz"
    print(skip_apple(words))
    