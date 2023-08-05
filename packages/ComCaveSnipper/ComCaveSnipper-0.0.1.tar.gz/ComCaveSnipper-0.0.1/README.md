**What is it?**

This is a small tool for the Comecave Launcher, to insert the pin automatically.
The tool grabs the screen and the related window, reads the given pin and does the mouse clicks for you.

**Requirements**

You need min _Python 3.7_ and  `tesseract-ocr`, 
download here https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0-alpha.20191030.exe

**Setup**
Check the _PATH_ in `framegrab.py` for tesseract. It should be something like `C:\Program Files\Tesseract-OCR\tesseract.exe`. 
If there are issues add the path to your _PATH_ in the system environment variable. 
Go to _Systemsteuerung\Alle Systemsteuerungselemente\System_ and click
on _Erweiterte Systemeinstellungen_. 
There choose _Umgebungsvariablen_. Click on Path in _Benutzervariablen_ and check if there is the right path to 
your _tesseract directory_. It should be like `C:\Program Files\Tesseract-OCR\`. 

**Known Issues**

If the screen resolution is bad, the tool is likely to make mistakes as it does not recognize the numbers correctly.

