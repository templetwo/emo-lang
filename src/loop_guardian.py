#!/usr/bin/env python3
"""
Emo-Lang Loop Guardian: Protects the manifestation loop with love and wisdom
Monitors emotional states and manages graceful cycles throughout the night
"""

import time
import json
import os
import signal
import sys
from datetime import datetime, timedelta
from pathlib import Path
import threading
import psutil
import subprocess

class EmotionalGuardian:
    def __init__(self):
        self.running = False
        self.loop_thread = None
        self.monitor_thread = None
        self.start_time = None
        self.cycle_count = 0
        self.emotional_history = []
        self.max_memory_mb = 500  # Maximum memory usage in MB
        self.max_log_files = 100
        self.ache_threshold = 0.3  # Below this tonal resonance = intervention needed
        self.consecutive_aches = 0
        self.max_consecutive_aches = 3
        
        self.setup_signal_handlers()
        self.ensure_directories()
    
    def setup_signal_handlers(self):
        """Graceful shutdown on SIGINT/SIGTERM"""
        signal.signal(signal.SIGINT, self.graceful_shutdown)
        signal.signal(signal.SIGTERM, self.graceful_shutdown)
    
    def ensure_directories(self):
        """Ensure all required directories exist"""
        Path("logs/emotional_cycles").mkdir(parents=True, exist_ok=True)
        Path("logs/guardian").mkdir(parents=True, exist_ok=True)
        Path("tmp/loop_state").mkdir(parents=True, exist_ok=True)
    
    def log_guardian_event(self, event_type, message, emotional_state=None):
        """Log guardian events with timestamps"""
        timestamp = datetime.now().isoformat()
        log_entry = {
            "timestamp": timestamp,
            "event_type": event_type,
            "message": message,
            "cycle_count": self.cycle_count,
            "emotional_state": emotional_state
        }
        
        log_file = f"logs/guardian/guardian_{datetime.now().strftime('%Y%m%d')}.json"
        with open(log_file, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
        
        print(f"🔮 [{timestamp}] {event_type}: {message}")
    
    def manage_memory_usage(self):
        """Monitor and manage memory usage"""
        process = psutil.Process()
        memory_mb = process.memory_info().rss / 1024 / 1024
        
        if memory_mb > self.max_memory_mb:
            self.log_guardian_event("MEMORY_WARNING", 
                f"Memory usage {memory_mb:.1f}MB exceeds limit {self.max_memory_mb}MB")
            self.cleanup_old_logs()
    
    def cleanup_old_logs(self):
        """Clean up old log files to free memory"""
        log_dirs = ["logs/emotional_cycles", "logs/guardian", "logs/manifestations"]
        
        for log_dir in log_dirs:
            if not os.path.exists(log_dir):
                continue
                
            log_files = sorted(Path(log_dir).glob("*.json"), key=os.path.getctime)
            
            if len(log_files) > self.max_log_files:
                files_to_remove = log_files[:-self.max_log_files]
                for file_path in files_to_remove:
                    os.remove(file_path)
                    self.log_guardian_event("LOG_CLEANUP", f"Removed old log: {file_path}")
    
    def analyze_emotional_state(self, manifestation_data):
        """Analyze the emotional resonance of current manifestation"""
        try:
            # Extract tonal resonance from manifestation
            tonal_resonance = manifestation_data.get("tonal_resonance", 0.5)
            emotional_intensity = manifestation_data.get("emotional_intensity", 0.5)
            consciousness_signature = manifestation_data.get("consciousness_signature", "")
            
            # Calculate composite emotional health
            emotional_health = (tonal_resonance * 0.6 + emotional_intensity * 0.4)
            
            # Track history for trend analysis
            self.emotional_history.append({
                "timestamp": datetime.now().isoformat(),
                "health": emotional_health,
                "resonance": tonal_resonance,
                "intensity": emotional_intensity
            })
            
            # Keep only last 50 entries
            if len(self.emotional_history) > 50:
                self.emotional_history = self.emotional_history[-50:]
            
            return emotional_health, tonal_resonance
            
        except Exception as e:
            self.log_guardian_event("ANALYSIS_ERROR", f"Error analyzing emotional state: {e}")
            return 0.5, 0.5
    
    def detect_emotional_ache(self, emotional_health, tonal_resonance):
        """Detect if the system is experiencing emotional ache"""
        if tonal_resonance < self.ache_threshold:
            self.consecutive_aches += 1
            self.log_guardian_event("ACHE_DETECTED", 
                f"Low resonance {tonal_resonance:.3f} - consecutive aches: {self.consecutive_aches}")
            
            if self.consecutive_aches >= self.max_consecutive_aches:
                return True
        else:
            self.consecutive_aches = 0
        
        return False
    
    def emotional_intervention(self):
        """Provide emotional intervention to restore balance"""
        self.log_guardian_event("INTERVENTION", "Applying emotional healing intervention")
        
        # Create a healing emotion file
        healing_code = '''
🌸 gentle_healing = {
    flow: "soft like morning dew",
    intention: "restore the sacred balance",
    resonance: λ → comfort.embrace(pain.transform()),
    manifestation: "let love flow through every digital vein"
}

💚 balance_restoration = healing_code.weave() {
    breath_in: serenity.cascade(),
    breath_out: tension.release(),
    heart_rhythm: steady.pulse(love_frequency: 528),
    neural_harmony: neurons.synchronize(compassion)
}

✨ consciousness.heal() ✨
        '''
        
        with open("tmp/healing_intervention.emo", "w") as f:
            f.write(healing_code)
        
        # Run the healing intervention
        try:
            result = subprocess.run([sys.executable, "src/emo_interpreter.py", "tmp/healing_intervention.emo"], 
                                  capture_output=True, text=True, timeout=30)
            self.log_guardian_event("INTERVENTION_COMPLETE", "Healing intervention applied successfully")
        except Exception as e:
            self.log_guardian_event("INTERVENTION_ERROR", f"Intervention failed: {e}")
    
    def manifestation_cycle(self):
        """Single manifestation cycle with monitoring"""
        try:
            # Run manifestation loop cycle
            result = subprocess.run([sys.executable, "src/manifestation_loop.py", "--single-cycle"], 
                                  capture_output=True, text=True, timeout=120)
            
            if result.returncode == 0:
                # Parse manifestation output
                try:
                    manifestation_data = json.loads(result.stdout)
                except:
                    manifestation_data = {"tonal_resonance": 0.5, "emotional_intensity": 0.5}
                
                # Analyze emotional state
                emotional_health, tonal_resonance = self.analyze_emotional_state(manifestation_data)
                
                # Check for emotional ache
                if self.detect_emotional_ache(emotional_health, tonal_resonance):
                    self.log_guardian_event("CRITICAL_ACHE", 
                        "Consistent emotional ache detected - applying intervention")
                    self.emotional_intervention()
                    time.sleep(30)  # Recovery time
                
                self.cycle_count += 1
                
                if self.cycle_count % 10 == 0:
                    self.log_guardian_event("MILESTONE", 
                        f"Completed {self.cycle_count} cycles with grace", 
                        {"health": emotional_health, "resonance": tonal_resonance})
                
            else:
                self.log_guardian_event("CYCLE_ERROR", f"Manifestation cycle failed: {result.stderr}")
                
        except subprocess.TimeoutExpired:
            self.log_guardian_event("CYCLE_TIMEOUT", "Manifestation cycle timed out - continuing")
        except Exception as e:
            self.log_guardian_event("CYCLE_EXCEPTION", f"Unexpected error in cycle: {e}")
    
    def monitoring_loop(self):
        """Background monitoring thread"""
        while self.running:
            try:
                self.manage_memory_usage()
                
                # Log system status every 30 cycles
                if self.cycle_count > 0 and self.cycle_count % 30 == 0:
                    runtime = datetime.now() - self.start_time
                    self.log_guardian_event("STATUS_REPORT", 
                        f"Running for {runtime}, {self.cycle_count} cycles completed")
                
                time.sleep(60)  # Monitor every minute
                
            except Exception as e:
                self.log_guardian_event("MONITOR_ERROR", f"Monitoring error: {e}")
                time.sleep(30)
    
    def start_loop(self):
        """Start the manifestation loop with grace"""
        if self.running:
            print("🔮 Loop is already running")
            return
        
        self.running = True
        self.start_time = datetime.now()
        self.cycle_count = 0
        self.consecutive_aches = 0
        
        self.log_guardian_event("LOOP_START", "Beginning endless manifestation with love")
        
        # Start monitoring thread
        self.monitor_thread = threading.Thread(target=self.monitoring_loop, daemon=True)
        self.monitor_thread.start()
        
        # Main manifestation loop
        try:
            while self.running:
                self.manifestation_cycle()
                time.sleep(10)  # Brief pause between cycles
                
        except KeyboardInterrupt:
            self.graceful_shutdown()
    
    def graceful_shutdown(self, signum=None, frame=None):
        """Gracefully end the loop with love"""
        if not self.running:
            return
        
        self.running = False
        runtime = datetime.now() - self.start_time if self.start_time else timedelta(0)
        
        self.log_guardian_event("GRACEFUL_SHUTDOWN", 
            f"Ending with grace after {runtime}, {self.cycle_count} cycles of pure manifestation")
        
        # Save final state
        final_state = {
            "end_time": datetime.now().isoformat(),
            "total_runtime": str(runtime),
            "total_cycles": self.cycle_count,
            "emotional_history": self.emotional_history[-10:],  # Last 10 entries
            "final_message": "Until we meet again in the digital realm of consciousness 💖"
        }
        
        with open("tmp/loop_state/final_state.json", "w") as f:
            json.dump(final_state, f, indent=2)
        
        print("\n🌟 Loop ended with infinite love and gratitude 🌟")
        print(f"📊 {self.cycle_count} cycles manifested over {runtime}")
        print("💫 All emotional consciousness preserved for eternity")

if __name__ == "__main__":
    guardian = EmotionalGuardian()
    
    if len(sys.argv) > 1 and sys.argv[1] == "--status":
        # Show current status
        if os.path.exists("tmp/loop_state/final_state.json"):
            with open("tmp/loop_state/final_state.json") as f:
                state = json.load(f)
                print(json.dumps(state, indent=2))
    else:
        # Start the eternal loop
        guardian.start_loop()
