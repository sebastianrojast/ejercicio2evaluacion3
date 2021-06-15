# Desarrollo del ejercicio n° 1:

""" Esta vez pude aplicar con algunos ajustes los módulos cv2 y sys del ejemplo n° 2. Los ajustes los iré 
presentando a continuación"""

#1) Importar módulos cv2 y sys
import cv2
import sys

#2) Acá al igual que en el ejercico anterior, incorporé al argumento de la variable faceCascades, el archivo 
# de cascada de .xml directamente. Con la declaración de una variable cascPath no me funcionaba.
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# 3) Posteriomente 
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        # flags=cv2.cv.CV_HAAR_SCALE_IMAGE  # AL igual que en el ejercico anterior, comenté flags, intenté
                                            # probar con cv2.CASCADE_SCALE_IMAGE (visto en Stack Overflow)
                                            # pero al comentar y junto a los demases cambios, logré poder
                                            # ejecutar el código 
    )

    # 4) Detección de rostros a través de la webcam
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # 5) Muestra el resultado en cámara
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 6) Cierre
video_capture.release()
cv2.destroyAllWindows()
