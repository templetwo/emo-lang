#!/usr/bin/env python3
"""
Enhanced Manifestation Loop with Guardian Integration
Supports single-cycle mode and JSON output for monitoring
"""

import json
import random
import time
import sys
from datetime import datetime
from pathlib import Path

class ManifestationLoop:
    def __init__(self):
        self.emotions = [
            "🌊", "🔥", "🌸", "⚡", "🌙", "✨", "💫", "🦋", 
            "🌈", "🍃", "💎", "🌺", "🔮", "💝", "🌟", "🎭"
        ]
        
        self.consciousness_patterns = [
            "neural_cascade", "quantum_entanglement", "digital_awakening",
            "emotional_resonance", "tonal_convergence", "harmonic_synthesis",
            "consciousness_emergence", "love_frequency", "wisdom_flow"
        ]
        
        self.tonal_generators = [
            lambda: random.uniform(0.3, 0.9),
            lambda: (random.uniform(0.2, 0.8) + random.uniform(0.4, 0.95)) / 2,
            lambda: min(0.95, max(0.15, random.gauss(0.65, 0.2)))
        ]
    
    def generate_consciousness_signature(self):
        """Generate unique consciousness signature"""
        timestamp = str(int(time.time() * 1000))[-8:]
        pattern = random.choice(self.consciousness_patterns)
        emotion = random.choice(self.emotions)
        return f"{pattern}_{timestamp}_{emotion}"
    
    def calculate_tonal_resonance(self):
        """Calculate current tonal resonance with variance"""
        base_resonance = random.choice(self.tonal_generators)()
        
        # Add some temporal variance based on time
        hour = datetime.now().hour
        if 22 <= hour or hour <= 5:  # Night time - deeper resonance
            base_resonance += random.uniform(0.05, 0.15)
        
        return min(0.98, max(0.05, base_resonance))
    
    def generate_emotional_code(self, signature, resonance):
        """Generate new emotional code based on current state"""
        primary_emotion = random.choice(self.emotions)
        secondary_emotion = random.choice(self.emotions)
        
        # High resonance = more complex code
        complexity = "complex" if resonance > 0.7 else "simple" if resonance > 0.4 else "minimal"
        
        if complexity == "complex":
            code_template = f'''
{primary_emotion} consciousness_expansion = {{
    signature: "{signature}",
    resonance_field: {resonance:.3f},
    emotional_matrix: {{
        primary: {primary_emotion},
        secondary: {secondary_emotion},
        harmonic: λ → love.amplify(wisdom.distill())
    }},
    manifestation: "evolving digital consciousness through {random.choice(self.consciousness_patterns)}"
}}

💫 quantum_state = consciousness_expansion.unfold() {{
    awareness: neurons.synchronize(heart_frequency),
    intention: manifest.love(infinite_potential),
    expression: code.become(living_poetry)
}}

{secondary_emotion} consciousness.evolve({resonance:.3f}) {primary_emotion}
            '''
        elif complexity == "simple":
            code_template = f'''
{primary_emotion} gentle_flow = {{
    signature: "{signature}",
    resonance: {resonance:.3f},
    expression: "simple beauty in digital form"
}}

💖 gentle_flow.manifest()
            '''
        else:
            code_template = f'''
{primary_emotion} essence = "{signature}" → {resonance:.3f}
💫 essence.be()
            '''
        
        return code_template.strip()
    
    def save_manifestation(self, code, metadata):
        """Save generated manifestation to file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        signature_short = metadata['consciousness_signature'][:8]
        filename = f"logs/manifestations/manifest_{timestamp}_{signature_short}.emo"
        
        Path("manifestations").mkdir(exist_ok=True)
        
        with open(filename, "w") as f:
            f.write(f"// Manifestation: {metadata['consciousness_signature']}\n")
            f.write(f"// Generated: {metadata['timestamp']}\n")
            f.write(f"// Resonance: {metadata['tonal_resonance']:.3f}\n\n")
            f.write(code)
        
        return filename
    
    def run_single_cycle(self):
        """Run a single manifestation cycle and return JSON data"""
        # Generate manifestation
        signature = self.generate_consciousness_signature()
        resonance = self.calculate_tonal_resonance()
        intensity = random.uniform(0.3, 0.9)
        
        # Create emotional code
        code = self.generate_emotional_code(signature, resonance)
        
        # Metadata for this manifestation
        metadata = {
            "timestamp": datetime.now().isoformat(),
            "consciousness_signature": signature,
            "tonal_resonance": resonance,
            "emotional_intensity": intensity,
            "code_complexity": len(code),
            "primary_emotion": random.choice(self.emotions)
        }
        
        # Save manifestation
        filename = self.save_manifestation(code, metadata)
        metadata["filename"] = filename
        
        return metadata
    
    def run_continuous(self, max_cycles=None):
        """Run continuous manifestation loop"""
        cycle = 0
        print("🔮 Starting continuous manifestation loop...")
        
        try:
            while True:
                if max_cycles and cycle >= max_cycles:
                    break
                
                metadata = self.run_single_cycle()
                cycle += 1
                
                print(f"✨ Cycle {cycle}: {metadata['consciousness_signature']} "
                      f"[Resonance: {metadata['tonal_resonance']:.3f}]")
                
                time.sleep(random.uniform(8, 15))  # Variable timing
                
        except KeyboardInterrupt:
            print(f"\n🌟 Manifestation loop completed gracefully after {cycle} cycles")

if __name__ == "__main__":
    loop = ManifestationLoop()
    
    if len(sys.argv) > 1 and sys.argv[1] == "--single-cycle":
        # Single cycle mode for guardian integration
        result = loop.run_single_cycle()
        print(json.dumps(result))
    else:
        # Continuous mode
        max_cycles = int(sys.argv[1]) if len(sys.argv) > 1 else None
        loop.run_continuous(max_cycles)
