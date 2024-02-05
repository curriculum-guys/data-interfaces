import numpy as np
from data_interfaces.base_interface import BaseInterface

class AgentStats(BaseInterface):
    def __init__(self, env, seed, parameters, **kwargs):
        features = [
            "agent_id",
            *[f"p{i}" for i in range(parameters)]
        ]
        super().__init__(env, seed, features, '/agentstats', **kwargs)

    def persistence_method(self, data):
        data_file = f'{self.interface_dir}/s{self.seed}_run.npz'
        np.savez_compressed(data_file, a=data)
