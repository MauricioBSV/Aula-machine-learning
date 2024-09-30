from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np

iris = datasets.load_iris()

# print(iris.data)
# print(iris.feature_names)
# print(iris.target_names)
# print(iris.target)
# print(iris.data.shape)
# print(iris.target.shape)

features = iris.data
target = iris.target

featuresALL = []
featuresALtura = []
featuresLargura = []

for feature in features:
    featuresALL.append(feature[0] + feature[1] + feature[2] + feature[3])
    featuresALtura.append(feature[2])
    featuresLargura.append(feature[3])

# print(featuresALL)

plt.scatter(featuresALtura, featuresLargura, color='red', alpha=1.0)
plt.rcParams["figure.figsize"] = [10,8]
plt.title("Iris Dataset Scatter Plot")
plt.xlabel("Features")
plt.ylabel("Target")
plt.show()

featuresALL = []

for feature in features:
    altura = [feature[0] for feature in features]  # Sepal Length
    largura = [feature[1] for feature in features]  

colors = np.array(['red', 'green', 'purple'])[target]
plt.rcParams["figure.figsize"] = [10, 8]
plt.title("Iris Dataset Scatter Plot")
plt.xlabel("Altura da Sépala (cm)")
plt.ylabel("Largura da Sépala (cm)")
plt.colorbar(label='Target')  
plt.show()
plt.scatter(featuresALtura, featuresLargura, color=colors, alpha=1.0)
plt.rcParams["figure.figsize"] = [10, 8]
plt.title("Iris Dataset Scatter Plot")
plt.xlabel("Altura da Sépala (cm)")
plt.ylabel("Largura da Sépala (cm)")
plt.colorbar(label='Target')
plt.show()




