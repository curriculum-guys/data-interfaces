import numpy as np
import pandas as pd
from datetime import datetime
from data_interfaces.base_interface import BaseInterface

class RunStats(BaseInterface):
    def __init__(self, env, seed, features, **kwargs):
        features = features if features else [
            'msteps',
            'bestfit',
            'bestgfit',
            'bestsam',
            'avgfit',
            'paramsize'
        ]
        super().__init__(env, seed, features, '/runstats', **kwargs)
        self.metrics = []

    def __metric_format(self, metric):
        return f'{self.interface_dir}/s{self.seed}_{metric}.npy'

    @property
    def __now(self):
        now = datetime.now()
        date_time = now.strftime("%Y%m%d")
        return date_time

    @property
    def __metrics_file(self):
        return f'{self.interface_dir}/s{self.seed}_metrics.csv'

    @property
    def __test_file(self):
        return f'{self.interface_dir}/s{self.seed}_test.csv'

    def save_test(self, score, steps):
        df = pd.DataFrame([{'score': score, 'steps': steps}])
        df.to_csv(self.__test_file)
        if self.upload_reference:
            self.upload_test()

    def save_metric(self, data, metric):
        metric_file = self.__metric_format(metric)
        data = np.asarray(data)
        np.save(metric_file, data)
        if metric not in self.metrics:
            self.metrics.append(metric)

    def upload_test(self):
        file_path = self.__test_file
        file_name = f"s{self.seed}_test_d{self.__now}.npy"
        try:
            print(f"[{self.interface_name}-test] Beginning the process of data uploading.")
            self.drive_manager.upload_file(file_path, file_name, self.upload_reference)
            print(f"[{self.interface_name}-test] Data Uploaded.")
        except Exception:
            print(f"[{self.interface_name}-test] Something went wrong when trying to upload data.")

    def upload_metric(self, metric):
        metric_file = self.__metric_format(metric)
        metric_name = f"s{self.seed}_{metric}_d{self.__now}.npy"
        try:
            print(f"[{self.interface_name}-{metric}] Beginning the process of data uploading.")
            self.drive_manager.upload_file(metric_file, metric_name, self.upload_reference)
            print(f"[{self.interface_name}-{metric}] Data Uploaded.")
        except Exception:
            print(f"[{self.interface_name}-{metric}] Something went wrong when trying to upload data.")

    def save(self):
        super().save()
        df = pd.DataFrame()
        try:
            for metric in self.metrics:
                metric_file = self.__metric_format(metric)
                m_df = np.load(metric_file)
                df[metric] = m_df
                if self.upload_reference:
                    self.upload_metric(metric)
        except:
            print(f"Something went wrong when trying to save individual metrics")

        if not df.empty:
            df.to_csv(self.__metrics_file)
