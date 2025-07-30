"""
RNG Crafting Tool - GangWarsRPG Development Kit
A professional tool for testing and designing random number generation mechanics for crafting systems.
"""

import tkinter as tk
from tkinter import ttk
import random
import json
import os

RARITY_DATA = {
    "Standard": {
        "color": "#9ca3af", "slot_base": 0, "slot_bonus": 1, "bonus": None,
        "default_chance": 65.0, "default_slot_chance": 75,
    },
    "Rare": {
        "color": "#3b82f6", "slot_base": 1, "slot_bonus": 2, "bonus": None,
        "default_chance": 30.0, "default_slot_chance": 50,
    },
    "Unique": {
        "color": "#8b5cf6", "slot_base": 3, "slot_bonus": 4, "bonus": None,
        "default_chance": 15.0, "default_slot_chance": 25,
    },
    "Elite": {
        "color": "#f59e0b", "slot_base": 5, "slot_bonus": 6, "bonus": None,
        "default_chance": 5.0, "default_slot_chance": 10,
    },
    "Epic": {
        "color": "#fbbf24", "slot_base": 6, "slot_bonus": 6, "bonus": None,
        "default_chance": 0.1, "default_slot_chance": 100,
    },
    "Legendary": {
        "color": "#ef4444", "slot_base": 8, "slot_bonus": 8, "bonus": "+10 Base Damage",
        "default_chance": 0.01, "default_slot_chance": 100,
    },
}

def generate_item(controls):
    rarity_choices = []
    total_weight = sum(controls[name]["chance_var"].get() for name in RARITY_DATA)

    if total_weight <= 0: return None

    for name in RARITY_DATA:
        weight = controls[name]["chance_var"].get()
        rarity_choices.append({"name": name, "weight": weight})

    random_num = random.uniform(0, total_weight)
    cumulative_weight, chosen_rarity_name = 0, ""
    for choice in rarity_choices:
        cumulative_weight += choice["weight"]
        if random_num <= cumulative_weight:
            chosen_rarity_name = choice["name"]
            break
    
    rarity_info = RARITY_DATA[chosen_rarity_name]
    slot_slider_val = controls[chosen_rarity_name]["slot_var"].get()
    
    chosen_slots = rarity_info["slot_base"]
    if random.uniform(0, 100) <= slot_slider_val:
        chosen_slots = rarity_info["slot_bonus"]
        
    return {
        "name": chosen_rarity_name, "slots": chosen_slots,
        "bonus": rarity_info["bonus"], "color": rarity_info["color"]
    }

class CraftingApp:
    def __init__(self, parent_window):
        self.parent = parent_window
        self.parent.title("RNG Crafting Tool - GangWarsRPG Development Kit")
        self.parent.geometry("1200x800")
        self.parent.configure(bg="#181c23")
        self.parent.minsize(1000, 700)
        
        # Center window
        self._center_window()
        
        # Statistics tracking
        self.craft_count = 0
        self.rarity_stats = {rarity: 0 for rarity in RARITY_DATA.keys()}
        
        # Setup styles and create UI
        self._setup_styles()
        self._create_header()
        self._create_main_layout()
        self._update_stats_display()

    def _center_window(self):
        """Center the window on the screen"""
        self.parent.update_idletasks()
        width = self.parent.winfo_width()
        height = self.parent.winfo_height()
        x = (self.parent.winfo_screenwidth() // 2) - (width // 2)
        y = (self.parent.winfo_screenheight() // 2) - (height // 2)
        self.parent.geometry(f"{width}x{height}+{x}+{y}")

    def _setup_styles(self):
        """Setup professional dark theme styling"""
        self.style = ttk.Style(self.parent)
        self.style.theme_use("clam")
        
        # Define color scheme
        colors = {
            'bg': '#181c23',
            'panel': '#23272e', 
            'card': '#2c313a',
            'accent': '#44bd32',
            'text': '#f5f6fa',
            'text_dim': '#ddd',
            'border': '#353b48'
        }
        
        # Configure styles
        self.style.configure("TFrame", background=colors['bg'])
        self.style.configure("Card.TFrame", background=colors['card'], relief="flat", borderwidth=1)
        self.style.configure("Panel.TFrame", background=colors['panel'], relief="flat", borderwidth=1)
        
        self.style.configure("TLabel", background=colors['bg'], foreground=colors['text'], font=("Segoe UI", 11))
        self.style.configure("Card.TLabel", background=colors['card'], foreground=colors['text'])
        self.style.configure("Title.TLabel", font=("Segoe UI", 18, "bold"), background=colors['bg'], foreground=colors['text'])
        self.style.configure("Subtitle.TLabel", font=("Segoe UI", 12), background=colors['bg'], foreground=colors['text_dim'])
        self.style.configure("Value.TLabel", font=("Segoe UI", 12, "bold"), background=colors['bg'], foreground=colors['accent'])
        
        self.style.configure("Craft.TButton", font=("Segoe UI", 14, "bold"), background=colors['accent'], foreground="white")
        self.style.map("Craft.TButton", background=[("active", "#3e8e2e"), ("pressed", "#2d6b22")])
        
        self.style.configure("TButton", background=colors['border'], foreground=colors['text'], font=("Segoe UI", 10))
        self.style.map("TButton", background=[("active", "#3b4252"), ("pressed", "#2e3440")])
        
        self.style.configure("TLabelFrame", background=colors['bg'], bordercolor=colors['border'])
        self.style.configure("TLabelFrame.Label", background=colors['bg'], foreground=colors['text'], font=("Segoe UI", 11, "bold"))
        
        self.style.configure("Horizontal.TScale", background=colors['bg'], troughcolor=colors['border'], 
                           borderwidth=0, lightcolor=colors['accent'], darkcolor=colors['accent'])

    def _create_header(self):
        """Create the header section with title and description"""
        header_frame = ttk.Frame(self.parent)
        header_frame.pack(fill="x", padx=20, pady=(20, 10))
        
        ttk.Label(header_frame, text="RNG Crafting Tool", style="Title.TLabel").pack(anchor="w")
        ttk.Label(header_frame, text="Design and test random number generation for crafting systems", 
                 style="Subtitle.TLabel").pack(anchor="w", pady=(5, 0))

    def _create_main_layout(self):
        """Create the main application layout"""
        main_container = ttk.Frame(self.parent)
        main_container.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Create three-column layout
        main_container.columnconfigure(0, weight=2)  # Controls
        main_container.columnconfigure(1, weight=1)  # Results
        main_container.columnconfigure(2, weight=1)  # Stats & History
        main_container.rowconfigure(0, weight=1)
        
        # Controls Panel
        self._create_controls_panel(main_container)
        
        # Results Panel  
        self._create_results_panel(main_container)
        
        # Stats & History Panel
        self._create_stats_panel(main_container)

    def _create_controls_panel(self, parent):
        """Create the rarity controls panel"""
        controls_frame = ttk.LabelFrame(parent, text="Crafting Probabilities", padding=15)
        controls_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        
        # Create scrollable content directly without canvas complexity
        # Reset button
        reset_frame = ttk.Frame(controls_frame)
        reset_frame.pack(fill="x", pady=(0, 15))
        ttk.Button(reset_frame, text="Reset to Defaults", command=self._reset_defaults).pack()
        
        # Create controls container
        self.controls = {}
        
        # Create controls for each rarity
        for rarity_name, data in RARITY_DATA.items():
            self._create_rarity_control(controls_frame, rarity_name, data)

    def _create_rarity_control(self, parent, rarity_name, data):
        """Create control widgets for a specific rarity"""
        # Main rarity frame with colored border
        rarity_frame = ttk.Frame(parent, style="Card.TFrame")
        rarity_frame.pack(fill="x", pady=8, padx=5)
        
        # Header with rarity name and color indicator
        header_frame = ttk.Frame(rarity_frame, style="Card.TFrame")
        header_frame.pack(fill="x", padx=15, pady=(15, 10))
        
        # Color indicator
        color_frame = tk.Frame(header_frame, bg=data["color"], width=20, height=20)
        color_frame.pack(side="left", padx=(0, 10))
        color_frame.pack_propagate(False)
        
        # Rarity name
        name_label = ttk.Label(header_frame, text=rarity_name, font=("Segoe UI", 12, "bold"), style="Card.TLabel")
        name_label.pack(side="left")
        
        # Slots info
        slot_info = f"Slots: {data['slot_base']}"
        if data['slot_base'] != data['slot_bonus']:
            slot_info += f"-{data['slot_bonus']}"
        ttk.Label(header_frame, text=slot_info, style="Card.TLabel").pack(side="right")
        
        self.controls[rarity_name] = {}
        
        # Chance control
        chance_frame = ttk.Frame(rarity_frame, style="Card.TFrame")
        chance_frame.pack(fill="x", padx=15, pady=5)
        
        chance_var = tk.DoubleVar(value=data["default_chance"])
        self.controls[rarity_name]["chance_var"] = chance_var
        
        ttk.Label(chance_frame, text="Drop Chance:", style="Card.TLabel").pack(anchor="w")
        
        chance_control_frame = ttk.Frame(chance_frame, style="Card.TFrame")
        chance_control_frame.pack(fill="x", pady=(5, 0))
        
        chance_slider = ttk.Scale(chance_control_frame, from_=0.01, to=100, orient=tk.HORIZONTAL, 
                                variable=chance_var, length=200)
        chance_slider.pack(side="left", fill="x", expand=True)
        
        chance_value_label = ttk.Label(chance_control_frame, textvariable=chance_var, 
                                     width=8, style="Card.TLabel")
        chance_value_label.pack(side="right", padx=(10, 0))
        
        # Bonus slots control (if applicable)
        if data["slot_base"] != data["slot_bonus"]:
            slot_frame = ttk.Frame(rarity_frame, style="Card.TFrame")
            slot_frame.pack(fill="x", padx=15, pady=(10, 15))
            
            slot_var = tk.IntVar(value=data["default_slot_chance"])
            self.controls[rarity_name]["slot_var"] = slot_var
            
            ttk.Label(slot_frame, text="Bonus Slot Chance (%):", style="Card.TLabel").pack(anchor="w")
            
            slot_control_frame = ttk.Frame(slot_frame, style="Card.TFrame")
            slot_control_frame.pack(fill="x", pady=(5, 0))
            
            slot_slider = ttk.Scale(slot_control_frame, from_=0, to=100, orient=tk.HORIZONTAL, 
                                  variable=slot_var, length=200)
            slot_slider.pack(side="left", fill="x", expand=True)
            
            slot_value_label = ttk.Label(slot_control_frame, textvariable=slot_var, 
                                       width=8, style="Card.TLabel")
            slot_value_label.pack(side="right", padx=(10, 0))
        else:
            # For rarities without bonus slots, create a disabled var
            self.controls[rarity_name]["slot_var"] = tk.IntVar(value=100)

    def _create_results_panel(self, parent):
        """Create the crafting results panel"""
        results_frame = ttk.LabelFrame(parent, text="Crafting Results", padding=15)
        results_frame.grid(row=0, column=1, sticky="nsew", padx=10)
        
        # Craft button
        craft_frame = ttk.Frame(results_frame)
        craft_frame.pack(fill="x", pady=(0, 20))
        
        ttk.Button(craft_frame, text="🎲 Craft Item", command=self._do_craft, 
                  style="Craft.TButton").pack(fill="x", ipady=10)
        
        # Results display
        result_card = ttk.Frame(results_frame, style="Card.TFrame")
        result_card.pack(fill="x", pady=10)
        
        # Result content frame
        self.result_content = ttk.Frame(result_card, style="Card.TFrame")
        self.result_content.pack(fill="x", padx=20, pady=20)
        
        # Initially show placeholder
        self._show_placeholder()
        
        # Quick actions
        actions_frame = ttk.Frame(results_frame)
        actions_frame.pack(fill="x", pady=(20, 0))
        
        ttk.Button(actions_frame, text="Craft 10x", command=lambda: self._multi_craft(10)).pack(fill="x", pady=2)
        ttk.Button(actions_frame, text="Craft 100x", command=lambda: self._multi_craft(100)).pack(fill="x", pady=2)

    def _create_stats_panel(self, parent):
        """Create the statistics and history panel"""
        stats_frame = ttk.LabelFrame(parent, text="Statistics & History", padding=15)
        stats_frame.grid(row=0, column=2, sticky="nsew", padx=(10, 0))
        
        # Statistics section
        stats_section = ttk.LabelFrame(stats_frame, text="Craft Statistics", padding=10)
        stats_section.pack(fill="x", pady=(0, 15))
        
        # Total crafts
        self.total_crafts_label = ttk.Label(stats_section, text="Total Crafts: 0", style="Value.TLabel")
        self.total_crafts_label.pack(anchor="w")
        
        # Rarity breakdown
        self.rarity_stats_frame = ttk.Frame(stats_section)
        self.rarity_stats_frame.pack(fill="x", pady=(10, 0))
        
        # History section
        history_section = ttk.LabelFrame(stats_frame, text="Recent History", padding=10)
        history_section.pack(fill="both", expand=True)
        
        # History listbox with scrollbar
        history_container = ttk.Frame(history_section)
        history_container.pack(fill="both", expand=True)
        
        self.history_listbox = tk.Listbox(
            history_container, 
            font=("Segoe UI", 10),
            bg="#2c313a",
            fg="#f5f6fa",
            selectbackground="#44bd32",
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            height=15
        )
        self.history_listbox.pack(side="left", fill="both", expand=True)
        
        history_scrollbar = ttk.Scrollbar(history_container, orient="vertical", command=self.history_listbox.yview)
        history_scrollbar.pack(side="right", fill="y")
        self.history_listbox.config(yscrollcommand=history_scrollbar.set)
        
        # Clear history button
        ttk.Button(history_section, text="Clear History", command=self._clear_history).pack(pady=(10, 0))

    def _show_placeholder(self):
        """Show placeholder content in results panel"""
        for widget in self.result_content.winfo_children():
            widget.destroy()
            
        placeholder_label = ttk.Label(
            self.result_content, 
            text="Click 'Craft Item' to begin",
            font=("Segoe UI", 14),
            style="Card.TLabel"
        )
        placeholder_label.pack(pady=20)

    def _show_result(self, item):
        """Display crafting result"""
        for widget in self.result_content.winfo_children():
            widget.destroy()
        
        # Rarity name with color
        rarity_label = ttk.Label(
            self.result_content,
            text=item["name"],
            font=("Segoe UI", 20, "bold"),
            foreground=item["color"],
            style="Card.TLabel"
        )
        rarity_label.pack(pady=(10, 5))
        
        # Slots information
        slots_label = ttk.Label(
            self.result_content,
            text=f"Upgrade Slots: {item['slots']}",
            font=("Segoe UI", 14),
            style="Card.TLabel"
        )
        slots_label.pack(pady=5)
        
        # Bonus information
        if item["bonus"]:
            bonus_label = ttk.Label(
                self.result_content,
                text=f"Bonus: {item['bonus']}",
                font=("Segoe UI", 12, "italic"),
                style="Card.TLabel"
            )
            bonus_label.pack(pady=(5, 10))

    def _do_craft(self):
        """Perform a single craft"""
        item = generate_item(self.controls)
        if item is None:
            self._show_error("Invalid configuration - check your chance values")
            return
        
        self._show_result(item)
        self._add_to_history(item)
        self._update_statistics(item)

    def _multi_craft(self, count):
        """Perform multiple crafts"""
        results = []
        for _ in range(count):
            item = generate_item(self.controls)
            if item is None:
                self._show_error("Invalid configuration - check your chance values")
                return
            results.append(item)
            self._update_statistics(item)
        
        # Show summary of last craft
        if results:
            self._show_result(results[-1])
            # Add summary to history
            self._add_multi_craft_to_history(results, count)

    def _show_error(self, message):
        """Show error message in results panel"""
        for widget in self.result_content.winfo_children():
            widget.destroy()
            
        error_label = ttk.Label(
            self.result_content,
            text="⚠️ Error",
            font=("Segoe UI", 16, "bold"),
            foreground="#ef4444",
            style="Card.TLabel"
        )
        error_label.pack(pady=(10, 5))
        
        message_label = ttk.Label(
            self.result_content,
            text=message,
            font=("Segoe UI", 12),
            style="Card.TLabel"
        )
        message_label.pack(pady=(0, 10))

    def _add_to_history(self, item):
        """Add single craft result to history"""
        history_text = f"{item['name']} | Slots: {item['slots']}"
        if item["bonus"]:
            history_text += f" ({item['bonus']})"
        
        self.history_listbox.insert(0, history_text)
        self.history_listbox.itemconfig(0, {'fg': item['color']})
        
        # Keep history manageable
        if self.history_listbox.size() > 1000:
            self.history_listbox.delete(900, tk.END)

    def _add_multi_craft_to_history(self, results, count):
        """Add multi-craft summary to history"""
        rarity_counts = {}
        for item in results:
            rarity_counts[item['name']] = rarity_counts.get(item['name'], 0) + 1
        
        summary_parts = []
        for rarity, rarity_count in rarity_counts.items():
            summary_parts.append(f"{rarity}: {rarity_count}")
        
        summary_text = f"🎲 {count}x Craft - {', '.join(summary_parts)}"
        self.history_listbox.insert(0, summary_text)
        self.history_listbox.itemconfig(0, {'fg': '#44bd32'})

    def _update_statistics(self, item):
        """Update craft statistics"""
        self.craft_count += 1
        self.rarity_stats[item['name']] += 1
        self._update_stats_display()

    def _update_stats_display(self):
        """Update the statistics display"""
        self.total_crafts_label.config(text=f"Total Crafts: {self.craft_count}")
        
        # Clear existing rarity stats
        for widget in self.rarity_stats_frame.winfo_children():
            widget.destroy()
        
        # Show rarity breakdown
        for rarity, count in self.rarity_stats.items():
            if self.craft_count > 0:
                percentage = (count / self.craft_count) * 100
                color = RARITY_DATA[rarity]['color']
                
                stat_text = f"{rarity}: {count} ({percentage:.1f}%)"
                stat_label = ttk.Label(
                    self.rarity_stats_frame,
                    text=stat_text,
                    foreground=color
                )
                stat_label.pack(anchor="w")

    def _clear_history(self):
        """Clear the craft history"""
        self.history_listbox.delete(0, tk.END)

    def _reset_defaults(self):
        """Reset all values to defaults"""
        for rarity_name, data in RARITY_DATA.items():
            self.controls[rarity_name]["chance_var"].set(data["default_chance"])
            if "slot_var" in self.controls[rarity_name]:
                self.controls[rarity_name]["slot_var"].set(data["default_slot_chance"])

# Run standalone for testing
if __name__ == "__main__":
    root = tk.Tk()
    app = CraftingApp(root)
    root.mainloop()