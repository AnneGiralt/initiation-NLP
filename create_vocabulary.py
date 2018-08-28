import h5py
import numpy as np
import os
import csv
import nltk
import json



maxsize = 10000000
csv.field_size_limit(maxsize)

def text_to_list(T):
    """This function take a text as a string and change it to a clean list of words"""
    tokens = nltk.word_tokenize(T)
    return clean_list_words(tokens)

def clean_list_words(L):
    clean_list = []
    for w in L:
        if w.isalpha():
            clean_list.append(w)
    return clean_list


#################################### create_vocabulary ####################################

def create_vocabulary(h5py_file, data):

	with open(data, newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		A = np.array(list(spamreader), dtype=list)
		dico = {}

	for t in A[:,0]:
		l = text_to_list(t)
		for w in l:
			fill_dict(dico, w)

	D = {}
	M = np.zeros((len(dico),2))
	i=0
	for k,v in dico.items():
		D[k] = i
		M[i, 0] = v
		i+=1

	with open("dictionary_voc.json", 'w') as f:
		json.dump(D,f)
	h5py_file.create_dataset("Vocabulary",  data=M)
	return None


def fill_dict(D,elt):
    if elt in D:
        D[elt]+=1
    else:
        D[elt]=1
    return None


if __name__ == '__main__':

	# Create a h5py file for all my datas.
	with h5py.File("mydatas.hdf5", 'w') as hf:
		# Split my dataset into two np_array A_train and A_val
		create_vocabulary(h5py_file = hf, data = "train.csv")


	# Create a numpy array with all vocabulary and respective term frequency for texts of A_train.	



