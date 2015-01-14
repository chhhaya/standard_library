import unittest

# 一些test只有很小的改变，比如参数不同，可以用subTest
# 这里如果不用subTest的话，i=1的时候就失败退出了
class NumbersTest(unittest.TestCase):
    def test_even(self):
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)
    def test_od(self):
        self.assertGreater(3, 4)

unittest.main()