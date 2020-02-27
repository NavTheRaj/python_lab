import matplotlib.pyplot as plt
import numpy as np

def file_operations():
    fname=input("Enter the filename\n")
    print("Enter the five data in file with its label\nIn this format\n Title:Number example Maths:95")
    with open(fname,"w") as fn: #fn=open(fname,"w+")
        for i in range(0,5):
            x=input()
            fn.write(str(x)+'\n')
    label=[]
    title=[]
    with open(fname,"r+") as fr:

            for line in fr:
                print(line)
                loc=line.rfind(':')
                t=line[0:loc]
                title.append(str(t))
                l=line[loc+1:]
                label.append(int(l))
            

    fr.close()
    return label,title

# loc=str_new.rfind(":")
def pie_graph(label,title):
    objects = title
    y_pos = np.arange(len(objects))
    x_pos = np.arange(len(label))
    performance = label
    colors=['blue','cyan','indigo','red','orange']

    plt.bar(y_pos, performance, align='center',color=colors)
    plt.xticks(y_pos)
    plt.yticks(performance)
    plt.xlabel('Items')
    plt.ylabel('Sales')
    plt.title('Stationary Product Sales Data')

    plt.show()

def main():
    label,title=file_operations()
    pie_graph(label,title)


main()
