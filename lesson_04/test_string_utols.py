import pytest
from string_utils import StringUtils


class TestStringUtils:
    """Тесты для класса StringUtils"""
    
    def setup_method(self):
        """Подготовка объекта для каждого теста"""
        self.utils = StringUtils()
    
    # ===== Тесты для capitalize =====
    def test_capitalize_positive_normal(self):
        """Позитивный тест: обычная строка"""
        result = self.utils.capitalize("skypro")
        assert result == "Skypro"
    
    def test_capitalize_positive_already_capitalized(self):
        """Позитивный тест: уже заглавная первая буква"""
        result = self.utils.capitalize("Skypro")
        assert result == "Skypro"
    
    def test_capitalize_positive_with_spaces(self):
        """Позитивный тест: строка с пробелом в начале"""
        result = self.utils.capitalize(" skypro")
        assert result == " skypro"  # Внимание: метод .capitalize() делает " Skypro"
    
    def test_capitalize_positive_empty_string(self):
        """Позитивный тест: пустая строка"""
        result = self.utils.capitalize("")
        assert result == ""
    
    def test_capitalize_positive_single_letter(self):
        """Позитивный тест: одна буква"""
        result = self.utils.capitalize("s")
        assert result == "S"
    
    def test_capitalize_negative_non_string(self):
        """Негативный тест: не строка (None)"""
        with pytest.raises(AttributeError):
            self.utils.capitalize(None)
    
    def test_capitalize_negative_number(self):
        """Негативный тест: число вместо строки"""
        with pytest.raises(AttributeError):
            self.utils.capitalize(123)
    
    # ===== Тесты для trim =====
    def test_trim_positive_normal(self):
        """Позитивный тест: обычная строка с пробелами"""
        result = self.utils.trim("   skypro")
        assert result == "skypro"
    
    def test_trim_positive_multiple_spaces(self):
        """Позитивный тест: много пробелов"""
        result = self.utils.trim("      skypro")
        assert result == "skypro"
    
    def test_trim_positive_no_spaces(self):
        """Позитивный тест: строка без начальных пробелов"""
        result = self.utils.trim("skypro")
        assert result == "skypro"
    
    def test_trim_positive_empty_string(self):
        """Позитивный тест: пустая строка"""
        result = self.utils.trim("")
        assert result == ""
    
    def test_trim_positive_only_spaces(self):
        """Позитивный тест: только пробелы"""
        result = self.utils.trim("   ")
        assert result == ""
    
    def test_trim_positive_mixed_whitespace(self):
        """Позитивный тест: табы и пробелы"""
        result = self.utils.trim("\t\n skypro")
        assert result == "\t\n skypro"  # Внимание: удаляет только обычные пробелы!
    
    def test_trim_negative_non_string(self):
        """Негативный тест: не строка"""
        with pytest.raises(AttributeError):
            self.utils.trim(None)
    
    # ===== Тесты для contains =====
    def test_contains_positive_exists(self):
        """Позитивный тест: символ существует"""
        result = self.utils.contains("SkyPro", "S")
        assert result is True
    
    def test_contains_positive_not_exists(self):
        """Позитивный тест: символ не существует"""
        result = self.utils.contains("SkyPro", "U")
        assert result is False
    
    def test_contains_positive_substring(self):
        """Позитивный тест: подстрока существует"""
        result = self.utils.contains("SkyPro", "ky")
        assert result is True
    
    def test_contains_positive_case_sensitive(self):
        """Позитивный тест: проверка регистра"""
        result = self.utils.contains("SkyPro", "s")
        assert result is False
    
    def test_contains_positive_empty_string(self):
        """Позитивный тест: пустая строка"""
        result = self.utils.contains("", "a")
        assert result is False
    
    def test_contains_positive_empty_symbol(self):
        """Позитивный тест: пустой искомый символ"""
        result = self.utils.contains("SkyPro", "")
        assert result is False  # Внимание: пустая строка всегда является подстрокой!
    
    def test_contains_positive_both_empty(self):
        """Позитивный тест: обе строки пустые"""
        result = self.utils.contains("", "")
        assert result is False
    
    def test_contains_negative_non_string(self):
        """Негативный тест: не строка"""
        with pytest.raises(AttributeError):
            self.utils.contains(None, "a")
    
    # ===== Тесты для delete_symbol =====
    def test_delete_symbol_positive_single_char(self):
        """Позитивный тест: удаление одного символа"""
        result = self.utils.delete_symbol("SkyPro", "k")
        assert result == "SyPro"
    
    def test_delete_symbol_positive_substring(self):
        """Позитивный тест: удаление подстроки"""
        result = self.utils.delete_symbol("SkyPro", "Pro")
        assert result == "Sky"
    
    def test_delete_symbol_positive_multiple_occurrences(self):
        """Позитивный тест: несколько вхождений"""
        result = self.utils.delete_symbol("hello world", "l")
        assert result == "heo word"
    
    def test_delete_symbol_positive_not_found(self):
        """Позитивный тест: символ не найден"""
        result = self.utils.delete_symbol("SkyPro", "x")
        assert result == "SkyPro"
    
    def test_delete_symbol_positive_all_occurrences(self):
        """Позитивный тест: удаление всех символов"""
        result = self.utils.delete_symbol("aaaaa", "a")
        assert result == ""
    
    def test_delete_symbol_positive_empty_string(self):
        """Позитивный тест: пустая строка"""
        result = self.utils.delete_symbol("", "a")
        assert result == ""
    
    def test_delete_symbol_positive_empty_symbol(self):
        """Позитивный тест: пустой символ для удаления"""
        result = self.utils.delete_symbol("SkyPro", "")
        assert result == "SkyPro"
    
    def test_delete_symbol_negative_non_string(self):
        """Негативный тест: не строка"""
        with pytest.raises(AttributeError):
            self.utils.delete_symbol(None, "a")