import csv 
import numpy as np
import plotly.express as pe

def getData(data,x,y):
    coffee=[]
    sleep=[]
    with open(data) as f:
        r1 = csv.DictReader(f)
        for i in r1:
            coffee.append(float(i[x]))
            sleep.append(float(i[y]))
    return{"x":coffee,"y":sleep}

def find(sourc,message):
    correlation = np.corrcoef(sourc["x"],sourc["y"])
    print(message,correlation[0,1])

def plot_graph1():
    with open("coffee.csv")as f:
        df = csv.DictReader(f)
        fig = pe.scatter(df,x="Coffee in ml",y="sleep in hours",color="week")
        fig.show()

def plot_graph2():
    with open("marks.csv")as f:
        df = csv.DictReader(f)
        fig = pe.scatter(df,x="Marks In Percentage",y="Days Present",color="Roll No")
        fig.show()

def main():
    data = "marks.csv"
    data1 = "coffee.csv"
    source = getData(data,x="Marks In Percentage",y="Days Present")
    source1 = getData(data1,x="Coffee in ml",y="sleep in hours")
    find(source,message="Correlation for data1: ")
    find(source1,message="Correlation for data2: ")
    plot_graph1()
    plot_graph2()

main()