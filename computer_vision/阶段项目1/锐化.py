import cv2
import numpy as np

# 打开视频文件
video_capture = cv2.VideoCapture('football.mp4')

# 检查视频是否成功打开
if not video_capture.isOpened():
    print("无法打开视频文件")
    exit()
fps = int(video_capture.get(cv2.CAP_PROP_FPS))
frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 创建VideoWriter对象，用于保存处理后的视频
fourcc = cv2.VideoWriter_fourcc(*'MP4V')  # 选择适当的编解码器
output_width, output_height = 640, 480  # 设置输出视频的分辨率
output_video = cv2.VideoWriter('football4.mp4', fourcc, fps, (frame_width, frame_height))

# 循环处理每一帧
while True:
    ret, frame = video_capture.read()
    if not ret:
        break  # 没有更多帧可读取，退出循环

    # 锐化图像
    sharpened_frame = cv2.filter2D(frame, -1, np.array([[-1, -1, -1],
                                                        [-1, 8.5, -1],
                                                        [-1, -1, -1]]))

    # 调整对比度和亮度
    alpha = 1.1  # 调整对比度的参数
    beta = 10    # 调整亮度的参数
    adjusted_frame = cv2.convertScaleAbs(sharpened_frame, alpha=alpha, beta=beta)

    # 将帧写入输出视频
    output_video.write(adjusted_frame)

# 释放视频读取器和输出视频写入器
video_capture.release()
output_video.release()

# 关闭所有窗口
cv2.destroyAllWindows()
