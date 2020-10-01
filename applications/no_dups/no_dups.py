def no_dups(s):
    # Your code here
    cache = {}
    count = 0

    string = set(s.split())
    if s == "":
        return ""
    for c in string:
        if c not in cache:
            cache[cache] = c
            count +=1
        return cache



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))