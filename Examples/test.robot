***Settings***
***Keywords***
${jira_user}    agubellini
${jira_password}    !9v834nd1235989SwostepS!

***Test Cases***
passed Test
    [Documentation]  This test will be passed so no bug will be opened
    Log To Console  \nThis is a test stream=STDOUT  no_newline=False
    [Teardown]  Teardown
failed Test
    [Documentation]  This is a failing test, a bug will be opened on teardown
    Run keyword and ignore error    Step number 1 of my test


Failed test number 2
    [Documentation]  This is a second failed test, another separate bug will be opened for this one
    Run keyword and ignore error    Remove String  ${na_list_1}  fail

