import pandas as pd
from data_interfaces.utils import get_root_dir

class BaseLoader:
    def __init__(self, seed, experiment, trials=10) -> None:
        self.data_dir = f'{self.__root_dir}/data/{experiment}'
        self.seed = seed
        self.experiment = experiment
        self.trials = trials

    @property
    def __root_dir(self):
        return get_root_dir()

    @property
    def max_gen(self):
        return max(self.data.index)

    def get_data(self, subpath, **kwargs):
        data_path = f'{self.data_dir}/{subpath}/s{self.seed}_run.csv'
        return pd.read_csv(data_path, index_col='gen', **kwargs)
