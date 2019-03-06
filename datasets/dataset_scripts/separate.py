
import pandas as pd
import os 
import shutil


def read_f():
    cwd = os.getcwd()
    dfile = pd.read_csv(os.path.join(cwd, 'fuckthis.csv'))

    return dfile.values



if __name__ == '__main__':

    dpath = '/Users/Cole/Documents/cpts/Metriguard/test-train-1'
    data = read_f()

    #print(data[34][7])
    #print(data[34][8])


    cwd = os.getcwd()
    

    for i in range(63,64):
        test = []
        train = []
        c = 1

        #getting test indexes
        test.append(data[i-1][7])
        test.append(data[i-1][8])
        #print(test)

        #getting train indexes
        for j in range(1,6):
            if j != test[0] and j != test[1]:
                train.append(j)

        #print(test)
        #print(train)
        '''
        for item in test:
            f1 = data[i-1][item]
            print(f1)
        '''

        for dirs in os.walk(cwd + '/data/dme'):
            #only one dir
            for d in dirs:
                #3rd item in folder is list with all csv files  
                if c == 3:
                    for fuck in d:
                        #print(fuck)

                        #dealing with testing 
                        for item in test:
                            f1 = str(data[i-1][item]) + '.csv'
                            if fuck.endswith(f1):
                                shutil.move(cwd+ '/data1/dme/'+fuck, dpath+'/sheet'+str(i)+'/test')

                        #dealing with training
                        for item in train:
                            f1 = str(data[i-1][item]) + '.csv'
                            if fuck.endswith(f1):
                                shutil.move(cwd+ '/data1/dme/'+fuck, dpath+'/sheet'+str(i)+'/train')

                c = c+1
        
    print(' ')





