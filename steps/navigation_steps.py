from pytest_bdd import given, parsers, when

from pages.my_info_page import MyInfoPage


@given("the user navigates to My Info")
@when("the user navigates to My Info")
def open_my_info(my_info_page: MyInfoPage) -> None:
    my_info_page.open_my_info()


@given(parsers.parse('the user opens "{section}" section'))
@when(parsers.parse('the user opens "{section}" section'))
def open_section(my_info_page: MyInfoPage, section: str) -> None:
    my_info_page.open_section(section)
