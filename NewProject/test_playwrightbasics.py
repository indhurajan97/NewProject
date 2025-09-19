import time
from playwright.sync_api import Page
def test_basics(page:Page):
     page.goto("https://www.saucedemo.com/")
     page.get_by_placeholder("Username").fill("standard_user")
     page.get_by_placeholder("Password").fill("secret_sauce")
     page.get_by_role("button",name="Login").click()
     time.sleep(5)
     slb = page.locator("inventory_item").filter(has_text="Sauce Labs Backpack")
     page.locator("btn btn_primary btn_small btn_inventory").filter(has_text="add-to-cart-sauce-labs-backpack").click()











