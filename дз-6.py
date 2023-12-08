def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
print(is_palindrome("шалаш"))
print(is_palindrome("задача"))

def register_person(name, surname, patronymic, age):
    return f'Иванов Иван Иванович 1973 г.р. зарегистрирован'
print(register_person("Иван", "Иванов", "Иванович", 1973))

def find_max(a, b, c=None):
    if c is not None:
        return a if a > b and a > c else b if b > a and b > c else c
    else:
        return a if a > b else b
print(find_max(2, 9))
print(find_max(4, 8, 1))