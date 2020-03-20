from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import requests
from requests.auth import HTTPBasicAuth
import json
from robot.output import LOGGER
from robot.output.loggerhelper import Message

class jiraissueopener(object):
    """
    With the following listener a user can automatically create Jira issues when tests fail. Each failed test will have an individual Jira issue for which 
    assignee, project id and issue type may be modified.
    """
    ROBOT_LISTENER_API_VERSION = 3
    def __init__(self, project_url=None, project_id=None, assignee=None, issue_type=None):
        self.project = project_url
        self.project_id = project_id
        self.jira_issues_list = []
        self.assignee = assignee
        self.issue_type = issue_type
        

    def end_test(self, data, result):
        self.suite_name = BuiltIn().get_variable_value("${SUITE_NAME}")
        self.user = BuiltIn().get_variable_value("${jira_user}")
        self.password = BuiltIn().get_variable_value("${jira_password}")
        if result.status != "PASS":
            payload = {
                    "fields":{
                                "project":  { "id": self.project_id },
                                "summary": self.suite_name + ": " + result.name + " has failed",
                                "description": "Error message:" + result.message + "\nDocumentation: " + result.doc,
                                "assignee": {"name": self.assignee },
                                "issuetype":    { "id": self.issue_type }
                            }
                }
            self._send_request(payload)

    def log_file(self, path):
        file = path
        self._upload_log_files(file)
 

    def _upload_log_files(self, file):
        headers = {"X-Atlassian-Token": "nocheck"}
        for i in self.jira_issues_list:
            attachments = {'file': open(file, 'rb')}
            try:
                upload_files = requests.post(self.project+i+"/attachments", files=attachments, headers=headers, auth=HTTPBasicAuth(self.user, self.password))
                print(upload_files)
            except Exception as e:
                print(e)

    def _send_request(self, data):
        headers = {"Content-type": "application/json" }
        try:
            request = requests.post(self.project, data=json.dumps(data), headers=headers, auth=HTTPBasicAuth(self.user, self.password))
            content = dict(request.json())
            jira_issue = content["key"]
            self.jira_issues_list.append(jira_issue)
        except Exception as e:
            print(e)

            
       

