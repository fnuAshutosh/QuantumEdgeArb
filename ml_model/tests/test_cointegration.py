import unittest
from ml_model.cointegration import KalmanFilter

class TestCointegration(unittest.TestCase):
    def test_train_simple(self):
        prices_a = [1,2,3,4,5]
        prices_b = [2,4,6,8,10]
        kf = KalmanFilter()
        res = kf.train(prices_a, prices_b)
        self.assertIn('coef', res)
        self.assertIn('pvalue', res)
        self.assertLessEqual(res['pvalue'], 1.0)

if __name__ == '__main__':
    unittest.main()
