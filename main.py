from typing import List

import pyautogui

import pygetwindow as gw

# 获取屏幕的宽度和高度
screenWidth, screenHeight = pyautogui.size()

# 获取当前鼠标的位置
currentMouseX, currentMouseY = pyautogui.position()

# 移动鼠标到屏幕的(100, 150)位置
pyautogui.moveTo(100, 150)

# 点击鼠标
pyautogui.click()

# 向下移动鼠标10像素
pyautogui.moveRel(None, 10)

# 执行双击操作
pyautogui.doubleClick()

# 在2秒内平滑移动鼠标至(1800,500)
pyautogui.moveTo(1800, 500, duration=2, tween=pyautogui.easeInOutQuad)

# 根据标题获取窗口列表，这里以"Visual Studio Code"为例
window_list: List[gw.Win32Window] = gw.getWindowsWithTitle(
    'Visual Studio Code'
)

# 如果找到了目标窗口
if len(window_list) > 0:
    # 获取第一个匹配的窗口
    window = window_list[0]

    # 输出窗口的位置和尺寸
    print(window.left, window.top, window.width, window.height)

    # 将窗口移动到(100, 100)位置
    window.moveTo(100, 100)

    # 将窗口大小调整为 800x600
    window.resizeTo(800, 600)

    # 最小化窗口
    window.minimize()

    # 最大化窗口
    window.maximize()

    # 恢复窗口（从最小化或最大化恢复到原始大小和位置）
    window.restore()
else:
    print("未找到指定标题的窗口")
