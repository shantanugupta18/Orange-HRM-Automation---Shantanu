from pytest_bdd import parsers, then, when

from pages.my_info_page import MyInfoWorkflowPage


@when("the user navigates to My Info section")
def go_myinfo(page) -> None:
    page.click("a[href*='viewMyDetails']")


@then("the requested section should be visible")
def verify_visible(page) -> None:
    assert page.locator("div.orangehrm-edit-employee-content").is_visible()


@then(parsers.parse('the page header should be "{header}"'))
def verify_page_header(context_page: MyInfoWorkflowPage, header: str) -> None:
    context_page.verify_section_header(header)


@when("the user edits allowed personal details")
def edit_allowed_personal_details(context_page: MyInfoWorkflowPage) -> None:
    context_page.edit_allowed_personal_details()


@then("changes should be saved successfully")
def verify_saved_changes(context_page: MyInfoWorkflowPage) -> None:
    context_page.verify_saved()


@then("restricted fields should be non-editable")
def verify_restricted_fields(context_page: MyInfoWorkflowPage) -> None:
    context_page.verify_restricted_fields()
