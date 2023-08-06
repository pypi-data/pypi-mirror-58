# Assigning High Impact Pairs

This package makes it easy to assign pairs to experts using logic based on fields from the unified dataset.
The aim is that engineers will only have to worry about the logic of assigning pairs, rather than the humdrum work of
getting the data in and out of tamr.

It's workflow is:
- Load the unified dataset (UD) for the mastering project. A csv file of the UD is saved locally, along with a version number. 
If the version number of the UD in Tamr differs to the saved version, the latest version will be downloaded and saved.
- Get the high impact pairs (HIP) out of Tamr.
- Join the HIP to the UD
- {Custom user logic to assign HIP to experts}
- Push the assigned pairs back to tamr.


