# exercises/contour_detection.py
"""
练习：轮廓检测

描述：
使用 OpenCV 检测图像中的轮廓并将其绘制出来。

请补全下面的函数 `contour_detection`。
"""
import cv2
import numpy as np

def contour_detection(image_path):
    """
    使用 OpenCV 检测图像中的轮廓
    参数:
        image_path: 图像路径
    返回:
        tuple: (绘制轮廓的图像, 轮廓列表) 或 (None, None) 失败时
    """
    # 请在此处编写代码
    # 提示：
    # 1. 使用 cv2.imread() 读取图像。
    # 2. 检查图像是否成功读取。
    # 3. 使用 cv2.cvtColor() 转为灰度图。
    # 4. 使用 cv2.threshold() 进行二值化处理。
    # 5. 使用 cv2.findContours() 检测轮廓 (注意不同 OpenCV 版本的返回值)。
    # 6. 创建图像副本 img.copy() 用于绘制。
    # 7. 使用 cv2.drawContours() 在副本上绘制轮廓。
    # 8. 返回绘制后的图像和轮廓列表。
    # 9. 使用 try...except 处理异常。
    try:
        # 1. 读取图像
        img = cv2.imread(image_path)

        # 2. 检查图像是否成功读取
        if img is None:
            raise ValueError("图像未能成功读取，请检查路径。")

        # 3. 转为灰度图
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 4. 使用自适应阈值处理，比固定阈值更鲁棒
        thresh = cv2.adaptiveThreshold(
            gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
        )

        # 5. 检测轮廓，处理不同OpenCV版本的返回值差异
        contour_result = cv2.findContours(
            thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
        )

        # 根据OpenCV版本处理返回值
        if len(contour_result) == 3:
            # OpenCV 3 返回三个参数：image, contours, hierarchy
            _, contours, _ = contour_result
        else:
            # OpenCV 4 及以上返回两个参数：contours, hierarchy
            contours, _ = contour_result

        # 确保 contours 是一个标准的 Python 列表
        contours = list(contours)

        # 6. 创建图像副本用于绘制
        img_copy = img.copy()

        # 7. 绘制轮廓，使用更细线条和半透明颜色
        cv2.drawContours(img_copy, contours, -1, (0, 255, 0), 1)

        return img_copy, contours
    except Exception as e:
        print(f"发生错误: {e}")
        return None, None
