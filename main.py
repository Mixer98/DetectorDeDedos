# Importamos la librería OpenCV
import cv2

# Creamos un objeto llamado 'cap' que accede a la cámara web principal (índice 0)
cap = cv2.VideoCapture(0)

# Verificamos si la cámara se abrió correctamente
if not cap.isOpened():
    print("No se pudo abrir la cámara.")
    exit()  # Salimos del programa si no hay cámara disponible

# Iniciamos un bucle infinito para capturar video en tiempo real
while True:
    # Leemos un fotograma (frame) de la cámara
    ret, frame = cap.read()

    # Si no se pudo leer el frame, se rompe el bucle
    if not ret:
        print("No se pudo capturar el frame.")
        break

    # Mostramos el frame en una ventana llamada "Cámara"
    cv2.imshow("Cámara", frame)

    # Esperamos 1 milisegundo y verificamos si se presionó la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # Si se presiona la tecla 'q', se rompe el bucle
        break

# Cuando se rompe el bucle:
# 1. Liberamos la cámara
cap.release()

# 2. Cerramos todas las ventanas abiertas por OpenCV
cv2.destroyAllWindows()
