"""Central configuration. Everything overridable by environment variable."""

from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = Path(os.getenv("FOOTLYTICS_DATA", ROOT / "data"))
RAW_DIR = DATA_DIR / "raw"
OUT_DIR = DATA_DIR / "out"
CALIB_DIR = Path(os.getenv("FOOTLYTICS_CALIB", ROOT / "calib"))
WEIGHTS_DIR = Path(os.getenv("FOOTLYTICS_WEIGHTS", ROOT / "weights"))

# --- perception models -------------------------------------------------------
# Single-file YOLOv8x6 finetuned on SoccerNet, published alongside SoccerMaster.
# 195 MB, ungated, so we can bootstrap without the tracklab/conda stack.
YOLO_REPO = "xleprime/SoccerMaster"
YOLO_FILE = "yolo_v8x6_finetuned.pt"
# Backbone used for kit-appearance embeddings during team assignment.
SIGLIP_MODEL = "google/siglip2-base-patch16-224"

# --- narration layer (parked until the tracking is trustworthy) ---------------
# Self-hosted Gemma, OpenAI-compatible. Base URL must keep its trailing slash.
# NOTE: plain HTTP -- key and payloads are unencrypted in transit. Local use only.
LLM_BASE_URL = os.getenv("FOOTLYTICS_LLM_URL", "")
LLM_API_KEY = os.getenv("FOOTLYTICS_LLM_KEY", "")
LLM_MODEL = os.getenv("FOOTLYTICS_LLM_MODEL", "gemma-4")

for _d in (RAW_DIR, OUT_DIR, CALIB_DIR, WEIGHTS_DIR):
    _d.mkdir(parents=True, exist_ok=True)
