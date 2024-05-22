import cv2
import numpy as np

# 打开视频文件
video_capture1 = cv2.VideoCapture('football3.avi')
video_capture2 = cv2.VideoCapture('football_caijian2.mp4')

# 检查视频是否成功打开
if not (video_capture1.isOpened() or video_capture2.isOpened()):
    print("无法打开视频文件")
    exit()
fps = int(video_capture1.get(cv2.CAP_PROP_FPS))
frame_width = int(video_capture1.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video_capture1.get(cv2.CAP_PROP_FRAME_HEIGHT))+int(video_capture2.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 创建VideoWriter对象，用于保存处理后的视频
fourcc = cv2.VideoWriter_fourcc(*'MP4V')  # 选择适当的编解码器

output_video = cv2.VideoWriter('football_pinjie2.mp4', fourcc, fps, (frame_width, frame_height))

# 循环处理每一帧
while True:
    ret1, frame1 = video_capture1.read()
    ret2, frame2 = video_capture2.read()

    if not ret1:
        break  # 没有更多帧可读取，退出循环

    # 合并图像
    adjusted_frame=np.concatenate((frame2,frame1),axis=0)

    print(frame1.shape,frame2.shape,adjusted_frame.shape)

    # 将帧写入输出视频
    output_video.write(adjusted_frame)

# 释放视频读取器和输出视频写入器
video_capture1.release()
video_capture2.release()
output_video.release()

# 关闭所有窗口
cv2.destroyAllWindows()
