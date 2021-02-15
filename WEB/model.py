import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
data=pd.read_csv("mushrooms.csv")
data=data.drop(['stalk-root','veil-type'], axis=1)

data['class']=data['class'].map({'p':0, 'e':1})
data['cap-shape']=data['cap-shape'].map({'b':1, 'c':2, 'x':3, 'f':4, 'k':5, 's':6})
data['cap-surface']=data['cap-surface'].map({'f':1, 'g':2, 'y':3, 's':4})
data['cap-color']=data['cap-color'].map({'n':1, 'b':2, 'c':3, 'g':4, 'r':5, 'p':6, 'u':7,'e':8, 'w':9, 'y':10})
data['bruises']=data['bruises'].map({'t':1, 'f':0})
data['odor']=data['odor'].map({'a':1, 'l':2, 'c':3, 'y':4, 'f':5, 'm':6, 'n':7, 'p':8, 's':9})
data['gill-attachment']=data['gill-attachment'].map({'a':1, 'd':2, 'f':3, 'n':4})
data['gill-spacing']=data['gill-spacing'].map({'c':1, 'w':2})
data['gill-size']=data['gill-size'].map({'n':1, 'b':2})
data['gill-color']=data['gill-color'].map({'k':1, 'n':2, 'g':3, 'p':4, 'w':5, 'h':6, 'u':7, 'e':8, 'b':9, 'r':10, 'y':11, 'o':12})
data['stalk-shape']=data['stalk-shape'].map({'e':1, 't':2})
data['stalk-surface-above-ring']=data['stalk-surface-above-ring'].map({'s':1, 'f':2, 'k':3, 'y':4})
data['stalk-surface-below-ring']=data['stalk-surface-below-ring'].map({'s':1, 'f':2, 'y':4, 'k':3})
data['stalk-color-above-ring']=data['stalk-color-above-ring'].map({'w':1, 'g':2, 'p':3, 'n':4, 'b':5, 'e':6, 'o':7, 'c':8, 'y':9})
data['stalk-color-below-ring']=data['stalk-color-below-ring'].map({'w':1, 'p':2, 'g':3, 'b':4, 'n':5, 'e':6, 'y':7, 'o':8, 'c':9})
data['veil-color']=data['veil-color'].map({'w':1, 'n':2, 'o':3, 'y':4})
data['ring-number']=data['ring-number'].map({'o':1, 't':2, 'n':3})
data['ring-type']=data['ring-type'].map({'p':1, 'e':2, 'l':3, 'f':4, 'n':5})
data['spore-print-color']=data['spore-print-color'].map({'k':1, 'n':2, 'u':3, 'h':4, 'w':5, 'r':6, 'o':7, 'y':8, 'b':9})
data['population']=data['population'].map({'s':1, 'n':2, 'a':3, 'v':4, 'y':5, 'c':6})
data['habitat']=data['habitat'].map({'u':1, 'g':2, 'm':3, 'd':4, 'p':5, 'w':6, 'l':7})


X = data[['odor','spore-print-color','gill-color','ring-type','stalk-surface-above-ring','stalk-surface-below-ring','gill-size','stalk-color-above-ring','stalk-color-below-ring','bruises','population','habitat']]
y=data['class']
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=42,test_size=0.2)

from sklearn.svm import SVC
svm_linear=SVC(kernel='linear')
m=svm_linear.fit(X_train,y_train)
pickle.dump(svm_linear, open('model.pkl','wb'))

