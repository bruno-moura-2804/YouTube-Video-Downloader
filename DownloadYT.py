import os
import platform
import tkinter as tk
from pytubefix import YouTube
from tkinter import messagebox

def download_video():
    url = entry.get()
    if not url:
        messagebox.showerror("Erro", "Por favor, insira uma URL válida.")
        return
    
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        
        system = platform.system().lower()

        if system == "windows":
            download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        elif system == "linux":
            download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        elif system == "darwin":
            download_folder = os.path.join(os.path.expanduser("~"), "Pictures")
        elif system == "android":
            download_folder = "/storage/emulated/0/DCIM/Camera"
        elif system == "ios":
            download_folder = os.path.join(os.path.expanduser("~"), "Documents")
        else:
            download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        
        stream.download(download_folder)
        
        messagebox.showinfo("Sucesso", f"Download Completo!\nArquivo salvo em: {download_folder}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

root = tk.Tk()
root.title("Download de Vídeos do YouTube")
root.geometry("400x200")

label = tk.Label(root, text="Digite a URL do YouTube:")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

download_button = tk.Button(root, text="Baixar Vídeo", command=download_video)
download_button.pack(pady=20)

root.mainloop()
