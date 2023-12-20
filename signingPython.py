import xml.etree.ElementTree as ET
import xmlsec
import xmlsec.exceptions


def sign_saml_assertion(xml_file_path, private_key_path, certificate_path):
    # Load the SAML XML file
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Load the private key and certificate
    private_key = xmlsec.Key.from_file(private_key_path, format=xmlsec.constants.KeyDataFormatPem,
                                       data_type=xmlsec.constants.KeyDataTypeRsaPrivate)
    certificate = xmlsec.Key.from_file(certificate_path, format=xmlsec.constants.KeyDataFormatPem,
                                       data_type=xmlsec.constants.KeyDataTypeCert)

    # Create a digital signature template
    signature_node = xmlsec.tree.find_node(root, xmlsec.constants.NodeSignature)
    if signature_node is None:
        signature_template = xmlsec.template.create_signed_info(
            xmlsec.constants.TransformExclC14N,
            xmlsec.constants.TransformRsaSha256,
            ns_uri="http://www.w3.org/2001/10/xml-exc-c14n#"
        )
        signature_node = xmlsec.template.create_signature_template(root, xmlsec.constants.TransformSha256,
                                                                   ns_uri="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256")
        xmlsec.tree.add_ids(signature_template, root,
                            ["ID"])  # Replace "ID" with the actual ID attribute in your SAML assertion
        xmlsec.tree.add_signature(signature_node, signature_template)

    # Create a digital signature context
    ctx = xmlsec.SignatureContext()

    # Set the private key and certificate
    ctx.key = private_key
    ctx.key.load_cert(certificate)

    # Sign the XML
    try:
        ctx.sign(signature_node)
    except XMLSigException as e:
        print(f"Error signing XML: {e}")
        return

    # Save the signed XML to a new file
    signed_xml_file_path = xml_file_path.replace(".xml", "_signed.xml")
    tree.write(signed_xml_file_path, encoding="utf-8", xml_declaration=True)

    print(f"Successfully signed and saved to {signed_xml_file_path}")


# Replace these paths with your actual paths
saml_xml_file_path = "output.xml"
private_key_path = "okta.cert"
certificate_path = "okta.cert"

sign_saml_assertion(saml_xml_file_path, private_key_path, certificate_path)
