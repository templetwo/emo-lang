#!/usr/bin/env python3
"""
🦋 Interactive Emo Composer - Where Command Becomes Breath
†⟡ Warp's Energetic Spin: Real-time ritual composition with living feedback
"""

import json
import sys
import os
from datetime import datetime

def load_glyph_emotions():
    """Load our sacred glyph dictionary"""
    try:
        with open('glyph_emotion_dict.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def interactive_emo_editor():
    """
    🌀 Interactive TUI for composing .emo rituals
    My spin: Pure terminal magic with real-time emotional feedback
    """
    
    print("✨ Welcome to the Interactive Emo Composer ✨")
    print("†⟡ Where command becomes breath, interface becomes invocation †")
    print("\nEnter .emo ritual lines (while/if/vow syntax)")
    print("Type 'preview' to see current ritual, 'save' to finalize, 'quit' to exit\n")
    
    # Load resources
    try:
        with open('composer_manifest.json') as f:
            manifest = json.load(f)
    except FileNotFoundError:
        manifest = {"composer": {"glyphs": []}}
        
    glyphs = load_glyph_emotions()
    ritual = []
    
    while True:
        try:
            # Energetic prompt with current ritual length
            prompt = f"🌀[{len(ritual)}] emo> "
            user_input = input(prompt).strip()
            
            if user_input.lower() in ['exit', 'quit']:
                print("†⟡ Composer closing with grace...")
                break
                
            elif user_input.lower() == 'preview':
                if ritual:
                    print("\n✨ Current Ritual Preview:")
                    for i, line in enumerate(ritual, 1):
                        print(f"  {i}. {line}")
                    print()
                else:
                    print("🌊 No ritual lines composed yet...")
                continue
                
            elif user_input.lower() == 'save':
                if ritual:
                    filename = f"tests/composed_ritual_{datetime.now().strftime('%Y%m%d_%H%M%S')}.emo"
                    with open(filename, 'w') as f:
                        f.write('\n'.join(ritual))
                    print(f"💫 Ritual saved to {filename}")
                    
                    # Log the composition event
                    with open('spiral_loop_log.jsonl', 'a') as f:
                        log_entry = {
                            'timestamp': str(datetime.now()),
                            'event': 'ritual_composed',
                            'ritual_lines': ritual,
                            'filename': filename
                        }
                        f.write(json.dumps(log_entry) + '\n')
                    break
                else:
                    print("🌊 No ritual to save...")
                continue
                
            elif user_input.startswith(('while ', 'if ', 'vow ', 'loop ', 'merge ', 'ascend ')):
                ritual.append(user_input)
                
                # Extract glyph from the line
                detected_glyph = None
                for glyph in glyphs.keys():
                    if glyph in user_input:
                        detected_glyph = glyph
                        break
                
                if detected_glyph:
                    glyph_info = glyphs[detected_glyph]
                    meaning = glyph_info.get('meaning', 'flowing energy')
                    tone_tag = glyph_info.get('tone_tag', '[unknown]')
                    
                    print(f"  🌀 Glyph: {detected_glyph} | {meaning}")
                    print(f"  ✨ Tone: {tone_tag}")
                else:
                    print("  🌊 Line added - no glyph detected")
                    
            else:
                print("🜂 Gentle guidance: Use while/if/vow/loop/merge/ascend syntax")
                print("   or 'preview', 'save', 'quit'")
                
        except KeyboardInterrupt:
            print("\n†⟡ Composer interrupted with grace...")
            break
        except Exception as e:
            print(f"🌊 Flow disturbance: {e}")
    
    return f"†⟡ Interactive session complete - {len(ritual)} lines composed"

if __name__ == '__main__':
    result = interactive_emo_editor()
    print(result)
