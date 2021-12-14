# robotframework-jiraissueopener

![Build](https://github.com/andreagubellini/robotframework-jiraissueopener/workflows/Upload%20Python%20Package/badge.svg?branch=master) [![Downloads](https://pepy.tech/badge/robotframework-jiraissueopener)](https://pepy.tech/project/robotframework-jiraissueopener) [![Downloads](https://pepy.tech/badge/robotframework-jiraissueopener/month)](https://pepy.tech/project/robotframework-jiraissueopener/month) ![PyPI](https://img.shields.io/pypi/v/robotframework-jiraissueopener?color=light%20green)

With the following listener a user can automatically create Jira issues when tests fail. Each failed test will have an individual Jira issue for which 
    assignee, project id and issue type may be modified.

## Issue reported data

The issue will report:

**Summary**: `suite_name: test_name has failed` (example: *No-Regression-Suite: Login test has failed*)

**Description**: 

     Error message: test_message
     Documentation: test_documentation

**Assignee**: assignee can be set as variable value

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
Executed `.robot` file must expose mandatory variables such as:

* ${JIRA_PROJECT}  Jira server api /issue/ url
* ${JIRA_PROJECT_ID}  your project id. Retrievable from project settings. Example: *11805*
* ${JIRA_ISSUE_TYPE}  `issue_type`: can be found on your jira settings. ([How-to](https://confluence.atlassian.com/jirakb/finding-the-id-for-issue-types-646186508.html)) Example: *10100* 

Example:
```
***Variables***
${JIRA_PROJECT}     https://jira.myserver.com/rest/api/2/issue/
${JIRA_PROJECT_ID}  11888
${JIRA_ISSUE_TYPE}  10100
${JIRA_ISSUE_KEY}   TEST
```

The listener arguments are:

`username`: your jira username
`password`: your jira password

## Example
The following is an example based on the dummy data used in **Usage**

`robot --listener "jiraissueopener;testusername;mycoolpassword" mytests.robot`

## Contributing
Pull requests are welcome. Please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)