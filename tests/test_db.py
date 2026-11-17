import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from db import run_query
from safety import UnsafeSQLError


class TestRunQuerySafety(unittest.TestCase):
    def test_rejects_non_select(self):
        bad = [
            "DROP TABLE olist_orders_dataset",
            "DELETE FROM olist_orders_dataset",
            "SELECT 1; DROP TABLE olist_orders_dataset",
        ]
        for sql in bad:
            with self.subTest(sql=sql):
                with self.assertRaises(UnsafeSQLError):
                    run_query(sql)


if __name__ == "__main__":
    unittest.main()