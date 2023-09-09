from playwright.sync_api import Page, Playwright

from test_basic.pages.first_page import FirstPage
from test_basic.urls.ulr import BASE_URL
from test_basic.locators.first_loc import First


class TestFirstPage:
    locator = First

    def test_first_test(self, page: Page) -> None:
        page = FirstPage(page, BASE_URL)
        page.open()
        page.login()
        product_header = page.return_element_by_locator(self.locator.PRODUCT_HEADER)
        assert product_header.is_visible(), "Product header is not visible"

    def test_second_test(self, page: Page) -> None:
        page = FirstPage(page, BASE_URL)
        page.open()
        page.login()
        page.logout()
        assert page.get_url() == "https://www.saucedemo.com/v1/index.html", "URL is not correct"

    def test_second_test1(self, playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.saucedemo.com/v1/")
        page.pause()
        page.locator("input[id='user-name']").fill("standard_user")
        page.locator("input[id='password']").fill("secret_sauce")
        page.locator("input[id='login-button']").click()
        page.locator("div[class='bm-burger-button']").click()
        page.locator("a[id='logout_sidebar_link']").click()
        assert page.url == "https://www.saucedemo.com/v1/index.html", "URL is not correct"
        page.close()
        context.close()
        browser.close()



