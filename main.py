from PyPDF2 import PdfReader, PdfWriter


def extract_desired_page(source_pdf: PdfReader, start_page: int, end_page: int) -> list:
    """
    Extracts desired pages from source pdf into list

    Args:
        source_pdf (PdfReader): The PdfReader object.
        start_page (int): Number of the page to start from.
        end_page (int): Number of the page to end at.

    Returns:
        Pages[]: List of pages in the start_page and end_page range.
    """
    pages = []
    for page_number in range(start_page, end_page):
        source_page = source_pdf.pages[page_number]
        pages.append(source_page)
    return pages


def extract_all_pages(source_pdf: PdfReader) -> list:
    """
    Extracts all pages from source pdf into list

    Args:
        source_pdf (PdfReader): The PdfReader object.

    Returns:
        Pages[]: List of all pages.
    """
    pages = []
    for page in source_pdf.pages:
        pages.append(page)
    return pages


def write_file(file_writer: PdfWriter) -> None:
    """
    Saves changes on PDF file

    Args: 
        file_writer (PdfWriter): PdfWriter object

    Returns:
        None
    """
    with open(file_writer.fileobj, 'wb') as output_file:
        file_writer.write(output_file)


def copy_pages(source_pdf: str, destination_pdf: str, start_page: int, end_page: int) -> None:
    """
    Copies desired pages from source pdf to destination pdf

    Args:
        source_pdf (str): Source pdf local filename
        destination_pdf (string): Source pdf local filename
        start_page (int): Page to start from copying
        end_page (int): Page to end at copying
    Returns:
        None
    """
    destination_pages = extract_desired_page(
        PdfReader(source_pdf), start_page, end_page)
    destination_pdf = PdfWriter(destination_pdf)
    for page in destination_pages:
        destination_pdf.add_page(page)
    write_file(destination_pdf)


def remove_pages_from_source(source_file: str, page_range_to_remove: list[int, int]) -> None:
    """
    Removes desired pages from the source file
    Args:
        source_file (str):  Source pdf local filename
        page_range_to_remove list[int, int]: Array with 2 indexes, where index: 0 -> start page and 1 -> end page

    Returns:
        None
    """
    source_file_reader = PdfReader(source_file)
    source_pages = extract_all_pages(source_file_reader)
    new_source_pdf = PdfWriter(source_file)
    for index, source_page in enumerate(source_pages):
        if index not in range(page_range_to_remove[0]-1, page_range_to_remove[1]):
            new_source_pdf.add_page(source_page)
    write_file(new_source_pdf)


def merge_files(source_file: str, target_file: str, source_file_merge_range: list[int, int], merge_at_page: int, clean_up_source: bool) -> None:
    """
    Copies desired pages from source_file to the target_file
    Args:
        source_file (str): Source pdf local filename
        target_file (str): Target pdf local filename
        source_file_merge_range list[int, int]: Array with 2 indexes, where index: 0 -> start page and 1 -> end page
        merge_at_page (int): The number of the page after which copied pages will be added. 
        clean_up_source (bool): True for cut and false for copying the pages
    Returns:
        None
    """
    source_file_pages = extract_desired_page(
        PdfReader(source_file), source_file_merge_range[0]-1, source_file_merge_range[1])
    target_file_pages = extract_all_pages(
        PdfReader(target_file))
    target_file_writer = PdfWriter(target_file)
    for index, target_page in enumerate(target_file_pages):
        actual_page_num = index+1
        target_file_writer.add_page(target_page)
        if actual_page_num == merge_at_page:
            for source_page in source_file_pages:
                target_file_writer.add_page(source_page)
    write_file(target_file_writer)
    if clean_up_source:
        remove_pages_from_source(source_file, source_file_merge_range)


def initialise_files(sample_file):
    # generate tg with 10 pgs
    copy_pages(sample_file,
               'destination_files/tg.pdf', 14, 24)

    # generate s1 with 50 pgs
    copy_pages(sample_file,
               'source_files/s1.pdf', 24, 74)

    # generate s2 with 40 pgs
    copy_pages(sample_file,
               'source_files/s2.pdf', 74, 114)


def run_app():
    initialise_files('gulliverstravels00swif.pdf')
    merge_files('source_files/s1.pdf',
                'destination_files/tg.pdf', [2, 6], 5, True)
    merge_files('source_files/s2.pdf',
                'destination_files/tg.pdf', [3, 8], 8, False)


run_app()
