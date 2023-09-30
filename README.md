# Python-Exif-Report

**exif-printer.py** is a Python script designed to generate PDF files from a collection of photos located in a directory. The primary objective for writing this script is to prepare evidence by documenting and presenting key information about the photos.

## Requirements

Before running the script, you need to install the following Python libraries:

- `exifread`
- `fpdf`
- `Tyf`

You can install these libraries using `pip`:

```bash
pip install exifread fpdf Tyf
```

## Usage

1. **Photo Directory**: Place your photos in a directory named "Photos" within the same directory as the script.

2. **Run the Script**: Execute the script, and it will process the photos and generate PDFs in the "OutputPDFs" directory.

   ```bash
   python exif-printer.py
   ```

3. **Generated PDFs**: The generated PDFs will be named sequentially, such as "1.pdf," "2.pdf," and so on. They will be saved in the "OutputPDFs" directory.

## Customization

You can customize the script according to your needs:

- Modify the tags to exclude from EXIF metadata extraction by editing the `for item in ("JPEGThumbnail", "TIFFThumbnail", "Filename", "EXIF MakerNote")` loop.

- Adjust the number of photos per PDF by changing the `tmp_list` length check (e.g., `if len(tmp_list) == 5:`).

- Customize the appearance and layout of the PDF by modifying the `PDF` class and its methods.

## Output

The script will generate PDF files in the "OutputPDFs" directory, each containing information about multiple photos, including their filenames, images, and EXIF metadata. These PDFs are suitable for archiving and sharing collections of photos with associated details. They are prepared with the specific objective of being used as evidence in a legal case, providing a comprehensive record of the photos and their metadata. Please ensure your photo directory structure matches the script's expectations for proper functioning.
