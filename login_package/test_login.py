def test_login():##############################################################################################################
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument("--start-maximized")

    # service = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
    # driver = webdriver.Chrome(service=service, options=options)

    driver=webdriver.Chrome(options=options)

    driver.get("https://payrup.com/")

    wait = WebDriverWait(driver, 5)  # wait up to 15 seconds

    # 1️⃣ Click the element to open login/OTP section
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div[2]/div/div[5]/div"))).click()

    # 2️⃣ Enter phone number
    wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/div/div/div[2]/div[1]/div/input"))).send_keys("9066353121")

    # 3️⃣ Click the “Continue” or “Send OTP” button
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/div/div[2]/div[2]/button"))).click()

    # 4️⃣ Enter OTP “9999”
    wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/div/div/div[2]/form/div[1]/div/input"))).send_keys("9999")


    toast = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'User logged in successfully')]")))

    # Get text
    toast_message = toast.text
    print("Captured Message:", toast_message)

    # Compare with expected result
    expected_message = "User logged in successfully."
    if toast_message.strip() == expected_message:
        print("✅ Test Passed: Login success message matched.")
    else:
        print("❌ Test Failed: Expected:", expected_message, "| Got:", toast_message)


    print("✅ Chrome launched and 9999 entered successfully!")