from selenium.webdriver.common.by import By


class DashboardLocator:
    TITLE_TEXT = (By.CLASS_NAME, "oxd-topbar-header-breadcrumb")
    LogOut_Drop_Down_BUTTON = (By.CLASS_NAME, "oxd-userdropdown-icon")
    LogOut_Button = (By.LINK_TEXT, "Logout")