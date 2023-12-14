AEA - ComputerVisionRoboticArm project

#Computer Vision 

Task 28/10

Il modello allenato con la regressione logistica di scikitlearn ha un'accuratezza del 100% sul dataset di training, qualsiasi sia la dimensione del dataset di test. In sintesi trova sempre una mappatura perfetta immagine-etichetta su tutte le immagini in cui è stato allenato. Invece l'accuratezza sul dataset di test ha varianza e valor atteso strettamente correlati alla dimensione del test dataset:

-Test_size-   -Accuracy y_train-   -Accuracy y_test- 
   0.05             100%               80% - 100%
   0.1              100%               90% - 100%
   0.2              100%               95% - 100%
   0.3              100%             96.7% - 100%
   0.4              100%             97.5% - 100%
   0.5              100%               98% - 100%
   0.6              100%               96% - 100%
   0.7              100%               94% - 100%
   0.8              100%               91% - 100%
   0.9              100%               60% - 100% 
   0.95             100%               48% - 100%
   
Si ha un leggero overfitting per Test_size in (0.05, 0.1), mentre è presente overfitting in (0.8, 0.95)

Test_size ottimale: (0.4, 0.5)
