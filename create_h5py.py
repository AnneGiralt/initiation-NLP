import h5py
import numpy as np
import os

# This function is directly used here, but wil be usefull later for the creation of X_test to !
def file_to_text(path, header = False):
    """This function takes the path of the file, extract the text from it, if necesary remove header"""
    with open(path) as text_1:
        text = text_1.read()
        
        if header :
            list_paragraphs =text.split("\n\n")
            text = ' '.join(list_paragraphs[1:])        
    
    return text


def size_dataset(path_dataset):
	""" This function gives the number of texts in the dataset."""
	N = 0

	for folder in os.listdir(path_dataset):
		for f in os.listdir(path_dataset + "/" + folder):
			if f == 'NOTE.txt':
				pass
			N+=1
	return N


def create_dataset_h5py_file(h5py_file, path_dataset, size):
    """Create the dataset as a numpy array in the h5py_file"""   
    numpy_data = np.zerros((size,3)) 
    i=0

    for folder in os.listdir(path_dataset):
		for f in os.listdir(path_dataset + "/" + folder):
			if f == 'NOTE.txt':
				pass

			text = file_to_text(folder + '/'+ f , header)
			numpy_data[i] = [text, folder, f]
			i+=1

	h5py_file.create_dataset("dataset_array",  data=numpy_data)
    return None


if __name__ == '__main__':

	PATH = "./dataset/train"
	N = size_dataset(path_dataset)

	# Create a h5py file for all my datas.
	F = h5py.File("mydatas.hdf5", "w")

	# Dump a array whith my dataset in a array N*3. Every line is given by a text, a category and the file number.
	create_dataset_h5py_file(h5py_file = F, path_dataset = , size = N)

	# Split my dataset into two np_array A_train and A_val


	# Create a numpy array with all vocabulary and respective term frequency for texts of A_train.


	



