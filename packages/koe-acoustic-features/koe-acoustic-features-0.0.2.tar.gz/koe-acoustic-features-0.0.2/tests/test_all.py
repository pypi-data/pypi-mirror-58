import unittest
import inspect

from koe_acoustic_features import AcousticExtractor
from koe_acoustic_features.freq_domain import FrequencyDomainExtractor
from koe_acoustic_features.linear_prediction import LinearPredictionExtractor
from koe_acoustic_features.mt_features import MtExtractor
from koe_acoustic_features.other_features import OtherFeatureExtractor
from koe_acoustic_features.scaled_freq_features import ScaledFrequencyExtractor
from koe_acoustic_features.time_domain import TimeDomainExtractor


class TestFrequencyDomain(unittest.TestCase):
    def setUp(self):
        self.extractors = [
            cls.from_file('audio.wav', 120, 500) for cls in [
                FrequencyDomainExtractor,
                LinearPredictionExtractor,
                MtExtractor,
                OtherFeatureExtractor,
                ScaledFrequencyExtractor,
                TimeDomainExtractor
            ]
        ]

    def test(self):
        for extractor in self.extractors:
            cls = extractor.__class__
            props = dir(extractor)
            for prop in props:
                func = getattr(extractor, prop)
                if inspect.ismethod(func) and not func.__self__ is cls and not prop.startswith('_'):
                    print('{} = {}'.format(prop, func()))

    def test_omni_extractor(self):
        extractor = AcousticExtractor.from_file('audio.wav', 120, 500)
        cls = extractor.__class__
        props = dir(extractor)
        for prop in props:
            func = getattr(extractor, prop)
            if inspect.ismethod(func) and not func.__self__ is cls and not prop.startswith('_'):
                print('{} = {}'.format(prop, func()))
