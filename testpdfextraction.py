import pyPDF2
pdf_file = open('C:\\Users\\Desktop\\demo.pdf', 'rt')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(0)
page_content = page.extractText()
page_content
