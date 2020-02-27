import matplotlib.pyplot as plt
import numpy as np
from numpy import mean

def read_file():
    fp=open("population.txt","r")
    data=fp.readlines()
    fp.close()
    date=list()
    number=list()
    new=list()
    predict_date_list=np.arange(2019,2031,1)
    print(predict_date_list)

    for lines in data:
        lines=lines.strip()
        new=lines.split(',')
        date.append(new[0])
        number.append(new[1])

    return date,number,predict_date_list

def data_converse(date,number):
    x = np.array(range(1,len(date)+1))
    y = np.asarray(number) #changing string data into numpy array
    y = list(map(int, y)) #changing into integer format
    [a,b] = np.polyfit(x,y,1) #1 is degree finding a and b value for ax+b

    return a,b,x,y

def plot_prediction(date,predict_date_list,x,y,a,b):
    new=np.append(date,predict_date_list) #EXTENDING DATE UPTO 2030
    plt.title("Forecasting Elementary Schools Population")
    plt.xlabel('Date')
    plt.ylabel('Number')
    xticks=new  #SETTING DATE FROM 2001 TO 2030 FOR GRAPHS
    plt.xticks(range(1,31),xticks)
    plt.scatter(x,y,color="blue")
    plt.plot([0,30],[b,30*a+b],'r--s') 
    plt.show()
def main():
    date,number,predict_date_list=read_file()
    a,b,x,y=data_converse(date,number)
    plot_prediction(date,predict_date_list,x,y,a,b)

main()
