import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_confirmed = 'time_series_19-covid-Confirmed.csv'
file_recovered = 'time_series_19-covid-Recovered.csv'
file_deaths = 'time_series_19-covid-Deaths.csv'

def get_confirmed_cases():
    return pd.read_csv(file_confirmed)

def plot_cases(df,date,y_label):
    columns = [df.columns[1]]
    columns = columns + [c for c in df.columns[4:]]
    df[columns].iloc[:,1:] = df[columns].iloc[:,1:].apply(pd.to_numeric)
    result = df[columns].groupby('Country/Region').sum()
    result = np.log(result)
    plt.figure(figsize=(20, 6))
    result = result.sort_values(by=date,ascending=False)
    y = result.index
    x = result[date]
    plt.bar(y, x, align='center', alpha=0.5)
    plt.ylabel(y_label)
    plt.xticks(rotation=90)
    plt.show()

def plot_confirmed_cases():
    plot_cases(df,date.today().strftime("%-m/%-d/%y"),'confirmed')
