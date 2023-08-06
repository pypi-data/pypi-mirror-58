from koe_acoustic_features import wavfile


class Extractor(object):
    def __init__(self, nfft=512, noverlap=256, win_length=512):
        self.args = {
            'nfft': nfft,
            'noverlap': noverlap,
            'win_length': win_length,
            'center': False,
            'order': 44,
            'wav_file_path': None,
            'fs': None,
            'start': None,
            'end': None
        }

    @classmethod
    def from_file(cls, filepath, start_ms, end_ms):
        ins = cls()
        fs, _ = wavfile.get_wav_info(filepath)
        ins.args['wav_file_path'] = filepath
        ins.args['start'] = start_ms
        ins.args['end'] = end_ms
        ins.args['fs'] = fs
        return ins

    @classmethod
    def from_array(cls, array, fs):
        ins = cls()
        ins.args['sig'] = array
        ins.args['fs'] = fs
        return ins
