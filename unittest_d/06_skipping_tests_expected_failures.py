import unittest
import sys
import widget

# 各种忽略

class MyTestCase(unittest.TestCase):
    @unittest.skip("demonstrating skipping")  # 无条件skip
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(widget.__version__ < (1, 4),
                     "not supported in this library version")  # 如果什么skip
    def test_format(self):
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "Requires Windows")  # 除非什么才不skip
    def test_windows_support(self):
        pass

@unittest.skip("Showing class skipping")
class MySkippedTestCase(unittest.TestCase):
    def test_not_run(self):
        pass

# 自定义skip装饰器
def skipUnlessHasattr(obj, attr):
    if hasattr(obj, attr):
        return lambda func: func
    return unittest.skip("{!r} doesn't have {!r}".format(obj, attr))


class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure    # 希望它测试不通过
    def test_fail(self):
        self.assertEqual(1, 0, "broken")

    # @skipUnlessHasattr(dict, "update")  # 这个不skip
    @skipUnlessHasattr(list, "add")  # 这个skip
    def test_diy_skip(self):
        self.assertEqual(1, 0, "broken")



unittest.main()
