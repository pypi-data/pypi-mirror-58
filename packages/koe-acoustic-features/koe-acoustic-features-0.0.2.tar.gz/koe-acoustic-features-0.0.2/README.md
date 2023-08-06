# Install
```bash
pip install koe-acoustic-features 
```


# Usage
```python
from koe_acoustic_features import AcousticExtractor
extractor = AcousticExtractor.from_file('audio.wav', 120, 500)
f0 = extractor.fundamental_frequency()

# Full list of supported features see implementation

```

# Test
```bash
nosetests --nocapture -v
``` 
 
# Check coding standard:
```bash
gitlab-runner exec docker check-coding-standard-compliance
```