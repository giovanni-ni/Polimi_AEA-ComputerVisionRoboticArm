

import cv2
import joblib

# Percorsi lettura/scrittura immagini da/su disco fisso 
img_path_w = ".../ComputerVision/Code/"

# Importiamo il Modello
lr = joblib.load("binary_mnist_model.pkl")


# Creiamo un oggetto dalla classe VideoCapture per acquisire dalla fotocamera, lo 0 seleziona la fotocamera predefinita
cap = cv2.VideoCapture(1, cv.CAP_DSHOW)

# Cap.isOpened controlla che cap abbia inizializzato corretamente la cattura della fotocamera
while (cap.isOpened()):
    # catturo frame-by-frame
    ret, frame = cap.read()
        
    if ret == True:
        # Visualizza il frame in una finestra
        cv2.imshow("Fotocamera", frame)

        i = 20
        while(1):
            i = i + 1
            # Salviamo il frame come immagine su disco fisso 
            cv2.imwrite(img_path_w+i+".jpg", frame)
            k = input("scatta")
        
    else:
        print("Impossibile leggere un frame dalla fotocamera")
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
# Rilascia la fotocamera
cap.release()
cv2.destroyAllWindows()

# dopo aver acquisito correttamente il frame dell'immagine da fotocamera, la salviamo su disco fisso
img_path = img_path_w


# Caricamento immagine su ndarray    
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# Processiamo l'immagine
small_img = cv2.resize(img, (28, 28))
x = small_img.flatten().astype(float)
x/=255.

# Riconoscimento dell'immagine
x = x.reshape(1,x.shape[0])
y = lr.predict(x)             # classe predetta
proba = lr.predict_proba(x)   # probabilità di appartenenza alle due classi

print("Model prediction: %d (%s)" % (y[0],proba[0]))

