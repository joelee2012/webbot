import time
from functools import wraps

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException


def trace_status(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            print('\t\33[32m[OK]\033[0m')
        except Exception:
            print('\t\033[91m[NOK]\033[0m')
            raise

    return wrapper


class Runner:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def click(self, value, selector='xpath'):
        wait = WebDriverWait(self.driver, self.timeout, ignored_exceptions=(
            ElementClickInterceptedException))
        # selector = getattr(By, selector.upper())
        # element = wait.until(
        #     EC.element_to_be_clickable((selector, value)))
        element = getattr(self.driver, f'find_element_by_{selector}')(value)
        wait.until(lambda x: element.click() or True)

    def input(self, value, text, selector='xpath'):
        elem = getattr(self.driver, f'find_element_by_{selector}')(value)
        elem.send_keys(text)

    def select(self, value, text, selector='xpath'):
        select = Select(
            getattr(self.driver, f'find_element_by_{selector}')(value))
        select.select_by_visible_text(text)

    def dynamic_select(self, value, text, selector='xpath'):
        elem = getattr(self.driver, f'find_element_by_{selector}')(value)
        elem.send_keys(text[:-1])
        wait = WebDriverWait(self.driver, self.timeout)
        pop_selector = (By.XPATH, f'//*[contains(text(),"{text[:-1]}")]')
        element = wait.until(
            EC.visibility_of_element_located(pop_selector))
        element.click()

    def scroll_window(self):
        time.sleep(3)
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

    def assert_contain(self, value, text, selector='xpath'):
        elem = getattr(self.driver, f'find_element_by_{selector}')(value)
        if text not in elem.text:
            raise ValueError(
                f'expect text contain "{text}", but got "{elem.text}"')

    def screenshot(self, filename):
        self.driver.save_screenshot(filename)

    def switch_window(self, index):
        self.driver.switch_to.window(self.driver.window_handles[int(index)])

    # @trace_status
    def run_action(self, action):
        print(f'run {action}', end='')
        try:
            getattr(self, action.name)(**action.args)
            print('\t\33[32m[OK]\033[0m')
        except Exception:
            print('\t\033[91m[NOK]\033[0m')
            self.screenshot(f'screenshot.png')
            raise
