from data_interfaces.base_interface import BaseInterface

class SpecialistStats(BaseInterface):
    def __init__(self, env, seed, name, **kwargs):
        features = [
            'generation',
            'specialist_score',
            'specialist_cycle',
            'specialist_fit_prediction_proportion',
            'specialist_score_prediction_proportion',
            'specialist_tn',
            'specialist_fp',
            'specialist_fn',
            'specialist_tp',
        ]
        super().__init__(env, seed, features, name, **kwargs)
