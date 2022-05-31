from sklearn import preprocessing
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor

#return 2 df each encoded by ordinal encoder, label encoder
def ordinal_label_encoder(df):
    df_ordinal = df.copy()
    df_label = df.copy()

    ord_enc = preprocessing.OrdinalEncoder()
    label_enc = preprocessing.LabelEncoder()

    df_categorical = df.select_dtypes(include=["object", "string", 'category'])

    df_numeric = df.select_dtypes(include=["int64", "float64"])

    #Convert categorical columns with ordinal encoder
    df_ordinal[df_categorical.columns] = df_categorical
    ord_enc.fit(df_categorical)

    df_ordinal = df_ordinal.reset_index() 
    df_ordinal[df_categorical.columns]= pd.DataFrame(ord_enc.transform(df_categorical))
    df_ordinal[df_categorical.columns]


    #Convert categorical columns with label encoder
    df_label = df_label.reset_index()

    for column in df_categorical.columns:
        label_enc.fit(df_categorical[column])
        df_label[column] = pd.DataFrame(label_enc.transform(df_categorical[column]))

    return df_ordinal, df_label

def regression_model(scaler, X, y, model, train_size_val, random_state_val):
    scaler.fit(X)
    X = scaler.transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=train_size_val, stratify=y, random_state=random_state_val)

    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)

    return accuracy

def regression_best_score (df, selected_features, target, train_size_val, random_state_val):

    df_ordinal, df_label = ordinal_label_encoder(df)

    X_by_encoder = {'OrdinalEncdoer': df_ordinal[selected_features], 
                'LabelEncoder': df_label[selected_features]}

    y_by_encoder = {'OrdinalEncdoer' : df_ordinal[target],
                    'LabelEncoder': df_label[target]}

    scalers = {'StandardScaler': preprocessing.StandardScaler(),
                'RobustScaler' : preprocessing.RobustScaler(),
                'MaxabsScaler' :preprocessing.MaxAbsScaler()}

    model_by_regression = {'LinearRegression' : LinearRegression(),
                            'PolynomialRegression': Pipeline([('poly', PolynomialFeatures(degree=2)), 
                                                              ('linear', LinearRegression(fit_intercept=False))]),
                            'DecisionTreeClassifier' : DecisionTreeClassifier()
                            }

    best = {
        'a':-1,
        'scaler':"not assigned yet",
        'encoder':"not assigned yet",
        'regression':"not assigned yet"
    }

    for s in scalers.keys():
        for e in X_by_encoder.keys():
            for r in model_by_regression.keys():
                accuracy = regression_model(scalers[s], X_by_encoder[e], y_by_encoder[e], model_by_regression[r], train_size_val, random_state_val)
                if best['a'] < accuracy:
                    best['a'] = accuracy
                    best['scaler'], best['encoder'], best['regression'] = s, e, r

    return best['a'], best['scaler'], best['encoder'], best['regression']