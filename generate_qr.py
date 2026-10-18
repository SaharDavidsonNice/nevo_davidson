"""Generate qr_code.png pointing at the GitHub Pages site.

Usage:
    pip install -r requirements.txt
    python generate_qr.py [url] [output.png]
"""
import sys

import qrcode

DEFAULT_URL = "https://sahardavidsonnice.github.io/nevo_davidson/"


def main() -> None:
    url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_URL
    output = sys.argv[2] if len(sys.argv) > 2 else "qr_code.png"

    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=12,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr.make_image(fill_color="black", back_color="white").save(output)
    print(f"Saved {output} -> {url}")


if __name__ == "__main__":
    main()
