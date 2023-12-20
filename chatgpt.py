from saml2 import BINDING_HTTP_POST
from saml2 import md, saml
from saml2.config import Config
from saml2.client import Saml2Client
import xml.etree.ElementTree as ET

# Load IDP metadata
idp_metadata = "metadata.xml"

# Create a SAML client
sp_config = Config()
sp_config.load({
    "metadata": {
        "local": [idp_metadata],
    },
    "service": {
        "sp": {
            "endpoints": {
                "assertion_consumer_service": [
                    ("[Your_ACS_URL]", BINDING_HTTP_POST),
                ],
            },
        },
    },
})
saml_client = Saml2Client(config=sp_config)

# Generate SAML assertion
authn_request_info = saml_client.prepare_for_authenticate()
saml_response = saml_client.parse_authn_request_response(
    saml_client.service.post(
        authn_request_info["url"], data=authn_request_info["data"]
    )
)
assertion = saml_response.assertions[0]

# Convert SAML assertion to XML string
assertion_xml = assertion.to_string()

# Parse XML string using ElementTree
root = ET.fromstring(assertion_xml)

# Print the SAML assertion XML
print(ET.tostring(root, encoding="unicode", method="xml"))
