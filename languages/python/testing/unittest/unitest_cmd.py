import unittest

@unittest.skip("demonstrating skipping")  # used this to skip tests . whole class is skipped
class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        # optional , this runs before running tests that starts with name "test_"
        self.widget = Widget('The widget')

    def tearDown(self):
        # optional , this runs after running tests that starts with name "test_"
        self.widget.dispose()
        self.widget = None

    def test_default_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')

## To run the test       /> python -m unittest unitest_cmd
