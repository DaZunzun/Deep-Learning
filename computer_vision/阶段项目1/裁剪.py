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
frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)) - (720 - 339)
frame_height2 = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)) - frame_height

# 创建VideoWriter对象，用于保存处理后的视频
fourcc = cv2.VideoWriter_fourcc(*'MP4V')  # 选择适当的编解码器

output_video = cv2.VideoWriter('football_caijian1.mp4', fourcc, fps, (frame_width, frame_height))
output_video2 = cv2.VideoWriter('football_caijian2.mp4', fourcc, fps, (frame_width, frame_height2))

# 循环处理每一帧
while True:
    ret, frame = video_capture.read()
    if not ret:
        break  # 没有更多帧可读取，退出循环

    # 裁剪图像
    adjusted_frame = frame[380:-1, :, :]
    adjusted_frame2 = frame[0:380, :, :]

    # print(adjusted_frame.shape,frame.shape,adjusted_frame2.shape)

    # 将帧写入输出视频
    output_video.write(adjusted_frame)
    output_video2.write(adjusted_frame2)

# 释放视频读取器和输出视频写入器
video_capture.release()
output_video.release()
output_video2.release()

# 关闭所有窗口
cv2.destroyAllWindows()
