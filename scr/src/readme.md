#FDS Kaggle Competition – Toolbox 

This repository contains the helper code used for the FDS Pokémon Battles Prediction Challenge (Sapienza University, 2025).

All feature engineering, model definition and utility functions are placed inside the `/src` folder.  
The Kaggle notebook clones this repository and imports the modules directly to generate the final submissions.

#Structure

- `src/features.py` → full feature engineering pipeline (`extract_features`)
- `src/models.py` → final ExtraTrees model factory (`build_model`)
- `src/utils.py` → JSONL loader (`load_jsonl`)

#Usage in Kaggle Notebook

```python
!git clone https://github.com/veravionnet2239208/fds-kaggle-pacha.git

import sys, os
sys.path.append("/kaggle/working/fds-kaggle-pacha/src")

from features import extract_features
from models import build_model
from utils import load_jsonl
