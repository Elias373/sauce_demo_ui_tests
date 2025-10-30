from selene import browser, have


class CartPage:
    def should_be_loaded(self):
        browser.element('.title').should(have.text('Your Cart'))
        return self

    def should_contain_item(self, item_name):
        browser.element('.cart_item').should(have.text(item_name))
        return self

    def should_have_items_count(self, count):
        items = browser.all('.cart_item')
        items.should(have.size(count))
        return self