import fitz
import os  # Importa o módulo que fornece interagir com o sistema operacional

def split_pdf(pdf_path, output_dir):                                                    #pdf_path: O caminho do arquivo PDF que será dividido.
    doc = fitz.open(pdf_path)                                                           #output_dir: O diretório onde as páginas divididas do PDF serão salvas.
    for page_num in range(len(doc)):
        new_doc = fitz.open()
        new_doc.insert_pdf(doc,from_page=page_num, to_page=page_num)
        output_filename = os.path.join(output_dir, f"page_{page_num+1}.pdf")
        new_doc.save(output_filename)

pdf_path = "curriculo_master.pdf"
output_dir = "Split_pages"
os.makedirs(output_dir,exist_ok=True)      # Cria o Diretório onde as páginas dividias serão salvas caso ele não exista
split_pdf(pdf_path,output_dir)