import schedule
import time

def my_scheduled_task():
    print("Executing scheduled task...")

# Schedule the task
schedule.every().day.at("10:00").do(my_scheduled_task)  # Runs every day at 10 AM
# schedule.every(5).minutes.do(my_scheduled_task)  # Uncomment to run every 5 minutes
# schedule.every().hour.do(my_scheduled_task)  # Uncomment to run every hour

print("Scheduler is running... Press Ctrl+C to stop.")

while True:
    schedule.run_pending()
    time.sleep(1)  # Prevents CPU overuse
