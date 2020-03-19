# robotframework-jiraissueopener

![Upload Python Package](https://github.com/andreagubellini/robotframework-jiraissueopener/workflows/Upload%20Python%20Package/badge.svg?branch=master)

With the following listener a user can automatically create Jira issues when tests fail. Each failed test will have an individual Jira issue for which 
    assignee, project id and issue type may be modified.

## Issue reported data

The issue will report:

**Summary**: `suite_name: test_name has failed` (example: *No-Regression-Suite: Login test has failed*)

**Description**: 

     Error message: test_message
     Documentation: test_documentation

**Assignee**: assignee can be set as listener argument

## Log files
Current execution `log.html` file is attached to all opened issues.

## Installation
```shell
pip install robotframework-jiraissueopener
```

## Dependencies
- Robotframework
- Requests

NB: above dependencies are installed automatically when using pip to retrieve `robotframework-jiraissueopener`

## Usage
Executed `.robot` file must have two variables called `${jira_user}` and `${jira_password}`.

Example:
```
***Variables***
${jira_user}   myuser
${jira_password}   mypassword
```

The listener arguments are:

`project_url`: your jira server url. Working example: *https://jira.myserver.com/rest/api/2/issue/*

`project_id`: your project id. Retrievable from project settings. Example: *11805*

`assignee`: assignee's username. Example: *agubellini*

`issue_type`: can be found on your jira settings. ([How-to](https://confluence.atlassian.com/jirakb/finding-the-id-for-issue-types-646186508.html)) Example: *10100* 

## Example
The following is an example based on the dummy data used in **Usage**

`robot --listener "robotframework-jiraissueopener;https://jira.myserver.com/rest/api/2/issue/;11805;agubellini;10100" mytests.robot`

## Contributing
Pull requests are welcome. Please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)