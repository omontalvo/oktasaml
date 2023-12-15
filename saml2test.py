from saml2 import BINDING_HTTP_POST
from saml2 import md, saml
from saml2.config import Config
from saml2.client import Saml2Client

# Load IDP metadata
idp_metadata = """
<md:EntityDescriptor xmlns:md="urn:oasis:names:tc:SAML:2.0:metadata" entityID="http://www.okta.com/exkdoyoe3zOskPHhO5d7">
<md:IDPSSODescriptor WantAuthnRequestsSigned="false" protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol">
<md:KeyDescriptor use="signing">
<ds:KeyInfo xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
<ds:X509Data>
<ds:X509Certificate>MIIDqDCCApCgAwIBAgIGAYxBKbriMA0GCSqGSIb3DQEBCwUAMIGUMQswCQYDVQQGEwJVUzETMBEG A1UECAwKQ2FsaWZvcm5pYTEWMBQGA1UEBwwNU2FuIEZyYW5jaXNjbzENMAsGA1UECgwET2t0YTEU MBIGA1UECwwLU1NPUHJvdmlkZXIxFTATBgNVBAMMDGRldi02MTQxMTc5NjEcMBoGCSqGSIb3DQEJ ARYNaW5mb0Bva3RhLmNvbTAeFw0yMzEyMDYyMjA0MDNaFw0zMzEyMDYyMjA1MDNaMIGUMQswCQYD VQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTEWMBQGA1UEBwwNU2FuIEZyYW5jaXNjbzENMAsG A1UECgwET2t0YTEUMBIGA1UECwwLU1NPUHJvdmlkZXIxFTATBgNVBAMMDGRldi02MTQxMTc5NjEc MBoGCSqGSIb3DQEJARYNaW5mb0Bva3RhLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoC ggEBAJp0UkRoiyPq8CXpQCqseSWCx0VR4JLD7k8WWS8WW82HPLevTUqPAWBpBSyMWSkTF9ZjHI8q HpShqjzqrOvayvamcJthPhmlWMB5GDKwuUYF/0pWvChYarlRIQZ0kdBUcr6AjSUZ46BV4uQROU1t Bo2Sx9GDwBUw/hN5mq1sNmguoLxqmbxTGN2coqRYWyumPruFehUkgPjKMHOl9l2RHRGxDacfhjnL Wp5h8HmHBiEaNcwMWUFQI35K/VfvFv9GRGOD7RughKk7u9bCEjZ6SlkAJmEVDjGZqLhcWMd6QgKS EeU5B2eZbVUK6NMlpjjkKJO5a2uQXFXUw+cDMosHUYkCAwEAATANBgkqhkiG9w0BAQsFAAOCAQEA PHbS9iK1U3nfc40dfXCvWkwlZQ7PdsZIwigJQ/Nle1LHMArqOlCg2pj93JwVyrwr309TM7JSc4js xoKvquL3qY1Dk2rg8rVEw2S1M/2r/zxfVtSzQ1Trwa4tP61F+ODkb5X5JC4xXDt6Z3GReUPD7IAy OK6wtCkL0S5dJ4uEYURA/0iFcLcy1ZQEIGix0rCzPYplQNFq/R0eJQW3qBFMjwQ8X76St9fj6+Q+ KhvFzx3fq9Ax0lKBKbHhuDT6mNSzV+hOc2fg8EMSiaxk1nJMsyG+ip+oY6tkS5mMd2e63MgalVqQ ASWRnakBu44jBsSjBfq8laBEYEVPv2spGcXTDQ==</ds:X509Certificate>
</ds:X509Data>
</ds:KeyInfo>
</md:KeyDescriptor>
<md:NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified</md:NameIDFormat>
<md:NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress</md:NameIDFormat>
<md:SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://dev-61411796.okta.com/app/purecloudcollaborate/exkdoyoe3zOskPHhO5d7/sso/saml"/>
<md:SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect" Location="https://dev-61411796.okta.com/app/purecloudcollaborate/exkdoyoe3zOskPHhO5d7/sso/saml"/>
</md:IDPSSODescriptor>
</md:EntityDescriptor>
"""

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
