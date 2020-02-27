import matplotlib.pyplot as plt

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
def pie_plot(label,title):
    labels = title
    sizes = label
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','cyan']
    explode = (0.1, 0, 0, 0)  # explode 1st slice
    patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
    plt.legend(patches, labels,loc="best")
    plt.axis('equal')
    # plt.tight_layout()
    plt.show()

def main():
    label,title=file_operations()
    pie_plot(label,title)


main()
