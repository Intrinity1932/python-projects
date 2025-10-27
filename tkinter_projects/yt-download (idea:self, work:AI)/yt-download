# yt-dlp needed for it - download it first
# directly usable - just launch the file
# requirment is only tkinter and yt-dlp

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import subprocess
import threading
import os
import sys

class DarkTheme:
    """Dark theme colors and styles"""
    def __init__(self):
        self.bg = "#2b2b2b"
        self.fg = "#ffffff"
        self.accent = "#007acc"
        self.secondary_bg = "#3c3c3c"
        self.entry_bg = "#3c3c3c"
        self.text_bg = "#1e1e1e"
        self.success = "#4CAF50"
        self.warning = "#FF9800"
        self.error = "#f44747"

class YTDLPGUI:
    def __init__(self, root):
        self.root = root
        self.theme = DarkTheme()
        self.setup_theme()
        self.root.title("yt-dlp Downloader - Professional Edition")
        self.root.geometry("700x700")
        self.root.resizable(True, True)
        self.root.configure(bg=self.theme.bg)
        
        # Variables
        self.url_var = tk.StringVar()
        self.download_path_var = tk.StringVar(value=os.path.expanduser("~/Downloads"))
        self.progress_var = tk.StringVar(value="Ready to download")
        self.downloading = False
        
        self.setup_ui()
        self.apply_styles()
        
    def setup_theme(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
    def apply_styles(self):
        # Configure styles
        self.style.configure('TFrame', background=self.theme.bg)
        self.style.configure('TLabel', background=self.theme.bg, foreground=self.theme.fg)
        self.style.configure('TLabelframe', background=self.theme.bg, foreground=self.theme.fg)
        self.style.configure('TLabelframe.Label', background=self.theme.bg, foreground=self.theme.fg)
        self.style.configure('TButton', background=self.theme.secondary_bg, foreground=self.theme.fg)
        self.style.configure('TEntry', fieldbackground=self.theme.entry_bg, foreground=self.theme.fg)
        self.style.configure('TCombobox', fieldbackground=self.theme.entry_bg, foreground=self.theme.fg)
        self.style.configure('TCheckbutton', background=self.theme.bg, foreground=self.theme.fg)
        self.style.configure('Horizontal.TProgressbar', 
                           background=self.theme.accent,
                           troughcolor=self.theme.secondary_bg)
        
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="15")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(5, weight=1)
        
        # Header
        header_frame = ttk.Frame(main_frame)
        header_frame.grid(row=0, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 15))
        
        title_label = ttk.Label(header_frame, text="🎬 yt-dlp Downloader", 
                               font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, sticky=tk.W)
        
        # URL Entry
        ttk.Label(main_frame, text="📺 Video URL:", font=('Arial', 10, 'bold')).grid(
            row=1, column=0, sticky=tk.W, pady=8)
        
        url_frame = ttk.Frame(main_frame)
        url_frame.grid(row=1, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=8)
        url_frame.columnconfigure(0, weight=1)
        
        url_entry = ttk.Entry(url_frame, textvariable=self.url_var, font=('Arial', 10))
        url_entry.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=(0, 5))
        
        # Paste button
        ttk.Button(url_frame, text="Paste", command=self.paste_url, 
                  style='Accent.TButton').grid(row=0, column=1)
        
        # Download Path
        ttk.Label(main_frame, text="📁 Download Folder:", font=('Arial', 10, 'bold')).grid(
            row=2, column=0, sticky=tk.W, pady=8)
        
        path_frame = ttk.Frame(main_frame)
        path_frame.grid(row=2, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=8)
        path_frame.columnconfigure(0, weight=1)
        
        path_entry = ttk.Entry(path_frame, textvariable=self.download_path_var, 
                              font=('Arial', 10))
        path_entry.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=(0, 5))
        
        ttk.Button(path_frame, text="Browse", command=self.browse_path).grid(row=0, column=1)
        
        # Quality Options Frame
        quality_frame = ttk.LabelFrame(main_frame, text="🎯 Download Options", padding="12")
        quality_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=12)
        quality_frame.columnconfigure(0, weight=1)
        
        # MP3 Options
        mp3_frame = ttk.Frame(quality_frame)
        mp3_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=8)
        
        self.mp3_var = tk.BooleanVar(value=True)
        mp3_check = ttk.Checkbutton(mp3_frame, text="🎵 Download as MP3 (Audio)", 
                                   variable=self.mp3_var, command=self.toggle_mp3_options,
                                   style='Bold.TCheckbutton')
        mp3_check.grid(row=0, column=0, sticky=tk.W)
        
        self.mp3_options_frame = ttk.Frame(mp3_frame)
        self.mp3_options_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=8, padx=20)
        
        ttk.Label(self.mp3_options_frame, text="Quality:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
        self.mp3_quality_var = tk.StringVar(value="320K")
        mp3_quality_combo = ttk.Combobox(self.mp3_options_frame, textvariable=self.mp3_quality_var, 
                                        values=["0 (Best VBR)", "320K", "256K", "192K", "128K"], 
                                        state="readonly", width=12)
        mp3_quality_combo.grid(row=0, column=1, sticky=tk.W)
        
        self.embed_thumb_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(self.mp3_options_frame, text="🖼️ Embed Thumbnail", 
                       variable=self.embed_thumb_var).grid(row=0, column=2, sticky=tk.W, padx=(20, 0))
        
        # Video Options
        video_frame = ttk.Frame(quality_frame)
        video_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=8)
        
        self.video_var = tk.BooleanVar()
        ttk.Checkbutton(video_frame, text="🎥 Download Video", variable=self.video_var,
                       command=self.toggle_video_options, style='Bold.TCheckbutton').grid(
                       row=0, column=0, sticky=tk.W)
        
        self.video_options_frame = ttk.Frame(video_frame)
        self.video_options_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=8, padx=20)
        
        ttk.Label(self.video_options_frame, text="Resolution:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
        self.resolution_var = tk.StringVar(value="1080p")
        resolution_combo = ttk.Combobox(self.video_options_frame, textvariable=self.resolution_var,
                                       values=["4K", "1440p", "1080p", "720p", "480p", "360p"],
                                       state="readonly", width=10)
        resolution_combo.grid(row=0, column=1, sticky=tk.W)
        
        self.embed_subs_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(self.video_options_frame, text="📝 Embed Subtitles", 
                       variable=self.embed_subs_var).grid(row=0, column=2, sticky=tk.W, padx=(20, 0))
        
        # Buttons Frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=4, column=0, columnspan=3, pady=20)
        
        self.style.configure('Accent.TButton', background=self.theme.accent, 
                           foreground='white', font=('Arial', 10, 'bold'))
        
        self.download_btn = ttk.Button(button_frame, text="🚀 Start Download", 
                                      command=self.start_download, style='Accent.TButton')
        self.download_btn.grid(row=0, column=0, padx=8)
        
        ttk.Button(button_frame, text="🗑️ Clear All", command=self.clear_all).grid(row=0, column=1, padx=8)
        
        ttk.Button(button_frame, text="ℹ️ Get Info", command=self.get_video_info).grid(row=0, column=2, padx=8)
        
        # Progress Frame
        progress_frame = ttk.LabelFrame(main_frame, text="📊 Progress", padding="10")
        progress_frame.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=8)
        progress_frame.columnconfigure(0, weight=1)
        
        # Progress text
        progress_label = ttk.Label(progress_frame, textvariable=self.progress_var, 
                                  font=('Arial', 9))
        progress_label.grid(row=0, column=0, sticky=tk.W)
        
        # Progress bar
        self.progress_bar = ttk.Progressbar(progress_frame, mode='indeterminate')
        self.progress_bar.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=5)
        
        # Output text area
        output_frame = ttk.LabelFrame(main_frame, text="📋 Download Output", padding="5")
        output_frame.grid(row=6, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=8)
        output_frame.columnconfigure(0, weight=1)
        output_frame.rowconfigure(0, weight=1)
        
        # Text widget for output with scrollbar
        self.output_text = tk.Text(output_frame, height=15, wrap=tk.WORD, 
                                  bg=self.theme.text_bg, fg=self.theme.fg,
                                  insertbackground=self.theme.fg,  # Cursor color
                                  selectbackground=self.theme.accent,  # Selection color
                                  font=('Consolas', 9))
        
        scrollbar = ttk.Scrollbar(output_frame, orient="vertical", command=self.output_text.yview)
        self.output_text.configure(yscrollcommand=scrollbar.set)
        
        self.output_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Status bar
        status_frame = ttk.Frame(main_frame)
        status_frame.grid(row=7, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(5, 0))
        
        self.status_var = tk.StringVar(value="✅ Ready")
        status_label = ttk.Label(status_frame, textvariable=self.status_var, 
                                font=('Arial', 8), foreground=self.theme.success)
        status_label.grid(row=0, column=0, sticky=tk.W)
        
        # Initialize options state
        self.toggle_mp3_options()
        self.toggle_video_options()
        
        # Custom styles
        self.style.configure('Bold.TCheckbutton', font=('Arial', 10, 'bold'))
        
    def toggle_mp3_options(self):
        if self.mp3_var.get():
            self.mp3_options_frame.grid()
        else:
            self.mp3_options_frame.grid_remove()
            
    def toggle_video_options(self):
        if self.video_var.get():
            self.video_options_frame.grid()
        else:
            self.video_options_frame.grid_remove()
            
    def paste_url(self):
        try:
            clipboard = self.root.clipboard_get()
            self.url_var.set(clipboard)
        except:
            pass
            
    def browse_path(self):
        path = filedialog.askdirectory(initialdir=self.download_path_var.get())
        if path:
            self.download_path_var.set(path)
            
    def clear_all(self):
        self.url_var.set("")
        self.output_text.delete(1.0, tk.END)
        self.progress_var.set("Ready to download")
        self.status_var.set("✅ Ready")
        
    def get_video_info(self):
        url = self.url_var.get().strip()
        if not url:
            messagebox.showwarning("Warning", "Please enter a URL first")
            return
            
        try:
            self.append_output("🔍 Fetching video information...\n")
            result = subprocess.run(["yt-dlp", "--get-title", "--get-duration", url], 
                                  capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0:
                info = result.stdout.strip().split('\n')
                self.append_output(f"📹 Title: {info[0] if info else 'N/A'}\n")
                self.append_output(f"⏱️ Duration: {info[1] if len(info) > 1 else 'N/A'}\n")
                self.append_output("✅ Video information retrieved successfully!\n")
            else:
                self.append_output("❌ Failed to get video information\n")
                
        except subprocess.TimeoutExpired:
            self.append_output("⏰ Timeout while fetching video information\n")
        except Exception as e:
            self.append_output(f"❌ Error: {str(e)}\n")
        
    def start_download(self):
        url = self.url_var.get().strip()
        if not url:
            messagebox.showerror("Error", "❌ Please enter a URL")
            return
            
        if not self.mp3_var.get() and not self.video_var.get():
            messagebox.showerror("Error", "❌ Please select at least one download option")
            return
            
        # Check if yt-dlp is available
        try:
            subprocess.run(["yt-dlp", "--version"], capture_output=True, check=True, timeout=10)
        except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
            messagebox.showerror("Error", 
                "yt-dlp not found!\n\n"
                "Please install yt-dlp first:\n"
                "pip install yt-dlp\n\n"
                "Also make sure FFmpeg is installed for audio conversion.")
            return
            
        self.downloading = True
        self.download_btn.config(state="disabled")
        self.progress_bar.start(15)
        self.progress_var.set("Starting download...")
        self.status_var.set("⏬ Downloading...")
        
        # Clear previous output
        self.output_text.delete(1.0, tk.END)
        
        # Start download in separate thread
        thread = threading.Thread(target=self.download_thread, args=(url,))
        thread.daemon = True
        thread.start()
        
    def download_thread(self, url):
        try:
            commands = self.build_commands(url)
            
            for i, command in enumerate(commands):
                if not self.downloading:
                    break
                    
                self.append_output(f"🔧 Executing command {i+1}/{len(commands)}:\n")
                self.append_output(f"💻 {' '.join(command)}\n\n")
                self.progress_var.set(f"Downloading... ({i+1}/{len(commands)})")
                
                process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, 
                                         text=True, bufsize=1, universal_newlines=True)
                
                # Read output in real-time
                for line in process.stdout:
                    if self.downloading:
                        self.append_output(line)
                    else:
                        process.terminate()
                        break
                    
                process.wait()
                
                if process.returncode != 0 and self.downloading:
                    self.append_output(f"\n❌ Error: Process exited with code {process.returncode}\n")
                    self.status_var.set("❌ Download failed")
                    break
                else:
                    self.append_output(f"✅ Command {i+1} completed successfully!\n\n")
                    
            if self.downloading:
                self.progress_var.set("Download completed! 🎉")
                self.status_var.set("✅ Download completed")
                self.append_output("\n🎉 All downloads completed successfully!\n")
                
        except Exception as e:
            self.append_output(f"\n❌ Error: {str(e)}\n")
            self.progress_var.set("Download failed! ❌")
            self.status_var.set("❌ Download failed")
            messagebox.showerror("Error", f"Download failed: {str(e)}")
        finally:
            self.downloading = False
            self.root.after(0, self.download_finished)
            
    def build_commands(self, url):
        commands = []
        base_cmd = ["yt-dlp", "--newline"]  # Newline for real-time output
        
        # Add output template
        output_template = f"-o {os.path.join(self.download_path_var.get(), '%(title)s.%(ext)s')}"
        base_cmd.extend(output_template.split())
        
        # MP3 download
        if self.mp3_var.get():
            mp3_cmd = base_cmd.copy()
            mp3_cmd.extend(["-x", "--audio-format", "mp3"])
            
            # Audio quality
            quality = self.mp3_quality_var.get()
            if quality == "0 (Best VBR)":
                mp3_cmd.extend(["--audio-quality", "0"])
            else:
                mp3_cmd.extend(["--audio-quality", quality])
                
            # Embed thumbnail
            if self.embed_thumb_var.get():
                mp3_cmd.append("--embed-thumbnail")
                
            mp3_cmd.append(url)
            commands.append(mp3_cmd)
        
        # Video download
        if self.video_var.get():
            video_cmd = base_cmd.copy()
            
            # Resolution selection
            resolution = self.resolution_var.get()
            if resolution == "4K":
                video_cmd.extend(["-f", "bestvideo[height<=2160]+bestaudio/best[height<=2160]"])
            elif resolution == "1440p":
                video_cmd.extend(["-f", "bestvideo[height<=1440]+bestaudio/best[height<=1440]"])
            elif resolution == "1080p":
                video_cmd.extend(["-f", "bestvideo[height<=1080]+bestaudio/best[height<=1080]"])
            elif resolution == "720p":
                video_cmd.extend(["-f", "bestvideo[height<=720]+bestaudio/best[height<=720]"])
            elif resolution == "480p":
                video_cmd.extend(["-f", "bestvideo[height<=480]+bestaudio/best[height<=480]"])
            else:  # 360p
                video_cmd.extend(["-f", "bestvideo[height<=360]+bestaudio/best[height<=360]"])
            
            # Embed subtitles
            if self.embed_subs_var.get():
                video_cmd.append("--write-sub")
                video_cmd.append("--embed-subs")
                
            video_cmd.append(url)
            commands.append(video_cmd)
            
        return commands
        
    def append_output(self, text):
        def update():
            self.output_text.insert(tk.END, text)
            self.output_text.see(tk.END)
            self.output_text.update_idletasks()
            
        self.root.after(0, update)
        
    def download_finished(self):
        self.progress_bar.stop()
        self.download_btn.config(state="normal")

    def on_closing(self):
        self.downloading = False
        self.root.destroy()

def main():
    root = tk.Tk()
    app = YTDLPGUI(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    
    # Center the window
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    root.mainloop()

if __name__ == "__main__":
    main()
