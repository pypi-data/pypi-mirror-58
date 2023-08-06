import unittest

import stdpopsim
from tests import test_models
from tests import test_species
from qc import arabidopsis_thaliana_qc


class TestSpecies(unittest.TestCase, test_species.SpeciesTestMixin):
    species = stdpopsim.get_species("AraTha")

    def test_basic_attributes(self):
        self.assertEqual(self.species.population_size, 10**4)
        self.assertEqual(self.species.generation_time, 1)


class TestGenome(unittest.TestCase, test_species.GenomeTestMixin):
    """
    Tests for the arabidopsis_thaliana genome.
    """
    genome = stdpopsim.get_species("AraTha").genome

    def test_basic_attributes(self):
        self.assertEqual(len(self.genome.chromosomes), 5)

    def test_chromosome_lengths(self):
        genome = self.genome
        self.assertEqual(genome.get_chromosome("chr1").length, 30427671)
        self.assertEqual(genome.get_chromosome("chr2").length, 19698289)
        self.assertEqual(genome.get_chromosome("chr3").length, 23459830)
        self.assertEqual(genome.get_chromosome("chr4").length, 18585056)
        self.assertEqual(genome.get_chromosome("chr5").length, 26975502)


species = stdpopsim.get_species("AraTha")


class TestDurvasula2017MSMC(
        unittest.TestCase, test_models.QcdCatalogDemographicModelTestMixin):
    """
    Basic tests for the Durvasula MSMC model.
    """
    model = species.get_demographic_model("SouthMiddleAtlas_1D17")
    qc_model = arabidopsis_thaliana_qc.Durvasula2017MSMC()


class TestHuberTwoEpoch(
        unittest.TestCase, test_models.QcdCatalogDemographicModelTestMixin):
    """
    Basic tests for the Huber et al. two epoch model.
    """
    model = species.get_demographic_model("African2Epoch_1H18")
    qc_model = arabidopsis_thaliana_qc.HuberTwoEpoch()


class TestHuberThreeEpoch(
        unittest.TestCase, test_models.QcdCatalogDemographicModelTestMixin):
    """
    Basic tests for the Huber three epoch model.
    """
    model = species.get_demographic_model("African3Epoch_1H18")
    qc_model = arabidopsis_thaliana_qc.HuberThreeEpoch()
