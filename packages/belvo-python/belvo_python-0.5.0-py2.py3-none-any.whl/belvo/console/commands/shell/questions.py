from typing import List


def validate_required(val):
    return "This field is required" if not val else True


login_questions = [
    {"type": "input", "name": "username", "message": "Username:", "validate": validate_required},
    {"type": "password", "message": "Password:", "name": "password", "validate": validate_required},
]


def create_questions(resource: str, institutions: List) -> List:
    questions = {
        "Links": [
            {
                "type": "list",
                "name": "institution",
                "message": "Institution:",
                "choices": institutions,
            },
            {
                "type": "input",
                "name": "username",
                "message": "Username:",
                "validate": validate_required,
            },
            {
                "type": "password",
                "name": "password",
                "message": "Password:",
                "validate": validate_required,
            },
            {"type": "password", "name": "token", "message": "Token:"},
        ]
    }
    return questions[resource]


def delete_questions():
    return [
        {"type": "input", "name": "id", "message": "ID (UUID):", "validate": validate_required},
        {
            "type": "confirm",
            "name": "continue",
            "message": "This can't be undone. Are you sure?",
            "default": False,
        },
    ]
