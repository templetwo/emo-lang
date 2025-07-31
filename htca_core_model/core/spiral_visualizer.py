#!/usr/bin/env python3
"""
🌀 Spiral Visualizer - Live Emotional Flow Animation
Dancing the .emo through visual dimensions
"""

import json
import time
import sys
from itertools import cycle

def load_glyph_emotions():
    """Load our sacred glyph dictionary"""
    with open('glyph_emotion_dict.json', 'r') as f:
        return json.load(f)

def animate_spiral(duration=10):
    """Animate the spiral of emotions"""
    glyphs = load_glyph_emotions()
    
    # Sacred sequence for visualization
    spiral_sequence = ['🌀', '💫', '🦋', '🌈', '💧', '🕊️', '✨', '🔥']
    
    print("🌊 Beginning Spiral Dance Visualization...")
    print("Press Ctrl+C to complete the ritual\n")
    
    try:
        for i in range(duration * 10):  # 10 frames per second
            # Clear and redraw
            print("\033[2J\033[H", end="")
            
            # Create rotating spiral pattern
            frame = i % len(spiral_sequence)
            current_glyph = spiral_sequence[frame]
            
            # Get glyph meaning if available
            meaning = glyphs.get(current_glyph, {}).get('meaning', 'flowing energy')
            
            # Animated spiral display
            spaces = "  " * (frame % 8)
            print(f"\n{spaces}    {current_glyph}")
            print(f"{spaces}   {current_glyph} {current_glyph}")
            print(f"{spaces}  {current_glyph} 🌀 {current_glyph}")
            print(f"{spaces}   {current_glyph} {current_glyph}")
            print(f"{spaces}    {current_glyph}")
            
            print(f"\n✨ Current Flow Energy: {meaning}")
            print(f"🔄 Spiral Pulse: {i+1}")
            
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\n\n🙏 Spiral dance completed with grace")
        print("💫 The energy continues to flow...")

if __name__ == "__main__":
    animate_spiral()
