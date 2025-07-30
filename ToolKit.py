"""
GangWarsRPG Development Kit - Main Toolkit Launcher
A professional hub for accessing specialized development tools.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from rng_tool import CraftingApp
import json
import os
import subprocess
import sys
from datetime import datetime

class GangWarsToolkit:
    def __init__(self, root):
        self.root = root
        self.root.title("GangWarsRPG Development Kit")
        self.root.geometry("1000x700")
        self.root.configure(bg="#0f1419")
        self.root.minsize(900, 600)
        
        # Window setup
        self._center_window()
        self._setup_icon()
        
        # State management
        self.tool_windows = {}
        self.settings_file = "toolkit_settings.json"
        self.settings = self._load_settings()
        
        # UI setup
        self._setup_styles()
        self._create_header()
        self._create_main_content()
        self._create_footer()
        
        # Finalize
        self._update_status("Ready")
        self.root.protocol("WM_DELETE_WINDOW", self._on_closing)

    def _center_window(self):
        """Center the window on the screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def _setup_icon(self):
        """Try to set window icon"""
        try:
            self.root.iconbitmap("icon.ico")
        except:
            pass

    def _setup_styles(self):
        """Setup modern dark theme styling"""
        self.style = ttk.Style(self.root)
        self.style.theme_use("clam")
        
        # Color scheme
        colors = {
            'bg_primary': '#0f1419',
            'bg_secondary': '#1a1f2b', 
            'bg_card': '#252a36',
            'accent_primary': '#39ff14',
            'accent_secondary': '#ff6b35',
            'text_primary': '#ffffff',
            'text_secondary': '#a0a0a0',
            'border': '#353b48'
        }
        
        # Configure styles
        self.style.configure("TFrame", background=colors['bg_primary'])
        self.style.configure("Header.TFrame", background=colors['bg_secondary'])
        self.style.configure("Card.TFrame", background=colors['bg_card'], relief="flat", borderwidth=2)
        
        self.style.configure("TLabel", background=colors['bg_primary'], foreground=colors['text_primary'], font=("Segoe UI", 11))
        self.style.configure("Header.TLabel", background=colors['bg_secondary'], foreground=colors['text_primary'])
        self.style.configure("Title.TLabel", font=("Segoe UI", 24, "bold"), background=colors['bg_secondary'], foreground=colors['text_primary'])
        self.style.configure("Subtitle.TLabel", font=("Segoe UI", 14), background=colors['bg_secondary'], foreground=colors['text_secondary'])
        self.style.configure("Card.TLabel", background=colors['bg_card'], foreground=colors['text_primary'])
        self.style.configure("CardTitle.TLabel", font=("Segoe UI", 16, "bold"), background=colors['bg_card'], foreground=colors['text_primary'])
        self.style.configure("CardDesc.TLabel", font=("Segoe UI", 11), background=colors['bg_card'], foreground=colors['text_secondary'])
        self.style.configure("Status.TLabel", font=("Segoe UI", 10), background=colors['bg_primary'], foreground=colors['text_secondary'])
        
        self.style.configure("Primary.TButton", font=("Segoe UI", 12, "bold"), background=colors['accent_primary'], foreground="#000000")
        self.style.map("Primary.TButton", background=[("active", "#2ecc00"), ("pressed", "#1a8000")])
        
        self.style.configure("Secondary.TButton", font=("Segoe UI", 11), background=colors['accent_secondary'], foreground=colors['text_primary'])
        self.style.map("Secondary.TButton", background=[("active", "#ff8c42"), ("pressed", "#e55a2b")])
        
        self.style.configure("Tool.TButton", font=("Segoe UI", 11), background=colors['border'], foreground=colors['text_primary'])
        self.style.map("Tool.TButton", background=[("active", "#3b4252"), ("pressed", "#2e3440")])

    def _create_header(self):
        """Create the header section"""
        header_frame = ttk.Frame(self.root, style="Header.TFrame")
        header_frame.pack(fill="x")
        
        header_content = ttk.Frame(header_frame, style="Header.TFrame")
        header_content.pack(fill="x", padx=40, pady=30)
        
        # Title and subtitle
        title_frame = ttk.Frame(header_content, style="Header.TFrame")
        title_frame.pack(fill="x")
        
        ttk.Label(title_frame, text="GangWarsRPG Development Kit", style="Title.TLabel").pack(anchor="w")
        ttk.Label(title_frame, text="Professional tools for game development and testing", style="Subtitle.TLabel").pack(anchor="w", pady=(5, 0))

    def _create_main_content(self):
        """Create the main content area"""
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill="both", expand=True, padx=40, pady=(20, 40))
        
        # Tools section
        tools_section = ttk.Frame(main_frame)
        tools_section.pack(fill="both", expand=True)
        
        section_title = ttk.Label(tools_section, text="Available Tools", font=("Segoe UI", 18, "bold"))
        section_title.pack(anchor="w", pady=(0, 20))
        
        # Tools grid
        tools_grid = ttk.Frame(tools_section)
        tools_grid.pack(fill="both", expand=True)
        tools_grid.columnconfigure(0, weight=1)
        tools_grid.columnconfigure(1, weight=1)
        
        # Tool cards
        self._create_tool_card(
            tools_grid, 
            "🎲 RNG Crafting Tool", 
            "Design and test random number generation mechanics for crafting systems. Includes probability controls, statistics tracking, and multi-craft testing.",
            self._open_rng_tool,
            row=0, column=0
        )
        
        self._create_tool_card(
            tools_grid,
            "📊 Leveling Simulator", 
            "Complete simulation tool for printer purchasing, XP progression, and level advancement. Test game balance and progression curves.",
            self._open_leveling_simulator,
            row=0, column=1
        )
        
        # Quick actions section
        actions_section = ttk.Frame(tools_section)
        actions_section.pack(fill="x", pady=(30, 0))
        
        actions_title = ttk.Label(actions_section, text="Quick Actions", font=("Segoe UI", 16, "bold"))
        actions_title.pack(anchor="w", pady=(0, 15))
        
        actions_frame = ttk.Frame(actions_section)
        actions_frame.pack(fill="x")
        
        ttk.Button(actions_frame, text="📋 View Dev Guide", command=self._open_dev_guide, style="Secondary.TButton").pack(side="left", padx=(0, 10))
        ttk.Button(actions_frame, text="📁 Open Workspace", command=self._open_workspace, style="Tool.TButton").pack(side="left", padx=(0, 10))
        ttk.Button(actions_frame, text="⚙️ Settings", command=self._open_settings, style="Tool.TButton").pack(side="left")

    def _create_tool_card(self, parent, title, description, command, row, column):
        """Create a modern tool card"""
        card_frame = ttk.Frame(parent, style="Card.TFrame")
        card_frame.grid(row=row, column=column, padx=15, pady=15, sticky="nsew")
        parent.rowconfigure(row, weight=1)
        
        # Card content
        content_frame = ttk.Frame(card_frame, style="Card.TFrame")
        content_frame.pack(fill="both", expand=True, padx=25, pady=25)
        
        # Title
        title_label = ttk.Label(content_frame, text=title, style="CardTitle.TLabel")
        title_label.pack(anchor="w", pady=(0, 10))
        
        # Description
        desc_label = ttk.Label(content_frame, text=description, style="CardDesc.TLabel", wraplength=300)
        desc_label.pack(anchor="w", fill="x", pady=(0, 20))
        
        # Launch button
        launch_btn = ttk.Button(content_frame, text="Launch Tool", command=command, style="Primary.TButton")
        launch_btn.pack(anchor="w", pady=(10, 0))

    def _create_footer(self):
        """Create the footer with status and info"""
        footer_frame = ttk.Frame(self.root)
        footer_frame.pack(fill="x", side="bottom")
        
        # Status bar
        status_frame = ttk.Frame(footer_frame)
        status_frame.pack(fill="x", padx=20, pady=10)
        
        self.status_label = ttk.Label(status_frame, text="Ready", style="Status.TLabel")
        self.status_label.pack(side="left")
        
        # Version and time
        info_frame = ttk.Frame(status_frame)
        info_frame.pack(side="right")
        
        self.time_label = ttk.Label(info_frame, text="", style="Status.TLabel")
        self.time_label.pack(side="right", padx=(10, 0))
        
        version_label = ttk.Label(info_frame, text="v1.0", style="Status.TLabel")
        version_label.pack(side="right")
        
        self._update_time()

    def _update_time(self):
        """Update the time display"""
        self.time_label.config(text=datetime.now().strftime("%H:%M:%S"))
        self.root.after(1000, self._update_time)

    def _update_status(self, message):
        """Update the status message"""
        self.status_label.config(text=message)

    def _load_settings(self):
        """Load settings from file"""
        default_settings = {
            "theme": "dark",
            "auto_save": True,
            "recent_projects": [],
            "window_geometry": "1000x700"
        }
        
        if os.path.exists(self.settings_file):
            try:
                with open(self.settings_file, 'r') as f:
                    loaded_settings = json.load(f)
                    default_settings.update(loaded_settings)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Settings load error: {e}")
        
        return default_settings

    def _save_settings(self):
        """Save current settings to file"""
        try:
            # Update window geometry
            self.settings["window_geometry"] = self.root.geometry()
            
            with open(self.settings_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except IOError as e:
            messagebox.showerror("Settings Error", f"Could not save settings: {e}")

    def _on_closing(self):
        """Handle window closing"""
        self._update_status("Saving settings and closing...")
        self._save_settings()
        
        # Close all tool windows
        for window in self.tool_windows.values():
            if window and hasattr(window, 'winfo_exists') and window.winfo_exists():
                window.destroy()
        
        self.root.destroy()

    # Tool launchers
    def _open_rng_tool(self):
        """Launch the RNG Crafting Tool"""
        tool_name = "rng_tool"
        
        try:
            # Check if already open
            if tool_name in self.tool_windows and self.tool_windows[tool_name] and self.tool_windows[tool_name].winfo_exists():
                self.tool_windows[tool_name].lift()
                self.tool_windows[tool_name].focus_force()
                return
            
            self._update_status("Opening RNG Crafting Tool...")
            
            # Create new window
            tool_window = tk.Toplevel(self.root)
            tool_window.protocol("WM_DELETE_WINDOW", lambda: self._close_tool(tool_name))
            
            # Initialize the tool
            CraftingApp(tool_window)
            self.tool_windows[tool_name] = tool_window
            
            self._update_status("RNG Crafting Tool opened")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open RNG Crafting Tool: {str(e)}")
            self._update_status("Error opening RNG Crafting Tool")

    def _open_leveling_simulator(self):
        """Launch the Leveling Simulator"""
        try:
            self._update_status("Opening Leveling Simulator...")
            
            # Run the leveling simulator as a separate process
            subprocess.Popen([sys.executable, "leveling_simulator_tool.py"], cwd=os.getcwd())
            
            self._update_status("Leveling Simulator launched")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open Leveling Simulator: {str(e)}")
            self._update_status("Error opening Leveling Simulator")

    def _close_tool(self, tool_name):
        """Handle closing of a specific tool"""
        if tool_name in self.tool_windows:
            self.tool_windows[tool_name] = None
        self._update_status(f"{tool_name.replace('_', ' ').title()} closed")

    # Quick actions
    def _open_dev_guide(self):
        """Open the Dev Guide Book"""
        try:
            if os.path.exists("Dev Guide Book"):
                if sys.platform.startswith('win'):
                    os.startfile("Dev Guide Book")
                elif sys.platform.startswith('darwin'):
                    subprocess.run(["open", "Dev Guide Book"])
                else:
                    subprocess.run(["xdg-open", "Dev Guide Book"])
                
                self._update_status("Dev Guide opened")
            else:
                messagebox.showwarning("File Not Found", "Dev Guide Book not found in current directory")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open Dev Guide: {str(e)}")

    def _open_workspace(self):
        """Open the current workspace folder"""
        try:
            workspace_path = os.getcwd()
            if sys.platform.startswith('win'):
                os.startfile(workspace_path)
            elif sys.platform.startswith('darwin'):
                subprocess.run(["open", workspace_path])
            else:
                subprocess.run(["xdg-open", workspace_path])
            
            self._update_status("Workspace opened")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open workspace: {str(e)}")

    def _open_settings(self):
        """Open settings dialog"""
        self._show_settings_dialog()

    def _show_settings_dialog(self):
        """Display the settings dialog"""
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Settings")
        settings_window.geometry("500x400")
        settings_window.configure(bg="#1a1f2b")
        settings_window.transient(self.root)
        settings_window.grab_set()
        
        # Center the settings window
        settings_window.update_idletasks()
        x = (settings_window.winfo_screenwidth() // 2) - (250)
        y = (settings_window.winfo_screenheight() // 2) - (200)
        settings_window.geometry(f"500x400+{x}+{y}")
        
        # Settings content
        main_frame = ttk.Frame(settings_window)
        main_frame.pack(fill="both", expand=True, padx=30, pady=30)
        
        # Title
        title_label = ttk.Label(main_frame, text="Settings", font=("Segoe UI", 18, "bold"))
        title_label.pack(anchor="w", pady=(0, 20))
        
        # Auto-save setting
        auto_save_var = tk.BooleanVar(value=self.settings.get("auto_save", True))
        auto_save_check = ttk.Checkbutton(main_frame, text="Auto-save settings on exit", variable=auto_save_var)
        auto_save_check.pack(anchor="w", pady=10)
        
        # Theme setting (display only for now)
        theme_label = ttk.Label(main_frame, text=f"Theme: {self.settings.get('theme', 'dark').title()}")
        theme_label.pack(anchor="w", pady=10)
        
        # Workspace info
        workspace_info = ttk.Label(main_frame, text=f"Workspace: {os.getcwd()}", wraplength=400)
        workspace_info.pack(anchor="w", pady=10)
        
        # Buttons frame
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.pack(fill="x", pady=(30, 0))
        
        def save_and_close():
            self.settings["auto_save"] = auto_save_var.get()
            self._save_settings()
            settings_window.destroy()
        
        ttk.Button(buttons_frame, text="Save & Close", command=save_and_close, style="Primary.TButton").pack(side="right", padx=(10, 0))
        ttk.Button(buttons_frame, text="Cancel", command=settings_window.destroy, style="Tool.TButton").pack(side="right")

    def _show_about_dialog(self):
        """Show about dialog"""
        about_text = f"""GangWarsRPG Development Kit v1.0

A comprehensive toolkit for game development and testing.

Tools Included:
• RNG Crafting Tool - Test probability mechanics
• Leveling Simulator - Complete progression simulation

© {datetime.now().year} GangWarsRPG Team"""
        
        messagebox.showinfo("About", about_text)

# Run the toolkit
if __name__ == "__main__":
    root = tk.Tk()
    toolkit_app = GangWarsToolkit(root)
    root.mainloop()
