from data_interfaces.loaders.base import BaseLoader

class ExploratoryAnalytics:
    def __init__(self,
        seeds,
        target_date,
        experiment='xdpole',
        interfaces=['base_conditions', 'initial_conditions', 'run_stats'],
    ):
        self.seeds = seeds
        self.target_date = target_date
        self.experiment = experiment
        self.interfaces = interfaces
        self._data = {}
        self.init_loaders()
        self.load_interfaces()

    def init_loaders(self):
        self.loaders = {}

        for seed in self.seeds:
            self.loaders[seed] = BaseLoader(
                seed=seed,
                experiment=self.experiment
            )
    
    def get_loader(self, seed) -> BaseLoader:
        return self.loaders.get(seed)

    def load_interfaces(self):
        for interface in self.interfaces:
            for seed in self.seeds:
                if seed not in self._data:
                    self._data[seed] = {}
                loader = self.get_loader(seed)
                inteface = interface.replace('_', '')
                self._data[seed][interface] = loader.get_data(inteface, self.target_date)
    
    def _get_interface_data(self, interface):
        interface_data = {}
        for seed in self.seeds:
            interface_data[seed] = self._get_seed_interface_data(seed, interface)
        return interface_data

    def _get_seed_interface_data(self, seed, interface):
        seed_data = self._data.get(seed)
        return seed_data.get(interface)

    def _get_seed_data(self, seed):
        return self._data.get(seed)

    def get_data(self, seed=None, interface=None):
        if seed and interface:
            return self._get_seed_interface_data(seed, interface)            
        elif seed and not interface:
            return self._get_seed_data(seed)
        elif interface and not seed:
            return self._get_interface_data(interface)
        else:
            return self._data
