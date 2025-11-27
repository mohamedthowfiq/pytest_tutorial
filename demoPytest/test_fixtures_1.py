import time,pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

@pytest.fixture(autouse=True)
def start_automatic_ficture():
    print("Start Test with automatic fixture")

#another name for post condition is teardown
@pytest.fixture(scope="function")
def setup_teardown():
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(4)
    driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
    driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
    driver.find_element(By.XPATH,"//button[text()=' Login ']").click()
    print("Login in")
    yield
    time.sleep(4)
    driver.find_element(By.XPATH,"//p[@class='oxd-userdropdown-name']").click()
    driver.find_element(By.XPATH,"//a[text()='Logout']").click()
    print("Log out")

def test1_Admin_title(setup_teardown):
    time.sleep(4)
    driver.find_element(By.XPATH,"//span[text()='Admin']").click()
    assert driver.title == "OrangeHRM"
    print("Test 1 is complete")

def test2_PIM_title(setup_teardown):
    time.sleep(4)
    driver.find_element(By.XPATH,"//span[text()='PIM']").click()
    assert driver.title == "OrangeHRM"
    print("Test 2 is complete")
