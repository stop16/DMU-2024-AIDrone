# 드론을 띄우고, 착륙시키는 제어 코드

from djitellopy import tello
import time, sys

drone_bat_low_level = 50 # 배터리 최저값

drone = tello.Tello()
drone.connect()

drone_bat_level = drone.get_battery()
if drone_bat_level < drone_bat_low_level:
    print("cannot proceed: low battery level")
    sys.exit() # 배터리가 낮으면 프로그램 종료

drone.takeoff()
time.sleep(1)
drone.land()
drone.end()