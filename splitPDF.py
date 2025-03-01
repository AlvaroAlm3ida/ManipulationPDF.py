import fitz
import os

def split_pdf(pdf_path, output_dir):
    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        new_doc = fitz.open()
        new_doc.insert_pdf(doc,from_page=page_num, to_page=page_num)
        output_filename = os.path.join(output_dir, f"page_{page_num+1}.pdf")
        new_doc.save(output_filename)

pdf_path = "curriculo_master.pdf"
output_dir = "Split_pages"
os.makedirs(output_dir,exist_ok=True)
split_pdf(pdf_path,output_dir)