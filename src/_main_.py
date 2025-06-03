from src.config_loader import load_config

def main():
    # ... argumentos
    config = load_config()
    output_dir = config.get("output_directory", "./output")
    
    if not args.info:
        print(f"Arquivo será salvo em: {output_dir}")
        # lógica de conversão usará output_dir

