import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.metrics import classification_report



class Logica:

    def process_file(self):
        df = pd.read_csv("C:/Users/lenovo/Documents/repositorio/MoneyMateProject/money_mate_back/util/Datosendeudamiento.csv", sep=";")
        # Resto del código de análisis... 

        variables_X = ['Ingresos_mensuales', 'Gastos_mensuales','imprevistos_mes']
        X = df[variables_X].values
        y = df['Endeudamiento']     
        sc = preprocessing.StandardScaler()
        X = sc.fit_transform(X)   
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state= 2)     

        k = 4
        modelo = KNeighborsClassifier(n_neighbors= k)       
        modelo.fit(X_train,y_train)     
        yhat = modelo.predict(X_test)
        
        print(yhat)

        
        metrics.accuracy_score(y_train, modelo.predict(X_train))
        metrics.accuracy_score(y_test, yhat)  

           
        return f"Realizando análisis... ${yhat}" 