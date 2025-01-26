from playwright.sync_api import Page, expect


""" 
Load main page
"""
def test_get_homepage(page, test_web_address):
    page.goto(f"http://{test_web_address}/")
    expect(page.locator(".t-subheading")).to_have_text("Choose Your Move")
    # ^^ TBC on .t-subheading

"""
Select/input a move and subit
    >> checking redirected to Results page once a move played
"""
# def test_get_homepage(page, test_web_address):
#     page.goto(f"http://{test_web_address}/")
#     page.fill("input[name='your_move]", "Rock")
#     page.click("text=Let's Battle!")
#     expect(page.locator("h1")).to_have_text("Result")