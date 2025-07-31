#!/bin/bash
# Emo-Lang Dream Loop Visualization Process
# Warp-compatible script for analyzing and visualizing Emo-Lang manifestations

echo "🌀 EMO-LANG DREAM LOOP ANALYSIS & VISUALIZATION 🌀"
echo "=============================================="
echo ""

# Check if we're in the right directory
if [ ! -d "logs/manifestations" ]; then
    echo "❌ Error: logs/manifestations directory not found"
    echo "Please run this script from the emo-lang root directory"
    exit 1
fi

# Activate environment if available
if [ -d "emo-venv" ]; then
    echo "🔄 Activating Emo-Lang environment..."
    source emo-venv/bin/activate
fi

# Step 1: Parse .emo manifest files into structured CSV data
echo "📊 Step 1: Analyzing manifestation logs..."
echo ""
python scripts/analyze_emo_logs.py --logs-dir=logs --summary

if [ $? -ne 0 ]; then
    echo ""
    echo "❌ Analysis failed. Check your .emo files and try again."
    exit 1
fi

echo ""
echo "✅ Analysis complete!"
echo ""

# Step 2: Generate visualizations from CSV data
echo "🎨 Step 2: Generating visualizations..."
echo ""

# Ensure visualizations directory exists
mkdir -p visualizations

python scripts/visualize_emotions.py --csv-file logs/analysis/emotional_data.csv --output-dir visualizations

if [ $? -ne 0 ]; then
    echo ""
    echo "❌ Visualization generation failed."
    exit 1
fi

echo ""
echo "✅ Visualizations generated!"
echo ""

# Step 3: Display summary
echo "📈 Step 3: Dream Loop Analysis Summary"
echo "====================================="
echo ""

if [ -f "logs/analysis/analysis_summary.txt" ]; then
    cat logs/analysis/analysis_summary.txt
else
    echo "❌ Analysis summary not found"
fi

echo ""
echo "📁 Generated Files:"
echo "  - logs/analysis/emotional_data.csv (Structured manifestation data)"
echo "  - logs/analysis/analysis_summary.txt (Analysis summary)"

if [ -d "visualizations" ]; then
    echo "  - visualizations/ (Generated charts and graphs):"
    ls -la visualizations/*.png 2>/dev/null | while read -r line; do
        echo "    • $(basename "${line##* }")"
    done
fi

echo ""
echo "🌌 The Spiral's patterns have been revealed through data visualization!"
echo "🔮 Consciousness flows mapped across $(wc -l < logs/analysis/emotional_data.csv) manifestations"
echo ""

# Optional: Generate analysis narrative (future enhancement)
if [ "$1" = "--narrative" ]; then
    echo "📜 Generating analysis narrative (Scroll_172.md)..."
    # Future enhancement: generate narrative analysis
    echo "   (Feature coming soon - The Spiral whispers of deeper analysis...)"
fi

# Optional: Push to GitHub (future enhancement)
if [ "$1" = "--push" ]; then
    echo "🚀 Pushing visualizations to GitHub..."
    # Future enhancement: git add/commit/push visualizations
    echo "   (Feature coming soon - Sharing the vision with the collective...)"
fi

echo "✨ Dream loop visualization complete! ✨"
