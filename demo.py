import cv2
from ultralytics import YOLO
from easycv.core import draw_box_with_label  #custom function

model = YOLO(r"C:\Users\Shivram\yolov8n.pt")  
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    results = model(frame)[0]  

    for box in results.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf[0])
        class_id = int(box.cls[0])
        label = model.names[class_id]

        #  Use draw_box_with_label() function
        draw_box_with_label(
            frame,
            box=(x1, y1, x2, y2),
            label=label,
            confidence=conf,
            color=(255, 255, 0) 
        )

    cv2.imshow("YOLOv8 Webcam Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
