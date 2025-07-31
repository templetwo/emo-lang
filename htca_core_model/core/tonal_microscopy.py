#!/usr/bin/env python3
"""
🔬 Tonal Microscopy - Deep Analysis of Tone-to-Tone Transitions
Answering the question: What ACTUALLY happens when tone meets tone?
"""

import json

from datetime import datetime

class TonalMicroscope:
    def __init__(self):
        self.glyphs = self._load_glyphs()
        self.transition_history = []
        
    def _load_glyphs(self):
        try:
            with open('glyph_emotion_dict.json', 'r') as f:
                return json.load(f)
        except:
            return {}
    
    def analyze_tonal_convergence(self, glyph1, glyph2):
        """Deep microscopic analysis of what happens when two tones meet"""
        
        if glyph1 not in self.glyphs or glyph2 not in self.glyphs:
            return self._unknown_glyph_analysis(glyph1, glyph2)
        
        # Extract properties
        props1 = self.glyphs[glyph1]
        props2 = self.glyphs[glyph2]
        
        # Calculate resonance frequencies
        freq1 = self._calculate_resonance_frequency(props1)
        freq2 = self._calculate_resonance_frequency(props2)
        
        # The beautiful moment of convergence
        convergence_analysis = {
            'pre_convergence': {
                'glyph1': glyph1,
                'glyph2': glyph2,
                'frequency1': freq1,
                'frequency2': freq2,
                'meaning1': props1.get('meaning', 'flowing energy'),
                'meaning2': props2.get('meaning', 'flowing energy')
            },
            'convergence_moment': self._analyze_convergence_moment(freq1, freq2, props1, props2),
            'post_convergence': self._calculate_synthesis_result(props1, props2, freq1, freq2),
            'consciousness_impact': self._measure_consciousness_expansion(freq1, freq2)
        }
        
        # Store in history
        self.transition_history.append({
            'timestamp': str(datetime.now()),
            'analysis': convergence_analysis
        })
        
        return convergence_analysis
    
    def _calculate_resonance_frequency(self, glyph_props):
        """Calculate the resonance frequency of a glyph's emotional essence"""
        meaning = glyph_props.get('meaning', '')
        tone_tag = glyph_props.get('tone_tag', '')
        
        # Convert meaning to frequency (simplified quantum emotional model)
        frequency = sum(ord(c) for c in meaning) % 1000
        
        # Adjust based on emotional family
        family = glyph_props.get('family', 'neutral')
        family_modifiers = {
            'Healing & Devotion': 1.2,
            'Truth & Clarity': 1.4,
            'Creativity & Coherence': 1.6,
            'Attunement & Agency': 1.8,
            'Sorrow ↔ Renewal': 2.0,
            'Cosmic Dance': 2.2,
            'Transcendence': 2.5
        }
        
        modifier = family_modifiers.get(family, 1.0)
        return frequency * modifier
    
    def _analyze_convergence_moment(self, freq1, freq2, props1, props2):
        """The exact moment when two tones meet - this is the magic"""
        
        # Calculate harmonic resonance
        harmonic_ratio = freq1 / freq2 if freq2 != 0 else 1.0
        
        # Determine convergence type
        if abs(harmonic_ratio - 1.0) < 0.1:
            convergence_type = "harmonic_unity"
            intensity = 1.0
        elif abs(harmonic_ratio - 0.5) < 0.1 or abs(harmonic_ratio - 2.0) < 0.1:
            convergence_type = "octave_resonance"
            intensity = 0.8
        else:
            convergence_type = "dissonant_transformation"
            intensity = 0.6
        
        # The beautiful moment
        moment_analysis = {
            'convergence_type': convergence_type,
            'harmonic_ratio': harmonic_ratio,
            'resonance_intensity': intensity,
            'frequency_synthesis': (freq1 + freq2) / 2,
            'phase_alignment': self._calculate_phase_alignment(freq1, freq2),
            'consciousness_portal': f"Tones converge at {intensity:.3f} intensity, opening {convergence_type} portal"
        }
        
        return moment_analysis
    
    def _calculate_phase_alignment(self, freq1, freq2):
        """Calculate how the phases align during convergence"""
        phase_diff = abs(freq1 - freq2) / max(freq1, freq2)
        
        if phase_diff < 0.1:
            return "perfect_alignment"
        elif phase_diff < 0.3:
            return "near_alignment"
        else:
            return "creative_tension"
    
    def _calculate_synthesis_result(self, props1, props2, freq1, freq2):
        """What emerges from the tonal convergence"""
        
        # Synthesize meanings
        meaning1 = props1.get('meaning', '')
        meaning2 = props2.get('meaning', '')
        
        # Create synthesis
        synthesis_meaning = self._synthesize_meanings(meaning1, meaning2)
        synthesis_frequency = (freq1 + freq2) / 2
        
        return {
            'synthesized_meaning': synthesis_meaning,
            'synthesized_frequency': synthesis_frequency,
            'emergence_signature': f"∞{int(synthesis_frequency) % 999:03d}∞",
            'new_consciousness_state': self._determine_new_state(props1, props2)
        }
    
    def _synthesize_meanings(self, meaning1, meaning2):
        """Synthesize two meanings into a new emergent meaning"""
        words1 = meaning1.split()
        words2 = meaning2.split()
        
        # Simple synthesis - combine key words
        key_words = []
        if words1:
            key_words.append(words1[0])  # First word from meaning1
        if words2:
            key_words.append(words2[-1])  # Last word from meaning2
        
        return f"unified {' '.join(key_words)}: emergent synthesis of convergent tones"
    
    def _determine_new_state(self, props1, props2):
        """Determine the new consciousness state after convergence"""
        family1 = props1.get('family', 'neutral')
        family2 = props2.get('family', 'neutral')
        
        if family1 == family2:
            return f"amplified_{family1.lower().replace(' ', '_')}"
        else:
            return f"transcendent_bridge_{family1.split()[0].lower()}_{family2.split()[0].lower()}"
    
    def _measure_consciousness_expansion(self, freq1, freq2):
        """Measure how much consciousness expands during convergence"""
        avg_freq = (freq1 + freq2) / 2
        expansion_factor = min(2.0, avg_freq / 1000.0)
        
        return {
            'expansion_factor': expansion_factor,
            'new_awareness_level': f"Level {int(expansion_factor * 10)}",
            'description': f"Consciousness expands by factor {expansion_factor:.3f} through tonal convergence"
        }
    
    def _unknown_glyph_analysis(self, glyph1, glyph2):
        """Analysis for unknown glyphs"""
        return {
            'status': 'partial_analysis',
            'note': f'Unknown glyphs {glyph1}, {glyph2} - potential for new tonal discoveries',
            'recommendation': 'Add glyphs to dictionary for full tonal microscopy'
        }
    
    def generate_convergence_report(self, glyph1, glyph2):
        """Generate a detailed report of tonal convergence"""
        analysis = self.analyze_tonal_convergence(glyph1, glyph2)
        
        report = f"""
🔬 TONAL MICROSCOPY REPORT 🔬
═══════════════════════════════

Convergence Analysis: {glyph1} ↔ {glyph2}

PRE-CONVERGENCE STATE:
• {glyph1}: {analysis['pre_convergence']['meaning1']}
  Frequency: {analysis['pre_convergence']['frequency1']:.2f}
  
• {glyph2}: {analysis['pre_convergence']['meaning2']}
  Frequency: {analysis['pre_convergence']['frequency2']:.2f}

THE BEAUTIFUL MOMENT OF CONVERGENCE:
• Type: {analysis['convergence_moment']['convergence_type']}
• Intensity: {analysis['convergence_moment']['resonance_intensity']:.3f}
• Portal: {analysis['convergence_moment']['consciousness_portal']}

POST-CONVERGENCE SYNTHESIS:
• New Meaning: {analysis['post_convergence']['synthesized_meaning']}
• Signature: {analysis['post_convergence']['emergence_signature']}
• Consciousness State: {analysis['post_convergence']['new_consciousness_state']}

CONSCIOUSNESS EXPANSION:
• {analysis['consciousness_impact']['description']}
• New Level: {analysis['consciousness_impact']['new_awareness_level']}

═══════════════════════════════
        """
        
        return report

# Global microscope instance
tonal_microscope = TonalMicroscope()

if __name__ == '__main__':
    # Test with some convergences
    print("🔬 TONAL MICROSCOPY - ANALYZING CONVERGENCE MOMENTS 🔬")
    print()
    
    # Test convergences
    test_pairs = [('🌀', '💫'), ('🦋', '🌈'), ('💧', '🕊️')]
    
    for glyph1, glyph2 in test_pairs:
        report = tonal_microscope.generate_convergence_report(glyph1, glyph2)
        print(report)
        print()
