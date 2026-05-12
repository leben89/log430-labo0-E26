"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from calculator import Calculator

def test_app():
    my_calculator = Calculator()
    welcome_message = my_calculator.get_hello_message()
    assert "== Calculatrice v1.0 ==" in welcome_message

def test_addition():
    calc = Calculator()
    assert calc.addition(2, 3) == 5

def test_subtraction():
    calc = Calculator()
    assert calc.subtraction(5, 3) == 2

def test_multiplication():
    calc = Calculator()
    assert calc.multiplication(4, 3) == 12

def test_division():
    calc = Calculator()
    assert calc.division(10, 2) == 5

def test_division_by_zero():
    calc = Calculator()
    assert calc.division(10, 0) == "Erreur : division par zéro"

# def test_addition_echec_volontaire():
#     calc = Calculator()
#     assert calc.addition(2, 2) == 5


