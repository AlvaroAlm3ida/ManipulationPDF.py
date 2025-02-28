import fitz

def merge_pdfs(pdf_list,output_pdf):
    merged_doc = fitz.open()    #criando um novo documento vazio
    for pdf in pdf_list:
        with fitz.open(pdf) as doc:     
            merged_doc.insert_pdf(doc)
    merged_doc.save(output_pdf)     # Salvando o PDF mesclado

pdf_list = ["antigo_resume.pdf","curriculo-2024.pdf"]   # Digite aqui o PDF que quer que seja mesclado
output_pdf = "curriculo_master.pdf"
merge_pdfs(pdf_list,output_pdf)