import numpy as np
from librosa import filters
from librosa import power_to_db

from koe_acoustic_features.extractor import Extractor
from koe_acoustic_features.utils import unroll_args, get_psd


def _cached_get_mel_filter(sr, n_fft, n_mels, fmin, fmax):
    return filters.mel(sr=sr, n_fft=n_fft, n_mels=n_mels, fmin=fmin, fmax=fmax)


class ScaledFrequencyExtractor(Extractor):
    def mfc(self):
        psd = get_psd(self.args) ** 2
        fs, nfft, ncep, fmin, fmax = unroll_args(self.args, ['fs', 'nfft', ('ncep', 20), ('fmin', 0.0), ('fmax', None)])
        if fmax is None:
            fmax = fs // 2

        # Build a Mel filter
        mel_basis = _cached_get_mel_filter(sr=fs, n_fft=nfft, n_mels=ncep * 2, fmin=fmin, fmax=fmax)
        melspect = np.dot(mel_basis, psd)
        return power_to_db(melspect)

    def mfcc(self):
        ncep = unroll_args(self.args, [('ncep', 20)])
        S = self.mfc()
        return np.dot(filters.dct(ncep, S.shape[0]), S)

    def mfcc_delta(self):
        cc = self.mfcc()
        diff = np.pad(np.diff(cc), ((0, 0), (1, 0)), 'constant', constant_values=0)
        return diff

    def mfcc_delta2(self):
        cc = self.mfc()
        diff = np.pad(np.diff(cc), ((0, 0), (1, 0)), 'constant', constant_values=0)
        return diff
