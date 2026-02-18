from pytest_bdd import then

@then("all fields should be non-editable")
def verify_readonly(context_page):
    context_page.verify_readonly()