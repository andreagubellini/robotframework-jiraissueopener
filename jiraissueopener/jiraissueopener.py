import json
import requests
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from requests.auth import HTTPBasicAuth
from robot.output import LOGGER
from robot.output.loggerhelper import Message

class jiraissueopener:
    ROBOT_LISTENER_API_VERSION = 3
    
    def __init__(self, user, password):
        """
        With the following listener a user can automatically create Jira issues when tests fail. Each failed test will have an individual Jira issue for which 
        assignee, project id and issue type may be modified.
        """
        self.jira_issues_list = []
        self.user = user
        self.password = password

    def end_test(self, data, result):
        self.suite_name = BuiltIn().get_variable_value("${SUITE_NAME}")
        self.project = BuiltIn().get_variable_value("${JIRA_PROJECT}")
        self.project_id = BuiltIn().get_variable_value("${JIRA_PROJECT_ID}")
        self.issue_type = BuiltIn().get_variable_value("${JIRA_ISSUE_TYPE}")
        self.project_key = BuiltIn().get_variable_value("${JIRA_PROJECT_KEY}")
        if result.status != "PASS":
            payload = {
                    "fields":{
                                "summary": self.suite_name + ": " + result.name + " has failed",
                                "issuetype":    { "id": self.issue_type },
                                "project":  { "id": self.project_id }, 
                                "description": "Error message: " + result.message + "\nDocumentation: " + result.doc,
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
        summary = data["fields"]["summary"]
        try:
            open_issue_count = self._get_issue(summary)
            if open_issue_count:
                request = requests.post(self.project, data=json.dumps(data), headers=headers, auth=HTTPBasicAuth(self.user, self.password))
                request.raise_for_status()
                content = dict(request.json())
                jira_issue = content["key"]
                self.jira_issues_list.append(jira_issue)
        except requests.exceptions.RequestException as e:
            LOGGER.error(e)

    def _get_issue(self, summary):
        headers = {"Content-type": "application/json" }
        project = self.project.rsplit("issue/", 1)
        params = {
            "jql": 'project = "{0}" AND resolution = Unresolved AND summary ~ "{1}"'.format(self.project_key, summary)
        }
        request = requests.get(project[0] + "search/", headers=headers, params=params, auth=HTTPBasicAuth(self.user, self.password))
        request.raise_for_status()
        resp = dict(request.json())
        if resp["total"] > 0:
            return False
        else:
            return True