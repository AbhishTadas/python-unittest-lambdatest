import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from parameterized import parameterized
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from concurrent.futures import ThreadPoolExecutor


def get_browser_options(browser):
    """Return browser-specific options with LambdaTest capabilities"""
    lt_options = {
        "username": username,
        "accessKey": access_key,
        "network": True,
        "build": "Selenium 4 Example",
        "name": f"Selenium 4 Test - {browser}",
        "w3c": True,
        "plugin": "python-python",
        "video": True,
        "platform": "Windows 10",
        browser.lower(): {
            "version": "latest"
        }
    }

    if browser == "Chrome":
        options = ChromeOptions()
    elif browser == "Firefox":
        options = FirefoxOptions()
    elif browser == "Edge":
        options = EdgeOptions()

    options.set_capability("LT:Options", lt_options)
    return options


class FirstSampleTest(unittest.TestCase):
    def setUp(self):
        """Run once before each test method"""
        pass

    def tearDown(self):
        """Run once after each test method"""
        if hasattr(self, 'driver'):
            self.driver.quit()

    @parameterized.expand([
        ("Chrome",),
        ("Firefox",),
        ("Edge",)
    ])
    def test_Scenario_1(self, browser):
        """Test demo site with parameterized browsers"""
        options = get_browser_options(browser)
        self.driver = webdriver.Remote(
            command_executor="https://hub.lambdatest.com:443/wd/hub",
            options=options,
        )
        driver = self.driver
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(30)
        driver.set_window_size(1920, 1080)

        driver.get("https://www.lambdatest.com/selenium-playground/")
        driver.find_element(By.XPATH, '//a[normalize-space()="Simple Form Demo"]').click()
        url = driver.current_url
        assert "simple-form-demo" in url.lower(), f"URL '{url}' does not contain expected text"
        welcome = "Welcome to LambdaTest"
        driver.find_element(By.ID, "user-message").send_keys(welcome)
        driver.find_element(By.ID, "showInput").click()
        message = driver.find_element(By.XPATH,
                                      "//label[contains(text(),'Your Message: ')]/following-sibling::p").get_attribute(
            "innerText")
        assert message == welcome, f"Expected message '{welcome}' but got '{message}'"

    @parameterized.expand([
        ("Chrome",),
        ("Firefox",),
        ("Edge",)
    ])
    def test_Scenario_2(self, browser):
        """Test demo site with parameterized browsers"""
        options = get_browser_options(browser)
        self.driver = webdriver.Remote(
            command_executor="https://hub.lambdatest.com:443/wd/hub",
            options=options,
        )
        driver = self.driver
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(30)

        driver.maximize_window()
        driver.get("https://www.lambdatest.com/selenium-playground/")
        driver.find_element(By.XPATH, '//a[normalize-space()="Drag & Drop Sliders"]').click()
        # Get slider element
        slider = driver.find_element(By.XPATH, '//input[@value=15]')
        action = ActionChains(driver)
        action.drag_and_drop_by_offset(slider, 215, 0).perform()
        # Verify final value is 95
        final_value = driver.find_element(By.ID, 'rangeSuccess').get_attribute("innerText")
        assert final_value == '95', f"Expected message 95 but got '{final_value}'"

    @parameterized.expand([
        ("Chrome",),
        ("Firefox",),
        ("Edge",)
    ])
    def test_Scenario_3(self, browser):
        """Test alerts with parameterized browsers"""
        options = get_browser_options(browser)
        self.driver = webdriver.Remote(
            command_executor="https://hub.lambdatest.com:443/wd/hub",
            options=options,
        )
        driver = self.driver
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(30)

        driver.get("https://www.lambdatest.com/selenium-playground/")
        driver.find_element(By.XPATH, "//a[normalize-space()='Input Form Submit']").click()
        driver.find_element(By.CLASS_NAME, "bg-lambda-900").click()
        error = driver.switch_to.active_element.get_attribute("validationMessage")
        assert error == "Please fill out this field."
        driver.find_element(By.XPATH, "//input[@id='name']").send_keys("John Doe")
        driver.find_element(By.XPATH, "//input[@id='inputEmail4']").send_keys("JohnDoe@gmail.com")
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys("qwerty")
        driver.find_element(By.XPATH, "//input[@id='company']").send_keys("Automation")
        driver.find_element(By.XPATH, "//input[@id='websitename']").send_keys("www.JohnDoeAutomation.com")
        Select(driver.find_element(By.NAME, "country")).select_by_visible_text("Afghanistan")
        driver.find_element(By.XPATH, "//input[@id='inputCity']").send_keys("Kabul")
        driver.find_element(By.XPATH, "//input[@id='inputAddress1']").send_keys("ABC")
        driver.find_element(By.XPATH, "//input[@id='inputAddress2']").send_keys("DEF")
        driver.find_element(By.XPATH, "//input[@id='inputState']").send_keys("state")
        driver.find_element(By.XPATH, "//input[@id='inputZip']").send_keys("123456")
        driver.find_element(By.CLASS_NAME, "bg-lambda-900").click()
        success = driver.find_element(By.CLASS_NAME, "success-msg").get_attribute("innerText")
        assert "Thanks for contacting us, we will get back to you shortly." == success


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(unittest.main)
