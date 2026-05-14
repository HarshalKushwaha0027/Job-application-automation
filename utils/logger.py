import csv
import os
from datetime import datetime

def log_application(company, status):

    os.makedirs("logs", exist_ok=True)

    with open("logs/applications.csv", "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            company,
            status,
            datetime.now()
        ])