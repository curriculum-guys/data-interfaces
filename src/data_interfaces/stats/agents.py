from data_interfaces.base_interface import BaseInterface

class AgentStats(BaseInterface):
    def __init__(self, env, seed, name, **kwargs):
        features = [
            'generation',
            'id',
            'parameters'
        ]
        super().__init__(env, seed, features, name, **kwargs)
