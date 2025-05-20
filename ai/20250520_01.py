from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

data = load_iris()
print(data.keys())
print(data.DESCR)


features = pd.DataFrame(data=data.data,
                        columns=data.feature_names)

print(features)

target = pd.DataFrame(data.target, columns=["species"])
iris = pd.concat([features, target], axis=1)


iris.rename({'sepal length (cm)' : 'sepal_length',
             'sepal width (cm)' : 'sepal_width',
             'petal length (cm)' : 'petal_length',
             'petal width (cm)' : 'petal_width'},
            axis=1, inplace=True)

# iris['species'] = \
#     iris.species.map(lambda x:data.target_names[x])


print(iris)
print(iris.isna().sum(axis=0))
print(iris.info())
print(iris.describe())
# print(iris.corr())

print(iris.groupby('species').size())

def boxplt_iris(feature_names, dataset):
    i = 1
    plt.figure(figsize=(11,9))
    for col in feature_names:
        plt.subplot(2,2,i)
        plt.axis('on')
        plt.tick_params(axis='both', left=True,
                        top=False, right=False,
                        bottom=True, labelleft=False,
                        labeltop=False, labelright=False,
                        labelbottom=False)
        dataset[col].plot(kind='box', subplots=True,
                          sharex=False, sharey=False)
        plt.title(col)
        i += 1
    # plt.show()
    
print(boxplt_iris(iris.columns[:-1], iris))


def histogram_iris(feature_names, dataset):
    i = 1
    plt.figure(figsize=(11,9))
    for col in feature_names:
        plt.subplot(2,2,i)
        plt.axis('on')
        plt.tick_params(axis='both', left=True,
                        top=False, right=False,
                        bottom=True, labelleft=False,
                        labeltop=False, labelright=False,
                        labelbottom=False)
        dataset[col].hist()
        plt.title(col)
        i += 1
    # plt.show()

print(histogram_iris(iris.columns[:-1], iris))


corr = iris.corr()
cmap = sns.diverging_palette(220,10, as_cmap=True)

plt.figure(figsize=(11,9))
sns.heatmap(corr, cmap=cmap, vmax=1.0, vmin=-1.0, center=0,
            square=True, linewidths=.5, cbar_kws={'shrink':.5})


sns.pairplot(iris, hue='species')
# plt.show()


from sklearn.model_selection import train_test_split
xTrain, xTest, yTrain, yTest = train_test_split(
    iris.iloc[:, :-1], iris.iloc[:, -1], test_size=0.33,
    random_state=42, shuffle=True)
print(yTest.describe)


from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(
    criterion='gini', splitter='best',
    max_depth=None, min_samples_split=2,
    min_samples_leaf=1, min_weight_fraction_leaf=0.0,
    max_features=None, min_impurity_decrease=0.0
)

print(model)
print(model.fit(xTrain, yTrain))
print(model.score(xTest, yTest))

from sklearn.model_selection import cross_val_score, KFold

cv = KFold(n_splits=10, shuffle=True, random_state=42)
results = cross_val_score(model, xTrain, yTrain, cv=cv)
fin_result = np.mean(results)

for i, _ in enumerate(results):
    print('{}번째 교차 검증 정확도: {}'.format(i, _))
    
print('\n교차검증 최종 정확도: {}'.format(fin_result))


from sklearn.model_selection import StratifiedKFold
cv1 = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
results = cross_val_score(model, xTrain, yTrain, cv=cv1)
fin_result = np.mean(results)

for i, _ in enumerate(results):
    print('{}번째 교차 검증 정확도: {}'.format(i, _))
    
print('\n교차검증 최종 정확도: {}'.format(fin_result))


import scikitplot as skplt
skplt.estimators.plot_learning_curve(model, xTrain, yTrain, figsize=(6,6))
# plt.show()

from sklearn.model_selection import GridSearchCV
estimator = DecisionTreeClassifier()
parameters = {
    'criterion' : ['gini','entropy'],
    'splitter' : ['best','random'],
    'max_depth' : [4,6,8,10,12],
    'min_weight_fraction_leaf' : [0.0,0.1,0.2,0.3],
    'random_state' : [7,23, 42, 78, 142],
    'min_impurity_decrease' : [0.0, 0.05, 0.1, 0.2]
}
model = GridSearchCV(estimator=estimator, param_grid=parameters,
                     cv = cv1, verbose=1, n_jobs=-1,
                     refit=True)
model.fit(xTrain, yTrain)
print('Best Estimator: \n', model.best_estimator_)
print('\nBest Estimator: \n', model.best_params_)
print('\nBest Score: \n', model.best_score_)

DecisionTreeClassifier(criterion='entropy',max_depth=4,random_state=23,splitter='random')
model.fit(xTrain,yTrain)
print('GSCV model score = ',model.score(xTest,yTest))

from sklearn.metrics import accuracy_score,confusion_matrix

pred = model.predict(xTest)
acc =accuracy_score(yTest,pred)
confMatrix = confusion_matrix(yTest,pred)
print('Accuracy: ',acc)
print('\nConfusion Matrix:',confMatrix)