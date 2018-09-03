import json
import nltk
import numpy as np
import h5py

import create_vocabulary

# Previously on initiation-NLP we ran the python files create_csv_database and then create_vocabulary.

# create_csv_database takes all files in the dataset and create a csv. 
# Every row is given by : a text, a number, a category 

# create_vocabulary only uses vocabulary of train text. It create two things a numpy array and a dictionnary.
# The numpy array is a h5py file with called vocabulary. Every row correspond to a word and gives two columns TF and IDF (initialised at 0). 
# The corespondance between the words of train's texts and the array vocabulary is given by the dictionary dictionary_voc.json.



def threshold(n, D):
	"""This function takes a dictionnary and a threshold as arguments 
	and return the dictionary with all associated values in vocabulary gretaer than n."""
	new_dict = {}
	for k,v in D.items():
		if vocabulary[v, 0] >= n:
			new_dict[k] =v
	return new_dict

# Import dico from dictionary_voc.json.
with open("dictionary_voc.json", 'r') as f:
		dico_index = json.load(f)


# Import numpy array vocabulary
f = h5py.File('mydatas.hdf5', 'a')
vocabulary = f['Vocabulary'][:]

# Remove word that apear less than threshold times
dico_index = threshold(5, dico_index)


# Calculate normalisation
N = np.sum(vocabulary[:,0])

# Calculate idf and put in numpy_voc


#for word, index in dico_index.items():




# Create X_train, X_val from A_train and A_val

# Create function text_to_vector 
## Take a text as argument. For every word in the dico_index.keys, check how many times this word occur and multiply by idf /normalisation. 

f.close()