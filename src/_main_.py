import argparse
from src.utils import get_docx_metadata

def main():
    parser = argparse.ArgumentParser(description="Word to PDF Converter")
    parser.add_argument("file", help="Path to the DOCX file")
    parser.add_argument("--info", action="store_true", help="Show DOCX metadata info")
    args = parser.parse_args()

    if args.info:
        metadata = get_docx_metadata(args.file)
        for key, value in metadata.items():
            print(f"{key.capitalize()}: {value}")
    else:
        # conversão para PDF aqui
        pass

if __name__ == "__main__":
    main()
