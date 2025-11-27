def test_income_calculator():################################################################################################

  from selenium import webdriver
  from selenium.webdriver.chrome.service import Service
  from selenium.webdriver.chrome.options import Options
  from selenium.webdriver.support.ui import WebDriverWait
  from selenium.webdriver.support import expected_conditions as EC
  from selenium.webdriver.common.by import By

  options = Options()
  options.add_experimental_option("detach",True)
  options.add_argument("--start-maximized")

  driver = webdriver.Chrome(options=options)

  wait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[Exception])

  print("line 1")

  driver.get("https://payrup.com/")

  become_a_merchant = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[text()='Become a Merchant']")))
  become_a_merchant.click()

  print("line 2")

  # SWITCH TO NEW TAB
  driver.switch_to.window(driver.window_handles[1])
  print("Switched to new tab")
  print("line 3")
  income_cal = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Income Calculator']")))
  print("line 4")
  income_cal.click()
  print("line 5")

  for i in range(3):
    no_of_transaction = wait.until(EC.element_to_be_clickable((By.XPATH,f"//input[@id=':r{i}:']")))
    no_of_transaction.send_keys("4")
  print("line 8")
  cal_btn = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Calculate']")))
  cal_btn.click()
  print("line 9")



















 





