# traffic-sign-detection
Traffic Sign Recognition Project
Overview:
This repository contains the code and resources for a Traffic Sign Recognition project using a Convolutional Neural Network (CNN). The project aims to predict traffic sign classes from images. The model is trained on a dataset comprising traffic sign images.

Project Structure:
trainmodel.py: Python script for training the CNN model on the provided dataset.
gui.py: Graphical User Interface (GUI) application for predicting traffic sign classes using the trained model.
Dataset: Folder containing the dataset of traffic sign images.
labels.csv: CSV file mapping class labels to traffic sign names.
model.h5: Pre-trained CNN model saved in the Hierarchical Data Format (HDF5) file.

Training the Model:
Run trainmodel.py to train the CNN model using the provided dataset.
The model will be saved as model.h5 after training.


GUI Application:
Execute gui.py to launch the GUI application.
Click the "Browse" button to select an image for prediction.
The selected image will be displayed, and clicking the "Predict" button will display the predicted traffic sign class.

Requirements:
Python 3
TensorFlow
NumPy
OpenCV
Pillow
Pandas
Matplotlib
tkinter (for GUI)

Acknowledgments:
The project utilizes the MNIST dataset for traffic sign recognition.
The model architecture is based on a Convolutional Neural Network.
References:
MNIST Dataset
TensorFlow Documentation
OpenCV Documentation
Pandas Documentation
Matplotlib Documentation
Feel free to explore, contribute, and provide feedback!

Author: kartikeyajoshi3009

Contact: kartikeyajoshi3009@gmail.com
