from data_interfaces.base_interface import BaseInterface

class CurriculumConditions(BaseInterface):
    def __init__(self, env, seed, features, trials=10, **kwargs):
        super().__init__(env, seed, features, '/curriculumconditions', **kwargs)
        self.trials = trials
