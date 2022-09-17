def Parkinsons(TestList):
    from scipy.stats import skew
    from sklearn.metrics import classification_report
    from sklearn.metrics import confusion_matrix
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import precision_recall_curve, average_precision_score,auc
    import pandas as pd
    import numpy as np

    data = pd.read_csv('parkinsons.csv')

    data_new = data.drop(['status'], axis=1)
    column = list(data_new.columns)

    def skewness_check(col):
        l=[]
        for name in col:
            value = data[name].skew()
            if(value>1.5 or value<-1.5):
                # print(name,":",value)
                l.append(name)
        return l

    col_skew = []
    col_skew = skewness_check(column)

    from sklearn.preprocessing import StandardScaler
    standard = StandardScaler()
    real_x = data.iloc[:,:-1].values
    real_y = data.iloc[:,-1].values
    real_x = standard.fit_transform(real_x)

    from sklearn.preprocessing import LabelEncoder
    labels=np.asarray(data.status)
    le=LabelEncoder().fit(labels)
    labels=le.transform(labels)
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(real_x, real_y, test_size=0.15, stratify=real_y)

    from sklearn.ensemble import GradientBoostingClassifier
    model_GB = GradientBoostingClassifier()
    model_GB.fit(x_train, y_train)
    y_predict_gb = model_GB.predict(TestList)
    pred=[labels[p] for p in y_predict_gb]
    return model_GB.score(x_test, y_test)*100, pred
