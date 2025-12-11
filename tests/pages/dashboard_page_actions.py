from tests.pages.base_page import BasePage
from tests.pages.locators.dashboard_locator import DashboardLocator


class DashboardPageActions(BasePage):

    def verify_dashboard_page(self):
        actual_title = self.get_text(DashboardLocator.TITLE_TEXT)
        assert actual_title == "Dashboard", f"Dashboard title mismatch. Expected 'Dashboard', got '{actual_title}'"

    def click_logout_button(self):
        self.click(DashboardLocator.LogOut_Drop_Down_BUTTON)
        self.click(DashboardLocator.LogOut_Button)
