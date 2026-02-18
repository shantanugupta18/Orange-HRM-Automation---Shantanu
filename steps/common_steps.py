from pytest_bdd import when, then

@when("the user navigates to My Info section")
def go_myinfo(page):
    page.click('a[href*="viewMyDetails"]')

@then("the requested section should be visible")
def verify_visible(page):
    assert page.locator("h6").is_visible()
