"""Ulauncher extension main class"""

import logging
import json
import os
from threading import Timer
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction
from ulauncher.config import EXT_PREFERENCES_DIR


LOGGER = logging.getLogger(__name__)


class StatusPagesExtension(Extension):
    """ Main extension class """

    def __init__(self):
        """ init method """

        LOGGER.info('Ititialize Status Pages Extension')

        super(StatusPagesExtension, self).__init__()

        self.load_pages()

        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

    def load_pages(self):
        """ Load status pages list into memory"""

        self.pages = []

        if (os.path.isfile(
                os.path.join(EXT_PREFERENCES_DIR, 'status_pages.json'))):
            LOGGER.info('Loading status pages from user')
            config = os.path.join(EXT_PREFERENCES_DIR, 'status_pages.json')
        else:
            LOGGER.info('Loading status pages from extension')
            config = os.path.join(os.path.dirname(__file__), 'data',
                                  'pages.json')

        with open(config) as f:  # pylint: disable=invalid-name
            self.pages = json.load(f)

        # refresh pages every hour
        t = Timer(3600, self.load_pages)  # pylint: disable=invalid-name
        t.start()


class KeywordQueryEventListener(EventListener):
    """ Handles Keyboard input """

    def on_event(self, event, extension):
        """ Handles the event """

        pages = extension.pages
        query = event.get_argument()
        if query:
            pages = [p for p in pages if query.lower() in p['label'].lower()]

        pages = sorted(pages, key=lambda k: k['label'])

        items = []
        for page in pages[:8]:
            items.append(
                ExtensionResultItem(
                    icon=page['icon'],
                    name=page['label'],
                    description="Click to open the service status page",
                    on_enter=OpenUrlAction(page['url'])))

        return RenderResultListAction(items)


if __name__ == '__main__':
    StatusPagesExtension().run()
