"""Tests standard tap features using the built-in SDK tests library."""

import datetime

from singer_sdk.testing import get_tap_test_class

from tap_greenhouse.tap import Tapgreenhouse

SAMPLE_CONFIG = {
    "start_date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"),
    "auth_token": "123",
}


# Run standard built-in tap tests from the SDK:
TestTapgreenhouse = get_tap_test_class(
    tap_class=Tapgreenhouse,
    config=SAMPLE_CONFIG,
)
