import tkinter as tk
from tkinter import filedialog

def open_file_dialog(title, filetypes):
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename(title=title, filetypes=filetypes)

def save_file_dialog(title, filetypes, defaultextension):
    root = tk.Tk()
    root.withdraw()
    return filedialog.asksaveasfilename(title=title, filetypes=filetypes, defaultextension=defaultextension)

input_filename = open_file_dialog("Select input text file", [("Text files", "*.txt"), ("All files", "*.*")])
output_filename = save_file_dialog("Select output text file", [("Text files", "*.txt"), ("All files", "*.*")], defaultextension=".txt")

if input_filename and output_filename:
    with open(input_filename, 'r', encoding='utf8') as infile:
        lines = infile.read().split('\n')

    formatted_lines = []
    previous_speaker = None

    for line in lines:
        if ':  ' in line:
            line = line.replace(':  ', ': ')
            
        if ': ' in line:
            speaker, content = line.split(': ', 1)

            if speaker != previous_speaker:
                formatted_lines.append(line)
            else:
                formatted_lines[-1] += f' {content}'

            previous_speaker = speaker
        elif line.strip():
            formatted_lines.append(line)

    formatted_text = '\n'.join(formatted_lines)


    with open(output_filename, 'w') as outfile:
        outfile.write(formatted_text)
else:
    print("No files selected. Exiting.")
