from cleo import Command


class AboutCommand(Command):
    """
    Short information about belvo-python.
    about
    """

    def handle(self):
        self.line(
            """<info>Belvo - Bank Connectivity Simplified</info>
<comment>This is the Python SDK for Belvo API.
See <fg=blue>https://belvo.co</> for more information.</comment>
"""
        )
