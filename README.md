# Automated Multimedia Summarization

This project provides a Gradio-based app to:

- Convert video to text summary and export as PDF
- Convert audio to text summary and export as PDF
- Summarize an existing PDF and export the summarized PDF
- Ask a follow-up question on the generated summary (demo logic)

## Project Structure

```
app.py
helpers/
	audio_to_text.py
	extract_text_from_pdf.py
	save_text_to_pdf.py
	summarize_text.py
	video_to_audio.py
output/
requirements.txt
README.md
```

## Requirements

- Python 3.10+ (recommended)
- FFmpeg (required for audio/video processing)
- Internet connection for model download (first run)

## Setup

### 1) Create and activate virtual environment

Windows (PowerShell):

```powershell
py -m venv venv
venv\Scripts\activate
```

Git Bash:

```bash
py -m venv venv
source venv/Scripts/activate
```

### 2) Install dependencies

```bash
pip install -U pip
pip install gradio moviepy pydub SpeechRecognition pypdf fpdf2 transformers torch sentencepiece
```

### 3) Install FFmpeg

Windows:

```powershell
winget install -e --id Gyan.FFmpeg
```

After installing FFmpeg, close and reopen terminal/VS Code so PATH updates are applied.

## Run the App

```bash
py app.py
```

Open the URL shown in terminal (usually `http://127.0.0.1:7860`).

## Screenshots

### App Interface

![App Interface](assets/images/app-interface.png)
 
### Summary Output Example

![Summary Output](assets/images/summary-output.png)

## How to Use

1. Select a task from dropdown.
2. Upload a video/audio/PDF file.
3. Click **Generate Summary**.
4. Download the generated summary PDF from the output panel.
5. (Optional) Ask a question in the Q&A section.

## Common Issues

### 1) `Couldn't find ffmpeg or avconv`

- Install FFmpeg and restart terminal/VS Code.
- Verify FFmpeg is available:

```bash
ffmpeg -version
```

### 2) Hugging Face symlink warning on Windows

This is a warning, not a failure. You can ignore it or set:

```powershell
setx HF_HUB_DISABLE_SYMLINKS_WARNING 1
```

### 3) `You have both PyFPDF & fpdf2 installed`

Keep only `fpdf2`:

```bash
pip uninstall -y fpdf pyfpdf
pip install -U fpdf2
```

### 4) First run is slow

The summarization model (`facebook/bart-large-cnn`) is downloaded on first run and may take several minutes.

## Notes

- `output/` stores generated PDFs and temporary files.
- Current Q&A function is placeholder demo logic and can be replaced with LLM/RAG pipeline.
