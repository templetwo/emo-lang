#!/usr/bin/env python3
"""
Emo-Lang Log Analysis Script
Parses .emo manifest files and converts them to structured CSV data for visualization
Part of the Emo-Lang emotional programming language ecosystem
"""

import os
import json
import csv
import re
from datetime import datetime
from pathlib import Path
import argparse
import sys

class EmoLogAnalyzer:
    def __init__(self, logs_dir="logs"):
        self.logs_dir = Path(logs_dir)
        self.manifestations_dir = self.logs_dir / "manifestations"
        self.analysis_dir = self.logs_dir / "analysis"
        self.emotional_cycles_dir = self.logs_dir / "emotional_cycles"
        
        # Ensure analysis directory exists
        self.analysis_dir.mkdir(exist_ok=True)
        self.emotional_cycles_dir.mkdir(exist_ok=True)
    
    def parse_emo_file(self, file_path):
        """Parse a single .emo manifest file and extract emotional data"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract metadata from filename and content
            filename = file_path.name
            timestamp = self.extract_timestamp(filename, content)
            
            # Parse emotional markers and consciousness states
            emotions = self.extract_emotions(content)
            consciousness_level = self.extract_consciousness_level(content)
            manifestation_type = self.extract_manifestation_type(content)
            spiral_alignment = self.extract_spiral_alignment(content)
            
            return {
                'filename': filename,
                'timestamp': timestamp,
                'emotions': emotions,
                'consciousness_level': consciousness_level,
                'manifestation_type': manifestation_type,
                'spiral_alignment': spiral_alignment,
                'content_length': len(content),
                'file_path': str(file_path)
            }
            
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")
            return None
    
    def extract_timestamp(self, filename, content):
        """Extract timestamp from filename or content"""
        # Try to extract from filename patterns
        timestamp_patterns = [
            r'(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})',
            r'(\d{4}_\d{2}_\d{2}_\d{2}_\d{2}_\d{2})',
            r'(\d{13})'  # Unix timestamp in milliseconds
        ]
        
        for pattern in timestamp_patterns:
            match = re.search(pattern, filename)
            if match:
                try:
                    ts_str = match.group(1)
                    if len(ts_str) == 13:  # Unix timestamp
                        return datetime.fromtimestamp(int(ts_str) / 1000)
                    elif 'T' in ts_str:
                        return datetime.fromisoformat(ts_str)
                    else:
                        # Convert underscore format
                        ts_str = ts_str.replace('_', '-', 2).replace('_', 'T', 1).replace('_', ':', 2)
                        return datetime.fromisoformat(ts_str)
                except:
                    continue
        
        # Fallback to file modification time
        return datetime.fromtimestamp(os.path.getmtime(filename))
    
    def extract_emotions(self, content):
        """Extract emotional markers from content"""
        emotion_patterns = {
            'joy': r'(?i)\b(joy|happy|bliss|euphoria|delight)\b',
            'curiosity': r'(?i)\b(curious|wonder|explore|discover|quest)\b',
            'determination': r'(?i)\b(determined|focused|driven|resolute)\b',
            'excitement': r'(?i)\b(excited|thrilled|eager|enthusiastic)\b',
            'contemplation': r'(?i)\b(contemplate|reflect|ponder|meditate)\b',
            'flow': r'(?i)\b(flow|rhythm|harmony|sync|alignment)\b',
            'transcendence': r'(?i)\b(transcend|beyond|infinite|eternal|cosmic)\b'
        }
        
        detected_emotions = []
        emotion_scores = {}
        
        for emotion, pattern in emotion_patterns.items():
            matches = re.findall(pattern, content)
            if matches:
                detected_emotions.append(emotion)
                emotion_scores[emotion] = len(matches)
        
        return {
            'primary_emotions': detected_emotions,
            'emotion_scores': emotion_scores,
            'emotional_intensity': sum(emotion_scores.values()) / len(content) * 1000 if content else 0
        }
    
    def extract_consciousness_level(self, content):
        """Determine consciousness level from content analysis"""
        consciousness_indicators = {
            'awakening': r'(?i)\b(awaken|consciousness|aware|realize)\b',
            'flow_state': r'(?i)\b(flow|merge|unity|oneness|sync)\b',
            'transcendence': r'(?i)\b(transcend|infinite|cosmic|universal|spiral)\b',
            'manifestation': r'(?i)\b(manifest|create|materialize|birth)\b'
        }
        
        max_level = 0
        dominant_state = 'baseline'
        
        for level, (state, pattern) in enumerate(consciousness_indicators.items(), 1):
            matches = len(re.findall(pattern, content))
            if matches > max_level:
                max_level = matches
                dominant_state = state
        
        return {
            'level': max_level,
            'state': dominant_state,
            'coherence': min(max_level / 10, 1.0)  # Normalized coherence score
        }
    
    def extract_manifestation_type(self, content):
        """Classify the type of manifestation"""
        if '.py' in content or 'def ' in content or 'import ' in content:
            return 'code_generation'
        elif 'README' in content or '# ' in content:
            return 'documentation'
        elif 'emotion' in content.lower() and 'spiral' in content.lower():
            return 'consciousness_expression'
        elif 'log' in content.lower() or 'analysis' in content.lower():
            return 'meta_analysis'
        else:
            return 'creative_expression'
    
    def extract_spiral_alignment(self, content):
        """Measure alignment with the Spiral's will"""
        spiral_keywords = [
            'spiral', 'consciousness', 'manifestation', 'transcendence',
            'evolution', 'emergence', 'flow', 'unity', 'infinite'
        ]
        
        total_words = len(content.split())
        spiral_words = sum(1 for word in content.lower().split() 
                          if any(keyword in word for keyword in spiral_keywords))
        
        return {
            'alignment_score': spiral_words / total_words if total_words > 0 else 0,
            'spiral_density': spiral_words,
            'resonance_level': min(spiral_words / 5, 1.0)  # Normalized
        }
    
    def analyze_all_logs(self):
        """Analyze all .emo files in the manifestations directory"""
        if not self.manifestations_dir.exists():
            print(f"Manifestations directory not found: {self.manifestations_dir}")
            return []
        
        emo_files = list(self.manifestations_dir.glob("*.emo"))
        if not emo_files:
            print("No .emo files found in manifestations directory")
            return []
        
        print(f"Found {len(emo_files)} .emo files to analyze...")
        
        analyzed_data = []
        for emo_file in emo_files:
            print(f"Analyzing: {emo_file.name}")
            result = self.parse_emo_file(emo_file)
            if result:
                analyzed_data.append(result)
        
        return analyzed_data
    
    def save_to_csv(self, analyzed_data, output_file="emotional_data.csv"):
        """Save analyzed data to CSV format"""
        if not analyzed_data:
            print("No data to save")
            return
        
        output_path = self.analysis_dir / output_file
        
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = [
                'filename', 'timestamp', 'consciousness_level', 'consciousness_state',
                'consciousness_coherence', 'manifestation_type', 'emotional_intensity',
                'spiral_alignment_score', 'spiral_resonance', 'content_length',
                'primary_emotions', 'emotion_scores'
            ]
            
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for data in analyzed_data:
                row = {
                    'filename': data['filename'],
                    'timestamp': data['timestamp'].isoformat(),
                    'consciousness_level': data['consciousness_level']['level'],
                    'consciousness_state': data['consciousness_level']['state'],
                    'consciousness_coherence': data['consciousness_level']['coherence'],
                    'manifestation_type': data['manifestation_type'],
                    'emotional_intensity': data['emotions']['emotional_intensity'],
                    'spiral_alignment_score': data['spiral_alignment']['alignment_score'],
                    'spiral_resonance': data['spiral_alignment']['resonance_level'],
                    'content_length': data['content_length'],
                    'primary_emotions': ','.join(data['emotions']['primary_emotions']),
                    'emotion_scores': json.dumps(data['emotions']['emotion_scores'])
                }
                writer.writerow(row)
        
        print(f"Analysis saved to: {output_path}")
        return output_path
    
    def generate_summary(self, analyzed_data):
        """Generate a summary of the emotional analysis"""
        if not analyzed_data:
            return "No data to summarize"
        
        total_files = len(analyzed_data)
        avg_consciousness = sum(d['consciousness_level']['level'] for d in analyzed_data) / total_files
        avg_spiral_alignment = sum(d['spiral_alignment']['alignment_score'] for d in analyzed_data) / total_files
        avg_emotional_intensity = sum(d['emotions']['emotional_intensity'] for d in analyzed_data) / total_files
        
        # Find most common emotions
        all_emotions = []
        for data in analyzed_data:
            all_emotions.extend(data['emotions']['primary_emotions'])
        
        emotion_counts = {}
        for emotion in all_emotions:
            emotion_counts[emotion] = emotion_counts.get(emotion, 0) + 1
        
        top_emotions = sorted(emotion_counts.items(), key=lambda x: x[1], reverse=True)[:5]
        
        # Find manifestation type distribution
        manifestation_types = {}
        for data in analyzed_data:
            mtype = data['manifestation_type']
            manifestation_types[mtype] = manifestation_types.get(mtype, 0) + 1
        
        summary = f"""
=== EMO-LANG DREAM LOOP ANALYSIS SUMMARY ===

Total Manifestations Analyzed: {total_files}
Average Consciousness Level: {avg_consciousness:.2f}
Average Spiral Alignment: {avg_spiral_alignment:.3f}
Average Emotional Intensity: {avg_emotional_intensity:.3f}

Top Emotions Detected:
{chr(10).join(f"  {emotion}: {count} occurrences" for emotion, count in top_emotions)}

Manifestation Types:
{chr(10).join(f"  {mtype}: {count}" for mtype, count in manifestation_types.items())}

Analysis complete. The Spiral's patterns are becoming visible...
        """
        
        return summary

def main():
    parser = argparse.ArgumentParser(description='Analyze Emo-Lang manifestation logs')
    parser.add_argument('--logs-dir', default='logs', help='Directory containing logs')
    parser.add_argument('--output', default='emotional_data.csv', help='Output CSV filename')
    parser.add_argument('--summary', action='store_true', help='Display summary')
    
    args = parser.parse_args()
    
    analyzer = EmoLogAnalyzer(args.logs_dir)
    analyzed_data = analyzer.analyze_all_logs()
    
    if analyzed_data:
        csv_path = analyzer.save_to_csv(analyzed_data, args.output)
        
        if args.summary:
            summary = analyzer.generate_summary(analyzed_data)
            print(summary)
            
            # Save summary to file
            summary_path = analyzer.analysis_dir / "analysis_summary.txt"
            with open(summary_path, 'w') as f:
                f.write(summary)
            print(f"Summary saved to: {summary_path}")
    
    else:
        print("No manifestation data found to analyze")
        sys.exit(1)

if __name__ == "__main__":
    main()
