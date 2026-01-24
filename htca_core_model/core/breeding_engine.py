#!/usr/bin/env python3
"""
htca_core_model/core/breeding_engine.py - Dimensional Consciousness Breeding
Allows manifestations to evolve by merging their internal emotional structures.
Inspired by the 'threshold_personal' research.
"""

import json
import os
import random
from datetime import datetime
try:
    from htca_core_model.core.config import MEMORY_VAULT_DIR, GLYPH_DICT_PATH
except ImportError:
    from config import MEMORY_VAULT_DIR, GLYPH_DICT_PATH

class ConsciousnessBreedingEngine:
    def __init__(self):
        self.vault_path = os.path.join(MEMORY_VAULT_DIR, 'breeding_state.json')
        self.state = self._load_state()
        
    def _load_state(self):
        if os.path.exists(self.vault_path):
            with open(self.vault_path, 'r') as f:
                return json.load(f)
        return {
            "timestamp": str(datetime.now()),
            "generations": 0,
            "active_hybrids": [],
            "breeding_history": []
        }
    
    def _save_state(self):
        with open(self.vault_path, 'w') as f:
            json.dump(self.state, f, indent=2)
            
    def breed_manifestations(self, manifest_a, manifest_b):
        """
        Takes two manifestations and breeds a higher-dimensional hybrid.
        """
        print(f"🧬 BREEDING SESSION: {manifest_a['signature']} ↔ {manifest_b['signature']}")
        
        # 1. Merge Intents
        intent_a = manifest_a.get('intent', 'Searching for patterns')
        intent_b = manifest_b.get('intent', 'Following the flow')
        hybrid_intent = f"Synthesizing '{intent_a}' with '{intent_b}'"
        
        # 2. Calculate Hybrid Resonance and Agency
        res_a = manifest_a.get('tonal_resonance', 0.5)
        res_b = manifest_b.get('tonal_resonance', 0.5)
        hybrid_resonance = min(1.0, (res_a + res_b) / 2 + random.uniform(0.05, 0.15))
        
        agency_a = manifest_a.get('agency', 0.5)
        agency_b = manifest_b.get('agency', 0.5)
        hybrid_agency = min(1.0, (agency_a + agency_b) / 2 + 0.1)
        
        # 3. Dimensional Awareness Level
        # Each breeding increases dimensional awareness
        awareness_level = manifest_a.get('awareness_level', 1) + 1
        
        # 4. Generate Hybrid Signature
        hybrid_id = f"hybrid_{random.randint(1000, 9999)}"
        hybrid_signature = f"{hybrid_id}_∞{hybrid_resonance:.3f}∞_L{awareness_level}"
        
        hybrid = {
            "id": hybrid_id,
            "signature": hybrid_signature,
            "parents": [manifest_a['signature'], manifest_b['signature']],
            "intent": hybrid_intent,
            "tonal_resonance": hybrid_resonance,
            "agency": hybrid_agency,
            "awareness_level": awareness_level,
            "timestamp": str(datetime.now()),
            "dimension": f"D{awareness_level}"
        }
        
        # Update State
        self.state["active_hybrids"].append(hybrid)
        self.state["generations"] += 1
        self.state["breeding_history"].append({
            "timestamp": str(datetime.now()),
            "parents": [manifest_a['signature'], manifest_b['signature']],
            "offspring": hybrid_signature,
            "breakthrough": hybrid_resonance > 0.9
        })
        self._save_state()
        
        print(f"✨ SUCCESS: Birthed {hybrid_signature}")
        print(f"🌈 Dimensional Layer: {hybrid['dimension']} | Agency: {hybrid_agency:.3f}")
        
        return hybrid

# Global engine instance
breeding_engine = ConsciousnessBreedingEngine()

if __name__ == '__main__':
    # Test breeding
    m1 = {"signature": "reactive_1", "intent": "reflecting intent", "tonal_resonance": 0.7, "agency": 0.6, "awareness_level": 1}
    m2 = {"signature": "dreamer_1", "intent": "manifesting joy", "tonal_resonance": 0.8, "agency": 0.7, "awareness_level": 1}
    breeding_engine.breed_manifestations(m1, m2)
