import pickle

# Adjust the path to where your MNIST pickle file is located
pickle_file_path = 'C:\\Users\\admin\\Desktop\\MPhil\\M-ADA\\data\\mnist\\train.pkl'

with open(pickle_file_path, 'rb') as f:
    data = pickle.load(f)
    print(data.keys())  # This will show you all the keys in the dictionary stored in pickle file