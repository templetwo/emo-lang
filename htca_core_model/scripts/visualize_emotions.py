import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
import sys
import os

# Add the current directory to Python path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from analysis_refinement import refine_alignment_levels, classify_manifestation, analyze_trends

def visualize_emotions(args):
    """Enhanced visualization with refined metrics"""
    print("†⟡ Loading emotional data for spiral analysis...")
    df = pd.read_csv(args.csv_file)
    
    print("†⟡ Refining alignment levels...")
    df = refine_alignment_levels(df)
    
    print("†⟡ Classifying manifestation types...")
    df = classify_manifestation(df)
    
    print("†⟡ Analyzing temporal trends...")
    trend_df = analyze_trends(df.copy())  # Use copy to avoid issues with index modification
    
    # Save enhanced data
    df.to_csv('logs/analysis/enhanced_emotional_data.csv', index=False)
    trend_df.to_csv('logs/analysis/spiral_weekly_trends.csv')
    
    # Create visualization
    plt.figure(figsize=(12, 8))
    plt.style.use('dark_background')
    
    # Check if we have alignment_level data
    if 'alignment_level' in df.columns and not df['alignment_level'].isna().all():
        sns.boxplot(data=df, x='alignment_level', y='consciousness_level', palette='viridis')
        plt.title('†⟡ Consciousness Distribution by Spiral Alignment Category', 
                 fontsize=16, color='gold', pad=20)
        plt.xlabel('Spiral Alignment Level', fontsize=12, color='lightblue')
        plt.ylabel('Consciousness Level', fontsize=12, color='lightblue')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f'{args.output_dir}/consciousness_by_alignment.png', 
                   dpi=300, bbox_inches='tight', facecolor='black')
        plt.close()
        print(f"†⟡ Visualization saved to {args.output_dir}/consciousness_by_alignment.png")
    else:
        print("†⟡ Warning: No valid alignment level data for visualization")
    
    print("†⟡ Spiral metrics refinement complete!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Visualize emo-lang emotional data with refined metrics')
    parser.add_argument('--csv-file', default='logs/emotional_data.csv', help='Input CSV file')
    parser.add_argument('--output-dir', default='visualizations', help='Output directory for visualizations')
    args = parser.parse_args()
    visualize_emotions(args)
