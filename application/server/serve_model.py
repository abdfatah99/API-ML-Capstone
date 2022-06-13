from io import BytesIO
from operator import mod
import os
import numpy as np
import tensorflow as tf
from PIL import Image
from keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

model = None

print(f'list of directory: {os.listdir()}')
print(f'getcwd result: {os.getcwd()}')

ROOT_PATH = os.path.abspath(os.curdir)
model_path = os.path.join(ROOT_PATH, "kukus_final_model.hdf5")

print(model_path)

target_size = (299, 299)

def load_model_func():
    print("test print load model func")
    model_inner = load_model(model_path)
    print("Model loaded")
    return model_inner


def predict(img: Image.Image):
    global model
    if model is None:
        model = load_model_func()

    img = img.resize(target_size)
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img /= 255.

    result = model.predict(img)
    print(f'hasil prediksi {result}')

    food_list = ['Apple', #0
             'Banana', #1
             'Cabbage', #2
             'Chicken Curry', #3
             'Chicken wings', #4
             'Eggs Benedict', #5
             'French Fries', #6
             'Fried Rice', #7
             'Lettuce', #8
             'Mango', #9
             'Omelette', #10
             'Orange', #11
             'Ramen', #12
             'Rendang',
             'Rice', #13
             'Spinach'] #14

    food_dict = {
        "Apple": "58",
        "Banana": "108",
        "Cabbage": "51",
        "Chicken Curry": "473",
        "Chicken Wings": "297",
        "Eggs Benedict": "251",
        "French Fries": "142",
        "Fried Rice": "180",
        "Lettuce": "41",
        "Mango": "46",
        "Omelette": "251",
        "Orange": "45",
        "Ramen": "102",
        "Rendang": "193",
        "Rice": "180",
        "Spinach": "16"
    }

    food_translate = {
        "Apple": "Apel",
        "Banana": "Pisang",
        "Cabbage": "Kubis",
        "Chicken Curry": "Kari Ayam",
        "Chicken Wings": "Sayap Ayam",
        "Eggs Benedict": "Telor 1/2 Matang",
        "French Fries": "Kentang Goreng",
        "Fried Rice": "Nasi Goreng",
        "Lettuce": "Selada",
        "Mango": "Mangga",
        "Omelette": "Telur",
        "Orange": "Jeruk",
        "Ramen": "Mie",
        "Rendang": "Rendang",
        "Rice": "Nasi",
        "Spinach": "Bayam"
    }

    result = result.tolist()
    list_result = max(result)
    hasil_pred = max(list_result)

    index = np.argmax(result)
    food_list.sort()
    print(f"hasil Prediksi label: {food_list[index]}")

    print(f'hasil_pred: {hasil_pred}')
    print(f'panjang_list: {len(list_result)}, type: {type(list_result)}')
    print(f'max: {hasil_pred}, type: {type(hasil_pred)}')

    #print(food_dict[hasil_pred])
    pred_result = food_list[index]
    nama = food_translate[pred_result]
    kalori = food_dict[pred_result]
    return {
        "nama": nama,
        "kalori": kalori
    }

def read_imagefile(file) -> Image.Image:
    image = Image.open(BytesIO(file))
    return image
