import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
np.random.seed(42)
x = np.random.rand(100, 1)
y = np.array(['Class1' if xi <= 0.5 else 'Class2' for xi in x[:50]])
print("\n Training data set upto first 50 numbers")
for i ,label in enumerate(y[:50],start=1):
    print(f"x{i}={x[i-1][0]:.3f}->classified as {label}")
k_values = [1, 2, 3, 4, 5, 20, 30]
for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x[:50], y)
    y_pred = knn.predict(x[50:])
    print(f"\nResults for k = {k}:")
    for i, label in enumerate(y_pred, start=51):
        print(f"x{i} = {x[i-1][0]:.3f} → Classified as{label}")
plt.figure(figsize=(8, 5))
plt.scatter(x[:50], np.zeros(50), c=['blue' if yi == 'Class1'else 'red' for yi in y],label="Labeled Data")
plt.scatter(x[50:], np.zeros(50), c='black', marker='x',label="Unlabeled Data")
plt.xlabel("x values")
plt.ylabel("Classification")
plt.title("KNN Classification of Random Data Points")
plt.legend( )
plt.show( )