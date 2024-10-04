import ngrok
import os
from urllib.parse import urlparse

# construct the api client
client = ngrok.Client(os.environ["NGROK_API_KEY"])

ngrok_winrm_public_url = None
# list all online tunnels
for t in client.tunnels.list():
    if t.public_url.startswith("https"):
        # search for the https one (WinRM)
        ngrok_winrm_public_url = t.public_url

if (ngrok_winrm_public_url == None):
    raise Exception("ngrok_winrm_public_url({}) is None, no WinRM tunnel found".format(ngrok_winrm_public_url))

ngrok_winrm_domain = urlparse(ngrok_winrm_public_url).netloc

if (ngrok_winrm_domain == None):
    raise Exception("ngrok_winrm_domain({}) is None, no WinRM valid domain".format(ngrok_winrm_domain))


if (ngrok_winrm_domain not in ngrok_winrm_public_url):
    raise Exception("ngrok_winrm_domain({}) is not a substring ngrok_winrm_public_url({}), no WinRM valid domain".format(ngrok_winrm_domain, ngrok_winrm_public_url))

print("ANSIBLE_HOST_PATTERN={}".format(ngrok_winrm_domain))
