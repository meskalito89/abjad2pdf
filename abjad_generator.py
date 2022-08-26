import abjad
import uuid

def text2pdf(text: str):
    voice = abjad.Voice(text, name='Voice 1')
    staff = abjad.Staff([voice], name='staff1')
    # abjad.show(staff, output_directory=file_url, should_open=False, should_persist_log=False)
    output_url = f'pdfs/{uuid.uuid1()}.pdf'
    abjad.persist.as_pdf(staff, output_url)
    return output_url


