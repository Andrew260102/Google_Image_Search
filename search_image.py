#import library
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.models import  Model
from PIL import Image
import pickle
import numpy as np
import math
import os


#Model
def get_extract_model():
    vgg16_model = VGG16(weights="imagenet")
    extract_model = Model(inputs=vgg16_model.inputs, outputs = vgg16_model.get_layer("fc1").output)
    return extract_model

# Covert image to tensor
def image_preprocess(img):
    img = img.resize((224,224))
    img = img.convert("RGB")
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return x

def extract_vector(model, image_path):
    print("Xu ly : ", image_path)
    img = Image.open(image_path)
    img_tensor = image_preprocess(img)

    # extract image features
    vector = model.predict(img_tensor)[0]
    # vector normalization
    vector = vector / np.linalg.norm(vector)
    return vector

# Translate the image to be searched for
search_image = "testimage/wolf.jpg"

# Model initialization
model = get_extract_model()

# extract image search features
search_vector = extract_vector(model, search_image)

# Load 4700 vector from vectors.pkl to variable
vectors = pickle.load(open("vectors.pkl","rb"))
paths = pickle.load(open("paths.pkl","rb"))

# find distance from search_vector to all vector in data set
distance = np.linalg.norm(vectors - search_vector, axis=1)

# Sort and  get K vectors with shortest distance
K = 16
ids = np.argsort(distance)[:K]

# Create oputput
nearest_image = [(paths[id], distance[id]) for id in ids]

# Show image
import matplotlib.pyplot as plt

axes = []
grid_size = int(math.sqrt(K))
fig = plt.figure(figsize=(10,5))


for id in range(K):
    draw_image = nearest_image[id]
    axes.append(fig.add_subplot(grid_size, grid_size, id+1))

    axes[-1].set_title(draw_image[1])
    plt.imshow(Image.open(draw_image[0]))

fig.tight_layout()
plt.show()