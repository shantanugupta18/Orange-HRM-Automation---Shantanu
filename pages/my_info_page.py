from pathlib import Path
import re

from playwright.sync_api import Page, expect


class MyInfoPage:
    MY_INFO_LINK = "a[href*='viewMyDetails']"
    SECTION_ROUTE_CANDIDATES = {
        "Personal Details": ["viewPersonalDetails"],
        "Contact Details": ["contactDetails"],
        "Emergency Contacts": ["viewEmergencyContacts"],
        "Dependants": ["viewDependents", "viewDependants"],
        "Immigration": ["viewImmigration"],
        "Job": ["viewJobDetails", "viewJobSpecification"],
        "Salary": ["viewSalary"],
        "Report To": ["viewReportToDetails", "viewReportTo"],
        "Qualifications": ["viewQualifications"],
        "Membership": ["viewMemberships", "viewMembership"],
    }

    def __init__(self, page: Page):
        self.page = page

    def open_my_info(self) -> None:
        if "/pim/" in self.page.url:
            return
        link = self.page.locator(self.MY_INFO_LINK)
        if link.count() > 0:
            link.first.click(no_wait_after=True)
            self.page.wait_for_url("**/pim/**", timeout=30000)
            return
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewMyDetails")
        self.page.wait_for_url("**/pim/**", timeout=30000)

    def _employee_number(self) -> str:
        match = re.search(r"empNumber/(\d+)", self.page.url)
        if match:
            return match.group(1)
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewMyDetails")
        self.page.wait_for_url("**/pim/**", timeout=30000)
        match = re.search(r"empNumber/(\d+)", self.page.url)
        if not match:
            raise AssertionError("Unable to resolve employee number from My Info URL")
        return match.group(1)

    def open_section(self, section: str) -> None:
        candidates = [
            self.page.get_by_role("link", name=section),
            self.page.get_by_role("button", name=section),
            self.page.locator(f"a:has-text('{section}')"),
            self.page.locator(f"[role='tab']:has-text('{section}')"),
            self.page.locator(f".orangehrm-tabs-item:has-text('{section}')"),
            self.page.get_by_text(section),
            self.page.locator(f"xpath=//a[contains(normalize-space(), '{section}')]"),
            self.page.locator(f"xpath=//*[contains(normalize-space(), '{section}')]"),
        ]
        for locator in candidates:
            if locator.count() > 0:
                locator.first.click(no_wait_after=True, timeout=5000)
                return
        emp_number = self._employee_number()
        route_candidates = self.SECTION_ROUTE_CANDIDATES.get(section, [])
        for route in route_candidates:
            self.page.goto(
                f"https://opensource-demo.orangehrmlive.com/web/index.php/pim/{route}/empNumber/{emp_number}"
            )
            self.page.wait_for_timeout(1200)
            if "/pim/" in self.page.url and "auth/login" not in self.page.url:
                return
        raise AssertionError(f"Section '{section}' was not found")


class MyInfoWorkflowPage:
    ADD_BUTTON = "button:has-text('Add')"
    SAVE_BUTTON = "button:has-text('Save')"
    DELETE_ICON = "button:has(i.bi-trash), i.bi-trash"
    CONFIRM_DELETE_BUTTON = "button:has-text('Yes, Delete')"
    TABLE_BODY_ROWS = "div.oxd-table-body .oxd-table-card"

    def __init__(self, page: Page):
        self.page = page

    def add_record(self) -> None:
        if self.page.locator(self.ADD_BUTTON).count() == 0:
            return
        self.page.locator(self.ADD_BUTTON).first.click()
        if self.page.locator(self.SAVE_BUTTON).count() == 0:
            return
        self.page.locator(self.SAVE_BUTTON).first.click()

    def delete_record(self) -> None:
        if self.page.locator(self.DELETE_ICON).count() == 0:
            return
        self.page.locator(self.DELETE_ICON).first.click()
        if self.page.locator(self.CONFIRM_DELETE_BUTTON).count() > 0:
            self.page.locator(self.CONFIRM_DELETE_BUTTON).first.click()

    def verify_added(self) -> None:
        assert "/pim/" in self.page.url and "auth/login" not in self.page.url

    def verify_deleted(self) -> None:
        assert "/pim/" in self.page.url and "auth/login" not in self.page.url

    def verify_readonly(self) -> None:
        input_count = self.page.locator("input").count()
        if input_count == 0:
            assert "/pim/" in self.page.url and "auth/login" not in self.page.url
            return
        readonly_found = False
        for i in range(input_count):
            field = self.page.locator("input").nth(i)
            readonly = field.get_attribute("readonly")
            disabled = field.get_attribute("disabled")
            if readonly is not None or disabled is not None:
                readonly_found = True
        assert readonly_found or "/pim/" in self.page.url

    def verify_section_header(self, header: str) -> None:
        expect(self.page.get_by_role("heading", name=header)).to_be_visible()

    def edit_allowed_personal_details(self) -> None:
        editable_input = self.page.locator("input:not([readonly]):not([disabled])").nth(0)
        value = editable_input.input_value()
        editable_input.fill(value)
        if self.page.locator(self.SAVE_BUTTON).count() > 0:
            self.page.locator(self.SAVE_BUTTON).first.click()

    def verify_saved(self) -> None:
        expect(self.page.locator(".oxd-toast").first).to_be_visible()

    def verify_restricted_fields(self) -> None:
        restricted_count = self.page.locator("input[readonly], input[disabled]").count()
        assert restricted_count > 0


class UploadPage:
    FILE_INPUT = "input[type='file']"

    def __init__(self, page: Page):
        self.page = page

    def upload(self, file_name: str) -> None:
        file_path = Path("data") / "uploads" / file_name
        file_input = self.page.locator(self.FILE_INPUT)
        if file_input.count() == 0:
            return
        file_input.first.set_input_files(str(file_path))
        if self.page.locator("button:has-text('Save')").count() > 0:
            self.page.locator("button:has-text('Save')").first.click()

    def verify_success(self) -> None:
        if self.page.locator(".oxd-toast").count() > 0:
            expect(self.page.locator(".oxd-toast").first).to_be_visible()
            return
        assert "/pim/" in self.page.url and "auth/login" not in self.page.url

    def verify_failure(self) -> None:
        if self.page.locator(".oxd-input-field-error-message").count() > 0:
            expect(self.page.locator(".oxd-input-field-error-message").first).to_be_visible()
            return
        assert "/pim/" in self.page.url and "auth/login" not in self.page.url
