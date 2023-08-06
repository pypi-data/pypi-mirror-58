import os
from jiratag_commitizen.cz.base import BaseCommitizen
from jiratag_commitizen import defaults
__all__ = ["ConventionalCommitsCz"]


class NoSubjectException(Exception):
    ...

class NaNException(Exception):
    ...

class NeedIssueCode(Exception):
    ...

def parse_scope(text):
    if not text:
        return ""

    scope = text.strip().split()
    if len(scope) == 1:
        return scope[0]

    return "-".join(scope)


def parse_subject(text):
    if isinstance(text, str):
        text = text.strip(".").strip()

    if not text:
        raise NoSubjectException("Subject is a required field")

    return text

def parse_confirm(text) -> bool:
    import re

    regex = r"(yes|ye|y)"
    return bool(re.match(regex, text, re.IGNORECASE))

def parse_number(text):
    if text and not str.isdigit(text):
        raise NaNException("Input must be a NUMBER")
    
    return text

class ConventionalCommitsCz(BaseCommitizen):
    bump_pattern = defaults.bump_pattern
    bump_map = defaults.bump_map

    def questions(self) -> list:
        questions = [
            {
                "type": "list",
                "name": "prefix",
                "message": "Select the type of change you are committing",
                "choices": [
                    {
                        "value": "fix",
                        "name": "fix: A bug fix. Correlates with PATCH in SemVer",
                    },
                    {
                        "value": "feat",
                        "name": "feat: A new feature. Correlates with MINOR in SemVer",
                    },
                    {"value": "docs", "name": "docs: Documentation only changes"},
                    {
                        "value": "style",
                        "name": (
                            "style: Changes that do not affect the "
                            "meaning of the code (white-space, formatting,"
                            " missing semi-colons, etc)"
                        ),
                    },
                    {
                        "value": "refactor",
                        "name": (
                            "refactor: A code change that neither fixes "
                            "a bug nor adds a feature"
                        ),
                    },
                    {
                        "value": "chore",
                        "name": (
                            "chore: A code change that doesn't impact end users "
                            "(adding a wrapper function, defining constants...)"
                        ),
                    },
                    {
                        "value": "perf",
                        "name": "perf: A code change that improves performance",
                    },
                    {
                        "value": "test",
                        "name": (
                            "test: Adding missing or correcting " "existing tests"
                        ),
                    },
                    {
                        "value": "build",
                        "name": (
                            "build: Changes that affect the build system or "
                            "external dependencies (example scopes: pip, docker, npm)"
                        ),
                    },
                    {
                        "value": "ci",
                        "name": (
                            "ci: Changes to our CI configuration files and "
                            "scripts (example scopes: GitLabCI)"
                        ),
                    },
                ],
            },
            {
                "type": "input",
                "name": "scope",
                "message": (
                    "Scope. Could be anything specifying place of the "
                    "commit change (users, db, poll):\n"
                ),
                "filter": parse_scope,
            },
            {
                "type": "input",
                "name": "jira_project_code",
                "message": (
                    "JIRA Project. Code of the project where the issue issue in JIRA. "
                    "It is usually an uppercase string code (we will uppercase them for you). E.g: AT, MCSW, PAN\n"
                ),
            },
            {
                "type": "input",
                "name": "issue_number",
                "filter": parse_number,
                "message": (
                    "JIRA Issue Number. The number that follows the project code. "
                    "E.g: EXAMPLE-123 will be issue number 123 in project EXAMPLE\n"
                ),
            },
            {
                "type": "input",
                "name": "subject",
                "filter": parse_subject,
                "message": (
                    "Subject. Concise description of the changes. "
                    "Imperative, lower case and no final dot:\n"
                ),
            },
            {
                "type": "input",
                "message": "Is this a BREAKING CHANGE? Correlates with MAJOR in SemVer (y/N)",
                "name": "is_breaking_change",
                "filter": parse_confirm,
            },
            {
                "type": "input",
                "name": "body",
                "message": (
                    "Body. Motivation for the change and contrast this "
                    "with previous behavior:\n"
                ),
            },
            {
                "type": "input",
                "name": "footer",
                "message": (
                    "Footer. Information about Breaking Changes and "
                    "reference issues that this commit closes:\n"
                ),
            },
        ]
        return questions

    def message(self, answers: dict) -> str:
        prefix = answers["prefix"]
        scope = answers["scope"]
        subject = answers["subject"]
        jira_project_code = answers["jira_project_code"]
        body = answers["body"]
        footer = answers["footer"]
        is_breaking_change = answers["is_breaking_change"]

        if scope:
            scope = f"({scope})"
        if is_breaking_change:
            body = f"BREAKING CHANGE: {body}"
        if jira_project_code:
            issue_number = answers["issue_number"]

            if not issue_number:
                raise NeedIssueCode("Issue number is required when providing the JIRA project code")
            
            subject = f"{jira_project_code.upper()}-{issue_number} | {subject}"
        if body:
            body = f"\n\n{body}"
        if footer:
            footer = f"\n\n{footer}"

        message = f"{prefix}{scope}: {subject}{body}{footer}"

        return message

    def example(self) -> str:
        return (
            "fix: correct minor typos in code\n"
            "\n"
            "see the issue for details on the typos fixed\n"
            "\n"
            "closes issue #12"
        )

    def schema(self) -> str:
        return (
            "<type>(<scope>): <issue> | <subject>\n"
            "<BLANK LINE>\n"
            "(BREAKING CHANGE: )<body>\n"
            "<BLANK LINE>\n"
            "<footer>"
        )

    def info(self) -> str:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        filepath = os.path.join(dir_path, "conventional_commits_info.txt")
        with open(filepath, "r") as f:
            content = f.read()
        return content
