import xml.etree.ElementTree as ET
from xml.dom import minidom
from datetime import datetime, timedelta, timezone

def create_saml_assertion():
    # Create the root element
    root = ET.Element("saml:Assertion", xmlns="urn:oasis:names:tc:SAML:2.0:assertion")
    root.set("ID", "123456")
    #root.set("IssueInstant", datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"))
    root.set("IssueInstant", datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))
    root.set("Version", "2.0")
    # print("ROOT COMPLETED")


    # Create and append sub-elements
    issuer = ET.SubElement(root, "saml:Issuer")
    issuer.text = "http://www.okta.com/exkdoyoe3zOskPHhO5d7"
    # print("ISSUER COMPLETED")

    subject = ET.SubElement(root, "saml:Subject")
    name_id = ET.SubElement(subject, "saml:NameID", Format="urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified")
    name_id.text = "orlando.montalvo@genesys.com"
    # print('SUBJECT COMPLETED')

    conditions = ET.SubElement(root, "saml:Conditions", NotBefore="2022-12-01T00:00:00Z", NotOnOrAfter="2024-01-01T00:00:00Z")
    audience_restriction = ET.SubElement(conditions, "saml:AudienceRestriction")
    audience = ET.SubElement(audience_restriction, "saml:Audience")
    audience.text = "https://login.usw2.pure.cloud/saml"
    # print('CONDITIONS COMPLETED')

    #authn_statement = ET.SubElement(root, "saml:AuthnStatement", AuthnInstant=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"), SessionIndex="abcdef1234567890")
    authn_statement = ET.SubElement(root, "saml:AuthnStatement", AuthnInstant=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), SessionIndex="abcdef1234567890")
    authn_context = ET.SubElement(authn_statement, "saml:AuthnContext")
    authn_context_class_ref = ET.SubElement(authn_context, "saml:AuthnContextClassRef")
    authn_context_class_ref.text = "urn:oasis:names:tc:SAML:2.0:ac:classes:Password"
    # print("AUTHN COMPLETED")

    # Create an ElementTree from the root element
    tree = ET.ElementTree(root)
    # print("TREE COMPLETED")
    # print(tree)

    # print(root.attrib)

    for child in root.iter():
        print(child.tag, child.attrib)

    tree.write('output.xml')



    # Format the XML for better readability
    #xml_string = minidom.parseString(ET.tostring(root)).toprettyxml(indent="    ")

    # Save the XML to a file
    #with open("somethingnew.xml", "w") as xml_file:
        #xml_file.write(xml_string)

if __name__ == "__main__":
    create_saml_assertion()
