import numpy as np
import matplotlib.pyplot as plot
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix


def predictModel(arr):
    patientdata = np.array(arr)
    dataset=pd.read_csv("data_train.csv")

    dataset.head(7)

    X=dataset.iloc[:,:9].values

    print(X.shape)

    y=dataset['Label'].values


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = None)


    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    row=sc.transform(patientdata.reshape(1,-1))
    row


    logisticregression = LogisticRegression(solver='liblinear', multi_class='ovr')
    logisticregression.fit(X_train, y_train)


    y_pred = logisticregression.predict(X_test)
    y_pred1= logisticregression.predict(row)
    print(y_pred1)
    print(y_pred)

    y_compare = np.vstack((y_test,y_pred)).T


    y_compare[:5,:]


    cm = confusion_matrix(y_test, y_pred)
    print(cm)

    a = cm.shape
    corrPred = 0
    falsePred = 0
    for row in range(a[0]):
        for c in range(a[1]):
            if row == c:
                corrPred +=cm[row,c]
            else:
                falsePred += cm[row,c]
    print('Correct predictions: ', corrPred)
    print('False predictions', falsePred)
    print ('Accuracy of the multiclass logistic classification is: ', corrPred/(cm.sum()))

    returndict = {'accuracy':corrPred/(cm.sum()), 'result':y_pred1}
    return returndict
