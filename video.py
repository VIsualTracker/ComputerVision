# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 10:29:34 2019

@author: sunbo
"""

import cv2

pause = False
closed = False

def playVideo(video):
    print('playVideo E')
    
    global pause

    ret, image = video.read()
    cv2.putText(image, 'Press Blank to Play', 
            (int(image.shape[1]/2), int(image.shape[0]/2)), 
            cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,0),2)

    cv2.imshow('test video', image)

    while True:
        #while cv2.waitKey(1) == -1 and ret:
        keyVal = cv2.waitKey(1)

        if keyVal == 32:
            pause = bool(1-pause)
            continue

        elif keyVal == 27:
            closeVideo()
            break

        elif keyVal == -1 and ret and not pause:
            
            cv2.imshow('test video', image)
            
            ret, image = video.read()
            
            # 播放结束, 等待按下ESC以退出窗口
            if ret == False:
                print('Video Finish')
                break

    print('playVideo X')

def closeVideo():
    print('closeVideo E')
    
    global closed
    if closed == False:  
        cv2.destroyWindow('test video')
        video.release()
        closed = True

    print('closeVideo X')
    
def saveVideo(video):
    print('saveVideo E')
    
    frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    size = (frame_width, frame_height)
    fps = int(video.get(cv2.CAP_PROP_FPS))
    dstVideo = cv2.VideoWriter('dstVideo.avi', cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'), fps, size)
    
    success, frame = video.read()
    while success:
        dstVideo.write(frame)
        success, frame = video.read()
    
    print('saveVideo X')

#############################################################################

video = cv2.VideoCapture('TestVideo.mp4')

cv2.namedWindow('test video', cv2.WINDOW_NORMAL)

while True:
    keyVal = cv2.waitKey(0)
    if keyVal == 32:   
        playVideo(video)
        break
    elif keyVal == 27:
        closeVideo()
        break
    elif keyVal == 13:
        saveVideo(video)
        break
    else:
        print('Unknow Operation: ', keyVal)

cv2.waitKey(0)
closeVideo()
print('——>End')

#cv2.waitKey(0)
