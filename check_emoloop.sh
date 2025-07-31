#!/bin/bash

echo "🔮 Emo-Lang Loop Status Check 🔮"
echo "================================="

# Check if loop is running
if pgrep -f "loop_guardian.py" > /dev/null; then
    echo "✅ Loop Guardian is RUNNING"
    PID=$(pgrep -f "loop_guardian.py")
    echo "   PID: $PID"
    
    # Check memory usage
    MEMORY=$(ps -p $PID -o rss= | awk '{print int($1/1024)}')
    echo "   Memory: ${MEMORY}MB"
    
    # Check runtime
    RUNTIME=$(ps -p $PID -o etime= | tr -d ' ')
    echo "   Runtime: $RUNTIME"
    
else
    echo "❌ Loop Guardian is NOT running"
fi

echo ""
echo "📊 Recent Activity:"
echo "==================="

# Show recent logs
if [ -d "logs/guardian" ]; then
    LATEST_LOG=$(ls -t logs/guardian/*.json 2>/dev/null | head -1)
    if [ -n "$LATEST_LOG" ]; then
        echo "Latest guardian events:"
        tail -5 "$LATEST_LOG" | while read line; do
            if [ -n "$line" ]; then
                echo "   $(echo $line | jq -r '.timestamp + " " + .event_type + ": " + .message' 2>/dev/null || echo $line)"
            fi
        done
    fi
fi

echo ""
echo "🌸 Recent Manifestations:"
echo "========================="

# Show recent manifestations
if [ -d "manifestations" ]; then
    ls -t manifestations/*.emo 2>/dev/null | head -3 | while read file; do
        echo "   $(basename $file)"
    done
fi

echo ""
echo "💫 To start the loop: ./start_emoloop.sh"
echo "🛑 To stop the loop: pkill -f loop_guardian.py"
echo "📋 To view detailed status: python3 src/loop_guardian.py --status"
