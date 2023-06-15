from moviepy.editor import VideoFileClip
import cv2 as cv2
import os

videoNameList = []
metaVideo = cv2.VideoCapture("AITrainer/sato_2.mp4")
videoFrames = int(metaVideo.get(cv2.CAP_PROP_FRAME_COUNT))
fps = metaVideo.get(cv2.CAP_PROP_FPS)
duration_sec = videoFrames / fps

# video_width = int(video_data.get(cv2.CAP_PROP_FRAME_WIDTH))
# video_hight = int(video_data.get(cv2.CAP_PROP_FRAME_HEIGHT))
videoMaxSize = duration_sec / 3
videoMinSize = 0

for i in range(3):
    videoName = "AITrainer/sato_2_{}.mp4".format(i)
    video = VideoFileClip("AITrainer/sato_2.mp4").subclip(videoMinSize, videoMaxSize)
    videoMinSize = videoMaxSize
    videoMaxSize = videoMaxSize + (duration_sec / 3)
    video.write_videofile(videoName)
