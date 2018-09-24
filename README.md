# techjob-alerts

## Initial Setup

 - clone the source with **git clone**
 - create a virtual environment (with conda or virtualenv)
 - install python packages with ```pip install -r requirements.txt```
 - copy example-secrets.txt into secrets.txt
 - fill secrets.txt with actual values

## How to run

### fetcher.py

**fetcher.py** uses **freelancersdk** library, specified in *requirements.txt*
which in turn requires some environment variables to be set

* FLN_OAUTH_TOKEN: The OAuth2 token to create the session with and must be specified
* FLN_URL: If you want to use the library to make requests against the Freelancer.com Sandbox, you can specifiy FLN_URL=https://www.freelancer-sandbox.com. If not specified, it defaults to https://www.freelancer.com.
