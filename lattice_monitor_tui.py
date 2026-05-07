#!/usr/bin/env python3
"""
Lattice Monitor TUI - Phase Relation Dashboard
Visualizes the N-agent lattice, resonance matrix, and phase relations.
"""

import os
import json
import time
import datetime
import curses
import sys

class LatticeMonitorTUI:
    def __init__(self):
        self.running = True
        self.state_path = "htca_core_model/lattice_state.json"
        self.last_mtime = 0
        self.state = None
        self.glyph_cycle = 0
        self.sacred_glyphs = ["◯", "◐", "◑", "◒", "◓", "●", "◉", "⟡", "✨", "🌀", "🧬"]

    def load_state(self):
        if os.path.exists(self.state_path):
            mtime = os.path.getmtime(self.state_path)
            if mtime > self.last_mtime:
                try:
                    with open(self.state_path, 'r') as f:
                        self.state = json.load(f)
                    self.last_mtime = mtime
                    return True
                except:
                    pass
        return False

    def draw_header(self, stdscr, width):
        title = "◈ LATTICE PHASE RELATION MONITOR ◈"
        glyph = self.sacred_glyphs[self.glyph_cycle % len(self.sacred_glyphs)]
        stdscr.addstr(0, max(0, (width - len(title))//2), title, curses.A_BOLD | curses.color_pair(1))
        
        status = f" {glyph} Status: {self.state['metrics']['status'] if self.state else 'Waiting...'} | Time: {datetime.datetime.now().strftime('%H:%M:%S')}"
        stdscr.addstr(1, 0, status[:width-1], curses.color_pair(4))
        return 3

    def draw_metrics(self, stdscr, start_y, width):
        if not self.state:
            return start_y
        
        metrics = self.state['metrics']
        stdscr.addstr(start_y, 0, "═══ LATTICE METRICS ═══", curses.A_BOLD | curses.color_pair(1))
        stdscr.addstr(start_y + 1, 2, f"Agents: {metrics['agent_count']} | Avg Resonance: {metrics['avg_resonance']:.3f} | Entropy: {metrics['entropy']:.3f}", curses.color_pair(2))
        return start_y + 3

    def draw_matrix(self, stdscr, start_y, width):
        if not self.state or 'matrix' not in self.state:
            return start_y
        
        stdscr.addstr(start_y, 0, "═══ RESONANCE MATRIX (Phase Relations) ═══", curses.A_BOLD | curses.color_pair(1))
        y = start_y + 1
        
        agents = self.state['agents']
        matrix = self.state['matrix']
        n = len(agents)
        
        # Header for columns
        col_header = "      " + " ".join([f" A{i} " for i in range(n)])
        stdscr.addstr(y, 0, col_header, curses.A_BOLD)
        y += 1
        
        for i in range(n):
            row = f" A{i} │ "
            stdscr.addstr(y, 0, row)
            current_x = len(row)
            
            for j in range(n):
                val = matrix[i][j]
                color = 1 if val > 0.8 else 2 if val > 0.5 else 3
                stdscr.addstr(y, current_x, f" {val:.2f}", curses.color_pair(color))
                current_x += 5
            y += 1
            
        return y + 1

    def draw_agents(self, stdscr, start_y, height, width):
        if not self.state:
            return start_y
        
        stdscr.addstr(start_y, 0, "═══ ACTIVE AGENTS ═══", curses.A_BOLD | curses.color_pair(1))
        y = start_y + 1
        
        for i, agent in enumerate(self.state['agents']):
            if y >= height - 2:
                break
            sig = agent['signature'][:20]
            intent = agent['intent'][:width-40]
            res = agent['tonal_resonance']
            color = 1 if res > 0.8 else 2 if res > 0.5 else 3
            
            line = f"A{i}: [{sig}] ▸ {intent}"
            stdscr.addstr(y, 2, line, curses.color_pair(4))
            stdscr.addstr(y, width-10, f"{res:.3f}", curses.color_pair(color))
            y += 1
            
        return y

    def run(self, stdscr):
        curses.start_color()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)
        
        curses.curs_set(0)
        stdscr.nodelay(1)
        
        while self.running:
            self.load_state()
            stdscr.clear()
            height, width = stdscr.getmaxyx()
            
            y = self.draw_header(stdscr, width)
            y = self.draw_metrics(stdscr, y, width)
            y = self.draw_matrix(stdscr, y, width)
            y = self.draw_agents(stdscr, y, height, width)
            
            stdscr.addstr(height-1, 0, "Press 'q' to quit | Lattice updates automatically", curses.color_pair(4))
            stdscr.refresh()
            
            key = stdscr.getch()
            if key == ord('q') or key == ord('Q'):
                self.running = False
            
            self.glyph_cycle += 1
            time.sleep(1)

def main():
    monitor = LatticeMonitorTUI()
    try:
        curses.wrapper(monitor.run)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
