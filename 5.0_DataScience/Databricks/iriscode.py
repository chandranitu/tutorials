#https://www.youtube.com/watch?v=OWJHHAtnAwY
# ML flow exampls

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import mlflow
import mlflow.sklearn


data =load_iris()
data.target
data.target_names
data.feature_names

X=data.data
y=data.target

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.25,random_state=10)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from sklearn.decomposition import PCA

X=data.data[:,:2]
y=data.target

x_min,x_max= X[:,0].min() - .5, X[:,0].max() + .5
y_min,y_max= X[:,0].min() - .5, X[:,0].max() + .5
plt.figure(2, figsize=(8,6))
plt.clf()

#plot the training points
plt.scatter(X[:,0],X[:,1],c=y,cmap=plt.cm.Set1,edgecolor='k')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal width')

plt.xlim(x_min,x_max)
plt.ylim(x_min,x_max)
plt.xticks(())
plt.yticks(())


fig=plt.figure(1,figsize=(8,6))
ax=Axes3D(fig,elev=-150,azim=110)
X_reduced=PCA(n_components=3).fit_transform(data.data)
ax.scatter(X_reduced[:,0],X_reduced[:,1],X_reduced[:,2],c=y,cmap=plt.cm.Set1, edgecolor='k',s=40)
ax.set_title("First three PCA directions")
ax.set_xlabel ( "1st eigenvector" )
ax.w_xaxis.set_ticklables([])

ax.set_ylabel ( "2nd eigenvector")
ax.w_yaxis.set_ticklables([])
ax.set_zlabel ("3rd eigenvector")
ax.w_zaxis.set_ticklables([])
fig.savefig('/dbfs/mlflow/iris/iris1.png')
plt.close(fig)
display()
display()

!rm -r /dbfs/mlflow/iris

# 1st iteration

mlflow.start_run()
dtc = DecisionTreeClassifier(random_state=10)
dtc.fit(X_train,Y_train) 
y_pred_class= dtc.predict(X_test)
accuracy= metrics.accuracy_score(Y_test,y_pred_class)
print (accuracy) 
mlflow.log_param("random_state",10 )
mlflow.log_metric("accuracy" , accuracy) 
mlflow.sklearn.log_model (dtc , "model") 
modelpath = "/dbfs/mlflow/iris/model-%s-%f" % ("decision_tree", 1) 

mlflow.sklearn.save_model (dtc, modelpath) # going to save pickle model alongwith my experiment ,(scikit generates pickle file of model.)	

mlflow.log_artifact("iris1.png" )# saving my artifacts. other artifacts could be feature columns, data with different versions,

#mlflow.end_run()


# 2nd iteration

mlflow.start_run()
dtc = DecisionTreeClassifier(max_depth=1,random_state=10)  #change
dtc.fit(X_train,Y_train) 
y_pred_class= dtc.predict(X_test)
accuracy= metrics.accuracy_score(Y_test,y_pred_class)
print(accuracy) 
mlflow.log_param("random_state",10 )  #change
mlflow.log_param("max_depth",1 )
mlflow.log_metric("accuracy" , accuracy) 
mlflow.sklearn.log_model (dtc , "model") 
modelpath = "/dbfs/mlflow/iris/model-%s-%f" % ("decision_tree", 2) #change

mlflow.sklearn.save_model (dtc, modelpath) # going to save pickle model alongwith my experiment ,(scikit generates pickle file of model.)	

mlflow.log_artifact("iris1.png" )# saving my artifacts. other artifacts could be feature columns, data with different versions,

#mlflow.end_run()
-------------------------------------- Deployment

mlflow.search_runs()
run_id1="1279274554041"
model_uri="runs:/" + run_id1+ "/model"
model =mlflow.sklearn.load_model(model_uri=model_uri) #to check right model
model.predict_prob(X_test)
model.get_prams()
