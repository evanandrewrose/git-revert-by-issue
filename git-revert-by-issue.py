from commands import getoutput
from os import system
import sys

def main():
    for issue in get_issue_commits(sys.argv[1]):
        system("git revert --no-edit " + issue)

def get_issue_commits(issue):
    issues = []

    for line in get_log().split('\n'):
        if issue in line:
            issues.append(line.split()[0])

    return issues

def get_log():
    log = getoutput("git log --pretty=oneline --abbrev-commit --date=relative")

    return log

main()
