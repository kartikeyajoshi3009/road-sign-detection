# Traffic Sign Recognition Project

## Overview:

This repository contains the code and resources for a Traffic Sign Recognition project using a Convolutional Neural Network (CNN). The project aims to predict traffic sign classes from images. The model is trained on a dataset comprising traffic sign images.

## Project Structure:

- **trainmodel.py:** Python script for training the CNN model on the provided traffic sign dataset.
- **gui.py:** Graphical User Interface (GUI) application for predicting traffic sign classes using the trained model.
- **Dataset:** Taken form kaggle https://www.kaggle.com/datasets/ahemateja19bec1025/traffic-sign-dataset-classification.
- **labels.csv:** CSV file mapping class labels to traffic sign names.
- **model.h5:** Pre-trained CNN model saved in the Hierarchical Data Format (HDF5) file.

## Usage:

### Training the Model:

1. Run `trainmodel.py` to train the CNN model using the provided traffic sign dataset.
2. The model will be saved as `model.h5` after training.

### GUI Application:

1. Execute `gui.py` to launch the GUI application.
2. Click the "Browse" button to select an image for prediction.
3. The selected image will be displayed, and clicking the "Predict" button will display the predicted traffic sign class.

## Requirements:

- Python 3
- TensorFlow
- NumPy
- OpenCV
- Pillow
- Pandas
- Matplotlib
- tkinter (for GUI)

## Acknowledgments:

- The project utilizes a traffic sign dataset for recognition.
- The model architecture is based on a Convolutional Neural Network.

## References:

- [Traffic Sign Dataset (https://www.kaggle.com/datasets/ahemateja19bec1025/traffic-sign-dataset-classification)]
- [TensorFlow Documentation](https://www.tensorflow.org/)
- [OpenCV Documentation](https://docs.opencv.org/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Matplotlib Documentation](https://matplotlib.org/)

Feel free to explore, contribute, and provide feedback!

**Author:** Kartikeya Joshi 

**Github:** kartikeyajoshi3009

**Contact:** kartikeyajoshi3009@gmail.com
