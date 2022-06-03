# NYC_Crime_DataAnalysis
2022 1st Semester DataScience Term Project Gachon Univ Dept. AISW

By Team member WonJae Lee, JuHyeong Kim, KyeongMin Lee

Our team conducted NYC crime data analysis for academic purpose using regression and clustering model 

# Function Description (Automatic Regression)

ordinal_label_encoder(df):

  return: df_ordinal, df_label 
  
  oridnal_label_encoder method takes argument of dataframe, and encodes categorical data with ordinal, label encoder.
  This function then returns two dataframe each encoded with ordinal, label encoder

regresison_model(scaler, X, y, model, train_size_val, random_state_val):
  
  return: accuracy
  
regression_best_model(df, selected_features, target, train_size_val, random_state_val):

  return: best accuracy(float), best scaler(text), best encoder(text), best regression(text)
  
  ![image](https://user-images.githubusercontent.com/90828283/171909682-d5b756d7-3d69-43e0-8a55-f219d2068ae9.png)

  
  regression_best_model method takes argument of dataframe, list of features to train, target feature, train size, random size
  It returns best accuracy and combination by trying every combination of
  
  Standard scaler, Robust Scaler, MaxabsScaler
  
  Label encoder, Ordinal encoder
  
  Linear, Polynomial, DecisionTreeClassifier regression
  

# File description

NYC_crime.ipynb : Source code & description & result screen

regression_function.py : Open source modules for automatic regression function

## Speical thanks to KhokiBernier
https://github.com/KhokiBernier

We've KhokiBernier's imported crime grouping categories,

and modified according to every Offense Description of latest NYC crime data (2022.April) 

![image](https://user-images.githubusercontent.com/90828283/171138266-ca715d16-f947-449c-803f-dd6aa1d69a15.png)

Datasets : NYC Opendata Crime data year to date

https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Map-Year-to-Date-/2fra-mtpn

Reference:

https://www.donga.com/news/Inter/article/all/20210327/106107177/1

https://www.kphn.org/bbs/board.php?bo_table=news_4&wr_id=66&page=2

https://www.joongang.co.kr/article/24090308#home

https://m.blog.naver.com/tjdrud1323/221720259834

https://rfriend.tistory.com/280

https://github.com/KhokiBernier/NYC-Neighborhood-Clustering/blob/main/NYC%20Neighborhood%20Clustering%20EDITED.ipynb
