# Python imports
import unittest

# Local imports
from goldberg_app.src.utils.profiling import Stopwatch
from goldberg_app.src.io.datamap import Datamap

# Third party imports

class DatamapReadTests(unittest.TestCase):

    #@unittest.skip('Skipped.')
    def test_read_template(self):
        data = Datamap(template="Template_FooBarBaz.xlsx")


if __name__ == '__main__':

    unittest.main()