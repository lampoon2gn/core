'''
creates folders sheets 1-138 with test and train folders inside in cwd

'''
import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        

# Example
#createFolder('./fuck/you')
#createFolder('./fuck/bitch')

if __name__ == '__main__':

        for i in range (1,139):

                s = 'sheet'
                s = s + str(i)

                s1 = './' + s + '/test'
                s2 = './' + s + '/train'

                createFolder(s1)
                createFolder(s2)
                

