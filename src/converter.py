# src/converter.py

import os
from pathlib import Path
from docx2pdf import convert

def convert_docx_to_pdf(input_path_str: str, output_path_str: str = None) -> str | None:
    """
    Converte um arquivo .docx para .pdf.

    Args:
        input_path_str: Caminho para o arquivo .docx de entrada.
        output_path_str: Caminho para o arquivo .pdf de saída (opcional).
                         Se não fornecido, o .pdf será salvo na mesma pasta
                         do arquivo de entrada com o mesmo nome.

    Returns:
        O caminho para o arquivo .pdf gerado em caso de sucesso, None caso contrário.
    """
    input_path = Path(input_path_str)
    
    # Tratamento de erro: arquivo de entrada não existe
    if not input_path.exists():
        print(f"Erro: Arquivo de entrada não encontrado em '{input_path_str}'")
        return None
    
    # Tratamento de erro: arquivo de entrada não é .docx
    if input_path.suffix.lower() != ".docx":
        print(f"Erro: Arquivo de entrada '{input_path_str}' não é um arquivo .docx válido.")
        return None

    if output_path_str:
        output_path = Path(output_path_str)
        # Garante que o diretório de saída exista
        output_path.parent.mkdir(parents=True, exist_ok=True)
    else:
        # Define o caminho de saída na mesma pasta do input com extensão .pdf
        output_path = input_path.with_suffix(".pdf")

    try:
        print(f"Convertendo '{input_path}' para '{output_path}'...")
        convert(str(input_path), str(output_path))
        print(f"Arquivo convertido com sucesso: '{output_path}'")
        return str(output_path)
    except Exception as e:
        print(f"Erro durante a conversão do arquivo '{input_path_str}': {e}")
        return None

if __name__ == '__main__':
    # Exemplo de uso (para teste direto do módulo)
    # Crie um arquivo dummy.docx na pasta 'test_files' para este exemplo funcionar
    test_input_dir = Path("test_files")
    test_input_dir.mkdir(exist_ok=True)
    test_input_file = test_input_dir / "exemplo.docx"
    
    # Para testar, você precisaria criar um arquivo .docx manualmente
    # ou usar python-docx para criar um programaticamente
    if not test_input_file.exists():
        print(f"Arquivo de teste '{test_input_file}' não encontrado. Crie-o para testar.")
    else:
        print("\n--- Testando conversão (saída no mesmo diretório) ---")
        convert_docx_to_pdf(str(test_input_file))

        print("\n--- Testando conversão (saída especificada) ---")
        test_output_file = test_input_dir / "exemplo_convertido.pdf"
        convert_docx_to_pdf(str(test_input_file), str(test_output_file))

        print("\n--- Testando erro: arquivo não existe ---")
        convert_docx_to_pdf("arquivo_inexistente.docx")

        print("\n--- Testando erro: arquivo não é .docx ---")
        non_docx_file = test_input_dir / "nao_e_docx.txt"
        with open(non_docx_file, "w") as f: # cria um arquivo .txt para teste
            f.write("Este não é um docx.")
        convert_docx_to_pdf(str(non_docx_file))
        # non_docx_file.unlink() # Limpa o arquivo de teste
