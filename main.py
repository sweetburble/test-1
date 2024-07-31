import cv2
import numpy as np
import pyautogui
import time
from PIL import ImageGrab

# 감시할 구역의 좌표 (x1, y1, x2, y2)
monitor_area = (880, 340, 1600, 520)  # 예시 좌표
# 변화 감지 기준 (변화가 없으면 클릭)
threshold = 1000  # 변화 감지 기준 (픽셀 수)

def capture_screen(area):
    # 스크린샷을 찍고, 지정된 영역을 자릅니다.
    img = ImageGrab.grab(bbox=area)
    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

def main():
    previous_frame = None

    while True:
        # 현재 화면 캡처
        current_frame = capture_screen(monitor_area)

        if previous_frame is not None:
            # 두 프레임의 차이 계산
            frame_diff = cv2.absdiff(current_frame, previous_frame)
            gray_diff = cv2.cvtColor(frame_diff, cv2.COLOR_BGR2GRAY)
            _, thresh = cv2.threshold(gray_diff, 30, 255, cv2.THRESH_BINARY)

            # 변화가 감지된 픽셀 수 계산
            change_count = np.sum(thresh == 255)

            # 변화가 없으면 클릭
            if change_count < threshold:
                print("변화 없음, 클릭합니다.")
                # 마우스 클릭 (중앙 좌표를 클릭)
                center_x = (monitor_area[0] + monitor_area[2]) // 2
                center_y = (monitor_area[1] + monitor_area[3]) // 2
                pyautogui.click(center_x, center_y)
                time.sleep(1)  # 클릭 후 1초 대기

        # 현재 프레임을 이전 프레임으로 설정
        previous_frame = current_frame.copy()

        # 감시 간격 (예: 0.5초)
        time.sleep(10)

if __name__ == "__main__":
    main()