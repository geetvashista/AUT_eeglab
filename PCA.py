import numpy as np
import mne
from sklearn.decomposition import PCA
from mne.decoding import UnsupervisedSpatialFilter

# import data

data = mne.read_epochs(r'')  # Fill in data path, assumed to be an instance of mne.Epoch


# prep raw data for input

data_array = data.get_data()
input_array = np.expand_dims(data_array, axis=0)


# PCA

pca = UnsupervisedSpatialFilter(PCA(10), average=False)  # Change n_components of PCA as desired
pca_data = pca.fit_transform(input_array)

# NOTE: n_components can be ‘mle’ also. See sklearn.decomposition.PCA doc.
