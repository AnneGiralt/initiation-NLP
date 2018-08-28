import csv
import os
import numpy as np

maxsize = 10000000
csv.field_size_limit(maxsize)



# This function is directly used here, but wil be usefull later for the creation of X_test to !
def file_to_text(path, header = False):
    """This function takes the path of the file, extract the text from it, if necesary remove header"""
    with open(path) as text_1:
        text = text_1.read()
        
        if header :
            list_paragraphs =text.split("\n\n")
            text = ' '.join(list_paragraphs[1:])        
    
    return text

#################################### create_csv_data ####################################

def folder_to_csv_file(file_name, folder_path, header = False, category = 0):
    """Given a path of text file this function transfom theses texts into a np.array with fist column is all texts and the second is the name of file"""
    
    with open(file_name, 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        
        for f in os.listdir(folder_path):
            if f == 'NOTE.txt':
                pass
            text = file_to_text(folder_path + '/'+ f , header)      
            
            spamwriter.writerow([text, f, category ])
    
    return None


def create_csv_data(csv_file_name, path_data):
    """Create a nice csv file from the train folder.
    Be carreful the function folder_to_file is in a "append" mode, 
    means that every time the create_csv_data function is used the database increase."""   
    for folder in os.listdir(path_data):
        folder_to_csv_file(file_name = csv_file_name, 
                           folder_path = path_data + "/" + folder, header = True, category= folder)
    return None

#################################### create_train_val ####################################

def create_train_val():
    """take datas in database.csv and create train.csv and test.csv"""
    with open('database.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        A = np.array(list(spamreader), dtype=list)

    A_train, A_val = split_train_val(A)

    with open('train.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for line in A_train:
            spamwriter.writerow(line)

    with open('val.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for line in A_val:
            spamwriter.writerow(line)

    return None



def split_train_val(A):
    """ Take a numpy array as argument and return two numpy array train and val"""
    len_A = A.shape[0]
    n_1 = int(len_A*4/5)
    n_2 = len_A - n_1

    shuffled_index = np.random.permutation(range(len_A))
    A_train = A[shuffled_index[0:n_1]]
    A_val = A[shuffled_index[n_1:len_A]]

    return A_train, A_val


if __name__ == '__main__':


    PATH = "./dataset/train"
    file = "database.csv"
    create_csv_data(csv_file_name = file, path_data = PATH)

    create_train_val()

    '''
    # Testing the function folder_to_csv_file on a test file !
    testing_path = "./dataset/train/alt.atheism"
    folder_to_csv_file(file_name = "test.csv", folder_path = testing_path, header = True)

    # Testing if the function folder_to_csv_file write correctly the content of the folder alt.atheism
    with open('test.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in list(spamreader)[100:102]:
            print(', '.join(row))
    '''