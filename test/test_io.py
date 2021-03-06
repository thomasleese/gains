from pathlib import Path
from unittest import TestCase

from gains.io import FitbodLoader


class TestFitbodLoader(TestCase):

    data_filename = Path(__file__).parent / "data.csv"

    def test_loading_data(self):
        loader = FitbodLoader(self.data_filename)
        analysis = loader.analysis

        exercises = analysis.exercises

        self.assertEqual(len(exercises), 890)
        self.assertEqual(exercises[3].average_weight, 38.5)
