import schedule
import time
import subprocess


def job():
    print("Récupération des contacts...")
    subprocess.run(["python3", "./script_print.py"])


schedule.every(10).seconds.do(job)

starter = 0
timer = 10
while True:
    print("Run script to : ", timer - starter)
    if timer - starter <= 0:
        print("TIMER STARTED")
        starter = 0
        timer = 10
    starter += 1
    schedule.run_pending()
    time.sleep(1)
