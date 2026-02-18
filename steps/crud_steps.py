from pytest_bdd import when, then

@when("the user adds a new record")
def add_record(context_page):
    context_page.add_record()

@when("the user deletes a record")
def delete_record(context_page):
    context_page.delete_record()

@then("the record should appear in the table")
def verify_added(context_page):
    context_page.verify_added()

@then("the record should be removed from the table")
def verify_deleted(context_page):
    context_page.verify_deleted()