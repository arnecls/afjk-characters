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

    def test_assumed_file_name_is_tried_before_gallery(self) -> None:
        calls: list[str] = []
        imageinfo = {
            "query": {
                "pages": {
                    "1": {
                        "imageinfo": [
                            {"url": "https://static.wikia.nocookie.net/a.png"}
                        ]
                    }
                }
            }
        }

        def fake_get(url: str, **_: object) -> bytes:
            calls.append(url)
            return json.dumps(imageinfo).encode()

        with patch.object(images, "_http_get", side_effect=fake_get):
            result = images._fandom_portrait_url("Aster")

        assert result is not None
        self.assertEqual(len(calls), 1)
        self.assertIn("Hero+Aster.png", calls[0])
        self.assertNotIn("prop=images", calls[0])

    def test_gallery_lookup_used_when_assumed_name_missing(self) -> None:
        gallery = {
            "query": {"pages": {"1": {"images": [
                {"title": "File:Hero Odd.png"}
            ]}}}
        }
        found = {
            "query": {"pages": {"2": {"imageinfo": [
                {"url": "https://static.wikia.nocookie.net/o.png"}
            ]}}}
        }

        def fake_get(url: str, **_: object) -> bytes:
            if "prop=images" in url:
                return json.dumps(gallery).encode()
            if "Hero+Odd.png" in url:
                return json.dumps(found).encode()
            return b"{}"

        with patch.object(images, "_http_get", side_effect=fake_get):
            self.assertIsNotNone(images._fandom_portrait_url("Odd"))

    def test_cdn_requests_send_fandom_referer(self) -> None:
        seen: dict[str, str] = {}

        class Resp:
            def __enter__(self):
                return self

            def __exit__(self, *_):
                return False

            def read(self) -> bytes:
                return b"x"

        def fake_open(req, timeout=0):
            seen.update(req.headers)
            return Resp()

        with patch.object(images.urllib.request, "urlopen", fake_open):
            images._http_get(
                "https://static.wikia.nocookie.net/afk-journey/x.png"
            )

        self.assertEqual(seen.get("Referer"), images.FANDOM_REFERER)

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
