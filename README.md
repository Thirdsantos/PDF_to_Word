# 📄 PDF to Word Converter

A simple and user-friendly desktop application that converts PDF files to Word documents (.docx format) with a clean graphical interface.

##  Features

- **Simple GUI**: Clean and intuitive interface built with Tkinter
- **One-click conversion**: Just select a PDF file and convert it instantly
- **Automatic saving**: Converted files are automatically saved to your Downloads folder
- **No installation required**: Standalone executable that runs on Windows
- **Fast conversion**: Efficient PDF to Word conversion using pdf2docx library

##  Quick Start

### Option 1: Download the Executable (Recommended)

1. **Download**: The executable file `app.exe` is located in the `dist/` folder
2. **Run**: Double-click `app.exe` to launch the application
3. **Convert**: Click "📂 Select PDF" to choose your PDF file
4. **Done**: Your converted Word document will be saved to your Downloads folder

### Option 2: Run from Source Code

If you prefer to run the Python source code:

1. **Install Python**: Make sure you have Python 3.7+ installed
2. **Install dependencies**:
   ```bash
   pip install pdf2docx tkinter
   ```
3. **Run the application**:
   ```bash
   python app.py
   ```

##  Requirements

- **Windows 10/11** (for the executable)
- **Python 3.7+** (if running from source)
- **Dependencies** (if running from source):
  - `pdf2docx`
  - `tkinter` (usually comes with Python)

##  How to Use

1. **Launch the Application**
   - Double-click `app.exe` or run `python app.py`

2. **Select PDF File**
   - Click the "📂 Select PDF" button
   - Browse and select your PDF file
   - Only `.pdf` files are supported

3. **Automatic Conversion**
   - The conversion process starts automatically
   - A progress message will appear during conversion

4. **Find Your File**
   - Converted Word documents are saved to your Downloads folder
   - The filename will be the same as your PDF but with `.docx` extension

##  File Locations

- **Executable**: `dist/app.exe`
- **Source Code**: `app.py`
- **Build Configuration**: `app.spec`
- **Output Files**: Your system's Downloads folder

##  Building the Executable

If you want to build your own executable:

1. **Install PyInstaller**:
   ```bash
   pip install pyinstaller
   ```

2. **Build the executable**:
   ```bash
   pyinstaller --onefile --windowed app.py
   ```

3. **Find the executable** in the `dist/` folder

##  Project Structure

```
pdf_converter/
├── app.py              # Main application code
├── app.spec            # PyInstaller configuration
├── dist/               # Built executable
│   └── app.exe        # Windows executable
├── build/              # Build artifacts
└── venv/               # Virtual environment
```

##  Troubleshooting

### Common Issues

- **"Conversion failed" error**: Make sure your PDF file isn't corrupted or password-protected
- **File not found**: Check that the PDF file exists and is accessible
- **Permission denied**: Ensure you have write access to your Downloads folder

### Tips

- Use PDF files that contain text (not just scanned images)
- Large PDF files may take longer to convert
- The application automatically handles file naming conflicts

##  Developer

**Developer**: Alfred


---

**Note**: This application is designed for Windows and has been tested on Windows 10/11. For other operating systems, you may need to run the Python source code directly. 