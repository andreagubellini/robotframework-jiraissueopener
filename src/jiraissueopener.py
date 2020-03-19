from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import requests
from requests.auth import HTTPBasicAuth
import json

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
    
    ROBOT_LISTENER_API_VERSION = 3
    def __init__(self, project_url=None, project_id=None, assignee=None, issue_type=None):
        
        """
        *user* = Jira username

        *password* = Jira password

        *project_url* = Jira project url. Example: https://127.0.0.1/rest/api/2/issue/

        *project_id* = the project id on which the issue will be opened. Retrieve this from your project's settings.

        *Import example* = ``Library    jiraissueopener   myuser   mypassword   https://127.0.0.1/rest/api/2/issue/   10800``
        """
        self.project = project_url
        self.project_id = project_id
        self.jira_issues_list = []
        self.assignee = assignee
        self.issue_type = issue_type
        

    def end_test(self, data, result):
        self.suite_name = BuiltIn().get_variable_value("${SUITE_NAME}")
        self.log_files = BuiltIn().get_variable_value("${LOG_FILE}")
        self.user = BuiltIn().get_variable_value("${jira_user}")
        self.password = BuiltIn().get_variable_value("${jira_password}")
        if result.status != "PASS":
            payload = {
                    "fields":{
                                "project":  { "id": self.project_id },
                                "summary": self.suite_name + ": " + result.name + " has failed",
                                "description": "Error message:\n" + result.message + "\nDocumentation: \n" + result.doc,
                                "assignee": {"name": self.assignee },
                                "issuetype":    { "id": self.issue_type }
                            }
                }
            self._send_request(payload)

    def log_file(self, log_file):
        file = log_file.path
        self._upload_log_files(file)
        

    def _upload_log_files(self, file):
        headers = {"X-Atlassian-Token": "nocheck"}
        for i in self.jira_issues_list:
            attachments = {'file': open(self.file, 'rb')}
            try:
                upload_files = requests.post(self.project+i+"/attachments", files=attachments, headers=headers, auth=HTTPBasicAuth(self.user, self.password))
                print(upload_files.content)
            except Exception as e:
                print(e)

    def _send_request(self, data):
        headers = {"Content-type": "application/json" }
        try:
            request = requests.post(self.project, data=json.dumps(data), headers=headers, auth=HTTPBasicAuth(self.user, self.password))
            print(request)
            content = dict(request.json())
            jira_issue = content["key"]
            print(jira_issue)
            self.jira_issues_list.append(jira_issue)
        except Exception as e:
            print(e)

            
       

