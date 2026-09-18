"""Tests for shared icon and hero portrait asset downloading."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.parse import parse_qs, urlsplit

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

import download_hero_images as images  # noqa: E402


class PortraitAssetTests(unittest.TestCase):
    def test_portrait_validator_accepts_png_and_webp(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            directory = Path(temp)
            (directory / "PNG Hero.png").write_bytes(
                images.PNG_SIGNATURE + b"payload"
            )
            (directory / "WebP Hero.png").write_bytes(
                b"RIFF" + b"\x00\x00\x00\x00WEBPpayload"
            )

            self.assertTrue(images.portrait_is_valid("PNG Hero", directory))
            self.assertTrue(images.portrait_is_valid("WebP Hero", directory))

    def test_portrait_validator_reports_missing_and_invalid_assets(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            directory = Path(temp)
            (directory / "Broken.png").write_bytes(b"<html>not an image</html>")

            self.assertEqual(
                images.validate_portraits(
                    ["Missing", "Broken"],
                    directory,
                ),
                ["Missing", "Broken"],
            )

    def test_gallery_match_uses_display_name_or_alias(self) -> None:
        payload = {
            "query": {
                "pages": {
                    "1": {
                        "images": [
                            {"title": "File:Hero_Elijah_&_Lailah.png"},
                        ],
                    }
                }
            }
        }

        self.assertEqual(
            images._gallery_image_title(payload, ["Twins", "Elijah & Lailah"]),
            "File:Hero_Elijah_&_Lailah.png",
        )

    def test_fandom_image_url_requests_original_format(self) -> None:
        gallery = {
            "query": {
                "pages": {
                    "1": {
                        "images": [{"title": "File:Hero_Kazim.png"}],
                    }
                }
            }
        }
        imageinfo = {
            "query": {
                "pages": {
                    "2": {
                        "imageinfo": [
                            {
                                "url": (
                                    "https://static.wikia.nocookie.net/"
                                    "afk/images/hero.png?cb=123"
                                )
                            }
                        ]
                    }
                }
            }
        }

        def fake_get(url: str, **_: object) -> bytes:
            if "prop=images" in url:
                return json.dumps(gallery).encode()
            return json.dumps(imageinfo).encode()

        with patch.object(images, "_http_get", side_effect=fake_get):
            result = images._fandom_portrait_url("Kazim")

        assert result is not None
        query = parse_qs(urlsplit(result).query)
        self.assertEqual(query["format"], ["original"])

    def test_download_portrait_fetches_and_validates_image(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            directory = Path(temp)
            with patch.object(
                images,
                "_fandom_portrait_url",
                return_value="https://example.test/portrait",
            ), patch.object(
                images,
                "_http_get",
                return_value=images.PNG_SIGNATURE + b"payload",
            ):
                result = images.download_portrait("New Hero", [], directory)

            self.assertEqual(result, "downloaded")
            self.assertTrue(
                images.portrait_is_valid("New Hero", directory)
            )

    def test_download_portrait_reports_unavailable_source(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            with patch.object(
                images,
                "_fandom_portrait_url",
                return_value=None,
            ):
                result = images.download_portrait("New Hero", [], Path(temp))

            self.assertEqual(result, "missing")


if __name__ == "__main__":
    unittest.main()
