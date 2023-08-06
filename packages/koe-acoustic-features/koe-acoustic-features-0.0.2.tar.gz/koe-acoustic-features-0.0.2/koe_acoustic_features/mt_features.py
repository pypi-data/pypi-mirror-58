import numpy as np
from scipy.fftpack import ifft
from skimage.measure import label
from skimage.measure import regionprops

from koe_acoustic_features.extractor import Extractor
from koe_acoustic_features.utils import maybe_cached_stft, unroll_args


def find_zc(arr):
    v_ = arr * np.roll(arr, 1, 0)
    return np.where((v_ < 0) & (arr < 0))


class MtExtractor(Extractor):
    def cached_tf_derivatives(self):
        tapered1 = maybe_cached_stft(self.args, 'dpss1')
        tapered2 = maybe_cached_stft(self.args, 'dpss2')

        real1 = np.real(tapered1)
        real2 = np.real(tapered2)
        imag1 = np.imag(tapered1)
        imag2 = np.imag(tapered2)

        time_deriv = (-real1 * real2) - (imag1 * imag2)
        freq_deriv = (imag1 * real2) - (real1 * imag2)

        return time_deriv, freq_deriv

    def time_derivative(self):
        time_deriv, _ = self.cached_tf_derivatives()
        return time_deriv

    def freq_derivative(self):
        _, freq_deriv = self.cached_tf_derivatives()
        return freq_deriv

    def frequency_modulation(self):
        time_deriv, freq_deriv = self.cached_tf_derivatives()
        return np.arctan(np.max(time_deriv, axis=0) / (np.max(freq_deriv, axis=0) + 0.1))

    def amplitude_modulation(self):
        time_deriv, _ = self.cached_tf_derivatives()
        return np.sum(time_deriv, axis=0)

    def goodness_of_pitch(self):
        nfft = self.args['nfft']
        stft = maybe_cached_stft(self.args, 'dpss1')

        # To restore the full spectrum, we should've conjugated the second half.
        # e.g. np.concatenate((stft, np.conj(stft[-2:0:-1, :])), axis=0)
        # But since the next line takes the absolute value of the spectrum - it doesn't matter.
        full_stft = np.concatenate((stft, stft[-2:0:-1, :]), axis=0)
        tmp = ifft(np.log(np.abs(full_stft)), axis=0)
        tmp = tmp.real[24:nfft // 2 + 1]
        return np.max(tmp, axis=0)
    
    def mtspect(self):
        tapered1 = maybe_cached_stft(self.args, 'dpss1')
        tapered2 = maybe_cached_stft(self.args, 'dpss2')
        return (np.abs(tapered1) ** 2 + np.abs(tapered2) ** 2) / 2

    def amplitude(self):
        s = self.mtspect()
        m_LogSum = np.sum(s[3:, :], axis=0)
        return 10 * (np.log10(m_LogSum))

    def entropy(self):
        s = self.mtspect()
        mean_log = np.mean(np.log(s[3:, :]), axis=0)
        log_mean = np.log(np.mean(s[3:, :], axis=0))
        return mean_log - log_mean

    def spectral_continuity(self):
        contours = self.frequency_contours()
        label_img = label(contours, connectivity=contours.ndim)
        props = regionprops(label_img)

        connection_mask = np.zeros(contours.shape, dtype=np.int32)
        continuity = np.zeros(contours.shape)

        for p in props:
            coords = p.coords
            y = coords[:, 0]
            x = coords[:, 1]

            num_pixels = len(coords)
            range_time = np.max(x) - np.min(x)
            continuity[(y, x)] = range_time
            if num_pixels > 5:
                connection_mask[(y, x)] = num_pixels
            else:
                connection_mask[(y, x)] = 0

        max_row_idx = np.argmax(connection_mask, axis=0)
        max_col_idx = np.arange(0, connection_mask.shape[1])

        max_continuity = connection_mask[(max_row_idx, max_col_idx)]

        continuity_at_max = continuity[(max_row_idx, max_col_idx)]
        continuity_frame = (continuity_at_max / max_continuity) * 100
        continuity_frame[np.where(np.isnan(continuity_frame))] = 0

        return continuity_frame

    def frequency_contours(self):
        derivs = self.spectral_derivative()
        derivs_abs = np.abs(derivs)

        row_thresh = 0.3 * np.mean(derivs_abs, axis=0)
        col_thresh = 100 * np.median(derivs_abs, axis=1)

        mask_row = derivs_abs <= row_thresh[None, :]
        mask_col = derivs_abs <= col_thresh[:, None]
        mask = (mask_row | mask_col)
        derivs[mask] = -0.1

        zcy, zcx = find_zc(derivs)
        contours = np.full(derivs.shape, False, dtype=np.bool)
        contours[zcy, zcx] = True

        return contours

    def mean_frequency(self):
        fs, nfft = unroll_args(self.args, ['fs', 'nfft'])
        s = self.mtspect()
        freq_range = nfft // 2 + 1
        idx = np.arange(freq_range)
        tmp = s * idx.reshape((freq_range, 1))
        x = np.sum(tmp, axis=0) / np.sum(s, axis=0) * fs / nfft
        return x

    def spectral_derivative(self):
        time_deriv, freq_deriv = self.cached_tf_derivatives()
        fm = self.frequency_modulation()

        cfm = np.cos(fm)
        sfm = np.sin(fm)
        spectral_deriv = (time_deriv * sfm + freq_deriv * cfm)

        spectral_deriv[0:3, :] = 0
        return spectral_deriv
