def HeartDisease(Testlist):
    import pandas as pd
    import numpy as np
    hddf=pd.read_csv('Heart_Disease_Prediction.csv')

    x=hddf.drop(['Heart Disease'],axis=1)
    y_dis=hddf['Heart Disease']
    y=hddf['Heart Disease'].map({'Presence':1,'Absence':0})

#Balancing the data
    one_target = int(np.sum(y))
    zero_counter = 0
    indices_to_remove = []

    for i in range(y.shape[0]):
        if y[i] == 0:
            zero_counter += 1
            if zero_counter > one_target:
                indices_to_remove.append(i)

    balanced_inputs = x.drop(indices_to_remove, axis=0)
    balanced_targets = y.drop(indices_to_remove, axis=0)

    reset_inputs = balanced_inputs.reset_index(drop=True)
    reset_targets = balanced_targets.reset_index(drop=True)

    # print("Balanced targets: ",balanced_targets)

    from sklearn.preprocessing import MinMaxScaler
    scaled_inputs = MinMaxScaler().fit_transform(balanced_inputs)

    from sklearn.model_selection import train_test_split
    x_train,x_test,y_train,y_test=train_test_split(scaled_inputs,balanced_targets,test_size=0.2,random_state=0)

    # print("Xtrain data:",x_train)
    # print("Y tarin data:",y_train)

    from sklearn.linear_model import LogisticRegression
    model=LogisticRegression().fit(x_train,y_train)
    pred=model.predict(Testlist)
    pr=[hddf['Heart Disease'][i] for i in pred]
    res = pr[0]
    acc=model.score(x_test,y_test)
    return acc*100, res