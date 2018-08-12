from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import re
import yaml

class Address:
    def __init__(self, address, city):
        self.address = address
        self.city = city

    def show(self):

        print('Address:' + self.address +  ' City: ' +  self.city)


class Tenant:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def show(self):

        print('Tenant Name:' + self.name +  ' Tenant Phone: ' +  self.phone + 'Tenant Email' + self.email)




def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue().splitlines()

    # fp.close()
    # device.close()
    # retstr.close()
    return text


result = convert_pdf_to_txt('/Users/lisyruiz/Documents/KeepePDFparser/appfolio_WO/demo.pdf')

address = Address(result[35], result[36])

tenant_info = Tenant(result[44], result[46], result[48])


address.show()
tenant_info.show()

with open('data.yml', 'w') as outfile:
    yaml.dump(tenant_info, outfile)
    yaml.dump(address, outfile)

# print(result)

 