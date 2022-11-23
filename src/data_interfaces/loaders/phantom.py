from data_interfaces.loaders.base import BaseLoader

class PhantomLoader(BaseLoader):
    def __init__(self, seed, trials, experiment, **kwargs) -> None:
        super().__init__(seed, experiment, trials, **kwargs)
        self.get_all()

    def get_all(self):
        self.data = self.get_data('runstats')
        self.initial_conditions_data = self.get_data('initialconditions')

    def read_conditions(self, gen):
        first_row = (gen-1) * self.generation_trials
        last_row = (gen * self.generation_trials)
        return self.initial_conditions_data.iloc[first_row:last_row]

    def read_evolution(self, gen):
        return list(self.evolution_data.iloc[gen-1])
