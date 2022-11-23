from data_interfaces.base_interface import BaseInterface

class InitialConditions(BaseInterface):
    def __init__(self, env, seed, features, trials=10, **kwargs):
        super().__init__(env, seed, features, '/initialconditions', **kwargs)
        self.trials = trials
