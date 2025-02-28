# ManipulationPDF.py
Este script Python utiliza a biblioteca PyMuPDF (também conhecida como fitz) para mesclar múltiplos arquivos PDF em um único documento. Ele permite combinar documentos PDF de forma simples e eficiente.
Função merge_pdfs(pdf_list, output_pdf)
Esta função recebe dois parâmetros:

pdf_list: Uma lista contendo os caminhos dos arquivos PDF a serem mesclados.
output_pdf: O nome ou caminho do arquivo PDF de saída, onde o conteúdo dos PDFs de entrada será armazenado.
O processo de mesclagem é realizado da seguinte forma:

Criação de um novo documento PDF vazio:
A função começa criando um novo documento PDF vazio (merged_doc) usando fitz.open().
Iteração sobre os PDFs a serem mesclados:
Para cada PDF na lista pdf_list, o código abre o arquivo PDF usando fitz.open(pdf).
Inserção das páginas do PDF atual:
O conteúdo de cada arquivo PDF é inserido no documento de saída merged_doc através do método insert_pdf(doc). Esse método copia todas as páginas do PDF aberto para o documento de saída.
Salvamento do documento PDF final:
Após a inserção das páginas de todos os arquivos, o documento resultante é salvo no caminho especificado em output_pdf usando o método save().
Exemplo de Uso:
O script é configurado para mesclar os arquivos "clcoding.pdf" e "clcodingpdf.pdf".
O arquivo resultante será salvo como "clcodingmerged.pdf".
Objetivo:
Este código oferece uma maneira automatizada de combinar vários arquivos PDF em um único documento, o que pode ser útil em muitos cenários, como:

Consolidar relatórios.
Unir várias partes de um projeto.
Organizar documentos.
Pré-requisitos:
Para usar este código, você precisa ter a biblioteca PyMuPDF instalada. Caso não tenha, pode instalá-la com o seguinte comando:

pip install pymupdf
