from data_interfaces.base_interface import BaseInterface

class InitialConditions(BaseInterface):
    def __init__(self, env, seed, features, **kwargs):
        super().__init__(env, seed, features, '/initialconditions', **kwargs)
