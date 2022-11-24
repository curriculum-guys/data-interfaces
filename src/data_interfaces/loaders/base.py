import pandas as pd
from data_interfaces.utils import get_root_dir

class BaseLoader:
    def __init__(self, seed, experiment, trials=10) -> None:
        self.data_dir = f'{self.__root_dir}/data/{experiment}'
        self.seed = seed
        self.experiment = experiment
        self.trials = trials
        self.set_data_format()

    @property
    def __root_dir(self):
        return get_root_dir()

    @property
    def max_gen(self):
        return max(self.data.index)

    def set_data_format(self, suffix=None, interface=None, date=None):
        base_name = f's{self.seed}'
        if interface:
            base_name += f'_{interface}'
        if date:
            base_name += f'_d{date}'    
        if suffix:
            base_name += suffix
        self.data_format = base_name + '.csv'

    def get_data(self, subpath, **kwargs):
        data_path = f'{self.data_dir}/{subpath}/{self.data_format}'
        return pd.read_csv(data_path, index_col='gen', **kwargs)
