from expregistry.registry.dataset_registry import DATASET_REGISTRY

@DATASET_REGISTRY.register("example_ds")
class ExampleDataset:
    def __init__(self, config):
        self.config = config
    # Your dataset parsing logic here