import pytest
from Тренировка_04_Task_01 import StringProcessor 


# Позитивные тесты:

# Позитивный тест 1: обычная строка без точки в конце
def test_process_normal_string_without_dot():
    result = StringProcessor.process("привет мир")
    assert result == "Привет мир."

# Позитивный тест 2: строка уже с точкой в конце
def test_process_string_with_dot():
    result = StringProcessor.process("привет мир.")
    assert result == "Привет мир."

# Позитивный тест 3: пустая строка
def test_process_empty_string():
    result = StringProcessor.process("")
    assert result == "."

# Позитивный тест: одно слово
def test_process_single_word():
    result = StringProcessor.process("слово")
    assert result == "Слово."

# Позитивный тест: строка уже с заглавной буквы
def test_process_already_capitalized():
    result = StringProcessor.process("Привет мир")
    assert result == "Привет мир."


# Негативные тесты:


# Негативный тест 1: передача None вместо строки
def test_process_with_none():
    with pytest.raises(AttributeError):
        StringProcessor.process(None)

# Негативный тест 2: передача числа вместо строки
def test_process_with_integer():
    with pytest.raises(AttributeError):
        StringProcessor.process(123)

# Негативный тест 3: передача списка вместо строки
def test_process_with_list():
    with pytest.raises(AttributeError):
        StringProcessor.process(["текст"])
