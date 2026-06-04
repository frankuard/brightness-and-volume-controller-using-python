import cv2
import time
import math
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python.vision import HandLandmarker,HandLandmarkerOptions 
from mediapipe.tasks.python.vision.core.vision_task_running_mode import VisionTaskRunningMode as VisionTaskRunningMode
 
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

 
base_options = python.BaseOptions(model_asset_path="models/hand_landmarker.task")

latest_result= [None]

def on_result(result,output_image,timestamp_ms):
    latest_result[0] = result
    
options = HandLandmarkerOptions(base_options=base_options,running_mode = VisionTaskRunningMode.LIVE_STREAM, num_hands = 2, min_hand_detection_confidence = 0.5, result_callback = on_result)

landmarker = HandLandmarker.create_from_options(options)
print("HandLandMaker createdd successfully!!")

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

devices = AudioUtilities.GetSpeakers()
interface = devices._dev.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume_control = cast(interface, POINTER(IAudioEndpointVolume))

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    frame = cv2.flip(frame,1)
    
    h,w = frame.shape[:2]
    
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    mp_image = mp.Image(image_format= mp.ImageFormat.SRGB,data=frame_rgb)
    
    timestamp_ms = int(time.time()*1000)
    
    landmarker.detect_async(mp_image,timestamp_ms)
    
    result = latest_result[0]
    
    if result and result.hand_landmarks:
        
        for i,hand_lms in enumerate(result.hand_landmarks):
            
            Connections = [(0,1),(1,2),(2,3),(3,4),(0,5),(5,6),(6,7),(7,8),(0,9),(9,10),(10,11),(11,12),(0,13),(13,14),(14,15),(15,16),(0,17),(17,18),(18,19),(19,20),(5,9),(9,13),(13,17)]
            
            for a,b in Connections:
                
                x1, y1 = int(hand_lms[a].x*w), int(hand_lms[a].y*h)
                
                x2, y2 = int(hand_lms[b].x*w), int(hand_lms[b].y*h)
                
                cv2.line(frame,(x1,y1),(x2,y2),(255,255,255),2)
                
            for j in range(21):
                lm =hand_lms[j]
                x = int(lm.x*w)
                y = int(lm.y*h)
                    
                cv2.circle(frame,(x,y),3,(0,200,0),-1)
                    
                cv2.putText(frame,str(j),(x+5,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.3,(255,255,255),1)
                
            thumb_tip = hand_lms[4]
            index_tip = hand_lms[8]
            
            thumb_x, thumb_y = int(thumb_tip.x*w), int(thumb_tip.y*h)
            
            index_x, index_y = int(index_tip.x*w), int(index_tip.y*h)
            
            distance = math.hypot(index_x-thumb_x, index_y-thumb_y)
            
            
            min_distance = 30
            max_distance = 160
            
            volume = np.interp(distance,[min_distance,max_distance],[0,100])
            
            volume = np.clip(volume,0,100)
            
            
            volume_control.SetMasterVolumeLevelScalar(volume / 100, None)
            
            
            cv2.putText(frame, str(int(volume)),(50,80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2)
            
            
                
    cv2.imshow("Volume Controller", frame)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
landmarker.close()
        