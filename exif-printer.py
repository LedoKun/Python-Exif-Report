import exifread
from fpdf import FPDF
from datetime import datetime
import Tyf
import glob


class PDF(FPDF):
    def __init__(self):
        super().__init__()

    def footer(self):
        now = datetime.now()  # current date and time
        date_time = now.strftime("%Y-%m-%d, %H:%M:%S")

        self.set_y(-15)
        self.set_font("Arial", "B", 8)
        self.cell(
            0,
            8,
            f"Timestamp: {date_time}",
            0,
            0,
            "C",
        )


def get_exif(path_to_image: str) -> dict:
    image_file = open(path_to_image, "rb")
    tags = exifread.process_file(image_file)

    for item in ("JPEGThumbnail", "TIFFThumbnail", "Filename", "EXIF MakerNote"):
        try:
            del tags[item]

        except:
            pass

    image_file.close()

    return tags

all_photos = glob.glob("Photos/*")

list_of_lists = []
tmp_list = []

for photo in all_photos:
    tmp_list.append(photo)

    if len(tmp_list) == 5:
        list_of_lists.append(tmp_list)
        tmp_list = []

if tmp_list:
    list_of_lists.append(tmp_list)

count = 1
for a_list in list_of_lists:

    # initiate pdf
    pdf = PDF()

    for photo_path in a_list:
        print(f"Processing: {photo_path}")

        pdf.add_page()

        filename = photo_path
        tags = get_exif(filename)

        # get location map
        tyf_img = Tyf.open(filename)
        map_filename = f"GeoTemp/{hash(filename)}.png"

        try:
            Tyf.ifd.dump_mapbox_location(tyf_img.ifd0, map_filename)
            has_map = True

        except:
            has_map = False

        # cell height
        ch = 8

        # page width
        pw = 210 - (2 * 10)

        pdf.set_font("Arial", "B", 12)
        pdf.cell(w=pw, h=ch * 2, txt=f"Filename: {filename}", ln=1, align="C")

        pdf.set_font("Arial", "B", 8)
        pdf.cell(w=pw, h=ch, txt="Image & Location:", ln=1)
        pdf.cell(w=pw, h=100, ln=1)

        pdf.image(filename, x=None, y=32, w=0, h=98)

        if has_map:
            pdf.image(map_filename, x=(2 * pw / 3) + 15, y=32, w=(pw / 3), h=0)

        pdf.set_font("Arial", "B", 12)
        pdf.cell(w=pw, h=ch * 2, txt="EXIF Information", ln=1, align="C")

        # cell height
        ch = 4

        ln = 0
        for tag, value in tags.items():
            if "GPS" in tag or "DateTime" in tag:
                pdf.set_font("Arial", "B", 8)

            else:
                pdf.set_font("Arial", "", 8)

            pdf.cell(w=pw / 2, h=ch, txt=f"{tag}: {value}", ln=ln)

            if ln == 0:
                ln = 1

            else:
                ln = 0

    print(f"Writing PDF: ./OutputPDFs/{count}.pdf")
    pdf.output(f"./OutputPDFs/{count}.pdf", "F")
    count += 1
