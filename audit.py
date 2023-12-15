import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
import time
from pprint import pprint

#Set Region
region = PureCloudPlatformClientV2.PureCloudRegionHosts.us_west_2
PureCloudPlatformClientV2.configuration.host = region.get_api_host()

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = "n80fCYIiUm64EepUmRn7geZfn1u-9XtOP6Nhrq6nRcgloApX2qSFcKVUqNOpHq2exiBC6pT9xxBhHSSEZNwOTg"

# or use get_client_credentials_token(...), get_saml2bearer_token(...) or get_code_authorization_token(...)
apiclient = PureCloudPlatformClientV2.api_client.ApiClient().get_client_credentials_token('e2b8729e-d9b9-46a9-aea0-c423667df6ea','ApFy9V5lQaP2wK35NeDwgT492-nSmIkMLdM2qrx5N4k')
authApi = PureCloudPlatformClientV2.AuthorizationApi(apiclient)
#print(authApi.get_authorization_permissions())

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.AuditApi();
#body = PureCloudPlatformClientV2.AuditQueryRequest() # AuditQueryRequest | query

body = {"serviceName":"Integrations","interval":"2023-11-12T00:00:00Z/2023-12-12T00:00:00Z"}

try:
    # Create audit query execution
    api_response = api_instance.post_audits_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->post_audits_query: %s\n" % e)
