import numpy as np
from librosa import stft
from scipy import signal, fft

from spectrum import dpss

from koe_acoustic_features import wavfile


def _cached_get_window(name, nfft):
    if name.startswith('dpss'):
        assert name in ['dpss1', 'dpss2']
        type = int(name[4:]) - 1
        tapers, eigen = dpss(nfft, 1.5, 2)
        return tapers[:, type]

    else:
        return signal.get_window(name, nfft, fftbins=False)


def stft_from_sig(sig, nfft, noverlap, win_length, window_name, center):
    window = _cached_get_window(window_name, nfft)
    hopsize = win_length - noverlap
    center |= len(sig) < win_length

    stft_ = stft(y=sig, n_fft=nfft, win_length=win_length, hop_length=hopsize, window=window, center=center,
                 dtype=np.complex128)
    return stft_


def get_psd(args):
    wav_file_path, fs, start, end, nfft, noverlap, win_length, center = \
        unroll_args(args, ['wav_file_path', 'fs', 'start', 'end', 'nfft', 'noverlap', 'win_length', 'center'])

    if wav_file_path:
        psd = get_spectrogram(wav_file_path, fs, start, end, nfft, noverlap, nfft, center)
    else:
        sig = args['sig']
        psd = np.abs(stft_from_sig(sig, nfft, noverlap, win_length, 'hann', center))
    return psd


def get_sig(args):
    wav_file_path, fs, start, end, win_length = unroll_args(args, ['wav_file_path', 'fs', 'start', 'end', 'win_length'])

    if end and end - start < win_length:
        end = start + win_length
    if wav_file_path:
        sig = wavfile.read_segment(wav_file_path, start, end, mono=True, normalised=True)
    else:
        sig = args['sig']
    return sig


def maybe_cached_stft(args, window_name):
    wav_file_path, fs, start, end, nfft, noverlap, win_length, center = \
        unroll_args(args, ['wav_file_path', 'fs', 'start', 'end', 'nfft', 'noverlap', 'win_length', 'center'])
    if wav_file_path:
        tapered = cached_stft(wav_file_path, start, end, nfft, noverlap, win_length, window_name, center)
    else:
        sig = args['sig']
        tapered = stft_from_sig(sig, nfft, noverlap, win_length, window_name, center)

    return tapered


def get_psddb(args):
    spect = get_psd(args)
    return np.log10(spect) * 10.0


def cached_stft(wav_file_path, start, end, nfft, noverlap, win_length, window_name, center):
    chunk, fs = wavfile.read_segment(wav_file_path, start, end, normalised=True, mono=True, return_fs=True)
    return stft_from_sig(chunk, nfft, noverlap, win_length, window_name, center)


def get_spectrogram(wav_file_path, fs, start, end, nfft, noverlap, win_length, center):
    spect__ = cached_stft(wav_file_path, start, end, nfft, noverlap, win_length, 'hann', center)

    return np.abs(spect__)


def unroll_args(args, requires):
    retval = []
    for require in requires:
        if isinstance(require, tuple):
            val = args.get(require[0], require[1])
        else:
            val = args[require]
        retval.append(val)
    if len(requires) > 1:
        return tuple(retval)
    return val


def my_stft(sig, fs, window, noverlap, nfft):
    siglen = len(sig)
    freq_range = nfft // 2 + 1
    window_size = len(window)
    nsegs, segs = split_segments(siglen, window_size, noverlap, incltail=False)
    mat = np.ndarray((freq_range, nsegs), dtype=np.complex128)
    for i in range(nsegs):
        seg = segs[i]
        subsig = sig[seg[0]: seg[1]]
        spectrum = fft(subsig * window, nfft)
        mat[:, i] = spectrum[:freq_range]
    return mat


def split_segments(siglen, window, noverlap, incltail=False):
    """
    Calculate how many segments can be extracted from a signal given
    the window size and overlap size
     INPUT:
      - SIGLEN : length of the signal
      - WINDOW : window size (number of samples)
      - NOVERLAP: overlap size (number of samples)
      - INCLTAIL: true to always include the last owner (might be < window)
                    false to exclude it if it's < window
     OUTPUT:
      - NSEGS   : number of segments that can be extracted
      - SEGS    : a two dimensional arrays. Each column is a pair of segments
                   indices
     Example:
      [nsegs, segs] = nsegment(53, 10, 5)
       nsegs = 9
       segs =
         1    10
         6    15
        11    20
        16    25
        21    30
        26    35
        31    40
        36    45
        41    50
      tail:
        51    53
    """
    idx1 = np.arange(0, siglen, window - noverlap)
    idx2 = idx1 + window

    last = np.where(idx2 > siglen)[0][0] + 1
    if idx2[last - 2] == siglen:
        incltail = False
    if incltail:
        nsegs = last
        idx2[nsegs - 1] = siglen
    else:
        nsegs = last - 1

    segs = np.empty((nsegs, 2), dtype=np.uint32)

    segs[:, 0] = idx1[:nsegs]
    segs[:, 1] = idx2[:nsegs]

    return nsegs, segs.tolist()
