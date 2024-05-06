# 이동하는 코드

from djitellopy import tello
import time, sys

drone = tello.Tello()
drone.connect()
drone.streamon()

try:
    drone.takeoff()

except KeyboardInterrupt: # Ctrl+C 눌러서 스크립트 실행 취소시 착륙 명령
    drone.land()
    drone.end()
