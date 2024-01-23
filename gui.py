import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
from tensorflow.keras.models import load_model
import cv2
import pandas as pd

model = load_model("model.h5")

class_labels = pd.read_csv('labels.csv')

def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        selected_image_path.set(file_path)
        display_selected_image(file_path)

def display_selected_image(image_path):
    image = Image.open(image_path)
    image = image.resize((200, 200), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)

    selected_image_display.config(image=photo)
    selected_image_display.image = photo

def preprocess_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (32, 32))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.equalizeHist(img)
    img = img / 255.0
    img = img.reshape(1, 32, 32, 1)
    return img

def predict_image():
    image_path = selected_image_path.get()
    if image_path:
        preprocessed_image = preprocess_image(image_path)
        prediction = model.predict(preprocessed_image)
        predicted_class = np.argmax(prediction)
        class_name = class_labels[class_labels['ClassId'] == predicted_class]['Name'].values[0]
        predicted_label.set(f"Prediction: {class_name}")

root = tk.Tk()

root.configure(bg="#0C0404")

window_icon = Image.open("image.png")
window_icon = window_icon.resize((32, 32), Image.ANTIALIAS)
window_icon_photo = ImageTk.PhotoImage(window_icon)

root.title("Traffic Sign Predictor")
root.iconphoto(True, window_icon_photo)

header_image = Image.open("image.png")
header_image = header_image.resize((400, 400), Image.ANTIALIAS)
header_image_photo = ImageTk.PhotoImage(header_image)

header_label = tk.Label(root, image=header_image_photo, bg="#0C0404")
header_label.pack()

selected_image_path = tk.StringVar()
predicted_label = tk.StringVar()

button_color = "#D5B85A"
text_color = "white"
button_font = ("Arial", 16)
text_font = ("Arial", 14)

browse_button = tk.Button(root, text="Browse", command=browse_image, bg=button_color, fg=text_color, font=button_font)
browse_button.pack(pady=15)

selected_image_label = tk.Label(root, text="Selected Image:", bg="#0C0404", fg=text_color, font=text_font)
selected_image_label.pack()

selected_image_display = tk.Label(root, bg="#0C0404")
selected_image_display.pack()

predict_button = tk.Button(root, text="Predict", command=predict_image, bg=button_color, fg=text_color, font=button_font)
predict_button.pack(pady=10)

predicted_label_display = tk.Label(root, textvariable=predicted_label, bg="#0C0404", fg=text_color, font=text_font)
predicted_label_display.pack()

root.mainloop()