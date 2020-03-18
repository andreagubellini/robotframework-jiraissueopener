#steps:
#gather robotframework informations
#wrap informations
#give them to a request
#post a new  bug
#retrieve bug id
#stamp the id
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import requests
from requests.auth import HTTPBasicAuth
import json

class Error(RuntimeError):
    ROBOT_CONTINUE_ON_FAILURE = True

class jiraissueopener(object):
    ROBOT_LIBRARY_SCOPE = 'TEST CASE'

    def __init__(self, user, password, project_url, project_id):
        self.user = user
        self.password = password
        self.project = project_url
        self.project_id = project_id

    @keyword('Open Jira Issue')
    def open_jira_issue(self, issue_id, assignee):
        self.test_message = BuiltIn().get_variable_value("${TEST_MESSAGE}")
        self.test_status = BuiltIn().get_variable_value("${TEST_STATUS}")
        self.test_doc = BuiltIn().get_variable_value("${TEST_DOCUMENTATION}")
        self.test_name = BuiltIn().get_variable_value("${TEST_NAME}")
        self.suite_name = BuiltIn().get_variable_value("${SUITE_NAME}")
        self.issue = issue_id
        if self.test_status == "FAIL":
            payload = {
                    "fields":{
                                "project":  { "id": self.project_id },
                                "summary": "Suite: " + self.suite_name + " Test: " + self.test_name,
                                "description": "Error: " + self.test_message + " " + "\nTest Documentation: " + self.test_doc,
                                "assignee": {"name": assignee },
                                "issuetype":    { "id": self.issue }
                            }
                }
            self._send_request(payload)
        else:
            print("Tests Passed")

    def _send_request(self, data):
        headers = {"Content-type": "application/json" }
        try:
            request = requests.post(self.project, data=json.dumps(data), headers=headers, auth=HTTPBasicAuth(self.user, self.password))
            print(request.content)
        except Exception as e:
            print(e)
   

#