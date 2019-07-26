# pylint: disable=W0611
from PIL import Image

def create_pixels(image):
    sequence_obj = image.getdata()
    list_sequence_obj = list(sequence_obj)
    generated_pixels = []

    for i in list_sequence_obj:
        generated_pixels.append(i)

    return generated_pixels
