import cv2

video = cv2.VideoCapture('video_sample.mkv')

while True:
    state,img = video.read()
    if state:
        cv2.imshow("video output",img)
        if cv2.waitKey(1) == 27:
            break
    else:
        break
video.release()
cv2.destroyAllWindows()