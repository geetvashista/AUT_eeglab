import mne
import mne_connectivity
import numpy as np

# Set variables

subject_ids = []  # Fill in all participant numbers to complete here
freqs = (2, 5, 10, 20, 50)  # frequencies of interest, must be within the fmin and fmax already specified
fname = r''  # path to epoched data


# Connectivity loop

output = []
for i in subject_ids:
    # import desired epoch
    fname2 = fname+str(i)+'_Cleaned'
    epochs = mne.read_epochs(fname2,
                             proj=True,
                             preload=True,
                             verbose=None
                             )

    # wpli calculator
    con = mne_connectivity.spectral_connectivity_time(epochs,
                                                      freqs=freqs,
                                                      method='wpli',
                                                      mode='multitaper',
                                                      fmin=(1., 4., 8., 13., 31),
                                                      fmax=(3., 7., 12., 30., 100),
                                                      sfreq=250,
                                                      average=False
                                                      )

    # generate connectivity matrix (lower triangle)
    tmp = con.get_data(output="dense")
    output.append(tmp)

# Final output
Connectivity_data = np.array(output)
