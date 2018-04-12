# -----------------
# Реализуйте функцию find_message, которая принимает на вход строку
# Соберите все заглавные буквы одним словом в том порядке, в котором они появляются в тексте.
# Например: text = «How are you? Eh, ok. Low or Lower? Ohhh.», Если мы собираем все заглавные буквы, получаем сообщение «HELLO».
# -----------------


def find_message(text):
    """Find a secret message"""
    if text.islower():
        return""
    u = [c for c in text if c.isupper()]
    s_out = ''.join(u)
    print(s_out)
    return s_out


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"

    print("Good!")