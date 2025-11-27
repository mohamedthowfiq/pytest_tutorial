def test_my_phone_book_current_date():#######################################################################################3
    import time
    from datetime import date,datetime
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.add_experimental_option("detach",True)
    options.add_argument("--start-maximized")

    driver=webdriver.Chrome(options=options)
    wait = WebDriverWait(driver,15,poll_frequency=2,ignored_exceptions=[Exception])

    driver.get("http://payrup.com")
    driver.maximize_window()

    #go to sign in box
    signup=wait.until(EC.element_to_be_clickable((By.XPATH,"(//h5[text()='Sign in' ])[2]")))
    signup.click()

    #entering mobile number to sign in
    enter_mobile_no=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder and @type='number']")))
    enter_mobile_no.send_keys("9066353121")

    #checkbox checking
    check_box = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[contains(@class,'MuiButtonBase-root MuiCheckbox-root MuiCheckbox-colorPrimary')]")))
    if check_box.is_selected()==True:
      check_box.click()

    #clicking get otp
    get_otp_btn = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Get OTP']")))
    get_otp_btn.click()

    #OTP entering
    time.sleep(2)
    otp=wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@aria-invalid='false' and @type='number']")))
    otp.send_keys("9999")

    #clicking logged in profile dropdown
    drop=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class,'MuiGrid-root MuiGrid-container') and @aria-haspopup='true']")))
    drop.click()

    #clicking profile in the drop down
    drop_opt=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[text()='Profile']/..")))
    drop_opt.click()

    #click my phone book
    my_phbook=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='My Phonebook']")))
    my_phbook.click()

    time.sleep(2)
    #click add fnds
    add_frnds_btn=wait.until(EC.visibility_of_element_located((By.XPATH,"//span[text()='Add Friends']")))
    add_frnds_btn.click()

    #enter full name
    full_name=wait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='fullName']")))
    full_name.send_keys("xyz")

    #enter email
    email=wait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='email']")))
    email.send_keys("abc@gmail.com")

    ############################################    CLAENDER START       ##########################################
    today = date.today()
    dd = today.strftime("%d")   # Day
    mm = today.strftime("%m")   # Month
    yyyy = today.strftime("%Y") # Year


    #dob click
    dob=wait.until(EC.presence_of_element_located((By.XPATH,"//input[@aria-label='Choose date']")))
    dob.click()

    user_year=yyyy
    user_month=mm
    user_date=dd

    drp_down_yr_arrow_btn = wait.until(EC.presence_of_element_located((By.XPATH,"//button[@aria-label='calendar view is open, switch to year view']")))
    drp_down_yr_arrow_btn.click()

    allyear=wait.until(EC.presence_of_all_elements_located((By.XPATH,"//button[contains(@class,'PrivatePickersYear-yearButton')]")))
    print("length of years:" ,len(allyear))
    print("line 1")
    for year in allyear:
      drp_down_year_choosing = year.text
      if drp_down_year_choosing==user_year:
          year.click()
          break
    print("line 2")   
    #choosing month
    for i in range(1,13):
      month_name=wait.until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'MuiPickersCalendarHeader-label')]"))).text
      # print(month_name)
      d={"1":"january","2":"february","3":"march","4":"april","5":"may","6":"june","7":"july","8":"august","9":"september","10":"october","11":"november","12":"december"}
      if month_name.split(" ")[0].lower() == d[user_month]:
        print("line 3")
        break
      else:
        print("line 4")
        next_month_arrow_btn = wait.until(EC.presence_of_element_located((By.XPATH,"//button[@aria-label='Next month']")))
        next_month_arrow_btn.click()
    print("line 5")
        
    #choosing date
    alldate = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//button[contains(@class,'MuiButtonBase-root MuiPickersDay-root MuiPickersDay')]")))

    for date in alldate:
      if user_date==date.text:
          date.click()
          break
    print("line 6")   
    # confirm the dob by click ok
    ok_btn=wait.until(EC.presence_of_element_located((By.XPATH,"//button[text()='OK']")))
    ok_btn.click()

    ####################################  CALENDER ENDING ##########################################################################
    print("line 7")
    #click ok
    ok_btn=wait.until(EC.presence_of_element_located((By.XPATH,"//button[text()='OK']")))
    ok_btn.click()

    #enter mobile number
    mobile_no=wait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='mobileNumber']")))
    mobile_no.send_keys("1234567890")

    #gender otp
    gender_opt=wait.until(EC.presence_of_element_located((By.XPATH,"//div[@role='button' and @aria-haspopup='listbox']")))
    gender_opt.click()

    #choose gender male or female
    male_or_female = wait.until(EC.presence_of_element_located((By.XPATH,"//li[@data-value='male']")))
    male_or_female.click()

    #click add friend btn
    add_frnd_btn = wait.until(EC.presence_of_element_located((By.XPATH,"//button[text()='Add Friend']")))
    add_frnd_btn.click()