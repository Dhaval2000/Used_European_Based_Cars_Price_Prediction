import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics.regressionplots import influence_plot
from sklearn.model_selection import train_test_split
import statsmodels.formula.api as smf
import numpy as np
import pickle

data = pd.read_csv(r'/Users/shaguftajahan/cleaned_autos.csv')
data.drop(labels=['Unnamed: 0'],axis=1,inplace=True)
data.reset_index(drop=True,inplace=True)

X = data.drop(['price','model','brand','kilometer_Bin'],axis=1)
y = data['price'] 

#RandomForestRegressor
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.02,random_state=0)
from sklearn.ensemble import RandomForestRegressor
random_reg = RandomForestRegressor()
random_reg.fit(X_train, y_train)

y_pred = random_reg.predict(X_test)
y_pred
 
r2_score = random_reg.score(X_test,y_test)
print(r2_score*100,'%') 

pickle_out = open('new_model.pkl','wb')
pickle.dump(random_reg,pickle_out)#saving our model in .pkl file 
pickle_out.close()
