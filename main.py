import requests 
import cv2 
import numpy as np 
import mediapipe
import pyautogui

face_mesh_landmarks = mediapipe.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

# Specify the desired window width and height
window_width = 800
window_height = 600
  
# Replace the below URL with your own. Make sure to add "/shot.jpg" at last. 
url = "http://192.168.0.103:8080/shot.jpg"
  
# While loop to continuously fetching data from the Url 
while True: 
    img_resp = requests.get(url) 
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8) 
    image = cv2.imdecode(img_arr, -1) 

    image = cv2.flip(image, 1)
    window_h, window_w, _ = image.shape
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    processed_image = face_mesh_landmarks.process(rgb_image)
    all_face_landmark_points = processed_image.multi_face_landmarks
    
    if all_face_landmark_points:
        one_face_landmark_points = all_face_landmark_points[0].landmark
        for id, landmark_point in enumerate(one_face_landmark_points[474:478]):
            x = int(landmark_point.x * window_w)
            y = int(landmark_point.y * window_h)
            if id == 1:
                mouse_x = int(screen_w / window_w * x)
                mouse_y = int(screen_h / window_h * y)
                pyautogui.moveTo(mouse_x, mouse_y)

            cv2.circle(image, (x, y), 3, (0, 0, 255))
        
        left_eye = [one_face_landmark_points[145], one_face_landmark_points[159]]
        for landmark_point in left_eye:
            x = int(landmark_point.x * window_w)
            y = int(landmark_point.y * window_h)
            cv2.circle(image, (x, y), 6, (0, 255, 0))
        
        if (left_eye[0].y - left_eye[1].y) < 0.015:
            pyautogui.click()
            pyautogui.sleep(0.5)
            print("Mouse Clicked")

    # Resize the image to the desired window size
    resized_image = cv2.resize(image, (window_width, window_height))
  
    cv2.imshow("Android_cam", resized_image)
  
    # Press Esc key to exit 
    if cv2.waitKey(1) == 27: 
        break
  
cv2.destroyAllWindows()
