import os

import anyscale.util

def report(message):
    """Show a message in the Anyscale Dashboard."""

    anyscale.util.send_json_request(
        "session_report_command",
        {"pid": os.getppid(), "message": message},
        post=True)

