import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import statistics
import random
import csv

df=pd.read_csv("sample_2.csv")
data=df["reading_time"].tolist()
def random_set_of_mean(counter):
    dataset=[]
    for i in range(0, counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean
mean_list=[]
#----------------reading section----------------
for i in range(0, 1000):
        set_of_mean=random_set_of_mean(100)
        mean_list.append(set_of_mean)
mean=statistics.mean(mean_list)
stdev=statistics.stdev(mean_list)
print("mean=", mean)
print("stdev=", stdev)
first_stdev_start, first_stdev_end=mean-stdev,mean+stdev
second_stdev_start, second_stdev_end=mean-(2*stdev),mean+(2*stdev)
third_stdev_start, third_stdev_end=mean-(3*stdev),mean+(3*stdev)
#----------------Code:1----------------
df=pd.read_csv("sample_2.csv")
data=df["reading_time"].tolist()
mean_of_sample_1=statistics.mean(data)
fig=ff.create_distplot([mean_list],["reading_time"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.15], mode='lines', name="mean"))
fig.add_trace(go.Scatter(x=[mean_of_sample_1, mean_of_sample_1], y=[0, 0.10], mode='lines', name="mean"))
fig.add_trace(go.Scatter(x=[first_stdev_end, first_stdev_end], y=[0, 0.10], mode='lines', name="mean"))
fig.add_trace(go.Scatter(x=[second_stdev_end, second_stdev_end], y=[0, 0.10], mode='lines', name="mean"))
fig.add_trace(go.Scatter(x=[third_stdev_end, third_stdev_end], y=[0, 0.10], mode='lines', name="mean"))
fig.show()
#----------------Code:2----------------
df=pd.read_csv("sample_2.csv")
data=df["reading_time"].tolist()
mean_of_sample_2=statistics.mean(data)
fig=ff.create_distplot([mean_list],["reading_time"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.15], mode='lines', name="mean"))
fig.add_trace(go.Scatter(x=[mean_of_sample_1, mean_of_sample_1], y=[0, 0.10], mode='lines', name="mean"))
fig.add_trace(go.Scatter(x=[first_stdev_end, first_stdev_end], y=[0, 0.10], mode='lines', name="mean"))
fig.add_trace(go.Scatter(x=[second_stdev_end, second_stdev_end], y=[0, 0.10], mode='lines', name="mean"))
fig.add_trace(go.Scatter(x=[third_stdev_end, third_stdev_end], y=[0, 0.10], mode='lines', name="mean"))
fig.show()
#----------------Code:3----------------
df=pd.read_csv("sample_2.csv")
data=df["reading_time"].tolist()
mean_of_sample_3=statistics.mean(data)
fig=ff.create_distplot([mean_list],["reading_time"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.15], mode='lines', name="mean"))
fig.add_trace(go.Scatter(x=[mean_of_sample_1, mean_of_sample_1], y=[0, 0.17], mode='lines', name="mean"))
fig.add_trace(go.Scatter(x=[first_stdev_end, first_stdev_end], y=[0, 0.17], mode='lines', name="mean"))
fig.add_trace(go.Scatter(x=[second_stdev_end, second_stdev_end], y=[0, 0.17], mode='lines', name="mean"))
fig.add_trace(go.Scatter(x=[third_stdev_end, third_stdev_end], y=[0, 0.17], mode='lines', name="mean"))
fig.show()
#----------------z score----------------
z_score=(mean-mean_of_sample_2)/stdev
print("zscore=", z_score)