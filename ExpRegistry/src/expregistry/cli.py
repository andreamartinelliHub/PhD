import shutil
from pathlib import Path

def create_new_dataset(dataset_name: str):
    template_dir = Path(__file__).parent / "registry" / "templates" / "dataset_template"
    target_dir = Path(__file__).parent / "datasets" / dataset_name
    
    ### update names

    if target_dir.exists():
        print(f"Error: Dataset {dataset_name} already exists.")
        return
        
    shutil.copytree(template_dir, target_dir)
    # Automatically generate the raw files directory
    (target_dir / "files").mkdir(exist_ok=True)
    print(f"Successfully created self-contained dataset block at {target_dir}")