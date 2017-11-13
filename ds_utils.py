import pandas as pd


class D_util:
    def __init__(self,path):
        self.path = path


    # @classmethod
    def __read(self):
        self.data = pd.read_json(self.path,typ='frame')

    def get_data(self):
        self.__read()
        return self.data