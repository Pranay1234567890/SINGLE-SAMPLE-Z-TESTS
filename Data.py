import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import random

df = pd.read_csv('D:\cfrbackup-LLGBPKSV\Whitehatjr\Python Classes\C-110-Project\medium_data.csv')
data = df['reading_time'].tolist()
population_mean = statistics.mean(data)
population_std = statistics.stdev(data)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    std_deviation = statistics.stdev(df)
    first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
    second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
    third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)
    fig = ff.create_distplot([df], ["reading_time"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="Mean"))
    fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 1], mode="lines", name="STANDARD DEVIATION 1"))
    fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 1], mode="lines", name="STANDARD DEVIATION 1"))
    fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 1], mode="lines", name="STANDARD DEVIATION 2"))
    fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 1], mode="lines", name="STANDARD DEVIATION 2"))
    fig.add_trace(go.Scatter(x=[third_std_deviation_start, third_std_deviation_start], y=[0, 1], mode="lines", name="STANDARD DEVIATION 3"))
    fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 1], mode="lines", name="STANDARD DEVIATION 3"))
    fig.show()

def setup():
    mean_list = []
    for i in range(100):
        set_of_means= random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    
    mean = statistics.mean(mean_list)
    std = statistics.stdev(mean_list)
    print(f'Population Mean is {population_mean}')
    print(f'Sampling Mean is {mean}')

    z_score = (mean - population_mean)/std
    print(f'The z score is {z_score}')

setup()