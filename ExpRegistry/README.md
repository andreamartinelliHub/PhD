

## 📂 Internal Directory Layout

```text
ExpRegistry/
├── pyproject.toml          # Library build metadata (Hatchling)
└── src/
    └── expregistry/
        ├── cli.py          # Unified execution and scaffolding entrypoint
        ├── engine.py       # Core training, validation, and testing loops
        ├── py.typed        # PEP 561 marker for IDE type-safety
        |
        ├── config/         # Hydra configuration layers (Base & User overrides)
        |   ├── user/       
        |   └── base_config.yaml    # Base configuration for experiments
        |
        ├── datasets/       # Self-contained dataset blocks
        |   ├── my_ds_1/       
        |   |   ├── my_ds.py/
        |   |   ├── my_ds_custom.yaml
        |   |   └── my_ds.yaml
        |   └── another_ds/
        |
        ├── models/         # Self-contained deep learning model architectures
        |   ├── my_model_1/       
        |   |   ├── my_model.py/
        |   |   ├── my_model_custom.yaml
        |   |   └── my_model.yaml
        |   └── another_model/
        |
        └── registry/       # Decorator-driven registries and scaffolding templates
            ├── dataset_registry.py
            ├── model_registtry.py
            └── templates/
```
