from djitellopy import tello
import time, sys

drone_bat_low_level = 50 # 배터리 최저값

drone = tello.Tello()
drone.connect()

drone_bat_level = drone.get_battery()
if drone_bat_level < drone_bat_low_level:
    print("cannot proceed: low battery level")
    sys.exit()

drone.takeoff()
time.sleep(1)
drone.land()
drone.end()