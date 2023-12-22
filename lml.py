from lxml import etree
from icecream import ic

import xmlsec

template = etree.parse('outputmodded.xml').getroot()
ic(template)

signature_node = xmlsec.tree.find_node(template, xmlsec.constants.NodeSignature)
ic(signature_node)
ctx = xmlsec.SignatureContext()
key = xmlsec.Key.from_file('privatekey.key', xmlsec.constants.KeyDataFormatPem)
ctx.key = key
ctx.sign(signature_node)
print(etree.tostring(template))
