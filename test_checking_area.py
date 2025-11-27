def common():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait

    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10, poll_frequency=2)

    return driver, wait


def test_income_calculator():
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC

    driver, wait = common()   # use this driver ONLY

    print("line 1")

    driver.get("https://payrup.com/")

    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Become a Merchant']"))).click()

    print("line 2")

    # switch tab
    driver.switch_to.window(driver.window_handles[1])
    print("Switched to new tab")
  
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Income Calculator']"))).click()
    print("line 5")

    for i in range(3):
        wait.until(EC.element_to_be_clickable((By.ID, f":r{i}:"))).send_keys("4")

    print("line 8")

    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Calculate']"))).click()
    print("line 9")
