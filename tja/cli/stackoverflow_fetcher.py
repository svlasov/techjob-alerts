import string

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

DB_USER = "heroku_s5jktn59"
DB_NAME = "heroku_s5jktn59"
DB_PASS = "5m1vhfkgr6cvemat6o3r4kgi0n"
DB_HOST = "ds215093.mlab.com"
DB_PORT = "15093"

MONGODB_URI = "mongodb://{user}:{password}@{host}:{port}/{db_name}".format(user=DB_USER, password=DB_PASS,
                                                                           host=DB_HOST, port=DB_PORT, db_name=DB_NAME)


client = MongoClient(MONGODB_URI)
db = client[DB_NAME]
Jobs = db.jobs

if __name__ == "__main__":

    resp = requests.get("https://stackoverflow.com/jobs?r=true&tl=python")

    if resp.ok:
        content = resp.content
        #pprint.pprint(content)

        soup = BeautifulSoup(content, 'html.parser')

        soup_jobs = soup.select("div.-item.-job")

        job_docs = []

        for sj in soup_jobs:
            title_selection = sj.select("a.s-link")

            if title_selection:
                title = title_selection[0]
                title_href = title.get('href')
                title_text = title.get_text()

            div_company = sj.select("div.-company")
            spans_company = div_company and div_company[0].select("span") or []
            if spans_company:
                company_name = spans_company[0].get_text()
                if len(spans_company) > 1:
                    company_location = spans_company[1].get_text().replace('-', ' ').strip()

            skill_selection = sj.select("a.post-tag")
            if skill_selection:
                skills = [
                    {
                        'text': skill_el.get_text(),
                        'href': skill_el.get("href")
                    }
                    for skill_el in skill_selection]

            job_doc = {
                'title': {
                    'text': title_text,
                    'href': title_href
                },
                '_id': title_href,
                'company': {
                    'name': company_name,
                    'location': company_location
                },
                'skills': skills
            }

            job_docs.append(job_doc)

            try:
                Jobs.insert(job_doc)
            except Exception as ex:
                print(ex)

            print(title_text)