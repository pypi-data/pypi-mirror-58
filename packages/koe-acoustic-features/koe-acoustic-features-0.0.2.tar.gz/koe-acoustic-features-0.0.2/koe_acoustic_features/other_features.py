import numpy as np
from librosa import feature as rosaft

from koe_acoustic_features.extractor import Extractor
from koe_acoustic_features.utils import get_psd, get_sig, unroll_args, get_psddb


class OtherFeatureExtractor(Extractor):
    def frame_entropy(self):
        psd = get_psd(self.args)

        # Entropy of each frame (time slice) averaged
        newsg = (psd.T / np.sum(psd)).T
        return np.sum(-newsg * np.log2(newsg), axis=0)

    def average_frame_power(self):
        """
        Average power = sum of PSD (in decibel) divided by number of pixels
        :param self.args:
        :return:
        """
        psddb = get_psddb(self.args)
        return np.mean(psddb, axis=0)

    def max_frame_power(self):
        """
        Max power is the darkest pixel in the spectrogram
        :param self.args:
        :return:
        """
        psddb = get_psddb(self.args)
        return np.max(psddb, axis=0)

    def tonnetz(self):
        sig = get_sig(self.args)
        fs = self.args['fs']
        return rosaft.tonnetz(y=sig, sr=fs)

    def chroma_stft(self):
        psd = get_psd(self.args)
        fs, nfft, noverlap = unroll_args(self.args, ['fs', 'nfft', 'noverlap'])
        hopsize = nfft - noverlap
        return rosaft.chroma_stft(y=None, sr=fs, S=psd, n_fft=nfft, hop_length=hopsize)

    def chroma_cqt(self):
        sig = get_sig(self.args)
        fs, nfft, noverlap = unroll_args(self.args, ['fs', 'nfft', 'noverlap'])
        hopsize = nfft - noverlap
        return rosaft.chroma_cqt(y=sig, sr=fs, hop_length=hopsize)

    def chroma_cens(self):
        sig = get_sig(self.args)
        fs, nfft, noverlap = unroll_args(self.args, ['fs', 'nfft', 'noverlap'])
        hopsize = nfft - noverlap
        return rosaft.chroma_cens(y=sig, sr=fs, hop_length=hopsize)
