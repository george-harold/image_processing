# -*- coding: UTF-8 -*-
# !/usr/bin/env python
# author: harold-chen
# website: https://github.com/george-harold

from PIL import Image
import numpy as np
import glob
import os

def concatenate_images(image_paths, vertical=True):
    imageArrays = [np.array(Image.open(path)) for path in image_paths]
    axis = 0 if vertical else 1
    resultImage = Image.fromarray(np.concatenate(imageArrays, axis=axis))

    return resultImage

def save_concatenated_images(image_paths, batch_size=4, vertical=True, save_path="image_{}.jpg"):
    for i in range(0, len(image_paths), batch_size):
        batch_paths = image_paths[i :i+batch_size]
        result_image = concatenate_images(batch_paths, vertical)
        result_image.save(save_path.format(i // batch_size + 1))

imagePaths = list(glob.glob(os.path.join("dataset", "*")))
save_concatenated_images(imagePaths, batch_size=4, vertical=True)
