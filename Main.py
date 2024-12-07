import pdfplumber
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import re

def extract_names_from_text(text) -> list:
    teacher_name_pattern = r'^(?:- )?(?:Classroom\s+)?([A-Z][a-zA-Z-]+(?:\s[A-Z][a-zA-Z-]+){1,3})$'
    teacher_names = re.findall(teacher_name_pattern, text, re.MULTILINE) # re.MULTILINE is used to match the start of each teacher name
    exclude_list = {'Course Schedule', 'Omnivox', 'Personal Data', 'Courses List', 'Classroom Classroom'} # create a set of strings to exclude unnecessary names
    teacher_names = [name for name in teacher_names if name not in exclude_list]

    return teacher_names

def extract_table_from_pdf(pdf_path: str, page_number: int, text_widget: tk.Text) -> None:
    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[page_number]
        text = page.extract_text()
        teacher_names = extract_names_from_text(text)

        text_widget.insert(tk.END, "Student Name:\n")
        for teacher_name in teacher_names:
            text_widget.insert(tk.END, f"- {teacher_name}\n")
        text_widget.insert(tk.END, "\n")

def select_pdf_file(text_widget) -> None:
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        extract_table_from_pdf(file_path, page_number=0, text_widget=text_widget)

def exit_app() -> None:
    root.destroy()

root = tk.Tk()
root.title("Schedule Review")

select_button = tk.Button(root, text="Select PDF", command=lambda: select_pdf_file(text_widget))
select_button.pack()

exit_button = tk.Button(root, text="Exit", command=exit_app)
exit_button.pack()

text_widget = tk.Text(root, wrap='word', width=80, height=20)
text_widget.pack()

root.mainloop()