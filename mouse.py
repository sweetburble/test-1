import pyautogui
import time

try:
    while True:
        # 마우스의 현재 위치를 가져옵니다.
        x, y = pyautogui.position()
        
        # 마우스의 현재 위치를 출력합니다.
        print(f"Mouse position: ({x}, {y})")
        
        # 1초 동안 대기합니다.
        time.sleep(1)
except KeyboardInterrupt:
    print("\n프로그램 종료")