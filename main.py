

import cv2
from cvzone.HandTrackingModule import HandDetector

# 1. Abrimos la cámara
cap = cv2.VideoCapture(0)

# 2. Creamos el detector de manos
detector = HandDetector(detectionCon=0.6, maxHands=1)

# 3. Bucle infinito para leer frames de la cámara y procesarlos
while True:
    # 4. Leemos un frame
    success, img = cap.read()
    if not success:
        print("No se pudo capturar la imagen")
        break

    # 5. Detectamos manos en el frame
    hands, img = detector.findHands(img)

    # 6. Si se detecta al menos una mano, contamos dedos
    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        totalFingers = fingers.count(1)

        # 7. Mostramos el número de dedos levantados en la imagen
        cv2.putText(img, f'Dedos: {totalFingers}', (10, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

    # 8. Mostramos la imagen con la detección
    cv2.imshow("DetectorDeDedos", img)

    # 9. Salir si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 10. Liberar recursos al salir
cap.release()
cv2.destroyAllWindows()
