import unittest
from execution_engine.router import route_order
from execution_engine.risk import check_risk

class TestEngine(unittest.TestCase):
    def test_route(self):
        result = route_order({'symbol':'NVDA','qty':1})
        self.assertTrue(result)

    def test_risk(self):
        with self.assertRaises(Exception):
            check_risk(0.1)
        self.assertFalse(check_risk(0.01))

if __name__ == '__main__':
    unittest.main()
