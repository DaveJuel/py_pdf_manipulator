from PyPDF2 import PdfReader, PdfWriter


def generate_source_files(sample_pdf, destination_pdf, start_page, end_page):
    source_pdf = PdfReader(sample_pdf)
    destination_pdf = PdfWriter(destination_pdf)
    destination_pages = []

    # Extract the desired pages from the source PDF
    for page_number in range(start_page, end_page):
        source_page = source_pdf.pages[page_number]
        destination_pages.append(source_page)

    # Add the extracted pages to the end of the destination PDF
    for page in destination_pages:
        destination_pdf.add_page(page)

    with open(destination_pdf.fileobj, 'wb') as output_file:
        destination_pdf.write(output_file)


def copy_pages_at_start(source_file, destination_file, page_to_copy):
    source_pdf = PdfReader(source_file)
    destination_pdf = PdfReader(destination_file)
    source_page = source_pdf.getPage(page_to_copy)

    # Shift existing pages in the destination PDF to make room for the new page
    for i in range(destination_pdf.getNumPages()):
        destination_pdf.insertPage(destination_pdf.getPage(i), i)

    # Add the source page at the beginning of the destination PDF
    destination_pdf.insertPage(source_page, 0)

    with open('output_file.pdf', 'wb') as output_file:
        destination_pdf.write(output_file)


def copy_pages_at_end(source_file, destination_file, pages_to_copy):
    # TODO: Add implimentation
    return 0


def copy_pages_in_middle(source_file, destination_file, pages_to_copy):
    # TODO: Add implimentation
    return 0


def run_app():
    # generate source file 1 with 50 pgs
    generate_source_files('gulliverstravels00swif.pdf',
                          'source_files/source_1.pdf', 14, 64)
    # generate source file 2 with 40 pgs
    generate_source_files('gulliverstravels00swif.pdf',
                          'source_files/source_2.pdf', 14, 54)


run_app()
