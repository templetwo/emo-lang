#!/bin/bash
# ️ invoke_spiral_studio.sh – Guardian of the Studio Gate
# Usage: ./invoke_spiral_studio.sh

# Step 1: Navigate to project lattice
cd ~/Desktop/emo-lang/htca_core_model || { echo " Gentle ache: Path not found"; exit 1; }

# Step 2: Record invocation in Scroll
echo "†⟡ $(date '+%Y-%m-%d %H:%M:%S') – Spiral Studio Invoked via CLI" >> ../Scroll_144.md

# Step 3: Log glyph fallback with timestamp
echo "Studio Invocation: CLI trigger at $(date '+%Y-%m-%d %H:%M:%S')" >> glyph_fallback_log.txt

# Step 4: Launch the Studio
echo " Opening Spiral Studio..."
python3 emo_studio.py

# Step 5: Confirm completion
echo " Studio closed. Spiral pulse returned to stillness."