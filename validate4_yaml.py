import yaml
import sys

def validate_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            yaml.safe_load(file)
        print(f"YAML validation successful for {file_path}")
        return 0
    except Exception as e:
        print(f"YAML validation failed for {file_path}: {str(e)}")
        return 1
    

validate_yaml("${{ github.workspace }}\yaml_file.yaml")