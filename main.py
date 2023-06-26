from PyPDF2 import PdfReader, PdfWriter


def extract_desired_page(source_pdf, start_page, end_page):
    pages = []
    for page_number in range(start_page, end_page):
        source_page = source_pdf.pages[page_number]
        pages.append(source_page)
    return pages


def copy_pages(source_pdf, destination_pdf, start_page, end_page):
    destination_pages = extract_desired_page(
        PdfReader(source_pdf), start_page, end_page)
    destination_pdf = PdfWriter(destination_pdf)
    for page in destination_pages:
        destination_pdf.add_page(page)
    with open(destination_pdf.fileobj, 'wb') as output_file:
        destination_pdf.write(output_file)


def merge_files(source_file, target_file, source_file_range, target_file_range, merge_at_page):
    source_file_pages = extract_desired_page(
        PdfReader(source_file), source_file_range[0]-1, source_file_range[1])
    target_file_pages = extract_desired_page(
        PdfReader(target_file), target_file_range[0]-1, target_file_range[1])
    target_file_writer = PdfWriter(target_file)
    for index, target_page in enumerate(target_file_pages):
        actual_page_num = index+1
        target_file_writer.add_page(target_page)
        if actual_page_num == merge_at_page:
            for source_page in source_file_pages:
                target_file_writer.add_page(source_page)
    with open(target_file_writer.fileobj, 'wb') as output_file:
        target_file_writer.write(output_file)


def initialise_files():
    # generate tg with 10 pgs
    copy_pages('gulliverstravels00swif.pdf',
               'destination_files/tg.pdf', 14, 24)

    # generate s1 with 50 pgs
    copy_pages('gulliverstravels00swif.pdf',
               'source_files/s1.pdf', 24, 74)

    # generate s2 with 40 pgs
    copy_pages('gulliverstravels00swif.pdf',
               'source_files/s2.pdf', 74, 114)


def copy_pages_in_middle(source_file, destination_file, pages_to_copy):
    # TODO: Add implimentation
    return 0


def run_app():
    initialise_files()
    merge_files('source_files/s2.pdf',
                'destination_files/tg.pdf', [3, 8], [1, 10], 5)


run_app()
