# This script is a QC implementation of the two population Tennessen Out Of Africa model
import msprime
import numpy as np
import math
import stdpopsim.models as models


class TennessenOnePopAfrica(models.DemographicModel):
    def __init__(self):
        # This model is the same as the Tennessen two population model except
        # the European population has been removed.

        # Since the Tennessen one population model largely uses parameters from
        # the Gravel et al 2001, we begin by taking the maximum likelihood value
        # from the table 2 of Gravel et al. 2011 using the Low-coverage + exons
        # data. Initially we copy over the pre- exponential growth population
        # size estimates, migration rates, and epoch times:
        generation_time = 25

        N_A = 7310  # Ancient population size
        N_AF0 = 14474  # Pre-modern african population size (pre and post OOA)

        T_AF = 148000 / generation_time  # Epoch transition from ancient to AF0
        T_AG = 5115 / generation_time  # start of 2nd european growth epoch

        # Next we include the additional parameters from Tennessen et al 2012
        # which include all exponential growth rates. These parameters are
        # copied from the section titled "Abundance of rare variation explained
        # by human demographic history" in Tennessen et al.

        r_AF0 = 1.66e-2  # The growth rate for the 1st african expansion

        # For the post exponenential growth popuation sizes we can calcuate the
        # population sizes at the start of the epoch using the formula f(t) =
        # x_0 * exp(r * (t_0-t))

        # African population size after 1st expansion
        N_AF1 = N_AF0 * math.exp(r_AF0 * T_AG)

        # Now we set up the population configurations. The population IDs are 0=YRI. This
        # includes both the inital sizes, growth rates, and migration rates.
        self.population_configurations = [
            msprime.PopulationConfiguration(
                initial_size=N_AF1, growth_rate=r_AF0),
        ]

        self.migration_matrix = [[0]]

        # Now we add the demographic events working backwards in time. Starting with the
        # growth slowdown in Europeans and the transition to a fixed population size in
        # Africans.
        self.demographic_events = [
            # Reversion to fixed population size in Africans
            msprime.PopulationParametersChange(
                time=T_AG, initial_size=N_AF0, growth_rate=0, population_id=0),
            # Change to ancestral population size pre OOA
            msprime.PopulationParametersChange(
                time=T_AF, initial_size=N_A, population_id=0)
        ]


class TennessenTwoPopOutOfAfrica(models.DemographicModel):
    def __init__(self):
        # Since the Tennessen two population model largely uses parameters from
        # the Gravel et al 2001, we begin by taking the maximum likelihood
        # value from the table 2 of Gravel et al. 2011 using the Low-coverage +
        # exons data. We ignore all values related to the asian (AS) population
        # as it is not present in the Tennessen two population model. Initially
        # we copy over the pre- exponential growth population size estimates,
        # migration rates, and epoch times:
        generation_time = 25

        N_A = 7310  # Ancient population size
        N_AF0 = 14474  # Pre-modern african population size (pre and post OOA)
        N_B = 1861  # OOA population size, pre-expansion
        N_EU0 = 1032  # European population size, pre-expansion

        m_AF0_B = 15e-5  # migration from pre-expansion africa to pre-expansion OOA
        m_AF1_EU1 = 2.5e-5  # migration from pre-expansion africa to 2nd-expansion euro

        T_AF = 148000 / generation_time  # Epoch transition from ancient to AF0
        T_B = 51000 / generation_time  # OOA time
        # The european asian split time, begins 1st growth period
        T_EU_AS = 23000 / generation_time

        # Next we include the additional parameters from Tennessen et al 2012
        # which include all exponential growth rates and the time of the second
        # round of growth in the European population/first round in the African
        # population. These parameters are copied from the section titled
        # "Abundance of rare variation explained by human demographic history"
        # in Tennessen et al.
        r_EU0 = 0.307e-2  # The growth rate for the 1st european expansion
        r_EU1 = 1.95e-2  # The growth rate for the 2nd european expansion
        r_AF0 = 1.66e-2  # The growth rate for the 1st african expansion

        T_AG = 5115 / generation_time  # start of 2nd european growth epoch

        # For the post exponenential growth popuation sizes we can calcuate the
        # population sizes at the start of the epoch using the formula
        # f(t) = x_0 * exp(r * (t_0-t)) European population size after 1st expansion
        N_EU1 = N_EU0 * math.exp(r_EU0 * (T_EU_AS-T_AG))
        # European population size after 2nd expansion
        N_EU2 = N_EU1 * math.exp(r_EU1 * T_AG)
        # African population size after 1st expansion
        N_AF1 = N_AF0 * math.exp(r_AF0 * T_AG)

        # Now we set up the population configurations. The population IDs are
        # 0=CEU and 1=YRI. This includes both the inital sizes, growth rates,
        # and migration rates.
        self.population_configurations = [
            msprime.PopulationConfiguration(
                initial_size=N_AF1, growth_rate=r_AF0),
            msprime.PopulationConfiguration(
                initial_size=N_EU2, growth_rate=r_EU1)
        ]
        self.migration_matrix = [
            [0, m_AF1_EU1],
            [m_AF1_EU1,       0],
        ]

        # Now we add the demographic events working backwards in time. Starting
        # with the growth slowdown in Europeans and the transition to a fixed
        # population size in Africans.
        self.demographic_events = [
            # Set the migration rate for 1st CEU growth period (for now stays same)
            msprime.MigrationRateChange(
                time=T_AG, rate=m_AF1_EU1, matrix_index=(0, 1)),
            msprime.MigrationRateChange(
                time=T_AG, rate=m_AF1_EU1, matrix_index=(1, 0)),
            # Growth slowdown in Europeans
            msprime.PopulationParametersChange(
                time=T_AG, initial_size=N_EU1, growth_rate=r_EU0, population_id=1),
            # Reversion to fixed population size in Africans
            msprime.PopulationParametersChange(
                time=T_AG, initial_size=N_AF0, growth_rate=0, population_id=0),
            # Set the migration rate for pre CEU/CHB split
            msprime.MigrationRateChange(
                time=T_EU_AS, rate=m_AF0_B, matrix_index=(0, 1)),
            msprime.MigrationRateChange(
                time=T_EU_AS, rate=m_AF0_B, matrix_index=(1, 0)),
            # Reversion to fixed population size at the time of the CHB/CEU split
            msprime.PopulationParametersChange(
                time=T_EU_AS, initial_size=N_B, growth_rate=0, population_id=1),
            # Coalescence between the OOA and YRI pops
            msprime.MassMigration(
                time=T_B, source=1, destination=0, proportion=1.0),
            # Change to ancestral population size pre OOA
            msprime.PopulationParametersChange(
                time=T_AF, initial_size=N_A, population_id=0)
        ]


class BrowningAmerica(models.DemographicModel):
    def __init__(self):
        # Parameters are taken from the Methods - Simulated data section
        # Population sizes
        N_AF0 = 7310  # Initial african population size
        N_AF1 = 14474  # Second african pop. size
        N_OOA = 1861  # OOA population size
        N_CEU0 = 1032  # European population size at CEU/CHB split
        N_CHB0 = 554  # Asian population size at CEU/CHB split
        N_ADMIX0 = 30000  # Initial size of admixed population

        # Epoch times
        T_AF0_AF1 = 5920  # initial increase in african pop. size
        T_AF1_OOA = 2040  # Time of OOA event
        T_CEU_CHB = 920  # Time of european/asian split
        T_ADMIX0 = 12

        # Migration rates
        m_AF1_OOA = 1.5e-4  # Bidirectional migration rate between african and OOA pops.
        m_AF1_CEU0 = 2.5e-5  # Migration rates between AF1 and CEU0
        m_AF1_CHB0 = 7.8e-6  # Migration rates between AF1 and CHB0
        m_CEU0_CHB0 = 3.11e-5  # Migration rates between CEU0 and CHB0

        # Mass migration to create admixed populations
        mm_AF1 = 1/6
        # Adjusted fraction for remaining population after AF migration (5/6 * 2/5 = 1/3)
        mm_CEU0 = 2/5
        # Adjusted fraction for remaining population (1/2 * 1 = 1/2)
        mm_CHB0 = 1.0

        # Growth rates
        r_CEU0 = 3.8e-3
        r_CHB0 = 4.8e-3
        r_ADMIX0 = 0.05

        # Calculate population sizes at modern (T=0) time
        N_CEU1 = N_CEU0 * math.exp(r_CEU0 * T_CEU_CHB)
        N_CHB1 = N_CHB0 * math.exp(r_CHB0 * T_CEU_CHB)
        N_ADMIX1 = N_ADMIX0 * math.exp(r_ADMIX0 * T_ADMIX0)

        # Set population sizes at T=0
        # pop0 is Africa, pop1 is Europe, pop2 is Asia, pop3 is admixed
        self.population_configurations = [
            msprime.PopulationConfiguration(
                initial_size=N_AF1, growth_rate=0),
            msprime.PopulationConfiguration(
                initial_size=N_CEU1, growth_rate=r_CEU0),
            msprime.PopulationConfiguration(
                initial_size=N_CHB1, growth_rate=r_CHB0),
            msprime.PopulationConfiguration(
                initial_size=N_ADMIX1, growth_rate=r_ADMIX0)
        ]

        # Migration matrix, all migrations to admixed population are 0
        self.migration_matrix = [
            [0, m_AF1_CEU0, m_AF1_CHB0, 0],
            [m_AF1_CEU0, 0, m_CEU0_CHB0, 0],
            [m_AF1_CHB0, m_CEU0_CHB0, 0, 0],
            [0, 0, 0, 0]
        ]

        # Now we add the demographic events working backwards in time.
        self.demographic_events = [
            # Admixed population recoalesces with origin populations (T_ADMIX0)
            msprime.MassMigration(
                time=T_ADMIX0, source=3, destination=0, proportion=mm_AF1),
            msprime.MassMigration(
                time=T_ADMIX0 + 0.0001, source=3, destination=1, proportion=mm_CEU0),
            msprime.MassMigration(
                time=T_ADMIX0 + 0.0002, source=3, destination=2, proportion=mm_CHB0),
            # Zero out migration rate (desn't matter but added for equality to prod.)
            msprime.MigrationRateChange(
                time=T_CEU_CHB, rate=0.0),
            # CEU and CHB coalesce and set population to OOA size (T_CEU_CHB)
            msprime.MassMigration(
                time=T_CEU_CHB+0.0001, source=2, destination=1, proportion=1.0),
            msprime.PopulationParametersChange(
                time=T_CEU_CHB+0.0002, initial_size=N_OOA, growth_rate=0.0,
                population_id=1),
            # Set OOA <--> AF migration rate (T_CEU_CHB)
            msprime.MigrationRateChange(
                time=T_CEU_CHB+0.0003, rate=m_AF1_OOA, matrix_index=(0, 1)),
            msprime.MigrationRateChange(
                time=T_CEU_CHB+0.0003, rate=m_AF1_OOA, matrix_index=(1, 0)),
            # Zero out migration rate (desn't matter but added for equality to prod.)
            msprime.MigrationRateChange(
                time=T_AF1_OOA, rate=0.0),
            # OOA and AF1 coalesce (T_OOA)
            msprime.MassMigration(
                time=T_AF1_OOA+0.0001, source=1, destination=0, proportion=1.0),
            # AF1 -> AF0 population size change (T_AF0_AF1)
            msprime.PopulationParametersChange(
                time=T_AF0_AF1, initial_size=N_AF0, population_id=0),
        ]


class RagsdaleArchaic(models.DemographicModel):
    def __init__(self):

        # All parameters were taken from table 1 of Ragsdale et al. (2019)
        generation_time = 29

        # Population sizes
        N_0 = 3600  # Size of archaic populations
        N_YRI = 13900  # Fixed size of YRI population
        N_B = 880  # Size of OOA population
        N_CEU0 = 2300  # Size of CEU population at CEU-CHB split
        N_CHB0 = 650  # Size of CHB population at CEU-CHB split

        # Population growth parameters
        r_CEU = 0.125e-2
        r_CHB = 0.372e-2

        # Migration parameters
        m_AF_B = 52.2e-5
        m_YRI_CEU = 2.48e-5
        m_YRI_CHB = 0
        m_CEU_CHB = 11.3e-5
        m_AF_ARCHAF = 1.98e-5
        m_OOA_NEAN = 0.825e-5

        # Epoch times
        T_AF = 300e3/generation_time
        T_OOA = 60.7e3/generation_time
        T_CEU_CHB = 36e3/generation_time
        T_ARCHAF_split = 499e3/generation_time
        T_ARCHAF_mig = 125e3/generation_time
        T_NEAN_split = 559e3/generation_time
        T_ARCH_ADMIX_end = 18.7e3/generation_time

        # Calculate population sizes at modern (T=0) time
        N_CEU1 = N_CEU0 * math.exp(r_CEU * T_CEU_CHB)
        N_CHB1 = N_CHB0 * math.exp(r_CHB * T_CEU_CHB)

        # Set population sizes at T=0
        # pop0 is Africa, pop1 is Europe, pop2 is Asia, pop3 is Neanderthal, pop4 is
        # archaic african
        self.population_configurations = [
            msprime.PopulationConfiguration(
                initial_size=N_YRI, growth_rate=0),
            msprime.PopulationConfiguration(
                initial_size=N_CEU1, growth_rate=r_CEU),
            msprime.PopulationConfiguration(
                initial_size=N_CHB1, growth_rate=r_CHB),
            msprime.PopulationConfiguration(
                initial_size=N_0, growth_rate=0),
            msprime.PopulationConfiguration(
                initial_size=N_0, growth_rate=0)
        ]

        # Setup initial migration matrix
        self.migration_matrix = [
            [0,         m_YRI_CEU,  m_YRI_CHB, 0, 0], # noqa
            [m_YRI_CEU, 0,          m_CEU_CHB, 0, 0], # noqa
            [m_YRI_CHB, m_CEU_CHB,  0,         0, 0], # noqa
            [0,         0,          0,         0, 0], # noqa
            [0,         0,          0,         0, 0] # noqa
        ]

        self.demographic_events = [
            # Migration between YRI and ARCHAF(E1)
            msprime.MigrationRateChange(
                time=T_ARCH_ADMIX_end, rate=m_AF_ARCHAF, matrix_index=(0, 4)),
            msprime.MigrationRateChange(
                time=T_ARCH_ADMIX_end, rate=m_AF_ARCHAF, matrix_index=(4, 0)),
            # Migration between CEU and NEAN(E1)
            msprime.MigrationRateChange(
                time=T_ARCH_ADMIX_end, rate=m_OOA_NEAN, matrix_index=(1, 3)),
            msprime.MigrationRateChange(
                time=T_ARCH_ADMIX_end, rate=m_OOA_NEAN, matrix_index=(3, 1)),
            # Migration between CHB and NEAN(E1)
            msprime.MigrationRateChange(
                time=T_ARCH_ADMIX_end, rate=m_OOA_NEAN, matrix_index=(2, 3)),
            msprime.MigrationRateChange(
                time=T_ARCH_ADMIX_end, rate=m_OOA_NEAN, matrix_index=(3, 2)),
            # Coalescence of CHB into CEU (E2)
            msprime.MassMigration(
                time=T_CEU_CHB, source=2, dest=1, proportion=1.0),
            # Reset migration rates (E2)(redundant)*
            msprime.MigrationRateChange(
                time=T_CEU_CHB, rate=0.0),
            # Migration rate change between OOA(CEU) and AF(YRI)(E2)
            msprime.MigrationRateChange(
                time=T_CEU_CHB, rate=m_AF_B, matrix_index=(0, 1)),
            msprime.MigrationRateChange(
                time=T_CEU_CHB, rate=m_AF_B, matrix_index=(1, 0)),
            # Migration between YRI and ARCHAF (E2)(redundant without mig. rate reset)*
            msprime.MigrationRateChange(
                time=T_CEU_CHB, rate=m_AF_ARCHAF, matrix_index=(0, 4)),
            msprime.MigrationRateChange(
                time=T_CEU_CHB, rate=m_AF_ARCHAF, matrix_index=(4, 0)),
            # Migration between CEU and NEAN (E2)(redundant without mig. rate reset)*
            msprime.MigrationRateChange(
                time=T_CEU_CHB, rate=m_OOA_NEAN, matrix_index=(1, 3)),
            msprime.MigrationRateChange(
                time=T_CEU_CHB, rate=m_OOA_NEAN, matrix_index=(3, 1)),
            # CEU change to fixed population size at the time of the CHB/CEU coal. (E2)
            msprime.PopulationParametersChange(
                time=T_CEU_CHB, initial_size=N_B, growth_rate=0, population_id=1),
            # Coalescence between the OOA and AF pops (E3)
            msprime.MassMigration(
                time=T_OOA, source=1, destination=0, proportion=1.0),
            # Reset migration rates (E3)
            msprime.MigrationRateChange(
                time=T_OOA, rate=0.0),
            # Migration between YRI and ARCHAF (E3)
            msprime.MigrationRateChange(
                time=T_OOA, rate=m_AF_ARCHAF, matrix_index=(0, 4)),
            msprime.MigrationRateChange(
                time=T_OOA, rate=m_AF_ARCHAF, matrix_index=(4, 0)),
            # Migration between archaic african and african pop. "ends" (E4)
            msprime.MigrationRateChange(
                time=T_ARCHAF_mig, rate=0),
            # AF reverts to ancestral population size pre OOA (E5)
            msprime.PopulationParametersChange(
                time=T_AF, initial_size=N_0, population_id=0),
            # Archaic AF population coalesces into AF (E6)
            msprime.MassMigration(
                time=T_ARCHAF_split, source=4, dest=0, proportion=1.0),
            # NEAN pop. coalesces into AF (E7)
            msprime.MassMigration(
                time=T_NEAN_split, source=3, dest=0, proportion=1.0)
        ]


class KammAncientSamples(models.DemographicModel):
    """
    Demographic inferred by momi described in Kamm et al. (2019). The model is
    illustrated in Figure 3, with parameters given in Table 2.
    """
    def __init__(self):

        generation_time = 25

        # population sizes
        N_Losch = 1.92e3
        N_Mbu = 1.73e4
        N_Mbu_Losch = 2.91e4
        N_Han = 6.3e3
        N_Han_Losch = 2.34e3
        N_Nean_Losch = 1.82e4
        N_Nean = 86.9
        N_LBK = 75.7
        N_Sard = 1.5e4
        N_Sard_LBK = 1.2e4

        # unknown population sizes
        # these should be set to ancestral Eurasian population size,
        # but at the moment it's unclear to me if that is N_Han_Losch? N_Losch?
        N_Basal = N_Losch
        N_Ust = N_Basal
        N_MA1 = N_Basal

        # population merge times in years, divided by generation time
        t_Mbu_Losch = 9.58e4 / generation_time
        t_Han_Losch = 5.04e4 / generation_time
        t_Ust_Losch = 5.15e4 / generation_time
        t_Nean_Losch = 6.96e5 / generation_time
        t_MA1_Losch = 4.49e4 / generation_time
        t_LBK_Losch = 3.77e4 / generation_time
        t_Basal_Losch = 7.98e4 / generation_time
        t_Sard_LBK = 7.69e3 / generation_time
        # t_GhostWHG_Losch = 1.56e3 / generation_time

        # pulse admixture times and fractions
        p_Nean_to_Eur = 0.0296
        t_Nean_to_Eur = 5.68e4 / generation_time
        p_Basal_to_EEF = 0.0936
        t_Basal_to_EEF = 3.37e4 / generation_time
        p_GhostWHG_to_Sard = 0.0317
        t_GhostWHG_to_Sard = 1.23e3 / generation_time

        # sample_times (in years), divided by estimated generation time
        t_Mbuti = 0
        t_Han = 0
        t_Sardinian = 0
        t_Loschbour = 7.5e3 / generation_time
        t_LBK = 8e3 / generation_time
        t_MA1 = 24e3 / generation_time
        t_UstIshim = 45e3 / generation_time
        t_Altai = 50e3 / generation_time

        # set up populations
        self.population_configurations = [
            msprime.PopulationConfiguration(  # Mbuti
                initial_size=N_Mbu, growth_rate=0,
                metadata={"name": "Mbuti", "sampling_time": t_Mbuti}),
            msprime.PopulationConfiguration(  # LBK
                initial_size=N_LBK, growth_rate=0,
                metadata={"name": "LBK", "sampling_time": t_LBK}),
            msprime.PopulationConfiguration(  # Sardinian
                initial_size=N_Sard, growth_rate=0,
                metadata={"name": "Sardinian", "sampling_time": t_Sardinian}),
            msprime.PopulationConfiguration(  # Loschbour
                initial_size=N_Losch, growth_rate=0,
                metadata={"name": "Loschbour", "sampling_time": t_Loschbour}),
            msprime.PopulationConfiguration(  # MA1
                initial_size=N_MA1, growth_rate=0,
                metadata={"name": "MA1", "sampling_time": t_MA1}),
            msprime.PopulationConfiguration(  # Han
                initial_size=N_Han, growth_rate=0,
                metadata={"name": "Han", "sampling_time": t_Han}),
            msprime.PopulationConfiguration(  # UstIshim
                initial_size=N_Ust, growth_rate=0,
                metadata={"name": "UstIshim", "sampling_time": t_UstIshim}),
            msprime.PopulationConfiguration(  # Neanderthal
                initial_size=N_Nean, growth_rate=0,
                metadata={"name": "Altai", "sampling_time": t_Altai}),
            msprime.PopulationConfiguration(  # Basal Eurasian
                initial_size=N_Basal, growth_rate=0,
                metadata={"name": "Basal", "sampling_time": -1})
        ]

        # no migration rates, only pulse events, so set mig mat to zeros
        num_pops = len(self.population_configurations)
        self.migration_matrix = [[0] * num_pops] * num_pops

        # Compute Neanderthal pop size decline rate
        # I'm assuming that the N_Nean is the size of Neanderthal population
        # at the time of sampling the Altai individual
        r_Nean = -np.log(N_Nean_Losch/N_Nean) / (t_Mbu_Losch-t_Altai)

        # Using columns in figure in Kamm paper as proxies for pop number
        self.demographic_events = [
            msprime.MassMigration(
                time=t_GhostWHG_to_Sard, source=2,
                destination=3, proportion=p_GhostWHG_to_Sard),
            msprime.MassMigration(
                time=t_Sard_LBK, source=2, destination=1,
                proportion=1.),
            msprime.PopulationParametersChange(
                time=t_Sard_LBK, initial_size=N_Sard_LBK,
                population_id=1),
            msprime.MassMigration(
                time=t_Basal_to_EEF, source=1, destination=8,
                proportion=p_Basal_to_EEF),
            msprime.MassMigration(
                time=t_LBK_Losch, source=1, destination=3,
                proportion=1.),
            msprime.MassMigration(
                time=t_MA1_Losch, source=4, destination=3,
                proportion=1.),
            msprime.PopulationParametersChange(
                time=t_Altai, initial_size=N_Nean,
                growth_rate=r_Nean, population_id=7),
            msprime.MassMigration(
                time=t_Han_Losch, source=5, destination=3,
                proportion=1.),
            msprime.PopulationParametersChange(
                time=t_Han_Losch, initial_size=N_Han_Losch,
                population_id=3),
            msprime.MassMigration(
                time=t_Ust_Losch, source=6, destination=3,
                proportion=1.),
            msprime.MassMigration(
                time=t_Nean_to_Eur, source=3, destination=7,
                proportion=p_Nean_to_Eur),
            msprime.MassMigration(
                time=t_Basal_Losch, source=8, destination=3,
                proportion=1.),
            msprime.MassMigration(
                time=t_Mbu_Losch, source=0, destination=3,
                proportion=1.),
            msprime.PopulationParametersChange(
                time=t_Mbu_Losch, initial_size=N_Mbu_Losch,
                population_id=3),
            msprime.PopulationParametersChange(
                time=t_Mbu_Losch, initial_size=N_Nean_Losch,
                growth_rate=0, population_id=7),
            msprime.MassMigration(
                time=t_Nean_Losch, source=7, destination=3,
                proportion=1.),
            msprime.PopulationParametersChange(
                time=t_Nean_Losch, initial_size=N_Nean_Losch,
                population_id=3)
        ]
