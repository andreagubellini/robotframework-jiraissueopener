***Settings***
Library     ../src/jiraissueopener.py    myuser   mypassword  https://127.0.0.1/rest/api/2/issue/     projectid

***Test Cases***
passed Test
    [Documentation]  This test will be passed so no bug will be opened
    Log To Console  \nThis is a test stream=STDOUT  no_newline=False
    [Teardown]  Teardown
failed Test
    [Documentation]  This is a failing test, a bug will be opened on teardown
    Run keyword and ignore error    Step number 1 of my test
    [Teardown]   Teardown
Failed test without Teardown
    [Documentation]  This test fails but since no "Open jira issue" keyword is attached to it no issue will be opened
    Run keyword and ignore error    Get Count  ${na_list_1}  ${na_list_2}
    [Teardown]  NONE
Failed test number 2
    [Documentation]  This is a second failed test, another separate bug will be opened for this one
    Run keyword and ignore error    Remove String  ${na_list_1}  fail
    [Teardown]  Teardown

***Keywords***
Teardown
    Run keyword and ignore error  Open Jira issue   10100    myuser
