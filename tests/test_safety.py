import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from safety import check_sql, UnsafeSQLError


class TestCheckSql(unittest.TestCase):
    def test_allowed(self):
        good = [
            "SELECT 1",
            "SELECT 1;",
            "SELECT created_at FROM orders",
            "SELECT replace(city, '-', ' ') FROM customers",
            "SELECT city, count(*) FROM customers GROUP BY city",
            "SELECT * FROM a JOIN b ON a.id = b.a_id",
            "WITH t AS (SELECT 1 AS x) SELECT * FROM t",
            "SELECT 1 UNION SELECT 2",
            "SELECT 1 UNION ALL SELECT 2",
        ]
        for sql in good:
            with self.subTest(sql=sql):
                check_sql(sql)

    def test_rejected(self):
        bad = [
            "DROP TABLE orders",
            "DELETE FROM orders",
            "UPDATE orders SET x = 1",
            "INSERT INTO orders VALUES (1)",
            "PRAGMA writable_schema = 1",
            "ATTACH DATABASE 'x.db' AS x",
            "SELECT 1; DROP TABLE orders",
            "SELECT 1; SELECT 2",
            "SELECT 1 UNION SELECT 2; DROP TABLE orders",
            "WITH t AS (SELECT 1) DELETE FROM orders",
            "dRoP tAbLe orders",
            "",
            "Sorry, I can't help with that.",
        ]
        for sql in bad:
            with self.subTest(sql=sql):
                with self.assertRaises(UnsafeSQLError):
                    check_sql(sql)


if __name__ == "__main__":
    unittest.main()