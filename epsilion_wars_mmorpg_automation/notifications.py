"""Desktop and other notifications."""

from desktop_notifier import DesktopNotifier

from epsilion_wars_mmorpg_automation.settings import app_settings

notifier = DesktopNotifier(
    app_name=app_settings.trainer_name,
    app_icon=None,
)


async def send_desktop_notify(message: str) -> None:
    """Send desktop notification."""
    await notifier.send(
        title=app_settings.trainer_name,
        message=message,
        timeout=app_settings.desktop_notification_timeout,
    )