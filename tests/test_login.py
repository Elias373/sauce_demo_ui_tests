import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.menu_page import MenuPage


@allure.suite("Authentication")
class TestLogin:

    @allure.title("Successful Login")
    def test_successful_login(self, browser_setup):
        login_page = LoginPage()
        main_page = MainPage()
        with allure.step("Open login page"):
            login_page.open()
        with allure.step("Enter valid credentials"):
            login_page.login("standard_user", "secret_sauce")
        with allure.step("Verify user is logged in"):
            main_page.should_be_loaded()

    @allure.title("Failed Login")
    def test_failed_login(self, browser_setup):
        login_page = LoginPage()
        with allure.step("Open login page"):
            login_page.open()
        with allure.step("Enter invalid credentials"):
            login_page.login("invalid_user", "invalid_password")
        with allure.step("Verify error message is shown"):
            login_page.should_have_error(
                "Epic sadface: Username and password do not match any user in this service"
            )

    @allure.title("Logout")
    def test_logout(self, logged_in_main_page):
        menu_page = MenuPage()
        with allure.step("Perform success logout"):
            menu_page.logout()
