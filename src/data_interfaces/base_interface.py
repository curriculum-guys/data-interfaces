import numpy as np
import pandas as pd
from data_interfaces.utils import get_root_dir, create_dir, remove_file, verify_file, create_dirs

class BaseInterface:
    def __init__(self,
        env,
        seed,
        columns,
        interface_dir,
        root=None,
        stage_length=1,
        upload_reference=None
    ):
        self._root = root
        self.columns = columns
        self.seed = seed
        self.env = env
        self.data_dir = f'{self.root}/data/'
        self.env_dir = self.data_dir + self.env
        create_dir(self.env_dir)
        self.interface_name = interface_dir.replace('/', '').replace('_', '')
        self.interface_dir = self.env_dir + interface_dir
        create_dirs(self.env_dir, interface_dir)
        self.stage_dir = self.interface_dir + '/stg/'
        create_dir(self.stage_dir)
        self.stages = []
        self.stage_length = stage_length

        self.upload_reference = upload_reference

    @property
    def root(self):
        return self._root if self._root else get_root_dir()

    @property
    def _empty_matrix(self):
        return np.zeros((self.n_stages * self.stage_length, self.n_columns))

    @property
    def n_stages(self):
        return len(self.stages)

    @property
    def n_columns(self):
        return len(self.columns)

    def _stg_format(self, stage):
        return f'{self.stage_dir}/s{self.seed}_stg{stage}.npy'

    def _stg_col(self):
        stg_col = []
        for stg in self.stages:
            stg_col += [stg] * self.stage_length
        return stg_col

    def _get_stg(self, stg):
        stg_file = self._stg_format(stg)
        if verify_file(stg_file):
            data = np.load(stg_file, allow_pickle=True)
            return data
        return []

    def _purge_stg(self):
        try:
            for stg in self.stages:
                stg_file = self._stg_format(stg)
                remove_file(stg_file)
        except Exception as e:
            print('Error Purging staging files')

    def save_stg(self, data, stage):
        stg_file = self._stg_format(stage)
        data = data if np.array(data).ndim > 1 else [data]
        np.save(stg_file, np.asarray(data))
        self.stages.append(stage)

    def persistence_method(self, data):
        data_file = f'{self.interface_dir}/s{self.seed}_run.csv'
        df = pd.DataFrame(data, columns=self.columns)
        df['gen'] = self._stg_col()
        df.to_csv(data_file, index=False)

    def save(self):
        save_data = self._empty_matrix
        row_index = 0
        for stg in self.stages:
            data = self._get_stg(stg)
            for row in data:
                save_data[row_index] = row
                row_index += 1
        self.persistence_method(save_data)
        self._purge_stg()
