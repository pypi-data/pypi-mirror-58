import torch
import numpy as np
import SimpleITK as sitk
from .interpolation import Interpolation


class RandomElasticDeformation:
    def __init__(
            self,
            num_controlpoints=4,
            std_deformation=15,
            probability=0.5,
            image_interpolation=Interpolation.LINEAR,
            seed=None,
            verbose=False,
            ):
        super().__init__(seed=seed, verbose=verbose)
        self.num_control_points = num_controlpoints
        self.std_deformation = std_deformation,
        self.probability = probability

    @staticmethod
    def get_params():
        return

    def apply_transform(self, sample):
        params = self.get_params()  # TODO
        sample['random_params'] = params  # TODO
        for key in 'image', 'label', 'sampler':
            if key == 'image':
                interpolation = self.image_interpolation
            else:
                interpolation = Interpolation.NEAREST
            if key not in sample:
                continue
            array = sample[key]
            array = self.apply_elastic_deformation(
                array,
                sample['affine'],
                params,  #### TODO
                interpolation,
            )
            sample[key] = array
        return sample
