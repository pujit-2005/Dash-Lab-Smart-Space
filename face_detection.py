import cv2
import mediapipe as mp


mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils


face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.2)


cap = cv2.VideoCapture(0)  

while cap.isOpened():
   
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to grab frame")
        break

    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
  
    results = face_detection.process(rgb_frame)
    
    
    if results.detections:
        for detection in results.detections:
            
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = frame.shape
            x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                         int(bboxC.width * iw), int(bboxC.height * ih)
            
            
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    
    cv2.imshow('Face Detection', frame)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close windows
cap.release()
cv2.destroyAllWindows()
