import requests
import json
from environments.envs import headers, slack_channel


def post_message_feature_slack() -> None:
    text = {
        "text": f"@here Ambiente de STAGING voltou!! \n"
                f":ultra_fast_parrot: :ultra_fast_parrot: :ultra_fast_parrot: :ultra_fast_parrot:"
    }
    requests.post(f"https://hooks.slack.com/services/{slack_channel}", headers=headers, data=json.dumps(text))
