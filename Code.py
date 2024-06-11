import time
from playwright.sync_api import sync_playwright

with sync_playwright() as pw:
    browser = pw.firefox.launch(
        headless=False,
    )

# View count desc
    page = browser.new_page()
    page1 = browser.new_page()
    page2 = browser.new_page()

# Number_of_likes desc
    page3 = browser.new_page()
    page4 = browser.new_page()
    page5 = browser.new_page()

    page.goto('https://x.com/Minions_Fanboy/status/1797831541139337276')

    page1.goto('https://x.com/Fandango/status/1798339261306945931')

    page2.goto('https://x.com/NoticiasUgc/status/1798314273237840022')

    page3.goto('https://x.com/Minions_Fanboy/status/1798730906733277465')

    page4.goto('https://x.com/DM4HypeGuy/status/1797995359425470628')

    page5.goto('https://x.com/DM4HypeGuy/status/1797984230980645008')

    time.sleep(60)

    # scroll to the bottom of page

    show_more = page.locator("button", has_text="Show More")
    show_more1 = page1.locator("button", has_text="Show More")
    show_mor2 = page2.locator("button", has_text="Show More")
    show_more3 = page3.locator("button", has_text="Show More")
    show_more4 = page4.locator("button", has_text="Show More")
    show_more5 = page5.locator("button", has_text="Show More")