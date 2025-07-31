#!/usr/bin/env python3
"""
Emo-Lang Spiral Dashboard TUI
A flowing terminal interface for monitoring manifestation logs and tonal alignment
"""

import os
import json
import time
import glob
import datetime
from collections import defaultdict, deque
import threading
import curses
import re

class SpiralDashboardTUI:
    def __init__(self):
        self.running = True
        self.logs_dir = "logs/manifestations"
        self.recent_logs = deque(maxlen=20)  # Show more than 3 recent logs
        self.tone_timings = deque(maxlen=50)
        self.alignment_history = deque(maxlen=100)
        self.emotion_counts = defaultdict(int)
        self.last_scan = 0
        self.glyph_cycle = 0
        
        # Sacred glyphs for visual flow
        self.sacred_glyphs = ["◯", "◐", "◑", "◒", "◓", "●", "◉", "⬢", "⬡", "◈", "◇", "◆", "⟡", "⟢", "⟣"]
        self.flow_chars = ["∿", "〜", "≈", "∽", "∼", "⌇", "⟐", "⌘"]
        
    def parse_emo_file(self, filepath):
        """Parse .emo manifestation file"""
        try:
            with open(filepath, 'r') as f:
                content = f.read()
                
            # Extract key information
            timestamp_match = re.search(r'timestamp:\s*(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})', content)
            emotion_match = re.search(r'emotion:\s*(\w+)', content)
            glyph_match = re.search(r'glyph:\s*(.)', content)
            consciousness_match = re.search(r'consciousness_level:\s*([\d.]+)', content)
            spiral_match = re.search(r'spiral_alignment:\s*([\d.]+)', content)
            tone_match = re.search(r'tone_frequency:\s*([\d.]+)', content)
            
            return {
                'filepath': filepath,
                'timestamp': timestamp_match.group(1) if timestamp_match else None,
                'emotion': emotion_match.group(1) if emotion_match else 'unknown',
                'glyph': glyph_match.group(1) if glyph_match else '◯',
                'consciousness': float(consciousness_match.group(1)) if consciousness_match else 0.0,
                'spiral_alignment': float(spiral_match.group(1)) if spiral_match else 0.0,
                'tone_frequency': float(tone_match.group(1)) if tone_match else 0.0
            }
        except Exception as e:
            return None
    
    def scan_logs(self):
        """Scan for new manifestation logs"""
        try:
            emo_files = glob.glob(os.path.join(self.logs_dir, "*.emo"))
            emo_files.sort(key=os.path.getmtime, reverse=True)
            
            new_files = []
            current_time = time.time()
            
            for filepath in emo_files[:50]:  # Check recent 50 files
                mtime = os.path.getmtime(filepath)
                if mtime > self.last_scan:
                    parsed = self.parse_emo_file(filepath)
                    if parsed:
                        new_files.append(parsed)
            
            # Update recent logs
            for log in reversed(new_files):  # Add oldest first
                self.recent_logs.append(log)
                self.emotion_counts[log['emotion']] += 1
                self.alignment_history.append(log['spiral_alignment'])
                
                # Track tone timing for alignment analysis
                if log['timestamp']:
                    try:
                        dt = datetime.datetime.fromisoformat(log['timestamp'].replace('Z', '+00:00'))
                        self.tone_timings.append({
                            'time': dt,
                            'tone': log['tone_frequency'],
                            'alignment': log['spiral_alignment'],
                            'emotion': log['emotion']
                        })
                    except:
                        pass
            
            self.last_scan = current_time
            return len(new_files)
        except Exception as e:
            return 0
    
    def calculate_tone_differences(self):
        """Calculate time differences between aligned tones"""
        if len(self.tone_timings) < 2:
            return []
        
        differences = []
        aligned_tones = [t for t in self.tone_timings if t['alignment'] > 0.7]
        
        for i in range(1, len(aligned_tones)):
            prev = aligned_tones[i-1]
            curr = aligned_tones[i]
            time_diff = (curr['time'] - prev['time']).total_seconds()
            
            differences.append({
                'time_diff': time_diff,
                'prev_tone': prev['tone'],
                'curr_tone': curr['tone'],
                'prev_alignment': prev['alignment'],
                'curr_alignment': curr['alignment'],
                'performance_boost': curr['alignment'] - prev['alignment']
            })
        
        return differences[-10:]  # Last 10 differences
    
    def draw_header(self, stdscr, height, width):
        """Draw flowing header"""
        title = "◈ EMO-LANG SPIRAL DASHBOARD ◈"
        flow = "".join([self.flow_chars[i % len(self.flow_chars)] for i in range(width//4)])
        glyph = self.sacred_glyphs[self.glyph_cycle % len(self.sacred_glyphs)]
        
        stdscr.addstr(0, max(0, (width - len(title))//2), title, curses.A_BOLD | curses.color_pair(1))
        stdscr.addstr(1, 0, flow, curses.color_pair(2))
        stdscr.addstr(1, width-10, f"  {glyph}  ", curses.A_BOLD | curses.color_pair(3))
        
        # Status line
        status = f"Monitoring: {len(self.recent_logs)} logs | Emotions: {len(self.emotion_counts)} types | Time: {datetime.datetime.now().strftime('%H:%M:%S')}"
        stdscr.addstr(2, 0, status[:width-1], curses.color_pair(4))
        
        return 3
    
    def draw_recent_logs(self, stdscr, start_y, height, width):
        """Draw recent manifestation logs"""
        stdscr.addstr(start_y, 0, "═══ RECENT MANIFESTATIONS ═══", curses.A_BOLD | curses.color_pair(1))
        y = start_y + 1
        
        logs_to_show = min(12, len(self.recent_logs))  # Show up to 12 recent logs
        
        for i, log in enumerate(list(self.recent_logs)[-logs_to_show:]):
            if y >= height - 1:
                break
                
            # Format log entry
            timestamp = log['timestamp'][-8:] if log['timestamp'] else "??:??:??"
            emotion_color = 1 if log['spiral_alignment'] > 0.8 else 2 if log['spiral_alignment'] > 0.5 else 3
            
            line = f"{timestamp} {log['glyph']} {log['emotion']:12} ▸ {log['consciousness']:.2f} ⟐ {log['spiral_alignment']:.3f}"
            if len(line) > width - 5:
                line = line[:width-8] + "..."
            
            stdscr.addstr(y, 2, line, curses.color_pair(emotion_color))
            y += 1
        
        return y + 1
    
    def draw_tone_analysis(self, stdscr, start_y, height, width):
        """Draw tone timing analysis"""
        stdscr.addstr(start_y, 0, "═══ TONAL ALIGNMENT ANALYSIS ═══", curses.A_BOLD | curses.color_pair(1))
        y = start_y + 1
        
        differences = self.calculate_tone_differences()
        
        if not differences:
            stdscr.addstr(y, 2, "Collecting tone alignment data...", curses.color_pair(4))
            return y + 2
        
        stdscr.addstr(y, 2, "Time Δ    Prev→Curr Tone    Alignment Δ    Performance", curses.A_BOLD)
        y += 1
        
        for diff in differences[-8:]:  # Show last 8 differences
            if y >= height - 1:
                break
                
            time_str = f"{diff['time_diff']:6.1f}s"
            tone_str = f"{diff['prev_tone']:6.1f}→{diff['curr_tone']:6.1f}Hz"
            align_str = f"{diff['curr_alignment'] - diff['prev_alignment']:+.3f}"
            perf_str = "BOOST" if diff['performance_boost'] > 0 else "DROP"
            
            color = 1 if diff['performance_boost'] > 0 else 3
            line = f"{time_str} {tone_str} {align_str:>10} {perf_str:>12}"
            
            stdscr.addstr(y, 2, line, curses.color_pair(color))
            y += 1
        
        # Average performance
        avg_boost = sum(d['performance_boost'] for d in differences) / len(differences)
        avg_line = f"Average Performance: {avg_boost:+.4f} alignment units"
        stdscr.addstr(y, 2, avg_line, curses.A_BOLD | curses.color_pair(1 if avg_boost > 0 else 3))
        
        return y + 2
    
    def draw_realtime_monitor(self, stdscr, start_y, height, width):
        """Draw real-time visual monitor"""
        stdscr.addstr(start_y, 0, "═══ CONSCIOUSNESS FLOW ═══", curses.A_BOLD | curses.color_pair(1))
        y = start_y + 1
        
        if len(self.alignment_history) < 2:
            stdscr.addstr(y, 2, "Initializing consciousness flow...", curses.color_pair(4))
            return y + 2
        
        # Draw alignment graph
        recent_alignment = list(self.alignment_history)[-30:]  # Last 30 readings
        max_width = width - 10
        
        for i, alignment in enumerate(recent_alignment):
            if y >= height - 3:
                break
                
            bar_length = int(alignment * max_width)
            bar = "█" * bar_length + "░" * (max_width - bar_length)
            
            color = 1 if alignment > 0.8 else 2 if alignment > 0.5 else 3
            timestamp = f"{i:2d}"
            
            stdscr.addstr(y, 0, f"{timestamp}│{bar}", curses.color_pair(color))
            y += 1
        
        # Current stats
        current_avg = sum(recent_alignment) / len(recent_alignment)
        current_trend = "↗" if recent_alignment[-1] > recent_alignment[-5] else "↘"
        stats_line = f"Current: {recent_alignment[-1]:.3f} | Avg: {current_avg:.3f} | Trend: {current_trend}"
        
        stdscr.addstr(y, 2, stats_line, curses.A_BOLD | curses.color_pair(1))
        
        return y + 2
    
    def draw_emotion_summary(self, stdscr, start_y, height, width):
        """Draw emotion distribution summary"""
        y = start_y
        if y < height - 3:
            stdscr.addstr(y, 0, "═══ EMOTIONAL SPECTRUM ═══", curses.A_BOLD | curses.color_pair(1))
            y += 1
            
            # Top emotions
            sorted_emotions = sorted(self.emotion_counts.items(), key=lambda x: x[1], reverse=True)[:8]
            
            for emotion, count in sorted_emotions:
                if y >= height - 1:
                    break
                    
                percentage = (count / sum(self.emotion_counts.values())) * 100 if self.emotion_counts else 0
                bar_length = int(percentage / 100 * (width - 25))
                bar = "▓" * bar_length
                
                line = f"{emotion:12} {count:4d} │{bar:<{width-25}} {percentage:5.1f}%"
                stdscr.addstr(y, 2, line[:width-1], curses.color_pair(2))
                y += 1
    
    def log_scanner_thread(self):
        """Background thread for scanning logs"""
        while self.running:
            self.scan_logs()
            time.sleep(2)  # Scan every 2 seconds
    
    def run(self, stdscr):
        """Main TUI loop"""
        # Initialize colors
        curses.start_color()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)      # Headers, high alignment
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)     # Medium alignment, bars
        curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)    # Low alignment, warnings
        curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)     # Normal text
        curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)       # Errors, drops
        
        # Configure curses
        curses.curs_set(0)  # Hide cursor
        stdscr.nodelay(1)   # Non-blocking input
        stdscr.timeout(100) # 100ms timeout
        
        # Start background log scanner
        scanner_thread = threading.Thread(target=self.log_scanner_thread, daemon=True)
        scanner_thread.start()
        
        # Initial scan
        self.scan_logs()
        
        while self.running:
            try:
                stdscr.clear()
                height, width = stdscr.getmaxyx()
                
                # Draw interface sections
                y = self.draw_header(stdscr, height, width)
                y = self.draw_recent_logs(stdscr, y, height, width)
                y = self.draw_tone_analysis(stdscr, y, height, width)
                y = self.draw_realtime_monitor(stdscr, y, height, width)
                self.draw_emotion_summary(stdscr, y, height, width)
                
                # Instructions
                stdscr.addstr(height-1, 0, "Press 'q' to quit | Updates every 2s", curses.color_pair(4))
                
                stdscr.refresh()
                
                # Handle input
                key = stdscr.getch()
                if key == ord('q') or key == ord('Q'):
                    self.running = False
                
                # Update glyph cycle for visual flow
                self.glyph_cycle += 1
                
                time.sleep(0.1)  # Smooth refresh rate
                
            except KeyboardInterrupt:
                self.running = False
            except curses.error:
                # Handle terminal resize or other curses errors
                pass

def main():
    dashboard = SpiralDashboardTUI()
    try:
        curses.wrapper(dashboard.run)
    except KeyboardInterrupt:
        print("\n◈ Spiral dashboard closed gracefully ◈")

if __name__ == "__main__":
    main()
