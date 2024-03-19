"""
Pickle is a Python module that allows you to serialize 
and deserialize objects. Serialization is essential when 
you want data to persist.
"""

import pickle
import os

# Create a testing object
data = {'name': 'Maurice', 'age': '25', 'user': 'zmauricetrammell'}

path = '../saved_data/data.pkl'

isExist = os.path.exists(path)
print(isExist)

if not isExist:
    # Serialize into a binary format
    with open('../saved_data/data.pkl','wb') as file:
        pickle.dump(data,file)
else:
    # Deserialize from binary
    with open('../saved_data/data.pkl','rb') as file:
        loaded_data = pickle.load(file)
        print(loaded_data)
