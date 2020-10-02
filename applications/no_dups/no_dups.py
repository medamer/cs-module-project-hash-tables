def no_dups(s):
    # Your code here
    cache = set()
    words = []


    if s == "":
        return ''

    for word in s.split():
        if word not in cache:
            words.append(word)
            cache.add(word)
            
    cache = " ".join(words)
    return cache



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))