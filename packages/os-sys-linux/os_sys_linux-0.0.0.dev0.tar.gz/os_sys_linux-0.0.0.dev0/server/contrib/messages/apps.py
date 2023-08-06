from server.apps import AppConfig
from server.utils.translation import gettext_lazy as _


class MessagesConfig(AppConfig):
    name = 'server.contrib.messages'
    verbose_name = _("Messages")
