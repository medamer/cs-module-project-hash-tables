def word_count(s):
    # Your code here
    d = {}
    sp_car = '":;,.-+=/\\|[]{}()*^&\`\"\t\r\n\f\b\a'
    if s in sp_car:
        return d
    strings = s.replace(sp_car, "")
    strings = strings.replace('.', '')
    strings = strings.replace(',', '')
    strings = strings.replace('"', '')
    words = strings.lower().split()
    
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))