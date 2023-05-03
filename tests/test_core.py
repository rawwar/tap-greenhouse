"""Tests standard tap features using the built-in SDK tests library."""

import datetime

SAMPLE_CONFIG = {
    "start_date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"),
    "auth_token": "123",
}


# Run standard built-in tap tests from the SDK:
