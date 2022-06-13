# Model API Bangkit Capstone Project

This Project is Bangkit Capstone Project and this is the one of the requirements for Bangkit 2022's Graduation.  
The API can accept food images with JPG and JPEG extensions. The Response from this API is the name of the food and the number of calories in the food

## How to run?

`uvicorn application.server.main:app`

Because Github limited file size, you have to [Download](https://colab.research.google.com/drive/1eNOo4X0R5V4m0RB8OcHB6U9P_KCumZqe?usp=sharing) the model on your own.

## Docker Image
If you want to run this app, simply you can download this [API Docker Image](https://hub.docker.com/repository/docker/fatahdocker/capstone-api) and run it locally or using Cloud Platform.  

* You can use the latest version for more updated

## API Endpoint

`hostname/predict/image`

## Attribute

Request : form-data

- key: file
- value: image-file (JPG, JPEG)

## Machine Learning

We use pre-build model InceptionV3 and some additional layers to the top of the architecture. The model can detect 16 food classes, they are:

1. Apple
2. Banana
3. Cabbage
4. Chicken Curry
5. Chicken wings
6. Eggs Benedict
7. French Fries
8. Fried Rice
9. Lettuce
10. Mango
11. Omelette
12. Orange
13. Ramen
14. Rendang
15. Rice
16. Spinach

## Training Custom Dataset

To train the model, you can generate the model by run this notebook:

- [kukus_v5.ipynb](https://colab.research.google.com/drive/1eNOo4X0R5V4m0RB8OcHB6U9P_KCumZqe?usp=sharing)

The custom dataset can be accessed in this google drive:

- [Kukus Custom Dataset](https://drive.google.com/file/d/12So0zCK-QibHSw_TzpBuj3uemnY1p-tD/view?usp=sharing)
