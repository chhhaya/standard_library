import unittest
from widget import Widget

class DefaultWidgetSizeTestCase(unittest.TestCase):
    def test_default_widget_size(self):
        widget = Widget('The widget')
        self.assertEqual(widget.size(), (50, 50))

class DefaultWidgetSizeTestCase2(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The Widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50, 50), 'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100, 150)
        self.assertEqual(self.widget.size(), (100, 150), 'wrong size after resize')


# TODO 如何使用？
def suite():
    suite = unittest.TestSuite()
    suite.addTest(DefaultWidgetSizeTestCase2('test_default_widget_size'))
    suite.addTest(DefaultWidgetSizeTestCase2('test_widget_resize'))
    return suite

if __name__ == '__main__':
    unittest.main()