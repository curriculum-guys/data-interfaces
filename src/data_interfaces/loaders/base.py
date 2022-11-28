import pandas as pd
from data_interfaces.utils import get_root_dir

class BaseLoader:
    def __init__(self, seed, experiment, interface=None, trials=10) -> None:
        data_dir = f'data/{interface}' if interface else 'data'
        self.data_dir = f'{self.__root_dir}/{data_dir}/{experiment}'
        self.seed = seed
        self.experiment = experiment
        self.trials = trials

    @property
    def __root_dir(self):
        return get_root_dir()

    @property
    def max_gen(self):
        return max(self.data.index)

    def get_data(self, interface, date, **kwargs):
        data_path = f'{self.data_dir}/{interface}/s{self.seed}_{interface}_d{date}.csv'
        return pd.read_csv(data_path, index_col='gen', **kwargs)
