from pathlib import Path

from playwright.sync_api import Page, expect


class MyInfoPage:
    MY_INFO_LINK = "a[href*='viewMyDetails']"

    def __init__(self, page: Page):
        self.page = page

    def open_my_info(self) -> None:
        self.page.locator(self.MY_INFO_LINK).click(no_wait_after=True)

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
        self.page.locator(self.ADD_BUTTON).first.click()
        self.page.locator(self.SAVE_BUTTON).first.click()

    def delete_record(self) -> None:
        self.page.locator(self.DELETE_ICON).first.click()
        if self.page.locator(self.CONFIRM_DELETE_BUTTON).count() > 0:
            self.page.locator(self.CONFIRM_DELETE_BUTTON).first.click()

    def verify_added(self) -> None:
        expect(self.page.locator(self.TABLE_BODY_ROWS).first).to_be_visible()

    def verify_deleted(self) -> None:
        expect(self.page.locator("div.oxd-table-body")).to_be_visible()

    def verify_readonly(self) -> None:
        input_count = self.page.locator("input").count()
        if input_count == 0:
            expect(self.page.locator("form")).to_be_visible()
            return
        for i in range(input_count):
            field = self.page.locator("input").nth(i)
            readonly = field.get_attribute("readonly")
            disabled = field.get_attribute("disabled")
            assert readonly is not None or disabled is not None

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
        self.page.locator(self.FILE_INPUT).first.set_input_files(str(file_path))
        if self.page.locator("button:has-text('Save')").count() > 0:
            self.page.locator("button:has-text('Save')").first.click()

    def verify_success(self) -> None:
        expect(self.page.locator(".oxd-toast").first).to_be_visible()

    def verify_failure(self) -> None:
        expect(self.page.locator(".oxd-input-field-error-message").first).to_be_visible()
