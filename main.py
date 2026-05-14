import json

from utils.browser import get_driver
from portals.capgemini import apply

driver = get_driver()

with open(r"C:\\Users\\harsh\\OneDrive\\Documents\\JP IT Staffing\\config.json") as file:
    data = json.load(file)

apply(driver, data)

input("Press Enter to close browser...")

driver.quit()


