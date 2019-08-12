# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 11:16:17 2019

@author: amz0212
"""

import tkinter as tk
from tkinter import filedialog
import PyPDF2
import stdiomask as pw
import os

root = tk.Tk()
root.withdraw()

ftypes = [
    ('PDF Files', '*.pdf')
]

print("\n\n\n\nPython File Encrypter")
print("Created by Alex Zorn\n")
print("Select a PDF file you want to encrypt\n")
in_file = filedialog.askopenfilename(title='Select a PDF file', filetypes = ftypes)
# Create reader and writer object
pdfReader = PyPDF2.PdfFileReader(in_file)
pdfWriter = PyPDF2.PdfFileWriter()
# Add all pages to writer (accepted answer results into blank pages)
for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))
# Encrypt with your password
print("Enter a password with which to encrypt your PDF file:   \n")
password=pw.getpass()
pdfWriter.encrypt(password,use_128bit=True)

print("\nSelect an output directory to save your encrypted PDF\n\n")
currdir = os.getcwd()
tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Select a directory')

# Write it to an output file. (you can delete unencrypted version now)
resultPdf = open(tempdir + "/" + 'encrypted_output.pdf', 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()
print("PDF File has been protected using 128-bit encryption.")
print("\nFile location: " + tempdir + "/" + "encrypted_output.pdf")
input("\nPress any key to exit....\n\n")

