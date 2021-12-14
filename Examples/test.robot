***Variables***
${JIRA_PROJECT}     https://placeholder.atlassian.net/rest/api/2/issue/
${JIRA_PROJECT_ID}  12023
${JIRA_ISSUE_TYPE}  10610

***Test Cases***
Failed test Case
    [Documentation]  This test fails. A jira issue will be opened.
    log to Consolee  \nThis is failed!  stream=STDOUT  no_newline=False

Passed test Case
    [Documentation]  This test passed. Nothing will be opened.
    Log To Console  \nThis is passed! hooray!  stream=STDOUT  no_newline=False

Failed test case 2
    [Documentation]  Another failed test. A new jira issue will be opened.
    log to Consolee  \nAnother failed!  stream=STDOUT  no_newline=False