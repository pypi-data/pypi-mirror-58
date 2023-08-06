# Install
```bash
pip install koe-acoustic-features 
```

# List of functions
 - normxcorr2
 - tictoc (as context)
 - sub2ind
 - ind2sub


# Usage
```python
from koe_acoustic_features import *

```

# Test
```bash
nosetests --nocapture -v
``` 
 
# Check coding standard:
```bash
gitlab-runner exec docker check-coding-standard-compliance
```