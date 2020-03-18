from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import requests
from requests.auth import HTTPBasicAuth
import json

class Error(RuntimeError):
    ROBOT_CONTINUE_ON_FAILURE = True

class jiraissueopener(object):
    """
    = Table of contents =

    - `Usage`
    - `Importing`
    - `Keywords`

    = Usage =

    With the following library, we can set specific tests to open a jira issue when *failed*.
    Each issue may have a specific type, be opened on a specific project and assigned to a specific user.
    """
    ROBOT_LIBRARY_SCOPE = 'TEST CASE'

    def __init__(self, user=None, password=None, project_url=None, project_id=None):
        """
        *user* = Jira username

        *password* = Jira password

        *project_url* = Jira project url. Example: https://127.0.0.1/rest/api/2/issue/

        *project_id* = the project id on which the issue will be opened. Retrieve this from your project's settings.

        *Import example* = ``Library    jiraissueopener   myuser   mypassword   https://127.0.0.1/rest/api/2/issue/   10800``
        """
        self.user = user
        self.password = password
        self.project = project_url
        self.project_id = project_id

    @keyword('Open Jira Issue')
    def open_jira_issue(self, issue_id, assignee):
        """Opens a jira issue.
        
        The issue can be assigned automatically to a specific assignee by passing the username of the assignee. Example: agubellini.

        The issue may be opened as a specific type by passing the issue id to "issue_id" parameter. Example: 10100
        """
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
