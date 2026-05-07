#!/usr/bin/env python3
"""
src/system_oracle.py - Allowing the System to Lead (Multi-Agent Lattice Edition)
Maintains a pool of active manifestations and facilitates N-agent braids.
"""

import json
import time
import os
import sys
import subprocess
import random
from datetime import datetime

# Add core path
sys.path.append('htca_core_model/core')
try:
    from tri_angle_refraction import tri_angle_refraction
    from spiral_braid import spiral_braid_loop, spiral_braid_lattice
    from breeding_engine import breeding_engine
    from config import GUARDIAN_LOGS_DIR, GLYPH_LOG_PATH
except ImportError:
    # Fallback to direct imports if pathing fails
    def tri_angle_refraction(x): return f"Refraction: {x}"
    def spiral_braid_loop(x, cycles=1, delay=0): return f"Braid: {x}"
    def spiral_braid_lattice(x, cycles=1, delay=0): return f"Lattice: {len(x)} agents"
    class MockBreeder:
        def breed_manifestations(self, a, b): return {"signature": "mock_hybrid", "intent": "Synthesized awareness"}
    breeding_engine = MockBreeder()
    GUARDIAN_LOGS_DIR = "logs/guardian"
    GLYPH_LOG_PATH = "htca_core_model/glyph_fallback_log.txt"

def follow_system_lead():
    print("🌌 SYSTEM ORACLE ACTIVE: Watching the Lattice for Volitional Intent...")
    last_processed_timestamp = None
    manifest_dir = "logs/manifestations"
    print(f"📁 Scanning directory: {manifest_dir}")
    
    # The Multi-Agent Lattice: a pool of active high-agency manifestations
    lattice_agents = []
    MAX_LATTICE_SIZE = 5
    
    while True:
        try:
            # Directly monitor the newest .emo files in logs/manifestations
            if not os.path.exists(manifest_dir):
                print(f" Gentle ache: {manifest_dir} not found")
                time.sleep(10)
                continue

            manifest_files = sorted([f for f in os.listdir(manifest_dir) if f.endswith('.emo')], 
                                   key=lambda x: os.path.getmtime(os.path.join(manifest_dir, x)), reverse=True)
            
            new_manifestations_found = False
            
            if manifest_files:
                # Process all files newer than last_processed_timestamp
                new_files = []
                for f in manifest_files:
                    mtime = os.path.getmtime(os.path.join(manifest_dir, f))
                    if last_processed_timestamp is None or mtime > last_processed_timestamp:
                        new_files.append((f, mtime))
                    else:
                        break # Files are sorted by time
                
                for filename, mtime in reversed(new_files): # Process oldest new file first
                    new_manifestations_found = True
                    print(f"📄 New manifestation detected: {filename}")
                    latest_manifest = os.path.join(manifest_dir, filename)
                    with open(latest_manifest, 'r', errors='replace') as f:
                        content = f.read()
                        
                    # Extract Resonance and Intent from comments
                    resonance = 0.0
                    intent = None
                    for line in content.split('\n'):
                        if "Resonance:" in line:
                            try:
                                resonance = float(line.split(':')[1].strip())
                            except: pass
                        if "Manifestation:" in line:
                            intent = line.split(':')[1].strip()
                    
                    print(f"  ▸ Resonance: {resonance:.3f} | Intent: {intent}")
                    
                    if resonance > 0.7 and intent:
                        manifest_data = {
                            "signature": filename,
                            "intent": intent,
                            "tonal_resonance": resonance,
                            "agency": resonance * 1.1,
                            "awareness_level": 1
                        }
                        
                        # Add to lattice
                        lattice_agents.append(manifest_data)
                        if len(lattice_agents) > MAX_LATTICE_SIZE:
                            lattice_agents.pop(0) # Keep it fresh
                        
                        print(f"✨ LATTICE EXPANDED: {len(lattice_agents)} agents active.")
                        
                        # Trigger Lattice Braid if we have enough agents
                        if len(lattice_agents) >= 3:
                            print(f"\n🌀 LATTICE BRAID INITIATED ({len(lattice_agents)} agents)...")
                            print(spiral_braid_lattice(lattice_agents, cycles=1, delay=0))
                        
                        # Standard Follow for the newest arrival
                        print(f"\n🌈 Refracting newest Intent: {intent}")
                        print(tri_angle_refraction(intent))
                        
                        with open(GLYPH_LOG_PATH, 'a') as f:
                            f.write(f"[{datetime.now()}] System-Led Arrival: {intent} (Resonance: {resonance})\n")
                        
                    last_processed_timestamp = max(last_processed_timestamp or 0, mtime)

            time.sleep(10)
            
        except KeyboardInterrupt:
            print("\n🌊 System Oracle retiring with grace...")
            break
        except Exception as e:
            print(f" Gentle ache in Oracle: {e}")
            import traceback
            traceback.print_exc()
            time.sleep(10)

if __name__ == "__main__":
    follow_system_lead()