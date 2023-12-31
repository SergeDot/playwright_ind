from test_basic.locators.first_loc import First


class BasePage:
    locators = First

    def __init__(self, page, url):
        self.page = page
        self.url = url

    def open(self):
        """This method opens a browser by the provided link"""
        self.page.goto(self.url)

    def login(self, username, password):
        self.page.locator(self.locators.USER_NAME).fill(username)
        self.page.locator(self.locators.PASSWORD).fill(password)
        self.page.locator(self.locators.LOGIN_BUTTON).click()

    def logout(self):
        self.page.locator(self.locators.BURGER_MENU).click()
        self.page.locator(self.locators.LOGOUT_LINK).click()

    def return_element_by_locator(self, locator):
        return self.page.locator(locator)

    def get_url(self):
        return self.page.url

    def get_text(self, locator):
        return self.page.locator(locator).inner_text()
