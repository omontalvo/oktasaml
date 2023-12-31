from saml2 import BINDING_HTTP_POST
from saml2 import md, saml
from saml2.config import Config
from saml2.client import Saml2Client

# Load IDP metadata
idp_metadata = """metadata.xml"""
print(idp_metadata)

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
                    ("https://login.usw2.pure.cloud/saml", BINDING_HTTP_POST),
                ],
            },
        },
    },
})
saml_client = Saml2Client(config=sp_config)
print(type(saml_client))
dir(saml_client)

# Generate SAML assertion
authn_request_info = saml_client.prepare_for_authenticate()
saml_response = saml_client.parse_authn_request_response(
    saml_client.service.post(
        authn_request_info["url"], data=authn_request_info["data"]
    )
)
assertion = saml_response.assertions[0]

# Print the SAML assertion
print(assertion)
