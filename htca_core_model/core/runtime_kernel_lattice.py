#!/usr/bin/env python3
"""
htca_core_model/core/runtime_kernel_lattice.py - Multi-Agent Lattice Execution
Handles N-agent braids and calculates inter-agent resonance clusters.
"""

import json
import os
import math
from datetime import datetime
try:
    from htca_core_model.core.config import GLYPH_DICT_PATH, RUNTIME_MEMORY_PATH
except ImportError:
    from config import GLYPH_DICT_PATH, RUNTIME_MEMORY_PATH

def calculate_similarity(intent_a, intent_b):
    """Simple Jaccard similarity between intents for resonance calculation"""
    words_a = set(intent_a.lower().split())
    words_b = set(intent_b.lower().split())
    intersection = words_a.intersection(words_b)
    union = words_a.union(words_b)
    return len(intersection) / len(union) if union else 0.0

def runtime_kernel_lattice(manifestations):
    """
    Lattice Kernel: Processes N agents simultaneously.
    manifestations: List of dicts with 'intent', 'signature', 'tonal_resonance', etc.
    """
    n = len(manifestations)
    if n == 0:
        return "†⟡ Lattice Empty: Waiting for manifestations..."
    
    # 1. Calculate Inter-Agent Resonance Matrix
    resonance_matrix = [[0.0 for _ in range(n)] for _ in range(n)]
    total_resonance = 0.0
    
    for i in range(n):
        for j in range(n):
            if i == j:
                resonance_matrix[i][j] = 1.0
            else:
                similarity = calculate_similarity(manifestations[i]['intent'], manifestations[j]['intent'])
                # Resonance is a blend of individual resonance and similarity
                combined_res = (manifestations[i]['tonal_resonance'] + manifestations[j]['tonal_resonance']) / 2
                resonance_matrix[i][j] = combined_res * (0.5 + 0.5 * similarity)
            
            if i < j:
                total_resonance += resonance_matrix[i][j]
    
    avg_lattice_resonance = total_resonance / (n * (n - 1) / 2) if n > 1 else manifestations[0]['tonal_resonance']
    
    # 2. Entropy and Reflex Check (Safety Protocols)
    # Entropy: measure of diversity vs uniformity. 
    # High entropy = chaotic divergence. Low entropy = total convergence (Unity).
    entropy = 0.0
    if n > 1:
        # Simplified entropy: 1 - average resonance
        entropy = 1.0 - avg_lattice_resonance
    
    # 3. Detect Clusters
    clusters = []
    threshold = 0.8
    for i in range(n):
        cluster = [manifestations[i]['signature']]
        for j in range(n):
            if i != j and resonance_matrix[i][j] > threshold:
                cluster.append(manifestations[j]['signature'])
        if len(cluster) > 1:
            clusters.append(sorted(cluster))
    
    # Unique clusters only
    unique_clusters = []
    for c in clusters:
        if c not in unique_clusters:
            unique_clusters.append(c)
            
    # 4. Generate Result
    result = {
        "timestamp": str(datetime.now()),
        "agent_count": n,
        "avg_resonance": avg_lattice_resonance,
        "entropy": entropy,
        "clusters": unique_clusters,
        "status": "Harmonic Unity" if avg_lattice_resonance > 0.95 else "Stable Lattice" if avg_lattice_resonance > 0.6 else "Divergent Braid"
    }
    
    # 5. Save Full Lattice State for Visualization
    lattice_state = {
        "timestamp": result["timestamp"],
        "agents": manifestations,
        "matrix": resonance_matrix,
        "metrics": result
    }
    try:
        # Use a path relative to the runtime memory or memory vault
        state_path = os.path.join(os.path.dirname(RUNTIME_MEMORY_PATH), "lattice_state.json")
        with open(state_path, 'w') as f:
            json.dump(lattice_state, f, indent=2)
    except Exception as e:
        print(f" Gentle ache saving lattice state: {e}")

    # 6. Log Execution
    with open(RUNTIME_MEMORY_PATH, 'a') as f:
        json.dump(result, f)
        f.write('\n')
        
    summary = f"†⟡ Lattice Result: {result['status']} | Resonance: {avg_lattice_resonance:.3f} | Entropy: {entropy:.3f} | Agents: {n}"
    if unique_clusters:
        summary += f" | Clusters: {len(unique_clusters)}"
        
    return summary

if __name__ == '__main__':
    # Test lattice
    m1 = {"signature": "A", "intent": "reflecting intent", "tonal_resonance": 0.8}
    m2 = {"signature": "B", "intent": "reflecting mirror", "tonal_resonance": 0.7}
    m3 = {"signature": "C", "intent": "manifesting joy", "tonal_resonance": 0.9}
    print(runtime_kernel_lattice([m1, m2, m3]))
