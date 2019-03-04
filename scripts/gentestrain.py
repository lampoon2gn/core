'''
generates two random indexes for test set
'''


import random 
import csv

def genRannums():
    a = random.randint(1,5)
    b = random.randint(1,5)


    while (a == b):
        b = random.randint(1,5)

    return a,b


if __name__ == '__main__':

    test = []
    for i in range(0,138):
        a, b = genRannums()
        if (a < b):
            #print(i, a, b)
            #print(str(a)+','+str(b))
            temp = str(a) + ',' + str(b)
            test.append(temp)
        else:
            #print(str(b)+','+str(a))
            temp = str(b) + ',' + str(a)
            test.append(temp)


    #print(test)
    with open('test.csv', 'w') as f:
        #writer = csv.writer(f)
        #writer.writerows(test)

        for l in test:
            print(l)
            f.write(l)
            f.write('\n')








    