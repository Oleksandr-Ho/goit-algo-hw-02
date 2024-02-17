"""Завдання 2

Необхідно розробити функцію, яка приймає рядок як вхідний параметр, додає всі його символи до двосторонньої черги 
(deque з модуля collections в Python), а потім порівнює символи з обох кінців черги, щоб визначити, чи є рядок паліндромом. 
Програма повинна правильно враховувати як рядки з парною, так і з непарною кількістю символів, 
а також бути нечутливою до регістру та пробілів."""


from collections import deque

def is_palindrome(s):
    # Видаляємо пробіли та переводимо рядок в нижній регістр
    formatted_str = ''.join(ch.lower() for ch in s if ch.isalnum())
    
    # Створюємо двосторонню чергу з символів отформатованого рядка
    char_deque = deque(formatted_str)
    
    # Перевіряємо символи з обох кінців черги, доки вона не буде пустою або не залишиться один символ
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

# Приклади використання
test_strings = ["A man a plan a canal Panama", "No lemon, no melon", "Hello, World!"]
for test_str in test_strings:
    print(f"\"{test_str}\" is a palindrome: {is_palindrome(test_str)}")
