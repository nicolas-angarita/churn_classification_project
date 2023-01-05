import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy import stats
    


plots = {1 : [111], 2: [121, 122], 3: [131, 132, 133]}

def countplot(x, y, train):
    '''visualization of countplot using a for loop to go through my features'''
    plt.figure(figsize=(10, 7))
    
    for i, j in enumerate(y):
        plt.subplot(plots[len(y)][i])
        chart = sns.countplot(x=j, hue=x, data=train, alpha=0.75, linewidth=0.5, edgecolor='black', color = 'dodgerblue')
        chart.set_title(j)
        
    return plt.show()    

def chi_test(feature, train):
    '''get result of chi-square for a feature to churn'''

    observed = pd.crosstab(train[feature], train.churn_encoded)
    chi2, p, degf, expected = stats.chi2_contingency(observed)

    print(f'chi² = {chi2:.3f}')
    print(f'p = {p:.3}')

