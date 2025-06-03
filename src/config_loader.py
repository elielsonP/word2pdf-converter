import yaml

def load_config(path="config.yaml"):
    try:
        with open(path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        return {}  # fallback para configurações padrão
