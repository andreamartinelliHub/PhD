# PhD Codebase - Andrea Martinelli

This repository serves as the central workspace and monorepo for my PhD research, focused on keeping machine learning experiments clean, fully reproducible, sorted, and fast.

## 🚀 Repository Architecture

This project is managed as a unified **`uv` Workspace**. All dependencies are locked globally at the root, while logic is broken down into modular workspace packages.

```text
phd/
├── .venv/                  # Shared virtual environment
├── pyproject.toml          # Root workspace configuration
├── uv.lock                 # Unified cryptographic lockfile
├── README.md               # You are here
└── ExpRegistry/            # Core Experiment Registry Library
    ├── pyproject.toml
    └── src/
        └── expregistry/    # Main package logic
```

## Install
git clone git@github.com:andreamartinelliHub/your_repo.git
cd phd

# Synchronize the entire workspace environment
uv sync

# Activate the environment
source .venv/bin/activate
