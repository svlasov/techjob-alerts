import pprint

from freelancersdk.session import Session
from freelancersdk.resources.projects.projects import search_projects
from freelancersdk.resources.projects.exceptions import \
    ProjectsNotFoundException
from freelancersdk.resources.projects.helpers import (
    create_search_projects_filter,
    create_get_projects_user_details_object,
    create_get_projects_project_details_object,
)

import os

FLN_OAUTH_TOKEN = "ZSq7fJiqHSq5raHHPWBOpSzPY3iiXJ"
FLN_URL = "https://www.freelancer.com"


def sample_search_projects():

    session = Session(oauth_token=FLN_OAUTH_TOKEN, url=FLN_URL)

    query = 'Python'
    search_filter = create_search_projects_filter(
        sort_field= 'time_updated',
        or_search_query= True,
    )

    try:
        p = search_projects(
            session,
            query=query,
            search_filter=search_filter
        )

    except ProjectsNotFoundException as e:
        print('Error message: {}'.format(e.message))
        print('Server response: {}'.format(e.error_code))
        return None
    else:
        return p


p = sample_search_projects()
if p:
    pprint.pprint('Found projects: {}'.format(p))