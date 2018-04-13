# -----------------
# Реализуйте функцию three_words
# Вам предоставляется строка со словами и числами,
# разделенными пробелами. Слова содержат только буквы.
# Вы должны проверить, содержит ли строка три слова подряд.
# Например, строка «start 5 one two three 7 end» содержит три слова подряд.
# -----------------


def three_words(words):
    t = words.split(" ")
    b = 0
    r = 0
    for i in t:
        if t[b].isalpha():
            r+=1
        else:
            r = 0
        b+=1
    if r >= 3:
         return True
    else:
         return False

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert three_words("Hello World hello"), "Hello"
    assert not three_words("He is 123 man"), "123 man"
    assert not three_words("1 2 3 4"), "Digits"
    assert three_words("bla bla bla bla"), "Bla Bla"
    assert not three_words("Hi"), "Hi"

print("eeeyy")