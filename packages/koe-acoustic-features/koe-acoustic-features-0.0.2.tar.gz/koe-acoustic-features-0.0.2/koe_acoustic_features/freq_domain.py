import numpy as np
from librosa import feature as rosaft
from scipy.stats import skew, kurtosis

from koe_acoustic_features.extractor import Extractor
from koe_acoustic_features.utils import get_sig, unroll_args, get_psd, get_psddb, split_segments

eps = 0.00000001


class FrequencyDomainExtractor(Extractor):
    def spectrum(self):
        psd = get_psd(self.args)
        return psd

    def spectral_bandwidth(self):
        psd = get_psd(self.args)
        fs, nfft, noverlap = unroll_args(self.args, ['fs', 'nfft', 'noverlap'])
        hopsize = nfft - noverlap
        return rosaft.spectral_bandwidth(y=None, sr=fs, S=psd, n_fft=nfft, hop_length=hopsize)

    def spectral_flux(self):
        psd = get_psd(self.args)
        diff = np.pad(np.diff(psd), ((0, 0), (1, 0)), 'constant', constant_values=0)
        return np.linalg.norm(diff, axis=0)

    def spectral_flatness(self):
        psd = get_psd(self.args)
        nfft, noverlap = unroll_args(self.args, ['nfft', 'noverlap'])
        hopsize = nfft - noverlap
        return rosaft.spectral_flatness(y=None, S=psd, n_fft=nfft, hop_length=hopsize)

    def spectral_centroid(self):
        psd = get_psd(self.args)
        fs, nfft, noverlap = unroll_args(self.args, ['fs', 'nfft', 'noverlap'])
        hopsize = nfft - noverlap
        return rosaft.spectral_centroid(y=None, sr=fs, S=psd, n_fft=nfft, hop_length=hopsize)

    def spectral_contrast(self):
        psd = get_psd(self.args)
        fs, nfft, noverlap = unroll_args(self.args, ['fs', 'nfft', 'noverlap'])
        hopsize = nfft - noverlap
        if fs < 12800:
            n_bands = 6
            fmin = int(fs / 2.0 ** (n_bands))
        else:
            fmin = 200
        return rosaft.spectral_contrast(y=None, sr=fs, S=psd, n_fft=nfft, hop_length=hopsize, fmin=fmin)

    def spectral_rolloff(self):
        psd = get_psd(self.args)
        fs, nfft, noverlap = unroll_args(self.args, ['fs', 'nfft', 'noverlap'])
        hopsize = nfft - noverlap
        return rosaft.spectral_rolloff(y=None, sr=fs, S=psd, n_fft=nfft, hop_length=hopsize)

    def spectral_crest(self):
        """
        a.k.a. spectral crest factor: ratio of max freq power over mean spectrum power
        :param self.args:
        :return:
        """
        psd = get_psd(self.args)
        sc = np.max(psd, axis=0) / np.mean(psd, axis=0)
        return sc

    def spectral_skewness(self):
        psd = get_psd(self.args)
        return skew(psd, axis=0)

    def spectral_kurtosis(self):
        psd = get_psd(self.args)
        return kurtosis(psd, axis=0)

    def spectral_decrease(self):
        """
        Compute index vector
        k       = [0:size(X,1)-1]
        k(1)    = 1
        kinv    = 1./k

        % compute slope
        vsd     = (kinv*(X-repmat(X(1,:),size(X,1),1)))./sum(X(2:end,:),1)

        % avoid NaN for silence frames
        vsd (sum(X(2:end,:),1) == 0) = 0

        :param self.args:
        :return:
        """
        psd = get_psd(self.args)

        k = np.arange(0, psd.shape[0])
        k[0] = 1
        kinv = 1 / k
        kinv = kinv.reshape((1, psd.shape[0]))

        sdecrease = np.matmul(kinv, (psd - psd[0, :])) / np.sum(psd[1:, :], axis=0)
        return sdecrease

    def harmonic_ratio(self):
        hrs, f0s = _harmonic_and_pitch(self.args)
        return hrs

    def fundamental_frequency(self):
        hrs, f0s = _harmonic_and_pitch(self.args)
        return f0s

    def total_energy(self):
        fs, nfft = unroll_args(self.args, ['fs', 'nfft'])
        psd = get_psd(self.args)

        # This is a little bit unclear. Eq (6.1) of Raven is the calculation below, but then it says it is in decibels,
        # which this is not!
        energy = np.sum(psd) * (fs / nfft)
        return energy

    def aggregate_entropy(self):
        psd = get_psd(self.args)

        # Entropy of energy in each frequency bin over whole time
        ebin = np.sum(psd, axis=1)
        ebin /= np.sum(ebin)
        return np.sum(-ebin * np.log2(ebin))

    def average_entropy(self):
        psd = get_psd(self.args)

        # Entropy of each frame (time slice) averaged
        newsg = (psd.T / np.sum(psd)).T
        averaged_entropy = np.sum(-newsg * np.log2(newsg), axis=0)
        averaged_entropy = np.mean(averaged_entropy)

        return averaged_entropy

    def average_power(self):
        """
        Average power = sum of PSD (in decibel) divided by number of pixels
        :param self.args:
        :return:
        """
        psddb = get_psddb(self.args)
        return np.sum(psddb) / np.size(psddb)

    def max_power(self):
        """
        Max power is the darkest pixel in the spectrogram
        :param self.args:
        :return:
        """
        psddb = get_psddb(self.args)
        return np.max(psddb)

    def max_frequency(self):
        """
        Max frequency is the frequency at which max power occurs
        :param self.args:
        :return: float: max frequency over the entire duration
        """
        psddb = get_psddb(self.args)
        fs = self.args['fs']
        max_index = np.argmax(np.max(psddb, axis=1))
        nyquist = fs / 2.0
        return max_index / psddb.shape[0] * nyquist

    def dominant_frequency(self):
        """
        Dominant frequency is the frequency at which max power occurs
        :param self.args:
        :return:
        """
        psddb = get_psddb(self.args)
        fs = self.args['fs']
        max_indices = np.argmax(psddb, axis=0)
        nyquist = fs / 2.0
        return max_indices / psddb.shape[0] * nyquist


def _harmonic_and_pitch(args):
    """
    Computes harmonic ratio and pitch
    """
    sig = get_sig(args)
    fs, noverlap, win_length = unroll_args(args, ['fs', 'noverlap', 'win_length'])
    siglen = len(sig)
    nsegs, segs = split_segments(siglen, win_length, noverlap, incltail=False)

    HRs = []
    F0s = []

    for i in range(nsegs):
        seg_beg, seg_end = segs[i]
        frame = sig[seg_beg:seg_end]

        M = int(np.round(0.016 * fs) - 1)
        R = np.correlate(frame, frame, mode='full')

        g = R[len(frame) - 1]
        R = R[len(frame):-1]

        # estimate m0 (as the first zero crossing of R)
        [a, ] = np.nonzero(np.diff(np.sign(R)))

        if len(a) == 0:
            m0 = len(R) - 1
        else:
            m0 = a[0]
        if M > len(R):
            M = len(R) - 1

        Gamma = np.zeros(M, dtype=np.float64)
        CSum = np.cumsum(frame ** 2)
        Gamma[m0:M] = R[m0:M] / (np.sqrt((g * CSum[M:m0:-1])) + eps)

        ZCR = frame_zcr(Gamma)

        if ZCR > 0.15:
            HR = 0.0
            f0 = 0.0
        else:
            if len(Gamma) == 0:
                HR = 1.0
                blag = 0.0
                Gamma = np.zeros(M, dtype=np.float64)
            else:
                HR = np.max(Gamma)
                blag = np.argmax(Gamma)

            # Get fundamental frequency:
            f0 = fs / (blag + eps)
            if f0 > 5000:
                f0 = 0.0
            if HR < 0.1:
                f0 = 0.0

        HRs.append(HR)
        F0s.append(f0)

    return np.array(HRs), np.array(F0s)


def frame_zcr(frame):
    """Computes zero crossing rate of frame"""
    count = len(frame)
    countZ = np.sum(np.abs(np.diff(np.sign(frame)))) / 2
    return countZ / float(count)
