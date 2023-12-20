from lxml import etree

import xmlsec

template = etree.parse('output.xml').getroot()

signature_node = xmlsec.tree.find_node(template, xmlsec.constants.NodeSignature)
ctx = xmlsec.SignatureContext()
key = xmlsec.Key.from_file('privatekey.key', xmlsec.constants.KeyDataFormatPem)
ctx.key = key
ctx.sign(signature_node)
print(etree.tostring(template))
