#!/usr/bin/env python3
"""
fetcher.py is an executable script which
provides function fetch() available for importing
from other modules
"""
import os

from freelancersdk.session import Session

env = {
    "FLN_OAUTH_TOKEN": "ZSq7fJiqHSq5raHHPWBOpSzPY3iiXJ",
    "FLN_URL": "https://www.freelancer.com"
}


def fetch(category=None):
    """
    Function fetch() returns latest job posts
    from freelance.com

    :param category:
    :return: list of dictionaries
    """

    session = Session(oauth_token=env["FLN_OAUTH_TOKEN"])
#    session.

def main():
    """ Main entry point of the app """

    for k, v in env.items():
        os.environ.setdefault(k, v)

    projects = fetch()

    print(projects)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()