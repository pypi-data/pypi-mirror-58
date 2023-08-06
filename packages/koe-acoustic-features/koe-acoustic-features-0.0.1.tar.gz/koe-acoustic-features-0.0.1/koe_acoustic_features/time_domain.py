import numpy as np
from librosa import feature as rosaft

from koe_acoustic_features.extractor import Extractor
from koe_acoustic_features.utils import unroll_args, get_sig, _cached_get_window


class TimeDomainExtractor(Extractor):
    def duration(self):
        start, end = unroll_args(self.args, ['start', 'end'])
        retval = np.ndarray((1, 1), dtype=np.float32)
        retval[0] = end - start
        return retval

    def zero_crossing_rate(self):
        sig = get_sig(self.args)
        nfft, noverlap = unroll_args(self.args, ['nfft', 'noverlap'])
        hopsize = nfft - noverlap
        zcr = rosaft.zero_crossing_rate(y=sig, frame_length=nfft, hop_length=hopsize, center=False)
        return zcr

    def time_axis(self):
        sig = get_sig(self.args)
        fs = unroll_args(self.args, ['fs'])
        length = len(sig)
        t_end_sec = length / fs
        time = np.linspace(0, t_end_sec, length)
        return time

    def log_attack_time(self):
        envelope = self.energy_envelope()
        stop_pos = np.argmax(envelope)
        stop_val = envelope[stop_pos]

        threshold_percent = 2

        threshold = stop_val * threshold_percent / 100
        tmp = np.where(envelope > threshold)[0]
        start_pos = tmp[0]
        if start_pos == stop_pos:
            start_pos -= 1

        time = self.time_axis()
        lat = np.ndarray((1, 1), dtype=np.float32)
        lat[0] = np.log10((time[stop_pos] - time[start_pos]))
        return lat

    def energy_envelope(self):
        sig = get_sig(self.args)
        nfft = unroll_args(self.args, ['nfft'])
        sig = np.abs(sig)
        hann_window = _cached_get_window('hanning', nfft)
        envelope = np.convolve(sig, hann_window, 'same')
        return envelope

    def temporal_centroid(self):
        envelope = self.energy_envelope()
        time = self.time_axis()

        tc = np.sum(envelope * time) / np.sum(envelope)
        return tc
