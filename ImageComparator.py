import cv2
import numpy as np
from skimage.measure import compare_ssim as ssim


class ImageComparator:
    def __init__(self, path1, path2):
        self.path1 = path1
        self.path2 = path2
        self.img1 = 0
        self.img2 = 0

    def load_images(self):
        self.img1 = cv2.imread(self.path1)
        self.img2 = cv2.imread(self.path2)

    def to_grayscale(self):
        self.img1 = cv2.cvtColor(self.img1, cv2.COLOR_BGR2GRAY)
        self.img2 = cv2.cvtColor(self.img2, cv2.COLOR_BGR2GRAY)

    def mse(self):
        err = np.sum((self.img1.astype("float") - self.img2.astype("float")) ** 2)
        err /= float(self.img1.shape[0] * self.img2.shape[1])
        return err

    def compare_images(self):
        msecomp = self.mse()
        ssimcomp = ssim(self.img1, self.img2)
        return msecomp, ssimcomp
