import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope="function")
def page(playwright: Playwright) -> None:
    print("\nStarting browser...")
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.set_viewport_size({"width": 1800, "height": 1000})
    yield page
    page.close()
    context.close()
    browser.close()
    print("\nBrowser closed...")


