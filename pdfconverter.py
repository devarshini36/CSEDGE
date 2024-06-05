import PyPDF2
from PIL import Image


def convert_to_text(pdf_file):
  """
  Converts a PDF file to plain text format.

  Args:
      pdf_file: Path to the PDF file.

  Returns:
      Extracted text content from the PDF file.
  """
  with open(pdf_file, 'rb') as pdf_reader:
    pdf_reader = PyPDF2.PdfReader(pdf_reader)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
      page = pdf_reader.pages[page_num]
      text += page.extract_text()
  return text


def convert_to_image(pdf_file, output_filename="output.jpg"):
  """
  Converts the first page of a PDF to an image file.

  Args:
      pdf_file: Path to the PDF file.
      output_filename: Optional filename for the output image (default: output.jpg).
  """
  with open(pdf_file, 'rb') as pdf_reader:
    pdf_reader = PyPDF2.PdfReader(pdf_reader)
    page = pdf_reader.pages[0]
    image = page.extract_image()

    if image:
      with open(output_filename, 'wb') as image_file:
        image_file.write(image)
    else:
      print(f"No image found on the first page of {pdf_file}")


def main():
  """
  Prompts user for input and calls conversion functions.
  """
  pdf_file = r"academic_certificate.pdf"
  format_choice = input("Convert to (t)ext or (i)mage? ")

  if format_choice.lower() == 't':
    text_content = convert_to_text(pdf_file)
    print(text_content)
  elif format_choice.lower() == 'i':
    output_filename = input("Enter desired output filename (default: output.jpg): ") or "output.jpg"
    convert_to_image(pdf_file, output_filename)
  else:
    print("Invalid choice. Please enter 't' for text or 'i' for image.")


if __name__ == "__main__":
  main()
