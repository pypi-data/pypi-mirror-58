"""
Catalog definitions for Homo Sapiens
"""
import math
import logging

import msprime

import stdpopsim

logger = logging.getLogger(__name__)

###########################################################
#
# Genome definition
#
###########################################################

# List of chromosomes.

# FIXME: add mean mutation rate data to this table.
# Name  Length  mean_recombination_rate mean_mutation_rate

# length information can be found here
# <http://hgdownload.soe.ucsc.edu/goldenPath/hg19/database/chromInfo.txt.gz>

# mean_recombination_rate was computed across all windows of the GRCh37 genetic map
# <ftp://ftp-trace.ncbi.nih.gov/1000genomes/ftp/technical/working/20110106_recombination_hotspots>
_chromosome_data = """\
chr1 	 249250621 	 1.1485597641285933e-08
chr2 	 243199373 	 1.1054289277533446e-08
chr3 	 198022430 	 1.1279585624662551e-08
chr4 	 191154276 	 1.1231162636001008e-08
chr5 	 180915260 	 1.1280936570022824e-08
chr6 	 171115067 	 1.1222852661225285e-08
chr7 	 159138663 	 1.1764614397655721e-08
chr8 	 146364022 	 1.1478465778920576e-08
chr9 	 141213431 	 1.1780701596308656e-08
chr10 	 135534747 	 1.3365134257075317e-08
chr11 	 135006516 	 1.1719334320833283e-08
chr12 	 133851895 	 1.305017186986983e-08
chr13 	 115169878 	 1.0914860554958317e-08
chr14 	 107349540 	 1.119730771394731e-08
chr15 	 102531392 	 1.3835785893339787e-08
chr16 	 90354753 	 1.4834607113882717e-08
chr17 	 81195210 	 1.582489036239487e-08
chr18 	 78077248 	 1.5075956950023575e-08
chr19 	 59128983 	 1.8220141872466202e-08
chr20 	 63025520 	 1.7178269031631664e-08
chr21 	 48129895 	 1.3045214034879191e-08
chr22 	 51304566 	 1.4445022767788226e-08
chrX 	 155270560 	 1.164662223273842e-08
chrY 	 59373566 	 0.0
"""


_genome2001 = stdpopsim.Citation(
    doi="http://dx.doi.org/10.1038/35057062",
    year="2001",
    author="The Genome Sequencing Consortium",
    reasons={stdpopsim.CiteReason.ASSEMBLY}
)

_tian2019 = stdpopsim.Citation(
    doi="https://doi.org/10.1016/j.ajhg.2019.09.012",
    year="2019",
    author="Tian, Browning, and Browning",
    reasons={stdpopsim.CiteReason.MUT_RATE}
)

_tremblay2000 = stdpopsim.Citation(
    doi="https://doi.org/10.1086/302770",
    year="2000",
    author="Tremblay and Vezina",
    reasons={stdpopsim.CiteReason.GEN_TIME}
)

_takahata1993 = stdpopsim.Citation(
    doi="https://doi.org/10.1093/oxfordjournals.molbev.a039995",
    year="1993",
    author="Takahata",
    reasons={stdpopsim.CiteReason.POP_SIZE}
)

_chromosomes = []
for line in _chromosome_data.splitlines():
    name, length, mean_rr = line.split()[:3]
    _chromosomes.append(stdpopsim.Chromosome(
        id=name, length=int(length),
        mutation_rate=1.29e-8,
        recombination_rate=float(mean_rr)))

_genome = stdpopsim.Genome(
        chromosomes=_chromosomes,
        mutation_rate_citations=[
            _tian2019.because(stdpopsim.CiteReason.MUT_RATE)],
        assembly_citations=[
            _genome2001])

_species = stdpopsim.Species(
    id="HomSap",
    name="Homo sapiens",
    common_name="Human",
    genome=_genome,
    generation_time=30,
    generation_time_citations=[
        _tremblay2000.because(stdpopsim.CiteReason.GEN_TIME)],
    population_size=10**4,
    population_size_citations=[
        _takahata1993.because(stdpopsim.CiteReason.POP_SIZE)]
    )

stdpopsim.register_species(_species)


###########################################################
#
# Genetic maps
#
###########################################################


_gm = stdpopsim.GeneticMap(
    species=_species,
    id="HapMapII_GRCh37",
    description="HapMap Phase II lifted over to GRCh37",
    long_description="""
        This genetic map is from the Phase II Hapmap project
        and based on 3.1 million genotyped SNPs
        from 270 individuals across four populations (YRI, CEU, CHB and JPT).
        Genome wide recombination rates were estimated using LDHat.
        This version of the HapMap genetic map was lifted over to GRCh37
        (and adjusted in regions where the genome assembly had rearranged)
        for use in the 1000 Genomes project. Please see the README file on
        the 1000 Genomes download site for details of these adjustments.
        """,
    url=(
        "https://ftp-trace.ncbi.nih.gov/1000genomes/ftp/technical/working/"
        "20110106_recombination_hotspots/"
        "HapmapII_GRCh37_RecombinationHotspots.tar.gz"),
    file_pattern="genetic_map_GRCh37_{id}.txt",
    citations=[
        stdpopsim.Citation(
            doi="https://doi.org/10.1038/nature06258",
            year=2007,
            author="The International HapMap Consortium",
            reasons={stdpopsim.CiteReason.GEN_MAP}),
        ]
    )
_species.add_genetic_map(_gm)

_gm = stdpopsim.GeneticMap(
    species=_species,
    id="DeCodeSexAveraged_GRCh36",
    description="Sex averaged map from deCode family study",
    long_description="""
        This genetic map is from the deCode study of recombination
        events in 15,257 parent-offspring pairs from Iceland.
        289,658 phased autosomal SNPs were used to call recombinations
        within these families, and recombination rates computed from the
        density of these events. This is the combined male and female
        (sex averaged) map. See
        https://www.decode.com/addendum/ for more details.""",
    url=(
        "http://sesame.uoregon.edu/~adkern/stdpopsim/decode/"
        "decode_2010_sex-averaged_map.tar.gz"),
    file_pattern="genetic_map_decode_2010_sex-averaged_{id}.txt",
    citations=[
        stdpopsim.Citation(
            year=2010,
            author="Kong et al",
            doi="https://doi.org/10.1038/nature09525",
            reasons={stdpopsim.CiteReason.GEN_MAP})]
    )
_species.add_genetic_map(_gm)


###########################################################
#
# Demographic models
#
###########################################################

# population definitions that are reused.
_yri_population = stdpopsim.Population(
    id="YRI",
    description="1000 Genomes YRI (Yorubans)")
_ceu_population = stdpopsim.Population(
    id="CEU",
    description=(
        "1000 Genomes CEU (Utah Residents (CEPH) with Northern and "
        "Western European Ancestry"))
_chb_population = stdpopsim.Population(
    id="CHB",
    description="1000 Genomes CHB (Han Chinese in Beijing, China)")


_tennessen_et_al = stdpopsim.Citation(
    author="Tennessen et al.",
    year=2012,
    doi="https://doi.org/10.1126/science.1219240",
    reasons={stdpopsim.CiteReason.DEM_MODEL})


def _ooa_3():
    id = "OutOfAfrica_3G09"
    description = "Three population out-of-Africa"
    long_description = """
        The three population Out-of-Africa model from Gutenkunst et al. 2009.
        It describes the ancestral human population in Africa, the out of Africa
        event, and the subsequent European-Asian population split.
        Model parameters are the maximum likelihood values of the
        various parameters given in Table 1 of Gutenkunst et al.
    """
    populations = [
        _yri_population,
        _ceu_population,
        _chb_population
    ]

    citations = [stdpopsim.Citation(
        author="Gutenkunst et al.",
        year=2009,
        doi="https://doi.org/10.1371/journal.pgen.1000695",
        reasons={stdpopsim.CiteReason.DEM_MODEL})
    ]

    generation_time = 25

    # First we set out the maximum likelihood values of the various parameters
    # given in Table 1.
    N_A = 7300
    N_B = 2100
    N_AF = 12300
    N_EU0 = 1000
    N_AS0 = 510
    # Times are provided in years, so we convert into generations.

    T_AF = 220e3 / generation_time
    T_B = 140e3 / generation_time
    T_EU_AS = 21.2e3 / generation_time
    # We need to work out the starting (diploid) population sizes based on
    # the growth rates provided for these two populations
    r_EU = 0.004
    r_AS = 0.0055
    N_EU = N_EU0 / math.exp(-r_EU * T_EU_AS)
    N_AS = N_AS0 / math.exp(-r_AS * T_EU_AS)
    # Migration rates during the various epochs.
    m_AF_B = 25e-5
    m_AF_EU = 3e-5
    m_AF_AS = 1.9e-5
    m_EU_AS = 9.6e-5

    return stdpopsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=generation_time,

        # Population IDs correspond to their indexes in the population
        # configuration array. Therefore, we have 0=YRI, 1=CEU and 2=CHB
        # initially.
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=N_AF, metadata=populations[0].asdict()),
            msprime.PopulationConfiguration(
                initial_size=N_EU, growth_rate=r_EU,
                metadata=populations[1].asdict()),
            msprime.PopulationConfiguration(
                initial_size=N_AS, growth_rate=r_AS,
                metadata=populations[2].asdict()),
        ],
        migration_matrix=[
            [      0, m_AF_EU, m_AF_AS],  # noqa
            [m_AF_EU,       0, m_EU_AS],  # noqa
            [m_AF_AS, m_EU_AS,       0],  # noqa
        ],
        demographic_events=[
            # CEU and CHB merge into B with rate changes at T_EU_AS
            msprime.MassMigration(
                time=T_EU_AS, source=2, destination=1, proportion=1.0),
            msprime.MigrationRateChange(time=T_EU_AS, rate=0),
            msprime.MigrationRateChange(
                time=T_EU_AS, rate=m_AF_B, matrix_index=(0, 1)),
            msprime.MigrationRateChange(
                time=T_EU_AS, rate=m_AF_B, matrix_index=(1, 0)),
            msprime.PopulationParametersChange(
                time=T_EU_AS, initial_size=N_B, growth_rate=0, population_id=1),
            # Population B merges into YRI at T_B
            msprime.MassMigration(
                time=T_B, source=1, destination=0, proportion=1.0),
            # Size changes to N_A at T_AF
            msprime.PopulationParametersChange(
                time=T_AF, initial_size=N_A, population_id=0)
        ],
        )


_species.add_demographic_model(_ooa_3())


def _ooa_2():
    id = "OutOfAfrica_2T12"
    description = "Two population out-of-Africa"
    long_description = """
        The model is derived from the Tennesen et al. analysis of the
        jSFS from European Americans and African Americans.
        It describes the ancestral human population in Africa, the out of Africa event,
        and two distinct periods of subsequent European population growth over the past
        23kya. Model parameters are taken from Fig. S5 in Fu et al.
    """
    populations = [
        stdpopsim.Population(id="AFR", description="African Americans"),
        stdpopsim.Population(id="EUR", description="European Americans")
    ]
    citations = [
        _tennessen_et_al,
        stdpopsim.Citation(
            author="Fu et al.",
            year=2013,
            doi="https://doi.org/10.1038/nature11690",
            reasons={stdpopsim.CiteReason.DEM_MODEL})
    ]

    generation_time = 25

    T_AF = 148e3 / generation_time
    T_OOA = 51e3 / generation_time
    T_EU0 = 23e3 / generation_time
    T_EG = 5115 / generation_time

    # Growth rates
    r_EU0 = 0.00307
    r_EU = 0.0195
    r_AF = 0.0166

    # population sizes
    N_A = 7310
    N_AF1 = 14474
    N_B = 1861
    N_EU0 = 1032
    N_EU1 = N_EU0 / math.exp(-r_EU0 * (T_EU0-T_EG))

    # migration rates
    m_AF_B = 15e-5
    m_AF_EU = 2.5e-5

    # present Ne
    N_EU = N_EU1 / math.exp(-r_EU * T_EG)
    N_AF = N_AF1 / math.exp(-r_AF * T_EG)

    return stdpopsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=generation_time,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=N_AF, growth_rate=r_AF,
                metadata=populations[0].asdict()),
            msprime.PopulationConfiguration(
                initial_size=N_EU, growth_rate=r_EU,
                metadata=populations[1].asdict())
        ],
        migration_matrix=[
            [0, m_AF_EU],
            [m_AF_EU, 0],
        ],
        demographic_events=[
            msprime.MigrationRateChange(
                time=T_EG, rate=m_AF_EU, matrix_index=(0, 1)),
            msprime.MigrationRateChange(
                time=T_EG, rate=m_AF_EU, matrix_index=(1, 0)),
            msprime.PopulationParametersChange(
                time=T_EG, growth_rate=r_EU0, initial_size=N_EU1, population_id=1),
            msprime.PopulationParametersChange(
                time=T_EG, growth_rate=0, initial_size=N_AF1, population_id=0),
            msprime.MigrationRateChange(
                time=T_EU0, rate=m_AF_B, matrix_index=(0, 1)),
            msprime.MigrationRateChange(
                time=T_EU0, rate=m_AF_B, matrix_index=(1, 0)),
            msprime.PopulationParametersChange(
                time=T_EU0, initial_size=N_B, growth_rate=0, population_id=1),
            msprime.MassMigration(
                time=T_OOA, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=T_AF, initial_size=N_A, population_id=0)
        ],
        )


_species.add_demographic_model(_ooa_2())


def _african():
    id = "Africa_1T12"
    description = "African population"
    long_description = """
        The model is a simplification of the two population Tennesen et al.
        model with the European-American population removed so that we are
        modeling the African population in isolation.
    """
    populations = [
        stdpopsim.Population(id="AFR", description="African"),
    ]
    citations = [_tennessen_et_al]

    generation_time = 25

    T_AF = 148e3 / generation_time
    T_EG = 5115 / generation_time

    # Growth rate
    r_AF = 0.0166

    # population sizes
    N_A = 7310
    N_AF1 = 14474

    # present Ne
    N_AF = N_AF1 / math.exp(-r_AF * T_EG)

    return stdpopsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=generation_time,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=N_AF, growth_rate=r_AF,
                metadata=populations[0].asdict()),
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=T_EG, growth_rate=0, initial_size=N_AF1, population_id=0),
            msprime.PopulationParametersChange(
                time=T_AF, initial_size=N_A, population_id=0)
        ],
        )


_species.add_demographic_model(_african())


def _america():
    id = "AmericanAdmixture_4B11"
    description = "American admixture"
    long_description = """
        Demographic model for American admixture, taken from Browning et al. 2011.
        This model extends the Gravel et al. (2011) model of African/European/Asian
        demographic history to simulate an admixed population with admixture
        occurring 12 generations ago. The admixed population had an initial size
        of 30,000 and grew at a rate of 5% per generation, with 1/6 of the
        population of African ancestry, 1/3 European, and 1/2 Asian.
    """
    populations = [
        stdpopsim.Population(id="AFR", description="Contemporary African population"),
        stdpopsim.Population(id="EUR", description="Contemporary European population"),
        stdpopsim.Population(id="ASIA", description="Contemporary Asian population"),
        stdpopsim.Population(
            id="ADMIX", description="Modern admixed population"),
    ]

    citations = [
        stdpopsim.Citation(
            author="Browning et al.",
            year=2011,
            doi="http://dx.doi.org/10.1371/journal.pgen.1007385",
            reasons={stdpopsim.CiteReason.DEM_MODEL})
    ]

    generation_time = 25

    # Model code was ported from Supplementary File 1.
    N0 = 7310  # initial population size
    Thum = 5920  # time (gens) of advent of modern humans
    Naf = 14474  # size of african population
    Tooa = 2040  # number of generations back to Out of Africa
    Nb = 1861  # size of out of Africa population
    mafb = 1.5e-4  # migration rate Africa and Out-of-Africa
    Teu = 920  # number generations back to Asia-Europe split
    Neu = 1032  # bottleneck population sizes
    Nas = 554
    mafeu = 2.5e-5  # mig. rates
    mafas = 7.8e-6
    meuas = 3.11e-5
    reu = 0.0038  # growth rate per generation in Europe
    ras = 0.0048  # growth rate per generation in Asia
    Tadmix = 12  # time of admixture
    Nadmix = 30000  # initial size of admixed population
    radmix = .05  # growth rate of admixed population
    # pop0 is Africa, pop1 is Europe, pop2 is Asia,  pop3 is admixed

    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=Naf, growth_rate=0.0,
            metadata=populations[0].asdict()),
        msprime.PopulationConfiguration(
            initial_size=Neu*math.exp(reu*Teu), growth_rate=reu,
            metadata=populations[1].asdict()),
        msprime.PopulationConfiguration(
            initial_size=Nas*math.exp(ras*Teu), growth_rate=ras,
            metadata=populations[2].asdict()),
        msprime.PopulationConfiguration(
            initial_size=Nadmix*math.exp(radmix*Tadmix), growth_rate=radmix,
            metadata=populations[3].asdict())
    ]

    migration_matrix = [
        [0, mafeu, mafas, 0],
        [mafeu, 0, meuas, 0],
        [mafas, meuas, 0, 0],
        [0, 0, 0, 0]
    ]
    # Admixture event, 1/6 Africa, 2/6 Europe, 3/6 Asia
    admixture_event = [
        msprime.MassMigration(
            time=Tadmix, source=3, destination=0, proportion=1.0/6.0),
        msprime.MassMigration(
            time=Tadmix+0.0001, source=3, destination=1, proportion=2.0/5.0),
        msprime.MassMigration(
            time=Tadmix+0.0002, source=3, destination=2, proportion=1.0)
    ]
    # Asia and Europe split
    eu_event = [
        msprime.MigrationRateChange(
            time=Teu, rate=0.0),
        msprime.MassMigration(
            time=Teu+0.0001, source=2, destination=1, proportion=1.0),
        msprime.PopulationParametersChange(
            time=Teu+0.0002, initial_size=Nb, growth_rate=0.0, population_id=1),
        msprime.MigrationRateChange(
            time=Teu+0.0003, rate=mafb, matrix_index=(0, 1)),
        msprime.MigrationRateChange(
            time=Teu+0.0003, rate=mafb, matrix_index=(1, 0))
    ]
    # Out of Africa event
    ooa_event = [
        msprime.MigrationRateChange(
            time=Tooa, rate=0.0),
        msprime.MassMigration(
            time=Tooa+0.0001, source=1, destination=0, proportion=1.0)
    ]
    # initial population size
    init_event = [
        msprime.PopulationParametersChange(
            time=Thum,
            initial_size=N0,
            population_id=0)
    ]
    demographic_events = admixture_event + eu_event + ooa_event + init_event

    return stdpopsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=generation_time,
        population_configurations=population_configurations,
        migration_matrix=migration_matrix,
        demographic_events=demographic_events,
        )


_species.add_demographic_model(_america())


def _ooa_archaic():
    id = "OutOfAfricaArchaicAdmixture_5R19"
    description = "Three population out-of-Africa with archaic admixture"
    long_description = """
        The three population out-of-African model popularized by Gutenkunst et al. (2009)
        and augmented by archaic contributions to both Eurasian and African populations.
        Two archaic populations split early in human history, before the African
        expansion, and contribute to Eurasian populations (putative Neanderthal branch)
        and to the African branch (a deep diverging branch within Africa). Admixture
        is modeled as symmetric migration between the archaic and modern human branches,
        with contribution ending at a given time in the past.
    """
    populations = [
        _yri_population,
        _ceu_population,
        _chb_population,
        stdpopsim.Population(
            "Neanderthal", "Putative Neanderthals", sampling_time=None),
        stdpopsim.Population(
            "ArchaicAFR", "Putative Archaic Africans", sampling_time=None),
    ]
    citations = [
        stdpopsim.Citation(
            author="Ragsdale and Gravel",
            year=2019,
            doi="https://doi.org/10.1371/journal.pgen.1008204",
            reasons={stdpopsim.CiteReason.DEM_MODEL})
    ]

    # First we set out the maximum likelihood values of the various parameters
    # given in Table 1 (under archaic admixture).
    N_0 = 3600
    N_YRI = 13900
    N_B = 880
    N_CEU0 = 2300
    N_CHB0 = 650

    # Times are provided in years, so we convert into generations.
    # In the published model, the authors used a generation time of 29 years to
    # convert from genetic to physical units
    generation_time = 29

    T_AF = 300e3 / generation_time
    T_B = 60.7e3 / generation_time
    T_EU_AS = 36.0e3 / generation_time
    T_arch_afr_split = 499e3 / generation_time
    T_arch_afr_mig = 125e3 / generation_time
    T_nean_split = 559e3 / generation_time
    T_arch_adm_end = 18.7e3 / generation_time

    # We need to work out the starting (diploid) population sizes based on
    # the growth rates provided for these two populations
    r_CEU = 0.00125
    r_CHB = 0.00372
    N_CEU = N_CEU0 / math.exp(-r_CEU * T_EU_AS)
    N_CHB = N_CHB0 / math.exp(-r_CHB * T_EU_AS)

    # Migration rates during the various epochs.
    m_AF_B = 52.2e-5
    m_YRI_CEU = 2.48e-5
    m_YRI_CHB = 0e-5
    m_CEU_CHB = 11.3e-5
    m_AF_arch_af = 1.98e-5
    m_OOA_nean = 0.825e-5

    # Population IDs correspond to their indexes in the population
    # configuration array. Therefore, we have 0=YRI, 1=CEU and 2=CHB
    # initially.
    # We also have two archaic populations, putative Neanderthals and
    # archaicAfrican, which are population indices 3=Nean and 4=arch_afr.
    # Their sizes are equal to the ancestral reference population size N_0.
    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=N_YRI, metadata=populations[0].asdict()),
        msprime.PopulationConfiguration(
            initial_size=N_CEU, growth_rate=r_CEU,
            metadata=populations[1].asdict()),
        msprime.PopulationConfiguration(
            initial_size=N_CHB, growth_rate=r_CHB,
            metadata=populations[2].asdict()),
        msprime.PopulationConfiguration(
            initial_size=N_0,
            metadata=populations[3].asdict()),
        msprime.PopulationConfiguration(
            initial_size=N_0,
            metadata=populations[4].asdict())
    ]
    migration_matrix = [                   # noqa
        [      0, m_YRI_CEU, m_YRI_CHB, 0, 0],  # noqa
        [m_YRI_CEU,       0, m_CEU_CHB, 0, 0],  # noqa
        [m_YRI_CHB, m_CEU_CHB,       0, 0, 0],  # noqa
        [      0,         0,         0, 0, 0],  # noqa
        [      0,         0,         0, 0, 0]   # noqa
    ]                                           # noqa
    demographic_events = [
        # first event is migration turned on between modern and archaic humans
        msprime.MigrationRateChange(
            time=T_arch_adm_end, rate=m_AF_arch_af, matrix_index=(0, 4)),
        msprime.MigrationRateChange(
            time=T_arch_adm_end, rate=m_AF_arch_af, matrix_index=(4, 0)),
        msprime.MigrationRateChange(
            time=T_arch_adm_end, rate=m_OOA_nean, matrix_index=(1, 3)),
        msprime.MigrationRateChange(
            time=T_arch_adm_end, rate=m_OOA_nean, matrix_index=(3, 1)),
        msprime.MigrationRateChange(
            time=T_arch_adm_end, rate=m_OOA_nean, matrix_index=(2, 3)),
        msprime.MigrationRateChange(
            time=T_arch_adm_end, rate=m_OOA_nean, matrix_index=(3, 2)),

        # CEU and CHB merge into B with rate changes at T_EU_AS
        msprime.MassMigration(
            time=T_EU_AS, source=2, destination=1, proportion=1.0),
        msprime.MigrationRateChange(time=T_EU_AS, rate=0),
        msprime.MigrationRateChange(
            time=T_EU_AS, rate=m_AF_B, matrix_index=(0, 1)),
        msprime.MigrationRateChange(
            time=T_EU_AS, rate=m_AF_B, matrix_index=(1, 0)),
        msprime.MigrationRateChange(
            time=T_EU_AS, rate=m_AF_arch_af, matrix_index=(0, 4)),
        msprime.MigrationRateChange(
            time=T_EU_AS, rate=m_AF_arch_af, matrix_index=(4, 0)),
        msprime.MigrationRateChange(
            time=T_EU_AS, rate=m_OOA_nean, matrix_index=(1, 3)),
        msprime.MigrationRateChange(
            time=T_EU_AS, rate=m_OOA_nean, matrix_index=(3, 1)),
        msprime.PopulationParametersChange(
            time=T_EU_AS, initial_size=N_B, growth_rate=0, population_id=1),

        # Population B merges into YRI at T_B
        msprime.MassMigration(
            time=T_B, source=1, destination=0, proportion=1.0),
        msprime.MigrationRateChange(time=T_B, rate=0),
        msprime.MigrationRateChange(
            time=T_B, rate=m_AF_arch_af, matrix_index=(0, 4)),
        msprime.MigrationRateChange(
            time=T_B, rate=m_AF_arch_af, matrix_index=(4, 0)),

        # Beginning of migration between African and archaic African populations
        msprime.MigrationRateChange(time=T_arch_afr_mig, rate=0),

        # Size changes to N_0 at T_AF
        msprime.PopulationParametersChange(
            time=T_AF, initial_size=N_0, population_id=0),

        # Archaic African merges with moderns
        msprime.MassMigration(
            time=T_arch_afr_split, source=4, destination=0, proportion=1.0),

        # Neanderthal merges with moderns
        msprime.MassMigration(
            time=T_nean_split, source=3, destination=0, proportion=1.0)
    ]

    return stdpopsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=generation_time,
        population_configurations=population_configurations,
        migration_matrix=migration_matrix,
        demographic_events=demographic_events,
        )


_species.add_demographic_model(_ooa_archaic())


def _zigzag():
    id = "Zigzag_1S14"
    description = "Periodic growth and decline."
    long_description = """
        A validation model used by Schiffels and Durbin (2014) and Terhorst and
        Terhorst, Kamm, and Song (2017) with periods of exponential growth and
        decline in a single population.
        """
    populations = [
        stdpopsim.Population("generic", "Generic expanding and contracting population"),
    ]
    citations = [
        stdpopsim.Citation(
            author="Schiffels and Durbin",
            year=2014,
            doi="https://doi.org/10.1038/ng.3015",
            reasons={stdpopsim.CiteReason.DEM_MODEL})
    ]

    generation_time = 29
    N0 = 14312

    g_1 = 0.023025
    t_1 = 33.333
    n_1 = N0

    g_2 = -0.005756
    t_2 = 133.33
    n_2 = N0/10

    g_3 = 0.0014391
    t_3 = 533.33
    n_3 = N0

    g_4 = -0.00035977
    t_4 = 2133.33
    n_4 = N0/10

    g_5 = 8.99448e-5
    t_5 = 8533.33
    n_5 = N0

    n_ancient = N0/10
    t_ancient = 34133.31

    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=N0, metadata=populations[0].asdict())
    ]

    demographic_events = [
            msprime.PopulationParametersChange(
                initial_size=n_1, time=t_1, growth_rate=g_1),
            msprime.PopulationParametersChange(
                initial_size=n_2, time=t_2, growth_rate=g_2),
            msprime.PopulationParametersChange(
                initial_size=n_3, time=t_3, growth_rate=g_3),
            msprime.PopulationParametersChange(
                initial_size=n_4, time=t_4, growth_rate=g_4),
            msprime.PopulationParametersChange(
                initial_size=n_5, time=t_5, growth_rate=g_5),
            msprime.PopulationParametersChange(
                time=t_ancient, initial_size=n_ancient, growth_rate=0)
    ]

    return stdpopsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=generation_time,
        population_configurations=population_configurations,
        demographic_events=demographic_events,
        )


_species.add_demographic_model(_zigzag())


def _kamm_ancient_eurasia():
    id = "AncientEurasia_9K19"
    description = "Multi-population model of ancient Eurasia"
    long_description = """
        This is the best-fitting model of a history of
        multiple ancient and present-day human populations
        sampled across Eurasia over the past 120,000 years.
        The fitting was performed using momi2 (Kamm et al. 2019),
        which uses the multi-population site-frequency spectrum
        as input data. The model includes a ghost admixture event
        (from unsampled basal Eurasians into early European
        farmers), and two admixture events where the source is
        approximately well-known (from Neanderthals into
        Non-Africans and from Western European hunter-gatherers
        into modern Sardinians. There are three present-day
        populations: Sardinians, Han Chinese and African Mbuti.
        Additionally, there are several ancient samples
        obtained from fossils dated at different times in
        the past: the Altai Neanderthal (Prufer et al. 2014),
        a Mesolithic hunter-gatherer (Lazaridis et al. 2014),
        a Neolithic early European sample (Lazaridis et al. 2014),
        and two Palaeolithic modern humans from Siberia - MA1
        (Raghavan et al. 2014) and  Ust'Ishim (Fu et al. 2014).
        All the ancient samples are represented by a single diploid
        genome.
    """
    # Sampling times are assuming 25 years per generation
    populations = [
        stdpopsim.Population(id="Mbuti",
                             description="Present-day African Mbuti",
                             sampling_time=0),
        # LBK: 8,000 years ago
        stdpopsim.Population(id="LBK",
                             description="Early European farmer (EEF)",
                             sampling_time=320),
        stdpopsim.Population(id="Sardinian",
                             description="Present-day Sardinian",
                             sampling_time=0),
        # Loschbour: 7,500 years ago
        stdpopsim.Population(id="Loschbour",
                             description="Western hunter-gatherer (WHG)",
                             sampling_time=300),
        # MA1: 24,000 years ago
        stdpopsim.Population(id="MA1",
                             description="Upper Palaeolithic MAl'ta culture",
                             sampling_time=960),
        stdpopsim.Population(id="Han",
                             description="Present-day Han Chinese",
                             sampling_time=0),
        # Ust Ishim: 45,000 years ago
        stdpopsim.Population(id="UstIshim",
                             description="early Palaeolithic Ust'-Ishim",
                             sampling_time=1800),
        # Altai Neanderthal: 50,000 years ago
        stdpopsim.Population(id="Neanderthal",
                             description="Altai Neanderthal from Siberia",
                             sampling_time=2000),
        stdpopsim.Population(id="BasalEurasian",
                             description="Basal Eurasians",
                             sampling_time=None),
    ]
    citations = [
        stdpopsim.Citation(
            author="Kamm et al.",
            year=2019,
            doi="https://doi.org/10.1080/01621459.2019.1635482",
            reasons={stdpopsim.CiteReason.DEM_MODEL})
    ]

    # Times are provided in years, so we convert into generations.
    generation_time = 25
    # Mutation_rate in Kamm et al. = 1.22e-8
    # Effective population sizes
    N_Losch = 1920
    N_Mbu = 17300
    N_Mbu_Losch = 29100
    N_Han = 6300
    N_Han_Losch = 2340
    N_Nean_Losch = 18200
    N_Nean = 86.9
    N_LBK = 75.7
    N_Sard = 15000
    N_Sard_LBK = 12000
    # Table A.1 has Altai at 50,000 years ago
    t_NeaPopSizeChange = 50000 / generation_time
    # Unknown but suspected parameters...
    N_Basal = N_Losch
    N_MA1 = N_Losch
    N_Ust = N_Losch
    # Population split times
    t_Mbu_Losch = 95800 / generation_time
    t_Han_Losch = 50400 / generation_time
    t_Ust_Losch = 51500 / generation_time
    t_Nean_Losch = 696000 / generation_time
    t_MA1_Losch = 44900 / generation_time
    t_LBK_Losch = 37700 / generation_time
    t_Basal_Losch = 79800 / generation_time
    t_Sard_LBK = 7690 / generation_time
    # Given that we're using best model estimate,
    # ghost WHG is directly descended from Loschbour,
    # so this parameter is not used
    # t_GhostWHG_Losch = 1560 / generation_time
    # Admixture times
    t_Nean_to_Eurasian = 56800 / generation_time
    t_Basal_to_EEF = 33700 / generation_time
    t_GhostWHG_to_Sard = 1230 / generation_time
    t_NeanGrowth = t_Mbu_Losch - t_NeaPopSizeChange
    logdiffNeanGrowth = math.log(N_Nean/N_Nean_Losch)
    r_NeanGrowth = logdiffNeanGrowth / t_NeanGrowth
    p_Nean_to_Eurasian = 0.0296
    p_Basal_to_EEF = 0.0936
    p_GhostWHG_to_Sard = 0.0317
    # Population IDs: Mbuti = 0; LBK = 1;
    # Sardinian = 2; Loschbour = 3; MA1 = 4;
    # Han = 5; Ust Ishim = 6; Neanderthal = 7;
    # Basal Eurasian = 8
    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=N_Mbu, metadata=populations[0].asdict()),
        msprime.PopulationConfiguration(
            initial_size=N_LBK, metadata=populations[1].asdict()),
        msprime.PopulationConfiguration(
            initial_size=N_Sard, metadata=populations[2].asdict()),
        msprime.PopulationConfiguration(
            initial_size=N_Losch, metadata=populations[3].asdict()),
        msprime.PopulationConfiguration(
            initial_size=N_MA1, metadata=populations[4].asdict()),
        msprime.PopulationConfiguration(
            initial_size=N_Han, metadata=populations[5].asdict()),
        msprime.PopulationConfiguration(
            initial_size=N_Ust, metadata=populations[6].asdict()),
        msprime.PopulationConfiguration(
            initial_size=N_Nean, metadata=populations[7].asdict()),
        msprime.PopulationConfiguration(
            initial_size=N_Basal, metadata=populations[8].asdict())
    ]
    demographic_events = [
        # Sardinian receives admixture from Loschbour / WHG
        msprime.MassMigration(
            time=t_GhostWHG_to_Sard, source=2, destination=3,
            proportion=p_GhostWHG_to_Sard),
        # Sardinian merges into LBK / EEF
        # Now pop 1: Sardinian-LBK ancestral pop
        msprime.MassMigration(
            time=t_Sard_LBK, source=2, destination=1,
            proportion=1.0),
        # Sardinian-LBK ancestral pop size change
        msprime.PopulationParametersChange(
            time=t_Sard_LBK, initial_size=N_Sard_LBK,
            population_id=1),
        # LBK / EEF receives admixture from Basal Eurasians
        msprime.MassMigration(
            time=t_Basal_to_EEF, source=1, destination=8,
            proportion=p_Basal_to_EEF),
        # LBK / EEF merges into Loschbour
        msprime.MassMigration(
            time=t_LBK_Losch, source=1, destination=3,
            proportion=1.0),
        # MA1 merges into Loschbour
        msprime.MassMigration(
            time=t_MA1_Losch, source=4, destination=3,
            proportion=1.0),
        # Neanderthal start change in population size
        msprime.PopulationParametersChange(
            time=t_NeaPopSizeChange, initial_size=N_Nean,
            growth_rate=r_NeanGrowth, population_id=7),
        # Han merges into Loschbour
        msprime.MassMigration(
            time=t_Han_Losch, source=5, destination=3,
            proportion=1.0),
        # Change in population size in Han-Losch ancestral pop
        msprime.PopulationParametersChange(
            time=t_Han_Losch, initial_size=N_Han_Losch,
            population_id=3),
        # UstIshim merges into Loschbour
        msprime.MassMigration(
            time=t_Ust_Losch, source=6, destination=3,
            proportion=1.0),
        # Loschbour / Non-Africans receive admixture from Neanderthals
        msprime.MassMigration(
            time=t_Nean_to_Eurasian, source=3, destination=7,
            proportion=p_Nean_to_Eurasian),
        # Basal Eurasians merge into Loschbour / Non-Africans
        msprime.MassMigration(
            time=t_Basal_Losch, source=8, destination=3,
            proportion=1.0),
        # Mbuti merge into Loschbour / Non-Africans
        msprime.MassMigration(
            time=t_Mbu_Losch, source=0, destination=3,
            proportion=1.0),
        # Change in population size in Mbuti-Losch ancestral pop
        msprime.PopulationParametersChange(
            time=t_Mbu_Losch, initial_size=N_Mbu_Losch,
            population_id=3),
        # Change in population size in Neanderthal, growth rate 0
        msprime.PopulationParametersChange(
            time=t_Mbu_Losch, initial_size=N_Nean_Losch, growth_rate=0,
            population_id=7),
        # Neanderthal merge into Loschbour / modern humans
        msprime.MassMigration(
            time=t_Nean_Losch, source=7, destination=3,
            proportion=1.0),
        # Ancestral hominin population size change
        msprime.PopulationParametersChange(
            time=t_Nean_Losch, initial_size=N_Nean_Losch,
            population_id=3),
    ]

    return stdpopsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=generation_time,
        population_configurations=population_configurations,
        demographic_events=demographic_events,
        )


_species.add_demographic_model(_kamm_ancient_eurasia())
