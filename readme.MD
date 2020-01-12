# Nedersaksisch NER

This repository contains the data belonging to the paper Named Entity 'Recognition in
a Group of Mutually Intelligible Dialects'.

## Contents
- `model`-folder: Contains the trained model by spaCy. Can be readily imported using spaCy to be used.
- `ns`-folder: Constitutes the Nedersaksisch language class. Can be placed in the `lang` folder in spaCy's source code to change or improve the model.
- `text-cleaner.py`: Script that removes characters from their accents.
- `train-and-evaluate-model.py`: Script used to train and evaluate the model. This script was used to create the model in the `model`folder.
- `training-data.txt` and `verification-data.txt`: Contain the training and verification data respectively. 