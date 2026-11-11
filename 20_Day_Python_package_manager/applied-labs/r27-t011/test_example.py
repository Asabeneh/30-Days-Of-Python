import os
from pathlib import Path
import subprocess
import sys
import unittest

from example import text_statistics


SAMPLE_TEXT = "one two two"
EXPECTED_STATISTICS = {
    "word_count": 3,
    "distinct_word_count": 2,
}


class TextStatisticsTests(unittest.TestCase):
    def test_sample_statistics_match_fixture(self):
        self.assertEqual(text_statistics(SAMPLE_TEXT), EXPECTED_STATISTICS)

    def test_empty_text_has_no_words(self):
        self.assertEqual(
            text_statistics(""),
            {"word_count": 0, "distinct_word_count": 0},
        )

    def test_import_succeeds_without_user_site_packages(self):
        lab_directory = Path(__file__).resolve().parent
        environment = os.environ.copy()
        environment["PYTHONNOUSERSITE"] = "1"
        result = subprocess.run(
            [
                sys.executable,
                "-s",
                "-c",
                (
                    "import site; "
                    "assert not site.ENABLE_USER_SITE; "
                    "from example import text_statistics; "
                    "print(text_statistics('one two two'))"
                ),
            ],
            cwd=lab_directory,
            env=environment,
            check=False,
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            result.stdout.strip(),
            "{'word_count': 3, 'distinct_word_count': 2}",
        )


if __name__ == "__main__":
    unittest.main()
