from pytest_bdd import when, then

@when('the user uploads "{file}"')
def upload(upload_page, file):
    upload_page.upload(file)

@then("Upload successful")
def upload_success(upload_page):
    upload_page.verify_success()

@then("Validation failed")
def upload_failed(upload_page):
    upload_page.verify_failure()