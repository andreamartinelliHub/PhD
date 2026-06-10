import TypeError

class DatasetRegistry:
    def __init__(self):
        self._registry = {}

    def register(self, name: str):
        def decorator(cls):
            if name in self._registry:
                raise ValueError(f"Dataset '{name}' is already registered.")
            self._registry[name] = cls
            return cls
        return decorator

    def get(self, name: str, *args, **kwargs):
        if name not in self._registry:
            raise KeyError(f"Dataset '{name}' not found in registry.")
        return self._registry[name](*args, **kwargs)

# Singleton instance to use across the library

DATASET_REGISTRY = DatasetRegistry()