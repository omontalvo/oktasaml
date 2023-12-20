import re
from lxml import etree
from icecream import ic
from signxml import XMLSigner, XMLVerifier

with open('output.xml', 'r') as file :
    data_to_sign = file.read()
    ic(data_to_sign)
with open("testcert.crt", "r") as cert,\
        open("privatekey.key", "r") as key:
    certificate = cert.read()
    private_key = key.read()

p = re.search('<saml:Subject>', data_to_sign).start()
tmp_message = data_to_sign[:p]
tmp_message = tmp_message +\
              '<ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#" Id="placeholder"></ds:Signature>'
data_to_sign = tmp_message + data_to_sign[p:]
print(data_to_sign)

saml_root = etree.fromstring(data_to_sign)
signed_saml_root = XMLSigner(c14n_algorithm="http://www.w3.org/2001/10/xml-exc-c14n#")\
    .sign(saml_root, key=private_key, cert=certificate)
verified_data = XMLVerifier().verify(signed_saml_root, x509_cert=certificate).signed_xml
signed_saml_root_str = etree.tostring(signed_saml_root, encoding='unicode')
print(signed_saml_root_str)
