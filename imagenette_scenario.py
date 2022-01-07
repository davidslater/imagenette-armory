"""
Imagenette scenario using ImageNet classifiers

This maps the 10 labels form Imagenette into the ImageNet 1000 label space
"""

import numpy as np

from armory.scenarios import image_classification

IMAGENETTE_MAP = np.array([0, 217, 482, 491, 497, 566, 569, 571, 574, 701])


class ImagenetteClassificationTask(image_classification.ImageClassificationTask):
    def next(self):
        super().next()
        self.y = IMAGENETTE_MAP[self.y] 
