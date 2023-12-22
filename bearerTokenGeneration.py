import requests
from bs4 import BeautifulSoup
import json
import urllib.parse

url = "https://dev-61411796-admin.okta.com/api/v1/authn"

payload = json.dumps({
  "username": "orlando.montalvo@genesys.com",
  "password": "H3llBlazer!",
  "options": {
    "multiOptionalFactorEnroll": True,
    "warnBeforePasswordExpired": True
  }
})
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Cookie': 'DT=DI1Rv7X1megT7Ks3nKLoaoH5g; JSESSIONID=BB82E5BA9E6EAD32A873F36063D81C9F'
}

response = requests.request("POST", url, headers=headers, data=payload)

response2 = response.json()


token = response2['sessionToken']


url = "https://dev-61411796.okta.com/home/purecloudcollaborate/0oadoyoe40Fe3skgY5d7/aln17dg4uvk2UENF91d8?sessionToken="+token

payload = {}
headers = {
  'Cookie': 'DT=DI1BEd4eYgtTD6PiC-TSuXVzw; proximity_bf520dbad5dce7b0ad856c7c3d35e79a=eyJ6aXAiOiJERUYiLCJwMnMiOiJ6WFZJekowMk9YMVpuU1RkbHFUX05BIiwicDJjIjoxMDAwLCJ2ZXIiOiIxIiwiZW5jIjoiQTI1NkdDTSIsImFsZyI6IlBCRVMyLUhTNTEyK0EyNTZLVyJ9.HbrY00tAAUZfwqorl_Bp_U-QMoOMozAhLmugcdeX9CQdlXyddOJmOg.BZ2H4jdHTaQ7Lrih.6CpJdJvgVY_oN_r6TJPCKMLLSYt_RfY3obYhh1FOUxAExBsEzFx2UVnPnWk46yf3LXEfl2ist98r7AJ7bLBmeWeZ44dO4D5Jpu-5SzVGfVYuOriQGQBXh5AreRPSf9DiGb0NbGj6zYqzMfzWxjb9qnPVEWbuw1s4QxlqNqh-i8kOUQ.MtWo8SFwUb1x17hV2ArHlw'
}

response = requests.request("GET", url, headers=headers, data=payload)

html = response.text
soup = BeautifulSoup(html, 'html.parser')

assertion = soup.find('input')['value']

url = "https://login.usw2.pure.cloud/oauth/token?grant_type=urn:ietf:params:oauth:grant-type:saml2-bearer&assertion="+urllib.parse.quote(assertion)+"&orgName=omontalvoDev"


payload = {}
files={}
headers = {
  'Authorization': 'Basic YThiMjBlY2YtYzJmOS00ODU4LTkyMTAtNTI2OGE2ZGRjODQ2OnR2WER1b0dQSE0zclppVmtzZDVWcFVOT05zYmtjVEdwNjJwLXlDczdKRlU=',
  'Cookie': 'ININ-Auth-Session=mlH1mS6Qg54TOkWVNsojHVwN_N19P79kp8x8BkCaef4='
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

bearerToken = response.json()


print("Session Token: " + token)
print("Bearer Token: " + bearerToken['access_token'])

