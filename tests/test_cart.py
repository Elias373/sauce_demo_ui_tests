import allure
from selene import browser, have
from pages.cart_page import CartPage





@allure.suite("Cart")
class TestCart:

    @allure.title("Add Item to Cart")
    @allure.suite("Cart")
    class TestCart:
        @allure.title("Add Item to Cart")
        def test_add_item_to_cart(self, logged_in_main_page):
            cart_page = CartPage()
            with allure.step("Add item to cart"):
                logged_in_main_page.add_item_to_cart('sauce-labs-backpack')
            with allure.step("Verify cart"):
                cart_page.open_cart()
                browser.element('.title').should(have.text('Your Cart'))
                cart_page.should_contain_item('Sauce Labs Backpack')
            with allure.step("Verify item count in cart"):
                cart_page.should_have_items_count(1)

    @allure.title("Remove Item from Cart")
    @allure.title("Remove Item from Cart")
    def test_remove_item_from_cart(self, logged_in_main_page):
        cart_page = CartPage()
        with allure.step("Add item to cart"):
            logged_in_main_page.add_item_to_cart('sauce-labs-backpack')
        with allure.step("Remove item from cart"):
            logged_in_main_page.remove_item_from_cart('sauce-labs-backpack')
        with allure.step("Verify cart is empty"):
            cart_page.open_cart()
            cart_page.should_have_items_count(0)










