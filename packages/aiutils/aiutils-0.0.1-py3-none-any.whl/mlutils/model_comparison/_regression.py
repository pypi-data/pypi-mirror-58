import pandas as pd

class RegressiveModels:
    def __init__(self, dataset):
        if(not dataset):
            raise TypeError('dataset expected but not passed')
            return
        if(self.__check_dataset(dataset)):
            self._dataset = dataset
        else:
            raise TypeError('Dataset does not pass requirements. Kindly read in the help section of what dataset to pass. ')
            return

    def __check_dataset(self, dataset):
        return True

    def compare_models(self, models, test_size, cross_validation, metrics):
       """  """

       print("this function works")

       if(not models):
           models = []

       # cross_validation
