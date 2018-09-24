import pprint

from freelancersdk.resources.projects import make_get_request
from freelancersdk.session import Session
from freelancersdk.resources.projects.projects import get_jobs
from freelancersdk.resources.projects.exceptions import \
    JobsNotFoundException
import os

env = {
    "FLN_OAUTH_TOKEN": "ZSq7fJiqHSq5raHHPWBOpSzPY3iiXJ",
    "FLN_URL": "https://www.freelancer.com"
}

for k,v in env.items():
    os.environ.setdefault(k, v)


def get_skills(session, **kwargs):
    """
    Get a list of jobs
    """

    keys = ['jobs[]', 'seo_details', 'lang']

    get_jobs_data = {k: v for k, v in kwargs.items() if k in keys}

    # GET /api/projects/0.1/jobs/
    response = make_get_request(session, 'jobs', params_data=get_jobs_data)
    json_data = response.json()
    if response.status_code == 200:
        return json_data['result']
    else:
        raise JobsNotFoundException(
            message=json_data['message'], error_code=json_data['error_code'])


def sample_get_jobs():
    url = os.environ.get('FLN_URL')
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')
    session = Session(oauth_token=oauth_token, url=url)

    get_jobs_data = {
        # 'job_ids': [
        #     20,
        #     32,
        # ],
        'seo_details': True,
        'lang': 'en',
    }

    try:
        j = get_skills(session, **get_jobs_data)
    except JobsNotFoundException as e:
        print('Error message: {}'.format(e.message))
        print('Server response: {}'.format(e.error_code))
        return None
    else:
        return j


j = sample_get_jobs()
if j:
    print('Found skills: {}'.format(len(j)))
    pprint.pprint('first skill: {}'.format(j[0]))