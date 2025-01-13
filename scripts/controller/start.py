import pyautogui
import time
import os

import win32gui
from virtual_joystick import VirtualJoystick

hwnd = win32gui.FindWindow(None, '指尖无双')
if hwnd:
    print(f"找到窗口句柄: {hwnd}")
    
    # 获取窗口左上角和右下角坐标
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    print(f"窗口左上角坐标: ({left}, {top})")
    print(f"窗口右下角坐标: ({right}, {bottom})")
    
        # 计算窗口中心坐标
    center_x = (left + right) // 2
    center_y = (top + bottom) // 2
    print(f"窗口中心坐标: ({center_x}, {center_y})")
    
    # 初始化 VirtualJoystick
    joystick = VirtualJoystick(center_x=center_x, center_y=center_y)
    
    # 示例操作
    joystick.move_to_center()
    time.sleep(2)
    
    joystick.move_right()
    time.sleep(2)
    
    joystick.move_up()
    time.sleep(2)
    
    joystick.move_to_center()
else:
    print("未找到窗口")
# project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# print(f"项目根目录: {project_root}")
# images_dir = os.path.join(project_root, 'data', 'images')

# # 等待几秒钟，确保您有时间切换到微信小游戏窗口
# print("请在5秒内切换到微信小游戏窗口...")
# time.sleep(5)

# start_game_pic_path  = os.path.join(images_dir,'start.png')
# # 找到微信小游戏的“开始游戏”按钮
# start_game_button = pyautogui.locateOnScreen(start_game_pic_path, confidence=0.9)
# if start_game_button:
#     start_game_button_center = pyautogui.center(start_game_button)
#     print(f"开始游戏按钮位置: {start_game_button_center}")
    
#     # 移动鼠标到开始游戏按钮并点击
#     pyautogui.moveTo(start_game_button_center, duration=0.2)
#     pyautogui.click()
# else:
#     print("未找到开始游戏按钮")

# # 等待游戏加载
# time.sleep(2)

# # 模拟游戏中的操作，例如点击屏幕中心
# game_center = (960, 540)  # 假设游戏窗口中心位置
# pyautogui.moveTo(game_center, duration=1)
# pyautogui.click()

# # 模拟一系列点击操作
# for _ in range(10):
#     pyautogui.click(game_center)
#     time.sleep(0.5)  # 每次点击间隔0.5秒

# # 结束游戏
# # 例如，找到游戏中的“退出游戏”按钮
# exit_game_button = pyautogui.locateOnScreen('exit_game_button.png', confidence=0.9)
# if exit_game_button:
#     exit_game_button_center = pyautogui.center(exit_game_button)
#     pyautogui.moveTo(exit_game_button_center, duration=1)
#     pyautogui.click()
# else:
#     print("未找到退出游戏按钮")