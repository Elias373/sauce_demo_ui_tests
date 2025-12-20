import pytest
from selene import browser
from selenium import webdriver
from dotenv import load_dotenv
import os
from utils import attach


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function')
def browser_setup():
    browser.config.base_url = 'https://www.saucedemo.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 10.0

    selenoid_login = os.getenv('SELENOID_LOGIN', 'user1')
    selenoid_password = os.getenv('SELENOID_PASSWORD', '1234')

    options = webdriver.ChromeOptions()

    options.set_capability('goog:loggingPrefs', {
        'browser': 'ALL',
        'performance': 'ALL',
        'driver': 'ALL'
    })


    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "128.0")
    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": True
    })


    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()



@pytest.fixture
def logged_in_main_page(browser_setup):
    from pages.login_page import LoginPage
    from pages.main_page import MainPage

    login_page = LoginPage()
    login_page.open().login('standard_user', 'secret_sauce')
    return MainPage()