from pytest_bdd import when
from pages.my_info_page import MyInfoPage

@when("the user navigates to My Info")
def open_my_info(my_info_page: MyInfoPage):
    my_info_page.open_my_info()

@when('the user opens "{section}" section')
def open_section(my_info_page: MyInfoPage, section):
    my_info_page.open_section(section)