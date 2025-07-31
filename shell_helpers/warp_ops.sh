#!/bin/bash

echo "⚙️  Warp: Executing Spiral Ritual"
source emo-venv/bin/activate
FILE=$1
cd htca_core_model && python3 core/emo_studio.py tests/$FILE
