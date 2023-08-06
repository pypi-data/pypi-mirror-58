import numpy as np
from scipy.signal import freqz

import spectrum

from koe_acoustic_features.extractor import Extractor
from koe_acoustic_features.utils import get_sig, unroll_args, _cached_get_window, split_segments


class LinearPredictionExtractor(Extractor):
    def lpc_spectrum(self):
        sig = get_sig(self.args)
        nfft, fs, noverlap, win_length, order = unroll_args(self.args, ['nfft', 'fs', 'noverlap', 'win_length', 'order'])
        hann_window = _cached_get_window('hanning', nfft)
        window = unroll_args(self.args, [('window', hann_window)])

        siglen = len(sig)
        nsegs, segs = split_segments(siglen, win_length, noverlap, incltail=False)

        lpcs = np.zeros((nfft, nsegs), dtype=np.complex64)
        for i in range(nsegs):
            seg_beg, seg_end = segs[i]
            frame = sig[seg_beg:seg_end]

            lpcs[:, i] = lpc_spectrum_frame(frame * window, order, nfft)
        return np.log10(abs(lpcs))

    def lpc_cepstrum(self):
        sig = get_sig(self.args)
        nfft, fs, noverlap, win_length, order = unroll_args(self.args, ['nfft', 'fs', 'noverlap', 'win_length', 'order'])
        hann_window = _cached_get_window('hanning', nfft)
        window = unroll_args(self.args, [('window', hann_window)])

        siglen = len(sig)
        nsegs, segs = split_segments(siglen, win_length, noverlap, incltail=False)

        lpcs = np.zeros((order, nsegs), dtype=np.float32)

        for i in range(nsegs):
            seg_beg, seg_end = segs[i]
            frame = sig[seg_beg:seg_end]

            lpcs[:, i] = lpc_cepstrum_frame(frame * window, order)
        return lpcs




    def lp_coefficients(self):
        sig = get_sig(self.args)
        nfft, fs, noverlap, win_length, order = unroll_args(self.args, ['nfft', 'fs', 'noverlap', 'win_length', 'order'])
        hann_window = _cached_get_window('hanning', nfft)
        window = unroll_args(self.args, [('window', hann_window)])

        siglen = len(sig)
        nsegs, segs = split_segments(siglen, win_length, noverlap, incltail=False)

        lp_coeffs = np.zeros((order, nsegs), dtype=np.float32)
        for i in range(nsegs):
            seg_beg, seg_end = segs[i]
            frame = sig[seg_beg:seg_end]

            lp_coeffs[:, i] = lp_coefficients_frame(frame * window, order)
        return lp_coeffs


def lpc_spectrum_frame(sig, order, nfft):
    lp, e = spectrum.lpc(sig, order)

    # Need to add 1 to the lp coefficients to make it similar to result from Matlab
    w, h = freqz(1, np.concatenate((np.array([1]), lp)), nfft)
    return h


def lp_coefficients_frame(sig, order):
    lp, e = spectrum.lpc(sig, order)
    return lp.astype(np.float32)


def lpc_cepstrum_frame(sig, order=None):
    """
    :param lpc: A sequence of lpc components. Need to be preprocessed by lpc()
    :param g: Error term for lpc sequence
    :param order: size of the array. Function returns order+1 length array. Default is len(seq)
    :return:
    """
    lp, g = spectrum.lpc(sig, order)
    cepst = np.zeros((order,), dtype=np.float32)

    for i in range(0, order):
        sum = 0
        for j in range(0, i):
            sum += (j - i) * lp[j] * cepst[i - j - 1]
        cepst[i] = -lp[i] + sum / (i + 1)

    return cepst
