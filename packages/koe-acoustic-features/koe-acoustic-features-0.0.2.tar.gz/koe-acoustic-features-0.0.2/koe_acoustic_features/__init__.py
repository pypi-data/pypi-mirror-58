from koe_acoustic_features.freq_domain import FrequencyDomainExtractor as _1
from koe_acoustic_features.linear_prediction import LinearPredictionExtractor as _2
from koe_acoustic_features.mt_features import MtExtractor as _3
from koe_acoustic_features.other_features import OtherFeatureExtractor as _4
from koe_acoustic_features.scaled_freq_features import ScaledFrequencyExtractor as _5
from koe_acoustic_features.time_domain import TimeDomainExtractor as _6


class AcousticExtractor(_1, _2, _3, _4, _5, _6):
    pass
