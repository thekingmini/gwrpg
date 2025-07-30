import tkinter as tk
from tkinter import ttk, messagebox
import uuid

# --- Game Data Definitions ---
PRINTERS = [
    {'level': 1, 'name': 'Silver Printer', 'cost': 1000, 'money': 200, 'xp': 18.5, 'color': '#C0C0C0'},
    {'level': 3, 'name': 'Tuned Gold Printer (VIP)', 'cost': 2000, 'money': 400, 'xp': 44.4, 'color': '#FFB700'},
    {'level': 5, 'name': 'Gold Printer', 'cost': 2000, 'money': 400, 'xp': 37.0, 'color': '#FFD700'},
    {'level': 15, 'name': 'Platinum Printer', 'cost': 3800, 'money': 760, 'xp': 70.3, 'color': '#E5E4E2'},
    {'level': 22, 'name': 'Tuned Diamond Printer (VIP)', 'cost': 6400, 'money': 1280, 'xp': 142.1, 'color': '#66D9EF'},
    {'level': 25, 'name': 'Diamond Printer', 'cost': 6400, 'money': 1280, 'xp': 118.4, 'color': '#B9F2FF'},
    {'level': 35, 'name': 'Emerald Printer', 'cost': 9800, 'money': 1960, 'xp': 181.3, 'color': '#50C878'},
    {'level': 42, 'name': 'Tuned Money Factory (VIP)', 'cost': 14000, 'money': 2800, 'xp': 310.8, 'color': '#9370DB'},
    {'level': 45, 'name': 'Money Factory', 'cost': 14000, 'money': 2800, 'xp': 259.0, 'color': '#8A2BE2'},
    {'level': 55, 'name': 'Silver Silo', 'cost': 19400, 'money': 3880, 'xp': 358.9, 'color': '#C0C0C0'},
    {'level': 62, 'name': 'Tuned Gold Silo (VIP)', 'cost': 24800, 'money': 4960, 'xp': 550.6, 'color': '#FFB700'},
    {'level': 65, 'name': 'Gold Silo', 'cost': 24800, 'money': 4960, 'xp': 458.8, 'color': '#FFD700'},
    {'level': 75, 'name': 'Ruby Silo', 'cost': 31400, 'money': 6280, 'xp': 580.9, 'color': '#E0115F'},
    {'level': 82, 'name': 'Quantum Factory (VIP)', 'cost': 38800, 'money': 7760, 'xp': 861.4, 'color': '#F0F8FF'},
    {'level': 85, 'name': 'Nuclear Factory', 'cost': 38800, 'money': 7760, 'xp': 717.8, 'color': '#32CD32'},
]

LEVEL_XP = {
    lvl: xp for lvl, xp in enumerate([
        0, 550, 1050, 1750, 2650, 3750, 5050, 6550, 8250, 10150, 12150, 14550, 17050,
        19750, 22650, 25750, 29050, 32550, 36250, 40150, 44250, 48550, 53050, 57750, 62650,
        67750, 73050, 78550, 84250, 90150, 96250, 102550, 109050, 115750, 122650, 129750,
        137050, 144550, 152250, 160150, 168250, 176550, 185050, 193750, 202650, 211750,
        221050, 230550, 240250, 250150, 260250, 270550, 281050, 291750, 302650, 313750,
        325050, 336550, 348250, 360150, 372250, 384550, 397050, 409750, 422650, 435750,
        449050, 462550, 476250, 490150, 504250, 518550, 533050, 547750, 562650, 577750,
        593050, 608550, 624150, 640150, 656250, 672550, 689050, 705750, 722650, 739750,
        757050, 774550, 792250, 810550, 828550, 846550, 865050, 883750, 902650, 921750,
        941050, 960550, 980250, 1000000
    ], start=1)
}
LEVEL_XP[1] = 0

class LevelingSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Leveling Simulator")
        self.root.geometry("1380x850")
        self.root.configure(bg="#181c23")
        self.xp_vars = {}
        self._init_variables()
        self._setup_styles()
        self._layout_ui()

    def _init_variables(self):
        self.level = 1
        self.xp = 0
        self.money = 1000
        self.cycle = 0
        self.owned_printers = []
        self.max_printers = 10

    def _setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Title.TLabel", font=("Segoe UI", 16, "bold"), background="#181c23", foreground="#f5f6fa")
        style.configure("Panel.TFrame", background="#23272e")
        style.configure("Value.TLabel", font=("Segoe UI", 12, "bold"), background="#181c23", foreground="#44bd32")
        style.configure("Label.TLabel", background="#181c23", foreground="#d3d3d3", font=("Segoe UI", 11))
        style.configure("Dark.TButton", background="#353b48", foreground="#f5f6fa", font=("Segoe UI", 10))
        style.map("Dark.TButton", background=[("active", "#3b4252")])
        style.configure("Treeview", background="#23272e", fieldbackground="#23272e", foreground="#f5f6fa", rowheight=23)
        style.configure("Treeview.Heading", background="#292e39", foreground="#fbc531", font=("Segoe UI", 10, "bold"))

    def _layout_ui(self):
        # -- Header --
        ttk.Label(self.root, text="Leveling Simulator", style="Title.TLabel").pack(pady=(12, 6))
        self._build_stats_panel()
        # -- Main Panels --
        main = ttk.Frame(self.root, style="Panel.TFrame")
        main.pack(fill="both", expand=True, padx=10, pady=6)
        main.columnconfigure(0, weight=2)
        main.columnconfigure(1, weight=2)
        main.columnconfigure(2, weight=1)
        self._printer_shop_panel(main)
        self._player_printers_panel(main)
        self._xp_tuner_panel(main)
        # -- Log & Controls --
        self._log_panel()
        self._controls_panel()

    def _build_stats_panel(self):
        stats = ttk.Frame(self.root, style="Panel.TFrame")
        stats.pack(fill="x", padx=12, pady=5)
        stats.columnconfigure((0,1,2,3,4,5), weight=1)
        self.level_label = ttk.Label(stats, text=f"Level: {self.level}", style="Value.TLabel")
        self.level_label.grid(row=0, column=0, sticky="w")
        self.xp_label = ttk.Label(stats, text=f"XP: {self.xp} / {self._xp_to_next()}", style="Value.TLabel")
        self.xp_label.grid(row=0, column=1, sticky="w")
        self.money_label = ttk.Label(stats, text=f"${self.money:,.0f}", style="Value.TLabel")
        self.money_label.grid(row=0, column=2, sticky="w")
        self.cycle_label = ttk.Label(stats, text=f"Cycle: {self.cycle}", style="Value.TLabel")
        self.cycle_label.grid(row=0, column=3, sticky="w")
        self.printer_count_label = ttk.Label(stats, text=f"Printers: {len(self.owned_printers)}/{self.max_printers}", style="Value.TLabel")
        self.printer_count_label.grid(row=0, column=4, sticky="w")
        self.time_label = ttk.Label(stats, text="Time: 0d 0h 0m", style="Value.TLabel")
        self.time_label.grid(row=0, column=5, sticky="w")

    def _printer_shop_panel(self, parent):
        frame = ttk.Frame(parent, style="Panel.TFrame")
        frame.grid(row=0, column=0, sticky="nsew", padx=(0,5), pady=3)
        ttk.Label(frame, text="Printer Shop", style="Label.TLabel", font=("Segoe UI", 13, "bold")).pack(pady=(4,2))
        canvas, scroll = self._make_scrollable(frame)
        self.shop_inner = ttk.Frame(canvas, style="Panel.TFrame")
        canvas.create_window((0,0), window=self.shop_inner, anchor="nw")
        self.shop_inner.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")
        self._show_shop_printers()

    def _player_printers_panel(self, parent):
        frame = ttk.Frame(parent, style="Panel.TFrame")
        frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=3)
        ttk.Label(frame, text="Your Printers", style="Label.TLabel", font=("Segoe UI", 13, "bold")).pack(pady=(4,2))
        canvas, scroll = self._make_scrollable(frame)
        self.owned_inner = ttk.Frame(canvas, style="Panel.TFrame")
        canvas.create_window((0,0), window=self.owned_inner, anchor="nw")
        self.owned_inner.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")
        self._refresh_owned_printers()

    def _xp_tuner_panel(self, parent):
        frame = ttk.Frame(parent, style="Panel.TFrame")
        frame.grid(row=0, column=2, sticky="nsew", padx=(5,0), pady=3)
        ttk.Label(frame, text="XP Tuner", style="Label.TLabel", font=("Segoe UI", 13, "bold")).pack(pady=(4,2))
        canvas, scroll = self._make_scrollable(frame)
        tuner_inner = ttk.Frame(canvas, style="Panel.TFrame")
        canvas.create_window((0,0), window=tuner_inner, anchor="nw")
        tuner_inner.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")
        for p in PRINTERS:
            row = ttk.Frame(tuner_inner, style="Panel.TFrame")
            row.pack(fill="x", pady=2, padx=4)
            ttk.Label(row, text=p["name"], style="Label.TLabel", width=19).pack(side="left")
            self.xp_vars[p["name"]] = tk.DoubleVar(value=p['xp'])
            entry = ttk.Entry(row, textvariable=self.xp_vars[p["name"]], width=7)
            entry.pack(side="right")
        ttk.Button(frame, text="Apply XP Changes", style="Dark.TButton", command=self._apply_xp_tuner).pack(fill="x", padx=6, pady=5)

    def _log_panel(self):
        frame = ttk.LabelFrame(self.root, text="Level-Up Log", style="Panel.TFrame")
        frame.pack(fill="both", expand=True, padx=10, pady=(8, 0))
        columns = ("level","time","cash")
        self.log = ttk.Treeview(frame, columns=columns, show="headings")
        for col, w in zip(columns, (60, 160, 120)):
            self.log.heading(col, text=col.capitalize())
            self.log.column(col, width=w, anchor="center")
        scroll = ttk.Scrollbar(frame, orient="vertical", command=self.log.yview)
        self.log.configure(yscrollcommand=scroll.set)
        self.log.pack(side="left", fill="both", expand=True, padx=7, pady=7)
        scroll.pack(side="right", fill="y")

    def _controls_panel(self):
        ctrl = ttk.Frame(self.root, style="Panel.TFrame")
        ctrl.pack(fill="x", pady=(5, 10), padx=10)
        ttk.Button(ctrl, text="Run Cycle (90s)", style="Dark.TButton", command=self._run_cycle).pack(side="left", expand=True, padx=5, ipady=4)
        self.auto_cycles_var = tk.StringVar(value="10")
        entry_frame = ttk.Frame(ctrl, style="Panel.TFrame")
        entry_frame.pack(side="left", padx=5)
        ttk.Label(entry_frame, text="Cycles:", style="Label.TLabel").pack()
        ttk.Entry(entry_frame, textvariable=self.auto_cycles_var, width=8).pack()
        ttk.Button(ctrl, text="Auto Run", style="Dark.TButton", command=self._auto_run).pack(side="left", expand=True, padx=5, ipady=4)
        ttk.Button(ctrl, text="Reset", style="Dark.TButton", command=self._reset).pack(side="left", expand=True, padx=5, ipady=4)

    def _make_scrollable(self, parent):
        canvas = tk.Canvas(parent, bg="#23272e", highlightthickness=0, borderwidth=0)
        scroll = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scroll.set)
        return canvas, scroll

    def _show_shop_printers(self):
        for widget in self.shop_inner.winfo_children():
            widget.destroy()
        for i, data in enumerate(PRINTERS):
            self._printer_card(self.shop_inner, data, i, shop=True)

    def _refresh_owned_printers(self):
        for widget in self.owned_inner.winfo_children():
            widget.destroy()
        for i, printer in enumerate(self.owned_printers):
            self._printer_card(self.owned_inner, printer, i, shop=False, owned=True)

    def _printer_card(self, parent, data, idx, shop=False, owned=False):
        f = tk.Frame(parent, bg="#292e39")
        f.grid(row=idx, column=0, sticky="ew", padx=6, pady=3)
        icon = tk.Frame(f, bg=data.get("color","#7f8fa6"), width=18, height=18)
        icon.pack(side="left", padx=6, pady=6)
        icon.pack_propagate(False)
        tk.Label(icon, text=data["name"].split()[0], bg=data.get("color","#7f8fa6"), fg="white", font=("Segoe UI", 8, "bold")).pack()
        info = tk.Frame(f, bg="#292e39")
        info.pack(side="left", fill="both", expand=True, padx=4)
        if shop:
            tk.Label(info, text=f"Lvl {data['level']}  |  ${data['cost']:,}", bg="#292e39", fg="#f5f6fa", font=("Segoe UI", 9, "bold")).pack(anchor="w")
            btnrow = tk.Frame(info, bg="#292e39")
            btnrow.pack(anchor="w", pady=2)
            ttk.Button(btnrow, text="Buy", style="Dark.TButton", command=lambda n=data['name']: self._buy_printer(n)).pack(side="left")
            ttk.Button(btnrow, text="Steal", style="Dark.TButton", command=lambda n=data['name']: self._steal_printer(n)).pack(side="left", padx=6)
        elif owned:
            status = "UNSTABLE! ({}/5)".format(data.get("collections",0)) if data.get("unstable") else "Operational"
            fg = "red" if data.get("unstable") else "#44bd32"
            tk.Label(info, text=status, bg="#292e39", fg=fg, font=("Segoe UI",10,"bold")).pack(anchor="w")
            f.bind("<Button-3>", lambda e, pid=data['id']: self._owned_context_menu(e, pid))

    def _owned_context_menu(self, event, printer_id):
        menu = tk.Menu(self.root, tearoff=0, bg="#23272e", fg="#f5f6fa")
        menu.add_command(label="Delete Printer", command=lambda: self._delete_printer(printer_id))
        menu.tk_popup(event.x_root, event.y_root)

    def _update_stats(self):
        self.level_label.config(text=f"Level: {self.level}")
        xp_next = self._xp_to_next()
        self.xp_label.config(text=f"XP: {self.xp:.1f} / {xp_next if xp_next else 'MAX'}")
        self.money_label.config(text=f"${self.money:,.0f}")
        self.cycle_label.config(text=f"Cycle: {self.cycle}")
        self.printer_count_label.config(text=f"Printers: {len(self.owned_printers)}/{self.max_printers}")
        self.time_label.config(text=f"Time: {self._format_time(self.cycle*90)}")
        self._refresh_owned_printers()

    def _xp_to_next(self):
        return LEVEL_XP.get(self.level+1, None)

    def _apply_xp_tuner(self):
        try:
            for p in PRINTERS:
                v = self.xp_vars[p["name"]].get()
                p["xp"] = float(v)
            self._show_shop_printers()
            messagebox.showinfo("XP Updated", "XP Per Cycle values have been updated.")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid XP value entered.\n{e}")

    def _buy_printer(self, name):
        if len(self.owned_printers) >= self.max_printers:
            messagebox.showwarning("Max Printers", "Max printers reached! Use 'Steal' for unstable 11th printer.")
            return
        data = next((p for p in PRINTERS if p['name']==name), None)
        if not data: return
        if self.level < data['level']:
            messagebox.showerror("Level Locked", f"Reach level {data['level']} to buy this printer.")
            return
        if self.money < data['cost']:
            messagebox.showerror("Not Enough Money", "You need more money to buy this printer.")
            return
        self.money -= data['cost']
        printer = data.copy()
        printer['id'] = str(uuid.uuid4())
        self.owned_printers.append(printer)
        self._update_stats()

    def _steal_printer(self, name):
        if len(self.owned_printers) != self.max_printers:
            messagebox.showwarning("Can't Steal", "Must have exactly 10 printers to steal an unstable one.")
            return
        data = next((p for p in PRINTERS if p['name'] == name), None)
        if not data: return
        if self.level < data['level']:
            messagebox.showerror("Level Locked", f"Reach level {data['level']} to steal this printer.")
            return
        printer = data.copy()
        printer['id'] = str(uuid.uuid4())
        printer['unstable'] = True
        printer['collections'] = 0
        self.owned_printers.append(printer)
        messagebox.showinfo("Stolen!", f"You stole an unstable {name}. It will explode after 6 collections!")
        self._update_stats()

    def _delete_printer(self, pid):
        self.owned_printers = [p for p in self.owned_printers if p['id'] != pid]
        self._update_stats()

    def _run_cycle(self):
        self.cycle += 1
        money, xp = 0, 0
        for printer in self.owned_printers:
            money += printer.get('money',0)
            xp += printer.get('xp',0)
            if printer.get('unstable'):
                printer['collections'] += 1
                if printer['collections'] > 5:
                    self._explode()
                    return
        self.money += money
        self.xp += xp
        self._check_level_up()
        self._update_stats()

    def _explode(self):
        messagebox.showwarning("KABOOM!", "Your unstable printer exploded! All your printers are destroyed.")
        self.owned_printers = []
        self._update_stats()

    def _check_level_up(self):
        while self.level < 100:
            need = self._xp_to_next()
            if need is not None and self.xp >= need:
                self.xp -= need
                self.level += 1
                # Log event
                time_str = self._format_time(self.cycle*90)
                self.log.insert("", "end", values=(self.level, time_str, f"${self.money:,.0f}"))
                messagebox.showinfo("Level Up!", f"You reached Level {self.level}!")
            else:
                break

    def _auto_run(self):
        try:
            n = int(self.auto_cycles_var.get())
            assert n > 0
            for _ in range(n):
                if not self.root.winfo_exists():
                    break
                self._run_cycle()
                self.root.update_idletasks()
        except:
            messagebox.showerror("Invalid Input", "Please enter a positive integer for cycles.")

    def _reset(self):
        if not messagebox.askyesno("Reset Progress", "Are you sure you want to reset all progress?"):
            return
        self._init_variables()
        for i in self.log.get_children():
            self.log.delete(i)
        self._update_stats()

    def _format_time(self, seconds):
        d = seconds // (24*3600)
        h = (seconds % (24*3600)) // 3600
        m = (seconds % 3600) // 60
        return f"{int(d)}d {int(h)}h {int(m)}m"

if __name__ == "__main__":
    root = tk.Tk()
    app = LevelingSimulator(root)
    app._update_stats()
    root.mainloop()
