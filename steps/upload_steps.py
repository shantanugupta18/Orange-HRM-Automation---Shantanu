from pytest_bdd import parsers, then, when

from pages.my_info_page import UploadPage


@when(parsers.parse('the user uploads "{file}"'))
def upload(upload_page: UploadPage, file: str) -> None:
    upload_page.upload(file)


@then("Upload successful")
def upload_success(upload_page: UploadPage) -> None:
    upload_page.verify_success()


@then("Validation failed")
def upload_failed(upload_page: UploadPage) -> None:
    upload_page.verify_failure()


@then(parsers.parse('"{outcome}" should be shown'))
def upload_outcome(upload_page: UploadPage, outcome: str) -> None:
    normalized = outcome.strip().lower()
    if normalized == "upload successful":
        upload_page.verify_success()
        return
    upload_page.verify_failure()
