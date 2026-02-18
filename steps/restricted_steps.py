from pytest_bdd import then

from pages.my_info_page import MyInfoWorkflowPage


@then("all fields should be non-editable")
def verify_readonly(context_page: MyInfoWorkflowPage) -> None:
    context_page.verify_readonly()
