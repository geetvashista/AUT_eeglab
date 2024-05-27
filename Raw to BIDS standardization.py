import pathlib
import mne
import mne_bids

# Import raw data

file = pathlib.Path(r'')  # Path to the raw data file
raw = mne.io.read_raw_curry(file, preload=True)  # current MNE function assumes acquisition is a curry file.
# Change as need, see MNE doc for options.


# Set line freq

raw.info['line_freq'] = 50


# Set participant details

participant = '01'  # participant number; must be a str
task = ''  # Name of experiment task
out_path = pathlib.Path(r'')  # Change to desired output directory


# BIDS write up

bids_path = mne_bids.BIDSPath(subject=participant,
                              task=task,
                              root=out_path)

mne_bids.write_raw_bids(raw,
                        bids_path=bids_path,
                        format='BrainVision',
                        allow_preload=True,
                        overwrite=False
                        )

# NOTE: the format of the raw data in the BIDS is now BrainVision, not curry.
# See MNE doc for options.
