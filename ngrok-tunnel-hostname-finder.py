import ngrok
import os

# construct the api client
client = ngrok.Client(os.environ["NGROK_API_KEY"])

ngrok_winrm_public_url = None
# list all online tunnels
for t in client.tunnels.list():
    if t.public_url.startswith("https"):
        # search for the https one (WinRM)
        ngrok_winrm_public_url = t.public_url

if (ngrok_winrm_public_url == None):
    raise Exception("ngrok_winrm_public_url is None, no WinRM tunnel found")

print("Proceed with {} as WinRM URL".format(ngrok_winrm_public_url))
