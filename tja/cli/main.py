#!/usr/bin/env python3

from freelancersdk.resources.projects.exceptions import \
    ProjectsNotFoundException
from freelancersdk.resources.projects.helpers import (
    create_search_projects_filter,
)
from freelancersdk.resources.projects.projects import search_projects
from freelancersdk.session import Session
from pymongo import MongoClient

FLN_OAUTH_TOKEN = "ZSq7fJiqHSq5raHHPWBOpSzPY3iiXJ"
FLN_URL = "https://www.freelancer.com"

DB_USER = "heroku_s5jktn59"
DB_NAME = "heroku_s5jktn59"
DB_PASS = "5m1vhfkgr6cvemat6o3r4kgi0n"
DB_HOST = "ds215093.mlab.com"
DB_PORT = "15093"

MONGODB_URI = "mongodb://{user}:{password}@{host}:{port}/{db_name}".format(user=DB_USER, password=DB_PASS,
                                                                           host=DB_HOST, port=DB_PORT, db_name=DB_NAME)


client = MongoClient(MONGODB_URI)
db = client[DB_NAME]
Projects = db.projects

def fetch_projects():

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
        return p['projects']

def main():

    project_docs = fetch_projects()

    for doc in project_docs:
        doc['_id'] = doc['id']

        try:
            Projects.insert(doc)
        except Exception as ex:
            print("couldn't insert duplicate")
    #if project_docs:


if __name__ == "__main__":
    main()
