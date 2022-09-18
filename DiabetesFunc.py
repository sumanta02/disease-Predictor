def Diabetes(TestList):
    import pandas as pd
    import numpy as np
    from sklearn.preprocessing import LabelEncoder
    from sklearn.feature_extraction import DictVectorizer
    from sklearn.model_selection import train_test_split
    from sklearn.neighbors import KNeighborsClassifier
    diadf=pd.read_csv('diabetes.csv')

    labels=np.asarray(diadf.Outcome)
    le=LabelEncoder().fit(labels)
    labels=le.transform(labels)

    df_sel=diadf.drop(['Outcome'],axis=1)
    df_features=df_sel.to_dict(orient='records')
    vec=DictVectorizer()
    features=vec.fit_transform(df_features).toarray()


    y_train,y_test,x_train,x_test=train_test_split(features,labels,test_size=0.1,random_state=0)


    model=KNeighborsClassifier(n_neighbors=3).fit(y_train,x_train)
    predictor=model.predict(TestList)
    pred=[p for p in predictor]
    acc=model.score(y_train,x_train)
    return acc*100, pred