from plyer import notification
from environments.envs import MESSAGE_SUCSS, MESSAGE_ERR


def notifier(SUCCESS):
    if SUCCESS:
        notification.notify(
            title="From Messenger",
            message=MESSAGE_SUCSS
        )
    else:
        notification.notify(
            title="From Messenger",
            message=MESSAGE_ERR
        )
