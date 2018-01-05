# Python imports
import unittest
import time

# Local imports
from goldberg_app.src.utils.profiling import Stopwatch

# Third party imports

class StopwatchTest(unittest.TestCase):

    #@unittest.skip('Skipped.')
    def test_basic_behavior(self):

        ss_1 = Stopwatch()
        ss_1.start()

        ss_1.tic()
        time.sleep(0.5)
        ss_1.toc()

        ss_1.tic()
        time.sleep(0.5)
        ss_1.toc()

        tic_tocs = ss_1.tic_tocs

        self.assertEqual(2, len(tic_tocs))

        print('success...')


if __name__ == '__main__':

    unittest.main()