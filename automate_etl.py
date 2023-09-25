import schedule
import time
import subprocess

def run_etl():
    # Run the ETL script using subprocess
    subprocess.run(["python", "ETL.py"])

# Schedule the ETL to run daily at a specific time (e.g., 9.45 PM)
schedule.every().day.at("21:45").do(run_etl)

# Run the scheduler continuously
while True:
    schedule.run_pending()
    time.sleep(1)