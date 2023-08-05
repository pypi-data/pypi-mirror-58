import json
from typing import Dict, List, Union

from cleo import Command
from prompt_toolkit import prompt
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.styles import style_from_dict
from prompt_toolkit.token import Token
from pygments import highlight
from pygments.formatters.terminal import TerminalFormatter
from pygments.lexers.data import JsonLexer
from PyInquirer import prompt as pyinquirer_prompt

from belvo import __version__
from belvo.client import Client

from .completers import NestedCompleter
from .questions import create_questions, delete_questions, login_questions

style = style_from_dict({Token.Toolbar: "#000000 bg:#ffffff"})


def get_bottom_toolbar_tokens(cli):
    return [(Token.Toolbar, f"belvo-python::shell (version: {__version__})")]


class BelvoShellQuit(EOFError):
    pass


completer = NestedCompleter.from_nested_dict(
    {
        "GET": {
            "Links": {"id=": None},
            "Accounts": {"id=": None},
            "Transactions": {"id=": None},
            "Owners": {"id=": None},
        },
        "CREATE": {"Links": None, "Accounts": None, "Transactions": None, "Owners": None},
        "DELETE": {
            "Links": {"id=": None},
            "Accounts": {"id=": None},
            "Transactions": {"id=": None},
            "Owners": {"id=": None},
        },
        "quit": None,
        "help": None,
        "version": None,
    }
)


class ShellCommand(Command):
    """
    Interactive shell that allows you to use test the Belvo API

    shell
        {url : Belvo API URL}
    """

    def handle(self):
        url_arg = self.argument("url")
        answers = pyinquirer_prompt(login_questions)
        url = answers.pop("url", url_arg)
        client = Client(url=url, **answers)
        institutions = list(client.Institutions.list())
        history = InMemoryHistory()

        try:
            while True:
                try:
                    action = prompt(
                        "> ",
                        completer=completer,
                        get_bottom_toolbar_tokens=get_bottom_toolbar_tokens,
                        style=style,
                        history=history,
                        auto_suggest=AutoSuggestFromHistory(),
                    )
                except KeyboardInterrupt:
                    continue
                except EOFError:
                    break

                self.execute(action, client, institutions=institutions)
        except EOFError:
            self.line("\n👋 Goodbye\n")

    def execute(self, text: str, client: Client, institutions: List) -> None:
        commands = {
            "quit": self.quit,
            "help": self.help,
            "GET": self.get,
            "CREATE": self.create,
            "DELETE": self.delete,
        }
        action = text.split(" ")
        func = commands.get(action[0], self.dummy)
        try:
            resource = action[1]
        except IndexError:
            resource = ""

        try:
            filters = action[2]
        except IndexError:
            filters = ""

        func(client=client, resource=resource, filters=filters, institutions=institutions)

    def quit(self, *args, **kwargs) -> None:
        raise BelvoShellQuit()

    def help(self, *args, **kw) -> None:
        self.line(
            """\n
<fg=cyan;options=bold>help</>       Show this message
<fg=cyan;options=bold>quit</>       Quit from this shell
<fg=cyan;options=bold>version</>    Show installed belvo-python version
"""
        )

    def dummy(self, *args, **kw):
        self.line(
            "\n🤖 I don't know that command."
            "\nTry <fg=yellow>'help'</> if you want to see all commands available.\n"
        )

    def parse_args(self, args: str) -> Dict:
        res = {}
        for arg in args.split(";"):
            if arg:
                key, value = arg.split("=")
                res.update({key: value})
        return res

    def print_response(self, response: Union[List, Dict]) -> None:
        formatted_json = json.dumps(response, indent=2)
        highlighted = highlight(formatted_json, JsonLexer(), TerminalFormatter())
        self.line(highlighted)

    def get(self, client: Client, resource: str, filters: str = None, *args, **kwargs) -> None:
        obj = getattr(client, resource)
        parsed_filters = self.parse_args(filters)
        id = parsed_filters.pop("id", None)

        if id:
            response = obj.get(id=id, **parsed_filters)
            self.print_response(response)
        else:
            response = obj.list(**parsed_filters)
            self.print_response(list(response))

    def create(self, client: Client, resource: str, institutions: List, *args, **kwargs) -> None:
        obj = getattr(client, resource)
        answers = pyinquirer_prompt(create_questions(resource, institutions))
        response = obj.create(**answers)
        self.print_response(response)

    def delete(self, client: Client, resource: str, *args, **kwargs) -> None:
        obj = getattr(client, resource)
        answers = pyinquirer_prompt(delete_questions)
        continue_ = answers.pop("continue")
        if continue_:
            response = obj.delete(**answers)
            self.print_response(response)
