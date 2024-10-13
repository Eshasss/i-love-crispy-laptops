from sklearn.datasets import load_iris
impord pandas as pd
iris = loas_iris
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

df["a"]=df["sepal length (cm)"]
df["b"]=df["sepal width (cm)"]
df["c"]=df["petal length (cm)"]
df["d"]=df["petal width (cm)"]


#df.shape -- Размеры
#df.drop

#df.dropna(axis="rows", inplace=True) -- Заменяет все Npnes
#df.to_csv("iris.csv")