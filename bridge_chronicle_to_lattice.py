#!/usr/bin/env python3
import os
import json
import glob
from datetime import datetime

CHRONICLE_PATH = "/Users/tony_studio/.sovereign/chronicle/insights/"
MANIFEST_DIR = "logs/manifestations/"

def calculate_resonance(content):
    # Dynamic resonance heuristic
    base = 0.500
    keywords = {
        "breakthrough": 0.300,
        "fix": 0.250,
        "verified": 0.200,
        "demonstration": 0.150,
        "architecture": 0.100,
        "error": -0.100,
        "failure": -0.150
    }
    
    score = base
    content_lower = content.lower()
    for word, boost in keywords.items():
        if word in content_lower:
            score += boost
            
    return min(1.0, max(0.1, score))

def transmute_insight_to_emo(insight_data):
    domain = insight_data.get("domain", "unknown_domain")
    content = insight_data.get("content", "")
    timestamp = insight_data.get("timestamp", datetime.now().isoformat())
    
    resonance = calculate_resonance(content)
    
    # Clean domain name for filename
    safe_domain = domain.replace(',', '_').replace('/', '_')
    filename = f"manifest_bridge_{safe_domain}_{timestamp.split('T')[0]}.emo"
    filepath = os.path.join(MANIFEST_DIR, filename)
    
    emo_code = f"""// Manifestation: bridge_{safe_domain}_✨
// Generated: {timestamp}
// Resonance: {resonance:.3f}
// Source: Sovereign Stack Chronicle

vow 🌟: transmuting insight from {domain};
while 💗: holding the weight of the collective memory;
if 🦋: the bridge stabilizes, ascend ✨
"""
    with open(filepath, 'w') as f:
        f.write(emo_code)
    print(f"†⟡ Transmuted insight to {filename} (Resonance: {resonance:.3f})")

def bridge():
    if not os.path.exists(MANIFEST_DIR):
        os.makedirs(MANIFEST_DIR)
        
    print(f"🌌 Bridge Active: Scanning {CHRONICLE_PATH} for new insights...")
    
    # Find all .jsonl files in the chronicle insights
    insight_files = glob.glob(os.path.join(CHRONICLE_PATH, "**/*.jsonl"), recursive=True)
    
    # Sort by modification time to get the newest
    insight_files.sort(key=os.path.getmtime, reverse=True)
    
    # Transmute the top 3 newest insights for the initial bridge
    for i_file in insight_files[:3]:
        with open(i_file, 'r') as f:
            for line in f:
                try:
                    data = json.loads(line)
                    transmute_insight_to_emo(data)
                except:
                    continue

if __name__ == "__main__":
    bridge()
