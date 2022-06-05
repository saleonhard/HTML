from xhtml2pdf import pisa 
import jinja2
templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "invoice.html"
template = templateEnv.get_template(TEMPLATE_FILE)

# This data can come from database query
body = {
    "data":{
        "order_id": 123,
        "order_creation_date": "2020-01-01 14:14:52",
        "company_name": "Test Company",
        "city": "Mumbai",
        "state": "MH",
    }
}

# This renders template with dynamic data 
sourceHtml = template.render(json_data=body["data"]) 
outputFilename = "invoice.pdf"

# Utility function
def convertHtmlToPdf(sourceHtml, outputFilename):
    # open output file for writing (truncated binary)
    resultFile = open(outputFilename, "w+b")

    # convert HTML to PDF
    pisaStatus = pisa.CreatePDF(
            src=sourceHtml,            # the HTML to convert
            dest=resultFile)           # file handle to receive result

    # close output file
    resultFile.close()

    # return True on success and False on errors
    print(pisaStatus.err, type(pisaStatus.err))
    return pisaStatus.err

if __name__ == "__main__":
    pisa.showLogging()
    convertHtmlToPdf(sourceHtml, outputFilename)