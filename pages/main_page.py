from selene import browser, have, be

class MainPage:
    def should_be_loaded(self):
        browser.element('.title').should(have.text('Products'))
        return self

    def add_item_to_cart(self, item_id):
        browser.element(f'#{item_id}').click()
        return self

    def cart_should_have_count(self, count):
        browser.element('.shopping_cart_badge').should(have.text(str(count)))
        return self

    def go_to_cart(self):
        browser.element('.shopping_cart_link').click()
        return self

    def open_about_page(self):
        browser.element('#react-burger-menu-btn').click()
        browser.element('#about_sidebar_link').click()
        return self

    def should_be_on_about_page(self):
        browser.should(have.url_containing('saucelabs.com'))
        return self

    def logout(self):
        browser.element('#react-burger-menu-btn').click()
        browser.element('#logout_sidebar_link').click()
        return self