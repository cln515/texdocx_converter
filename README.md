# Texdocx converter
mutual convertion program of tex file and word file (.docx)

#Purpose

Editing tex source in Microsoft word

-Co-editing under OneDrive environment
-Cooperation with Microsoft word addons such as grammar correction (e.g. Grammarly)

# How to use

- copy python programs to your tex workspace
- $python tex2docx.py
- then all .tex files in the workspace folder are converted to .docx file
 - e.g. root.tex > root.docx
- edit root.docx
- $python docx2tex.py
- then all .docx files in the workspace folder are converted to .tex file

# Notation
Conversion doesn't run when modified time of distination file is later than of a source file


