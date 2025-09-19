from playwright.sync_api import Playwright
from utils.apiutils import APIUtils
def e2eapi(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    apiutils = APIUtils()
    apiutils.create_order(playwright)

    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_placeholder("email@example.com").fill("indhurajan019@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Indhu1997#")
    page.get_by_role("button", name="login").click()
