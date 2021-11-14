from PIL import Image
import numpy as np


def WhiteToTransparent(img):
    img = img.convert("RGBA")
    imgnp = np.array(img)

    white = np.sum(imgnp[:,:,:3], axis=2)
    white_mask = np.where(white == 255*3, 1, 0)

    alpha = np.where(white_mask, 0, imgnp[:,:,-1])

    imgnp[:,:,-1] = alpha

    img = Image.fromarray(np.uint8(imgnp))
    return img