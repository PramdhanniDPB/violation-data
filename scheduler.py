import subprocess
import time
from datetime import datetime

# =========================
# CONFIGURATION
# =========================

# Jalan setiap Senin pukul 00:00
SCHEDULE_WEEKDAY = 0  # Monday
SCHEDULE_TIME = "00:00"

COMMAND = ".\\flow.bat"

# =========================
# SCHEDULER
# =========================

def run_command():
    print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] Running: {COMMAND}")

    try:
        result = subprocess.run(
            COMMAND,
            shell=True,
            capture_output=True,
            text=True
        )

        print("Exit code:", result.returncode)

        if result.stdout:
            print("OUTPUT:")
            print(result.stdout)

        if result.stderr:
            print("ERROR:")
            print(result.stderr)

    except Exception as e:
        print("Failed to execute command:", e)


def scheduler():
    executed_week = None

    print("Scheduler started.")
    print("Schedule: Every Monday at", SCHEDULE_TIME)
    print("Command:", COMMAND)

    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        current_week = now.isocalendar().week, now.isocalendar().year

        if (
            now.weekday() == SCHEDULE_WEEKDAY
            and current_time == SCHEDULE_TIME
            and current_week != executed_week
        ):
            executed_week = current_week
            run_command()

        time.sleep(1)


if __name__ == "__main__":
    scheduler()