from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import time

def upload_file(driver, button_text):

    try:

        print(f"Starting upload: {button_text}")

        upload_btn = driver.find_element(
            By.XPATH,
            f"//*[contains(text(),'{button_text}')]"
        )

        driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            upload_btn
        )

        time.sleep(2)

        driver.execute_script(
            "arguments[0].click();",
            upload_btn
        )

        print(f"Opened {button_text} popup")

        time.sleep(3)

        device_buttons = driver.find_elements(
            By.XPATH,
            "//*[contains(text(),'Upload from Device')]"
        )

        for d in device_buttons:

            if d.is_displayed():

                driver.execute_script(
                    "arguments[0].click();",
                    d
                )

                print("Clicked Upload From Device")

                break

        time.sleep(3)

        print(f"{button_text} workflow completed")

    except Exception as e:

        print(f"{button_text} upload failed")
        print(e)
        
def apply(driver, DATA):
# =========================================
# CONFIG
# =========================================


     
     

    # =========================================
    # OPEN JOB PAGE
    # =========================================

    driver.get(DATA["job_url"])

    print("Opened Job Page")

    time.sleep(5)


    # =========================================
    # CLICK APPLY BUTTON
    # =========================================

    apply_buttons = driver.find_elements(
        By.XPATH,
        "//*[contains(text(),'Apply for this job')]"
    )

    print(f"Found {len(apply_buttons)} apply buttons")

    clicked = False

    for element in apply_buttons:

        try:

            text = element.text.strip()

            print("TEXT:", text)

            if "Apply" in text:

                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    element
                )

                time.sleep(2)

                driver.execute_script(
                    "arguments[0].click();",
                    element
                )

                clicked = True

                print("Clicked Apply")

                break

        except Exception as e:
            print(e)

    if not clicked:

        print("Could not click Apply button")

        input("Press Enter to close...")

        driver.quit()

        exit()


    # =========================================
    # WAIT FOR SUCCESSFACTORS PAGE
    # =========================================

    time.sleep(10)

    print(driver.current_url)

    print("Waiting for application form...")

    # =========================================
    # WAIT FOR SUCCESSFACTORS REDIRECT
    # =========================================

    print("Waiting for SuccessFactors redirect...")

    # =========================================
    # SWITCH TO NEW TAB
    # =========================================

    time.sleep(5)

    tabs = driver.window_handles

    print("Tabs:", len(tabs))

    driver.switch_to.window(tabs[-1])

    print("Switched To New Tab")

    print(driver.current_url)

    time.sleep(10)

    print("Reached SuccessFactors")

    print(driver.current_url)

    # =========================================
    # WAIT FOR FORM
    # =========================================

    time.sleep(5)

    print("Filling Form...")


    # =========================================
    # RESUME
    # =========================================

    upload_file(
        driver,
        "Upload a Resume"
    )

    # =========================================
    # COVER LETTER
    # =========================================

    upload_file(
        driver,
        "Upload a Cover Letter"
    )

    # =========================================
    # EMAIL
    # =========================================

    driver.find_element(
        By.NAME,
        "fbclc_userName"
    ).send_keys(DATA["email"])

    driver.find_element(
        By.NAME,
        "fbclc_emailConf"
    ).send_keys(DATA["email"])

    print("Filled Email")


    # =========================================
    # PASSWORD
    # =========================================

    driver.find_element(
        By.NAME,
        "fbclc_pwd"
    ).send_keys(DATA["password"])

    driver.find_element(
        By.NAME,
        "fbclc_pwdConf"
    ).send_keys(DATA["password"])

    print("Filled Password")


    # =========================================
    # FIRST NAME
    # =========================================

    driver.find_element(
        By.NAME,
        "fbclc_fName"
    ).send_keys(DATA["first_name"])

    print("Filled First Name")


    # =========================================
    # LAST NAME
    # =========================================

    driver.find_element(
        By.NAME,
        "fbclc_lName"
    ).send_keys(DATA["last_name"])

    print("Filled Last Name")


    # =========================================
    # PHONE
    # =========================================

    driver.find_element(
        By.NAME,
        "fbclc_phoneNumber"
    ).send_keys(DATA["phone"])

    print("Filled Phone")

    
    # =========================================
    # SCROLL TO COUNTRY DROPDOWN
    # =========================================

    country_dropdown = driver.find_element(
        By.XPATH,
        "//select"
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        country_dropdown
    )

    time.sleep(2)

    print("Scrolled")


    # =========================================
    # COUNTRY OF RESIDENCE
    # =========================================

    try:

        country = driver.find_element(
            By.XPATH,
            "//input[contains(@aria-label,'Country of Residence')]"
        )

        country.click()

        time.sleep(1)

        country.send_keys("India")

        time.sleep(1)

        country.send_keys(Keys.DOWN)

        country.send_keys(Keys.ENTER)

        print("Selected Country")

    except Exception as e:

        print("Country Selection Failed")
        print(e)

    # =========================================
    # HANDLE ALL DROPDOWNS
    # =========================================

    dropdowns = driver.find_elements(
        By.TAG_NAME,
        "select"
    )

    print(f"Found {len(dropdowns)} dropdowns")

    for d in dropdowns:

        try:

            select = Select(d)

            options = [
                o.text.strip()
                for o in select.options
            ]

            # choose safe answer
            if "No Selection" in options:

                select.select_by_visible_text(
                    "No Selection"
                )

            elif "No" in options:

                select.select_by_visible_text(
                    "No"
                )

            elif "India" in options:

                select.select_by_visible_text(
                    "India"
                )

        except:
            pass

    checkboxes = driver.find_elements(
        By.XPATH,
        "//input[@type='checkbox']"
    )

    for c in checkboxes:

        try:

            if not c.is_selected():

                driver.execute_script(
                    "arguments[0].click();",
                    c
                )

        except:
            pass

    input("Check filled form and press Enter...")

    print("Application automation completed successfully")