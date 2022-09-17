#TestList is a 2D list.
def BreastCancer(TestList):
    #importing Libraries and packages
    import pandas as pd
    import numpy as np
    from sklearn.datasets import load_breast_cancer
    from sklearn.preprocessing import LabelEncoder
    from sklearn.feature_extraction import DictVectorizer
    from sklearn.model_selection import train_test_split
    from sklearn.svm import SVC
    bc=load_breast_cancer()
    bcdf=pd.DataFrame(bc.data,columns=bc.feature_names)
    
    #Label Encoding
    labels=np.asarray(bc.target)
    le=LabelEncoder()
    le.fit(labels)
    labels=le.transform(labels)
    dfsel=bcdf.to_dict(orient='records')
    vec=DictVectorizer()

    #Splitting the data for training and testing
    features=vec.fit_transform(dfsel).toarray()
    y_tr,y_te,x_tr,x_te=train_test_split(features,labels,test_size=0.1,random_state=0)
    
    #Using Support Vector Classifier
    model=SVC(kernel='linear',C=1).fit(y_tr,x_tr)
    pre=model.predict(TestList)
    pred_arr=[bc.target_names[i] for i in pre]
    acc=model.score(y_te,x_te)
    return acc*100, pred_arr
    
