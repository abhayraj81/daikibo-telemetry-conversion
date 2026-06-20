import json
import unittest
from datetime import datetime, timezone


def convert_from_format_1(json_object):
    location_parts = json_object["location"].split("/")

    return {
        "deviceID": json_object["deviceID"],
        "deviceType": json_object["deviceType"],
        "timestamp": json_object["timestamp"],
        "location": {
            "country": location_parts[0],
            "city": location_parts[1],
            "area": location_parts[2],
            "factory": location_parts[3],
            "section": location_parts[4]
        },
        "data": {
            "status": json_object["operationStatus"],
            "temperature": json_object["temp"]
        }
    }


def convert_from_format_2(json_object):
    timestamp = int(
        datetime.strptime(
            json_object["timestamp"],
            "%Y-%m-%dT%H:%M:%S.%fZ"
        ).replace(tzinfo=timezone.utc).timestamp() * 1000
    )

    return {
        "deviceID": json_object["device"]["id"],
        "deviceType": json_object["device"]["type"],
        "timestamp": timestamp,
        "location": {
            "country": json_object["country"],
            "city": json_object["city"],
            "area": json_object["area"],
            "factory": json_object["factory"],
            "section": json_object["section"]
        },
        "data": {
            "status": json_object["data"]["status"],
            "temperature": json_object["data"]["temperature"]
        }
    }


def transform_telemetry(json_object):
    if "device" in json_object:
        return convert_from_format_2(json_object)

    return convert_from_format_1(json_object)


class TestTelemetryTransformation(unittest.TestCase):

    def setUp(self):
        with open("data-1.json", "r", encoding="utf-8") as file:
            self.data_1 = json.load(file)

        with open("data-2.json", "r", encoding="utf-8") as file:
            self.data_2 = json.load(file)

        with open("data-result.json", "r", encoding="utf-8") as file:
            self.expected = json.load(file)

    def test_format_1_conversion(self):
        self.assertEqual(
            transform_telemetry(self.data_1),
            self.expected
        )

    def test_format_2_conversion(self):
        self.assertEqual(
            transform_telemetry(self.data_2),
            self.expected
        )


if __name__ == "__main__":
    unittest.main()