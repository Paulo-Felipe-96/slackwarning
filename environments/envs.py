from requests.structures import CaseInsensitiveDict

slack_channel = "TOKEN_SLACK_CHANNEL_AQUI"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Content-Type"] = "application/json"

# API Dashboard
_url = "URL_DE_API"
_headers = {'Content-Type': 'application/json', 'Authorization': 'SEU_TOKEN_AQUI'}

# payload esperado pela api
_payload = {}

# Notifier

MESSAGE_ERR = f"Something went wrong. API is OFF :/"
MESSAGE_SUCSS = f"God damn! API-V2 STG is back!"
