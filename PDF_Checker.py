import PyPDF2
import os

def extract_text_from_pdf(pdf_path):
    """Extracts all text from a PDF and returns it as a dictionary."""
    if not os.path.exists(pdf_path):
        print(f"Error: File '{pdf_path}' not found. Make sure it's in the correct folder.")
        return {}

    print(f"Found file: {pdf_path}")  # Debugging line

    extracted_data = {}
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page_num, page in enumerate(reader.pages, start=1):
            text = page.extract_text()
            if text:
                extracted_data[f"Page_{page_num}"] = text.strip()
            else:
                extracted_data[f"Page_{page_num}"] = "[No Text Found]"

    return extracted_data

def compare_pdfs(reference_pdf, test_pdf):
    """Compares text content of two PDFs page by page."""
    ref_data = extract_text_from_pdf(reference_pdf)
    test_data = extract_text_from_pdf(test_pdf)

    if not ref_data or not test_data:
        print("Error: One or both files are empty or missing.")
        return

    differences = {}
    for page, ref_text in ref_data.items():
        test_text = test_data.get(page, "[Page Missing]")
        if test_text != ref_text:
            differences[page] = {
                "expected": ref_text,
                "found": test_text
            }

    if differences:
        print("Differences Found:")
        for page, diff in differences.items():
            print(f"Page: {page}")
            print(f"Expected: {diff['expected']}")
            print(f"Found: {diff['found']}")
    else:
        print("The test PDF matches the reference PDF")

if __name__ == "__main__":
    reference_pdf = "test_task.pdf"  # Reference file (provided by HR)
    test_pdf = "test_file.pdf"  # Replace with your test file

    print("Checking files in:", os.getcwd())  # Debugging line
    compare_pdfs(reference_pdf, test_pdf)
