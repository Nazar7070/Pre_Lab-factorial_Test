"""
Тестовий файл для оригінального коду (original_code.py).

Коментарі:
- Тестові дані представлені у вигляді рядків.
- Простий функціональний підхід без класів.
- Менша модульність, деяка дубльованість коду.
"""
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from refactored_code import process_user_data, User


def test_case_1():
    data = ["Alice, Smith, 19, alice@example.com"]
    result = process_user_data(data)
    assert len(result) == 1
    assert result[0]['first_name'] == "Alice"

def test_case_2():
    data = ["Bob, Brown, 17, bob@example.com"]
    result = process_user_data(data)
    assert len(result) == 0  # вік менше 18

def test_case_3():
    data = []
    result = process_user_data(data)
    assert result == []

def test_case_4():
    data = ["Carol, Jones, 25, carol@example.com"]
    result = process_user_data(data)
    assert result[0]['last_name'] == "Jones"

def test_case_5():
    data = ["Dave, White, 20, dave@example.com", "Eve, Black, 16, eve@example.com"]
    result = process_user_data(data)
    assert len(result) == 1
    assert result[0]['first_name'] == "Dave"

def test_case_6():
    data = ["Invalid Data"]
    result = process_user_data(data)
    assert result == []

def test_case_7():
    data = ["John, Doe, abc, john@example.com"]
    result = process_user_data(data)
    assert result == []  # некоректний вік

def test_case_8():
    data = ["Anna, Taylor, 18, anna@example.com"]
    result = process_user_data(data)
    assert len(result) == 1
    assert result[0]['age'] == 18

def test_case_9():
    data = ["Mark, , 22, mark@example.com"]
    result = process_user_data(data)
    assert len(result) == 1
    assert result[0]['last_name'] == ""

def test_case_10():
    data = [" , Lee, 30, lee@example.com"]
    result = process_user_data(data)
    assert len(result) == 1
    assert result[0]['first_name'] == ""

def test_case_11():
    data = ["Kate, Green, 0, kate@example.com"]
    result = process_user_data(data)
    assert len(result) == 0  # вік 0 - не проходить

def test_case_12():
    data = ["Sam, Wilson, 120, sam@example.com"]
    result = process_user_data(data)
    assert len(result) == 1

def test_case_13():
    data = ["Peter, Parker, 21, peter@example.com"]
    result = process_user_data(data)
    assert result[0]['email'] == "peter@example.com"

def test_case_14():
    data = ["Lucy, Hale, 19"]
    result = process_user_data(data)
    assert result == []  # недостатньо полів

def test_case_15():
    data = ["Tom, Hardy, 25, tom@example.com", "Jerry, Mouse, 17, jerry@example.com"]
    result = process_user_data(data)
    assert len(result) == 1
    assert result[0]['first_name'] == "Tom"

def test_case_16():
    data = [" ", " , , , "]
    result = process_user_data(data)
    assert result == []

def test_case_17():
    data = ["Nina, Brown, 18, nina@example.com"]
    result = process_user_data(data)
    assert len(result) == 1

def test_case_18():
    data = ["Oleg, Ivanov, 19, oleg@example.com", "Olga, Petrova, 20, olga@example.com"]
    result = process_user_data(data)
    assert len(result) == 2

def test_case_19():
    data = ["Invalid, Data, 19"]
    result = process_user_data(data)
    assert result == []

def test_case_20():
    data = ["Max, Payne, -1, max@example.com"]
    result = process_user_data(data)
    assert len(result) == 0  # від’ємний вік
