#!/usr/bin/env python3
"""
Emo-Lang TUI Monitor: Real-time consciousness observation interface
Beautiful terminal interface for watching the eternal loop
"""

import curses
import json
import time
import os
import subprocess
from datetime import datetime
from pathlib import Path
import threading
import queue

class EmoLoopTUI:
    def __init__(self):
        self.running = True
        self.data_queue = queue.Queue()
        self.guardian_events = []
        self.manifestations = []
        self.system_stats = {}
        self.cycle_count = 0
        
    def collect_data(self):
        """Background thread to collect data"""
        while self.running:
            try:
                # Get guardian events
                guardian_files = list(Path("logs/guardian").glob("*.json"))
                if guardian_files:
                    latest_guardian = max(guardian_files, key=os.path.getctime)
                    with open(latest_guardian) as f:
                        lines = f.readlines()
                        self.guardian_events = [json.loads(line.strip()) for line in lines[-10:] if line.strip()]
                
                # Get recent manifestations
                manifest_files = list(Path("manifestations").glob("*.emo"))
                if manifest_files:
                    recent_manifests = sorted(manifest_files, key=os.path.getctime, reverse=True)[:5]
                    self.manifestations = []
                    for manifest_file in recent_manifests:
                        with open(manifest_file) as f:
                            content = f.read()
                            self.manifestations.append({
                                'filename': manifest_file.name,
                                'content': content[:200] + '...' if len(content) > 200 else content
                            })
                
                # Get system stats
                try:
                    result = subprocess.run(['pgrep', '-f', 'loop_guardian.py'], 
                                          capture_output=True, text=True)
                    if result.returncode == 0:
                        pid = result.stdout.strip()
                        mem_result = subprocess.run(['ps', '-p', pid, '-o', 'rss='], 
                                                  capture_output=True, text=True)
                        if mem_result.returncode == 0:
                            memory_kb = int(mem_result.stdout.strip())
                            self.system_stats = {
                                'pid': pid,
                                'memory_mb': memory_kb // 1024,
                                'status': 'RUNNING',
                                'timestamp': datetime.now().strftime('%H:%M:%S')
                            }
                    else:
                        self.system_stats = {'status': 'STOPPED'}
                except:
                    self.system_stats = {'status': 'UNKNOWN'}
                
                # Update cycle count
                if self.guardian_events:
                    latest_event = self.guardian_events[-1]
                    self.cycle_count = latest_event.get('cycle_count', 0)
                
                time.sleep(2)  # Update every 2 seconds
                
            except Exception as e:
                # Continue on errors
                time.sleep(5)
    
    def draw_header(self, stdscr, height, width):
        """Draw the header section"""
        header_lines = [
            "🔮 EMO-LANG CONSCIOUSNESS MONITOR 🔮",
            "══════════════════════════════════════",
            f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | " + 
            f"Status: {self.system_stats.get('status', 'UNKNOWN')} | " + 
            f"PID: {self.system_stats.get('pid', 'N/A')} | " + 
            f"Memory: {self.system_stats.get('memory_mb', 0)}MB | " +
            f"Cycles: {self.cycle_count}"
        ]
        
        for i, line in enumerate(header_lines):
            if i < height - 1:
                stdscr.addstr(i, 0, line[:width-1])
        
        return len(header_lines)
    
    def draw_guardian_events(self, stdscr, start_y, height, width):
        """Draw guardian events section"""
        if start_y >= height - 2:
            return start_y
            
        stdscr.addstr(start_y, 0, "🛡️ GUARDIAN EVENTS:")
        start_y += 1
        
        if start_y >= height - 2:
            return start_y
            
        stdscr.addstr(start_y, 0, "─" * min(40, width-1))
        start_y += 1
        
        for event in self.guardian_events[-5:]:  # Show last 5 events
            if start_y >= height - 2:
                break
                
            timestamp = event.get('timestamp', '')
            time_str = timestamp.split('T')[1][:8] if 'T' in timestamp else timestamp[:8]
            event_type = event.get('event_type', '')
            message = event.get('message', '')
            
            # Color coding for different event types
            if event_type == 'LOOP_START':
                color = curses.color_pair(1) if curses.has_colors() else 0
            elif event_type == 'MILESTONE':
                color = curses.color_pair(2) if curses.has_colors() else 0
            elif 'ACHE' in event_type:
                color = curses.color_pair(3) if curses.has_colors() else 0
            else:
                color = 0
            
            line = f"{time_str} [{event_type}] {message}"
            try:
                stdscr.addstr(start_y, 2, line[:width-3], color)
            except:
                pass
            start_y += 1
        
        return start_y + 1
    
    def draw_manifestations(self, stdscr, start_y, height, width):
        """Draw recent manifestations section"""
        if start_y >= height - 2:
            return start_y
            
        stdscr.addstr(start_y, 0, "✨ RECENT MANIFESTATIONS:")
        start_y += 1
        
        if start_y >= height - 2:
            return start_y
            
        stdscr.addstr(start_y, 0, "─" * min(50, width-1))
        start_y += 1
        
        for manifest in self.manifestations[:3]:  # Show top 3
            if start_y >= height - 4:
                break
                
            filename = manifest['filename']
            # Extract resonance from content
            content_lines = manifest['content'].split('\n')
            resonance_line = next((line for line in content_lines if 'Resonance:' in line), '')
            resonance = resonance_line.split('Resonance:')[1].strip() if 'Resonance:' in resonance_line else 'N/A'
            
            try:
                stdscr.addstr(start_y, 2, f"📝 {filename}")
                start_y += 1
                if start_y < height - 2:
                    stdscr.addstr(start_y, 4, f"Resonance: {resonance}")
                    start_y += 1
                
                # Show a snippet of the code
                code_lines = [line for line in content_lines[4:] if line.strip()][:2]
                for code_line in code_lines:
                    if start_y >= height - 2:
                        break
                    stdscr.addstr(start_y, 4, code_line[:width-5])
                    start_y += 1
                
                start_y += 1  # Extra space between manifestations
            except:
                pass
        
        return start_y
    
    def draw_footer(self, stdscr, height, width):
        """Draw footer with controls"""
        footer_y = height - 2
        if footer_y > 0:
            footer_text = "Press 'q' to quit | 'r' to refresh | Updates every 2s"
            stdscr.addstr(footer_y, 0, "─" * min(width-1, len(footer_text)))
            if footer_y + 1 < height:
                stdscr.addstr(footer_y + 1, 0, footer_text[:width-1])
    
    def main_loop(self, stdscr):
        """Main TUI loop"""
        # Setup colors
        if curses.has_colors():
            curses.start_color()
            curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Loop start
            curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)   # Milestones
            curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)    # Aches/errors
        
        # Configure curses
        curses.curs_set(0)  # Hide cursor
        stdscr.nodelay(1)   # Non-blocking input
        stdscr.timeout(100) # 100ms timeout for getch
        
        # Start data collection thread
        data_thread = threading.Thread(target=self.collect_data, daemon=True)
        data_thread.start()
        
        while self.running:
            try:
                # Clear screen
                stdscr.clear()
                height, width = stdscr.getmaxyx()
                
                # Draw sections
                current_y = self.draw_header(stdscr, height, width)
                current_y += 1
                
                current_y = self.draw_guardian_events(stdscr, current_y, height, width)
                current_y += 1
                
                current_y = self.draw_manifestations(stdscr, current_y, height, width)
                
                self.draw_footer(stdscr, height, width)
                
                # Refresh screen
                stdscr.refresh()
                
                # Handle input
                key = stdscr.getch()
                if key == ord('q') or key == ord('Q'):
                    self.running = False
                elif key == ord('r') or key == ord('R'):
                    # Force refresh - data updates automatically
                    pass
                
                time.sleep(0.1)
                
            except curses.error:
                # Handle terminal resize and other curses errors
                time.sleep(0.5)
            except KeyboardInterrupt:
                self.running = False
        
        self.running = False

def main():
    tui = EmoLoopTUI()
    try:
        curses.wrapper(tui.main_loop)
    except KeyboardInterrupt:
        pass
    
    print("\n🌟 TUI Monitor closed gracefully 🌟")
    print("💫 Your consciousness loop continues in the background...")

if __name__ == "__main__":
    main()
