"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture
def book():
    return Product("book", 100, "This is a book", 1000)
@pytest.fixture
def magazine():
    return Product("magazine", 100, "This is a book", 1000)

@pytest.fixture
def sudoku():
    return Product("sudoku", 100.05, "This is a book", 1000)




class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, book, magazine):

        assert book.check_quantity(50) == True
        assert magazine.check_quantity(1050) == False

        with pytest.raises(ValueError):
            book.check_quantity(0)
            #assert book.check_quantity(0) is ValueError

    def test_product_buy(self, book):

        book.buy(50)
        assert book.quantity == 950

    def test_product_buy_more_than_available(self, book):
        with pytest.raises(ValueError):
            book.buy(1001)
            #assert book.buy(2000) is ValueError


@pytest.fixture
def cart():
    return Cart()


class TestCart:
    def test_add_product(self, cart, book, magazine, sudoku):

        with pytest.raises(ValueError):
            assert cart.add_product(book, 0) is ValueError

        cart.add_product(book, 10)
        assert cart.products[book] == 10

        cart.add_product(magazine, 7)
        assert cart.products[magazine] == 7

        cart.add_product(book)
        assert cart.products[book] == 11

        cart.add_product(book, 10)
        assert cart.products[book] == 21

    def test_remove_product(self, cart, book, magazine, sudoku):
        cart.add_product(sudoku, 10)
        cart.add_product(magazine, 7)

        cart.remove_product(book)
        assert book not in cart.products.keys()

        cart.remove_product(sudoku, 5)
        assert cart.products[sudoku] == 5

        cart.remove_product(sudoku, 5)
        assert sudoku not in cart.products.keys()

        cart.remove_product(magazine, 9)
        assert magazine not in cart.products.keys()

    def test_clear(self, cart, sudoku, magazine):
        cart.add_product(sudoku, 10)
        cart.add_product(magazine, 7)

        cart.clear()
        assert len(cart.products) == 0

    def test_get_total_price(self, cart, sudoku, magazine):
        cart.add_product(sudoku, 10)
        cart.add_product(magazine, 7)

        cart.get_total_price()
        assert cart.get_total_price() == 1700.5

    def test_buy(self, cart, sudoku, magazine):
        cart.add_product(sudoku, 10)
        cart.add_product(magazine, 7)

        cart.buy()
        assert sudoku.quantity == 990
        assert magazine.quantity == 993

        cart.add_product(sudoku, 1050)
        with pytest.raises(ValueError):
            cart.buy()
            #assert cart.buy() is ValueError