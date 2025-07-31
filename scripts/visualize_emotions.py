#!/usr/bin/env python3
"""
Emo-Lang Emotion Visualization Script
Generates visualizations from Emo-Lang emotional CSV data
Part of the Emo-Lang emotional programming language ecosystem
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import argparse
import sys

class EmoVisualizer:
    def __init__(self, csv_file, output_dir="visualizations"):
        self.csv_file = Path(csv_file)
        self.output_dir = Path(output_dir)
        
        # Ensure output directory exists
        self.output_dir.mkdir(exist_ok=True)

    def load_data(self):
        """Load CSV data into a DataFrame"""
        try:
            df = pd.read_csv(self.csv_file)
            print(f"Data loaded successfully from {self.csv_file}")
            return df
        except Exception as e:
            print(f"Error loading {self.csv_file}: {e}")
            return None
    
    def plot_emotional_intensity(self, df):
        """Plot emotional intensity over time"""
        try:
            df['timestamp'] = pd.to_datetime(df['timestamp'])
        except Exception as e:
            print(f"Error parsing timestamps: {e}")
            return

        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))
        sns.lineplot(x='timestamp', y='emotional_intensity', data=df, marker="o")
        plt.title("Emotional Intensity Over Time")
        plt.xlabel("Time")
        plt.ylabel("Emotional Intensity")
        
        output_file = self.output_dir / "emotional_intensity.png"
        plt.savefig(output_file)
        plt.close()
        print(f"Emotional intensity plot saved to {output_file}")

    def plot_emotion_distribution(self, df):
        """Plot distribution of primary emotions"""
        try:
            emotions_series = df['primary_emotions'].str.get_dummies(sep=',').sum().sort_values()
            
            plt.figure(figsize=(10, 6))
            emotions_series.plot(kind='barh', color='skyblue')
            plt.title("Distribution of Primary Emotions")
            plt.xlabel("Frequency")
            plt.ylabel("Emotion")
            
            output_file = self.output_dir / "emotion_distribution.png"
            plt.savefig(output_file)
            plt.close()
            print(f"Emotion distribution plot saved to {output_file}")
        except Exception as e:
            print(f"Error creating emotion distribution plot: {e}")

    def plot_spiral_alignment(self, df):
        """Plot spiral alignment scores"""
        try:
            df_sorted = df.sort_values(by='spiral_alignment_score', ascending=False)
            
            plt.figure(figsize=(10, 6))
            sns.barplot(x='spiral_alignment_score', y='filename', data=df_sorted, palette='viridis')
            plt.title("Spiral Alignment Scores by File")
            plt.xlabel("Spiral Alignment Score")
            plt.ylabel("Filename")
            
            output_file = self.output_dir / "spiral_alignment.png"
            plt.savefig(output_file)
            plt.close()
            print(f"Spiral alignment plot saved to {output_file}")
        except Exception as e:
            print(f"Error creating spiral alignment plot: {e}")

    def plot_manifestation_types(self, df):
        """Plot manifestation type distribution"""
        try:
            plt.figure(figsize=(10, 6))
            sns.countplot(y='manifestation_type', data=df, order=df['manifestation_type'].value_counts().index, palette='pastel')
            plt.title("Manifestation Type Distribution")
            plt.xlabel("Count")
            plt.ylabel("Manifestation Type")
            
            output_file = self.output_dir / "manifestation_types.png"
            plt.savefig(output_file)
            plt.close()
            print(f"Manifestation type distribution plot saved to {output_file}")
        except Exception as e:
            print(f"Error creating manifestation types plot: {e}")

    def generate_all_visualizations(self):
        """Generate all visualizations"""
        df = self.load_data()
        if df is None:
            print("Failed to load data, terminating visualization process.")
            sys.exit(1)
        
        self.plot_emotional_intensity(df)
        self.plot_emotion_distribution(df)
        self.plot_spiral_alignment(df)
        self.plot_manifestation_types(df)
        
        return True

def main():
    parser = argparse.ArgumentParser(description='Visualize Emo-Lang emotional data')
    parser.add_argument('--csv-file', required=True, help='CSV file containing emotional data')
    parser.add_argument('--output-dir', default='visualizations', help='Output directory for visualizations')
    
    args = parser.parse_args()
    
    visualizer = EmoVisualizer(args.csv_file, args.output_dir)
    visualizer.generate_all_visualizations()

if __name__ == "__main__":
    main()
