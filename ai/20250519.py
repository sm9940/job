import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = sns.load_dataset("iris")
tips = sns.load_dataset("tips")
titanic = sns.load_dataset("titanic")
flights = sns.load_dataset("flights")

# sns.jointplot(x="sepal_length", 
#               y="sepal_width", 
#               data=data,
#               kind="kde")
# plt.suptitle("JointPlot by Iris Sepal " \
# "width/lenght", y=1.02)

# sns.pairplot(data, hue="species", markers=["o", "s", "D"])
# plt.title("Iris pair plot...")
print(titanic.head())
# titanic = titanic.dropna()
# titanic.age = titanic.age.fillna(0)
# titanic.age = titanic.age.astype(int)

print(titanic.age)
titanic_size = titanic.pivot_table(index="class", 
                                   columns="sex",
                                   aggfunc="size")
# titanic_size = titanic_size.fillna(0)
# titanic_size = titanic_size.astype(int)
print("===========================")
print(titanic_size.head())
# sns.heatmap(
#     titanic_size, cmap=sns.light_palette("red", as_cmap=True), annot=True, fmt="d"
# )
# plt.title("Heatmap...")
# sns.violinplot(x="day",
#                y="total_bill",
#                data=tips)
# sns.stripplot(x="day",
#                y="total_bill",
#                data=tips, jitter=False)
# sns.swarmplot(x="day",
#                y="total_bill",
#                data=tips)

# sns.boxplot(x="day",
#             y="total_bill",
#             hue="sex",
#             data=tips)
print(flights.describe)
flights_passengers = flights.pivot(index="month", 
                                   columns="year",
                                   values="passengers")

# sns.heatmap(
#     flights_passengers, cmap=sns.light_palette("red", as_cmap=True), 
#     annot=True, fmt="d"
# )

def sinplot(flip=1) :
    x = np.linspace(0, 14, 100)
    for i in range (1, 7):
        plt.plot(x, np.sin(x + i) * .5 *(7 - i ) * flip)
sns.set_style("darkgrid")        
sinplot()

plt.title("Sin plot")
plt.show()
