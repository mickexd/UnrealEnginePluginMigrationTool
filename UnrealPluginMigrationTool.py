import subprocess
from tkinter import Tk, Canvas, Label, Entry, Button, filedialog, messagebox
import os


def get_engine_path():
    engine_path = filedialog.askdirectory()
    engine_path = engine_path.replace("/", "\\")
    engine_entry.delete(0, "end")
    engine_entry.insert(0, engine_path)


def get_origin_path():
    origin_path = filedialog.askopenfilename(filetypes=[("Plugin Files", "*.uplugin")])
    origin_path = origin_path.replace("/", "\\")
    origin_entry.delete(0, "end")
    origin_entry.insert(0, origin_path)


def get_output_path():
    output_path = filedialog.askdirectory()
    output_path = output_path.replace("/", "\\")
    output_entry.delete(0, "end")
    output_entry.insert(0, output_path)


def migrate_plugin():
    origin = origin_entry.get()
    output = output_entry.get()
    engine = engine_entry.get()
    engine = '"' + engine + '"'
    origin = '"' + origin + '"'
    output = '"' + output + '"'

    command = rf"{engine}\Engine\Build\BatchFiles\RunUAT.bat BuildPlugin -plugin={origin} -package={output}\Migrated"

    try:
        subprocess.run(command, shell=True)
        messagebox.showinfo(
            title="Migration complete", message="Your plugin was succesfully ported"
        )
    except Exception as e:
        messagebox.showerror(title="Error", message="Error during the migration")


window = Tk()
window.title("Unreal Engine Plugin Migration Tool")
window.config(padx=50, pady=50)
canvas = Canvas(window, width=800, height=600)

engine_label = Label(window, text="Engine Path:")
engine_label.grid(column=0, row=0)

engine_entry = Entry(window, width=60)
engine_entry.grid(column=1, row=0)
engine_entry.insert(0, "Select the root of the engine folder")

engine_button = Button(window, text="Select Engine Path", command=get_engine_path)
engine_button.grid(column=2, row=0)

origin_label = Label(window, text="Origin Path:")
origin_label.grid(column=0, row=1)

origin_entry = Entry(window, width=60)
origin_entry.grid(column=1, row=1)

origin_button = Button(window, text="Select Origin Plugin", command=get_origin_path)
origin_button.grid(column=2, row=1)

output_label = Label(window, text="Output Path:")
output_label.grid(column=0, row=2)

output_entry = Entry(window, width=60)
output_entry.grid(column=1, row=2)

output_button = Button(window, text="Select Output Path", command=get_output_path)
output_button.grid(column=2, row=2)

print_button = Button(window, text="Begin Plugin Migration", command=migrate_plugin)
print_button.grid(column=1, row=3)

window.mainloop()
