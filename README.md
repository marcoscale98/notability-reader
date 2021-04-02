# notability-reader
This program tries to read Notability files and visualize them on screen 
(in particularly on Windows where it's missing 
the Notability App)   

## How does it work a .note file?
https://jvns.ca/blog/2018/03/31/reverse-engineering-notability-format/  
## Roadmap  
1. A .note to PDF file converter  
1.1. Unzip the .note folder  
1.2. Find the points of freehand writing in _Session.plist_  
1.3. Apply points to source PDF (in _PDFs_ folder)  
2. A command line reader of .note files  
3. A .note file reader with a GUI  

## Other informations
- the directory "bdb_transazioni" contains an example of 
.note file (already unzipped)
- Session.plist contains information from freehand writing
