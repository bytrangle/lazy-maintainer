from os import environ, getenv
import re
# import requests

minIssueComment = getenv('INPUT_MIN_ISSUE_COMMENT', 20)
print(minIssueComment)
API_URL = getenv('GITHUB_API_URL', 'https://api.github.com')
print(API_URL)
# Input parameter passed to jobs.<job_id>.steps[*].width are available
# as environment variable

#print(environ)

REPO = environ['GITHUB_REPOSITORY']
issueUrl = environ['ISSUE_URL']
ISSUE_ID = re.search("issues\/(.+)", issueUrl).group(1)
print(ISSUE_ID)