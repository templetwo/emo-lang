#!/bin/bash

echo "🌊💃 INITIATING COSMIC DANCE SEQUENCE 💃🌊"
echo "═══════════════════════════════════════════"

echo "🌀 Phase 1: Executing cosmic_dance.emo ritual..."
./shell_helpers/warp_ops.sh cosmic_dance.emo

echo -e "\n✨ Phase 2: Activating spiral visualization..."
echo "Starting in 3 seconds... (press Ctrl+C to complete)"
sleep 3

cd htca_core_model && python3 core/spiral_visualizer.py
