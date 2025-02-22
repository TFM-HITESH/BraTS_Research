import synapseclient
import synapseutils
import os

# Set Synapse cache directory to D:/datasets
os.environ["SYNAPSE_CACHE_DIR"] = "D:/Datasets/BraTS_2024"

# Initialize and log in to Synapse
syn = synapseclient.Synapse()
syn.login(authToken="")  # Replace with actual token

# Download files to D:/datasets
files = synapseutils.syncFromSynapse(syn, 'syn59059776', path="D:/Datasets/BraTS_2024")
