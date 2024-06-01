import os
import subprocess

def convert_pdf_to_text(pdf_path, text_path):
    try:
        subprocess.run(['pdftotext', '-layout', pdf_path, text_path], check=True)
        print(f"Converted {pdf_path} to {text_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error converting {pdf_path}: {e}")

def process_folders(main_folder):
    for subdir, _, files in os.walk(main_folder):
        for file in files:
            if file.endswith('.pdf'):
                pdf_path = os.path.join(subdir, file)
                text_file_name = file.replace('.pdf', '.txt')
                text_path = os.path.join(subdir, text_file_name)
                convert_pdf_to_text(pdf_path, text_path)

main_folder = './'
process_folders(main_folder)
