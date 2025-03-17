import schedule
import time
from pioreactor.background_jobs.temperature_automation import start_temperature_automation
from pioreactor.background_jobs.stirring import start_stirring
from pioreactor.background_jobs.od_reading import start_od_reading

temp = start_temperature_automation("thermostat", target_temperature=30)
stirrer = start_stirring(target_rpm=550)
od = start_od_reading()
print(f"action，init RPM = 550, temp = 30, od_reading ON")

def set_change():
    temp.target_temperature = 35
    stirrer.target_rpm = 600
    print(f"RPM set {stirrer.target_rpm}, temp set {temp.target_temperature}")

def stop_control():
    temp.disconnected()
    stirrer.disconnected()
    od.disconnected()
    print("control_closed")
    exit()

schedule.every(2).minutes.do(set_change)
schedule.every(3).minutes.do(stop_control)

while True:
    schedule.run_pending()
    time.sleep(1)




