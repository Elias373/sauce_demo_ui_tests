import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage

login = LoginPage()
main = MainPage()
cart = CartPage()



@allure.title("1. Успешный логин")
def test_successful_login():
    login.open().login('standard_user', 'secret_sauce')
    main.should_be_loaded()

@allure.title("2. Добавление товара в корзину и проверка")
def test_add_item_to_cart():
    login.open().login('standard_user', 'secret_sauce')
    main.add_item_to_cart('add-to-cart-sauce-labs-backpack')
    main.cart_should_have_count(1)
    main.go_to_cart()
    cart.should_contain_item('Sauce Labs Backpack')

@allure.title("3. Открытие страницы About")
def test_open_about_page():
    login.open().login('standard_user', 'secret_sauce')
    main.open_about_page()
    main.should_be_on_about_page()

@allure.title("4. Успешный логаут")
def test_successful_logout():
    login.open().login('standard_user', 'secret_sauce')
    main.logout()
    login.should_be_loaded()

@allure.title("5. Неуспешный логин")
def test_failed_login():
    login.open().login('invalid_user', 'invalid_password')
    login.should_have_error('Username and password do not match')