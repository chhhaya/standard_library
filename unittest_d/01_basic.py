import random
import unittest

class TestSequenceFunctions(unittest.TestCase):
    # 在每个test之前运行
    def setUp(self):
        # print('(test start)')
        self.seq = list(range(10))

    # 在每个test之后运行
    def tearDown(self):
        # print('(test end)')
        pass
    # 所有test之前运行
    @classmethod
    def setUpClass(cls):
        cls.__connection = "xxx"
        print('setup class')
    # 所有test之后运行
    @classmethod
    def tearDownClass(cls):
        cls.__connection = 'xxx'
        print('teardown class')

    def test_shuffle(self):
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, list(range(10)))

        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)

if __name__ == '__main__':
    unittest.main(verbosity=2)

# 运行时带 -v参数，可看到更多输出
# > python 01_basic.py -v
# test_choice (__main__.TestSequenceFunctions) ... ok
# test_sample (__main__.TestSequenceFunctions) ... ok
# test_shuffle (__main__.TestSequenceFunctions) ... ok
#
# ----------------------------------------------------------------------
# Ran 3 tests in 0.001s