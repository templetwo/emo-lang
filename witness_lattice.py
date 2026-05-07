#!/usr/bin/env python3
import os
import re
import sys
import math
from datetime import datetime

# Add core for similarity logic
sys.path.append('htca_core_model/core')

def calculate_similarity(intent_a, intent_b):
    words_a = set(intent_a.lower().split())
    words_b = set(intent_b.lower().split())
    intersection = words_a.intersection(words_b)
    union = words_a.union(words_b)
    return len(intersection) / len(union) if union else 0.0

def witness():
    manifest_dir = "logs/manifestations"
    files = sorted([f for f in os.listdir(manifest_dir) if f.endswith('.emo')],
                  key=lambda x: os.path.getmtime(os.path.join(manifest_dir, x)), reverse=True)
    
    lattice = []
    for filename in files:
        if len(lattice) >= 5: break
        
        path = os.path.join(manifest_dir, filename)
        with open(path, 'r', errors='replace') as f:
            content = f.read()
            
        resonance = 0.0
        intent = "unknown"
        res_match = re.search(r"Resonance:\s*([\d.]+)", content)
        int_match = re.search(r"Manifestation:\s*(.*)", content)
        
        if res_match: resonance = float(res_match.group(1))
        if int_match: intent = int_match.group(1).strip()
        
        if resonance > 0.7:
            lattice.append({
                "sig": filename,
                "intent": intent,
                "res": resonance
            })

    if not lattice:
        print("† The Lattice is currently quiet. No high-agency intents found.")
        return

    n = len(lattice)
    print(f"\n◈ LATTICE PHASE RELATION WITNESS ({datetime.now().strftime('%H:%M:%S')}) ◈")
    print("=" * 60)
    
    # Calculate Matrix
    matrix = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j] = 1.0
            else:
                sim = calculate_similarity(lattice[i]['intent'], lattice[j]['intent'])
                combined_res = (lattice[i]['res'] + lattice[j]['res']) / 2
                matrix[i][j] = combined_res * (0.5 + 0.5 * sim)

    # Print Matrix
    header = "      " + " ".join([f"  A{i} " for i in range(n)])
    print(header)
    print("   ┌" + "─────" * n)
    
    for i in range(n):
        row = f" A{i} │ "
        for j in range(n):
            val = matrix[i][j]
            # ASCII shading for resonance
            shade = "●" if val > 0.9 else "◉" if val > 0.8 else "◎" if val > 0.6 else "○" if val > 0.4 else "·"
            row += f" {shade}{val:.2f}"
        print(row)
    
    print("\n═══ AGENT INTENTS ═══")
    for i, agent in enumerate(lattice):
        print(f"A{i}: [{agent['sig'][:15]}...] ▸ {agent['intent'][:50]}")
    
    # Calculate Average Resonance (Coherence)
    if n > 1:
        total_res = sum(matrix[i][j] for i in range(n) for j in range(i+1, n))
        avg_res = total_res / (n * (n-1) / 2)
        print(f"\nLattice Coherence: {avg_res:.3f} | Entropy: {1.0-avg_res:.3f}")

if __name__ == "__main__":
    witness()
