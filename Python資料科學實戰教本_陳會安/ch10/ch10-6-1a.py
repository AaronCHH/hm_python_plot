import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")

sns.set()
sns.stripplot(x="species", y="sepal_length", jitter=False, data=df)
plt.show()
