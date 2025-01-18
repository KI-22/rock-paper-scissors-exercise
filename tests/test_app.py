from playwright.sync_api import Page, expect

def test_get_homepage(page, test_web_address):
    page.goto(f"http://{test_web_address}/")
    expect(page.locator(".t-title")).to_have_text("Hello :)")