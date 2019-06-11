import wfdb
import numpy as np
import matplotlib.pyplot as plt

def get_ptb_data(num_samples, sample_length):
    ptb_entries = []
    with open ("data/CONTROLS", "r") as controlsFile:
        for line in controlsFile:
            ptb_entries.append(line.strip("\n").split("/"))
    ptb_data = []
    for ptb_entry in ptb_entries[0:num_samples]:
        signal, fields = wfdb.rdsamp(ptb_entry[1], channels=[2], sampfrom=0, sampto=sample_length, pb_dir='ptbdb/' + ptb_entry[0])
        x = signal.flatten()
        ptb_data.append(x);
    return ptb_data