import cv2
import math
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      continue

    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
       
        ip = hand_landmarks.landmark[8]
        ix,iy,iz = ip.x,ip.y,ip.z
        # nomalize the coordinates
        ix = min(math.floor(ix * image.shape[1]), image.shape[1] - 1)
        iy = min(math.floor(iy * image.shape[0]), image.shape[0] - 1)

        cv2.putText(image,f'({ix:.1f},{iy:.1f})',(ix,iy),
          fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
          fontScale=1,
          color=(0,255,255)
        )
               
    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()