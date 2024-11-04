import pytest

# Определяем функции для тестирования
def multy(a, c):
    return a * c

def delen(a, c):
    return a / c

# Тесты
def test_multy():
    # Проверяем корректное умножение
    assert multy(2, 3) == 6
    assert multy(-1, 5) == -5
    assert multy(0, 10) == 0
    assert multy(0.1, 0.2) == pytest.approx(0.02, rel=1e-2)

def test_delen():
    # Проверяем корректное деление
    assert delen(6, 2) == 3
    assert delen(-10, 2) == -5
    assert delen(5, 1) == 5

    # Проверяем деление на дробь
    assert delen(1, 0.5) == pytest.approx(2, rel=1e-2)

    # Проверяем деление на ноль (ожидаем исключение)
    with pytest.raises(ZeroDivisionError):
        delen(10, 0)

# Запуск тестов можно выполнить через команду терминала:
# pytest имя_файла.py


# Запуск тестов
if __name__ == '__main__':
    pytest.main()
