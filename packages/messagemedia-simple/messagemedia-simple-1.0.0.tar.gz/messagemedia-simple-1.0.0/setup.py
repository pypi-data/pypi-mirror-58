# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['messagemedia_simple']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.22.0,<3.0.0']

setup_kwargs = {
    'name': 'messagemedia-simple',
    'version': '1.0.0',
    'description': 'Simple MessageMedia module for sending SMS messages.',
    'long_description': '# Simple MessageMedia API wrapper\n\n[![PyPI Version](https://img.shields.io/pypi/v/messagemedia-simple.svg?color=4fc921)](https://pypi.org/project/messagemedia-simple/)\n[![CircleCI](https://circleci.com/gh/mludvig/messagemedia-simple.svg?style=shield)](https://circleci.com/gh/mludvig/messagemedia-simple)\n[![Python Versions](https://img.shields.io/pypi/pyversions/messagemedia-simple.svg)](https://pypi.org/project/messagemedia-simple/)\n\nSimple and easy to use module for sending SMS and MMS messages through [MessageMedia API](https://developers.messagemedia.com/code/messages-api-documentation/).\n\n## Installation\n\nThe easiest way is to install the package from [Python Package Index](https://pypi.org/project/messagemedia-simple/):\n\n```\npip3 install messagemedia-simple\n```\n\nNote that `messagemedia-simple` is *only available* for **Python 3.6 and newer**. Installation for older Python versions will fail.\n\n## Usage - sending a SMS message\n\nThe module interface pretty much mirrors the [MessageMedia *Mesages* API](https://developers.messagemedia.com/code/messages-api-documentation/).\nRefer to the API documentation for details about all the possible settings.\n\n```\nfrom messagemedia_simple import MessagesAPI\n\nAPI_KEY = "ABCDEFGH1234567890XX"\nAPI_SECRET = "1234567890asdfghjkl1234567890x"\n\n# MessageMedia API object\nmm = MessagesAPI(API_KEY, API_SECRET, hmac_auth=True)\n\n# Send a SMS message and print `message_id`\nsend_response = mm.send_message("Some content", "+1234567890")\nprint(f"message_id: {send_response[\'message_id\']})\n```\n\nNow we can check the message delivery status as it progresses from *enroute* through *submitted* to *delivered*:\n\n```\nstatus_response = mm.get_message_status(send_response["message_id"])\nprint(f"status: {status_response[\'status\']})\n```\n\nAnd finally we can retrieve *Message Replies*. Unfortunately through the API we can only\nretrieve *all* queued, unconfirmed replies rather than just those for a given `message_id`.\nThe filtering has to be done locally after all the replies are retrieved.\n\n```\n# Retrieve all replies from MessageMedia\nreplies_response = mm.get_replies()\n\n# Filter only the relevant replies\nmy_replies = [r for r in replies_response["replies"] if r["message_id"]==send_response["message_id"]]\n\n# Process the replies\nfor reply in my_replies:\n  print(f"{reply[\'content\']}")\n```\n\nMessageMedia API has a concept of *confirming a reply* - as soon as a reply is confirmed it is no longer\nreturned from `get_replies()` call. That means only confirm a reply after it\'s successfully processed,\nfor example written to a local database. Multiple replies can be confirmed at once if needed.\n\n```\nfor reply in my_replies:\n  print(f"{reply[\'content\']}")\n  mm.confirm_replies(reply["reply_id"])\n```\n\nLikewise we can retrieve and confirm the delivery reports using `get_delivery_reports()` and\n`confirm_delivery_reports()`. The logic of the operation is the same as with replies.\n\n## Author\n\nMichael Ludvig <mludvig@logix.net.nz>\n',
    'author': 'Michael Ludvig',
    'author_email': 'mludvig@logix.net.nz',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mludvig/messagemedia-simple',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
