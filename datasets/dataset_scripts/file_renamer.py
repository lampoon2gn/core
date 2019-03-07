import os

# Function to rename multiple files 
def rename_file_name(sheet_number): 
    i = 0
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    #Rename test files
    for filename in os.listdir(sheet_number + "/test"): 
        dst = sheet_number + "_test_{}.csv".format(chars[i])
        src = sheet_number + '/test/{}'.format(filename) 
        dst = sheet_number + '/test/{}'.format(dst) 
         
        os.rename(src, dst) 
        i += 1
    
    i = 0
    #Rename training files
    for filename in os.listdir(sheet_number + "/train"): 
        dst = sheet_number + "_train_{}.csv".format(chars[i])
        src = sheet_number + '/train/{}'.format(filename) 
        dst = sheet_number + '/train/{}'.format(dst) 
         
        os.rename(src, dst) 
        i += 1

def file_renamer():

    #Loop through the files
    for number in range(1, 139):
        rename_file_name("sheet{}".format(number))
  
if __name__ == '__main__': 
     
    file_renamer()