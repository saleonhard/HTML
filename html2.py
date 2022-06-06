import os
import pdfkit

#WKHTMLTOPDF_PATH = '/usr/local/bin/wkhtmltopdf'
WKHTMLTOPDF_PATH = '/Program Files/wkhtmltopdf/bin'
def generate_pdf(html, static_path,  _path):
    config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)
    _status = pdfkit.from_string(
        html,
        os.path.join(static_path, _path),
        configuration=config,
        options={
            'page-size': 'A4',
            'margin-top': '0',
            'margin-right': '0',
            'margin-left': '0',
            'margin-bottom': '0',
            'zoom': '1.2',
            'encoding': "UTF-8",
        })
    return _path if _status else ''


html = "<h1>Hello World !!!</h1>"
static_path = "/static/"
file_path = "pdfs/out.pdf"
generate_pdf(html, static_path, file_path)