# Tagz icon generator — price tag symbol and uniform wordmark
from PIL import Image, ImageDraw, ImageFont

S = 1024
WHITE = "#ffffff"
BLACK = "#000000"
FONT = "Anton.ttf"
WORDMARK_SIZE = 205
LINE_WIDTH = 26


def draw_price_tag(draw, cx, cy):
    points = [
        (cx - 155, cy - 110),
        (cx + 35, cy - 110),
        (cx + 155, cy),
        (cx + 35, cy + 110),
        (cx - 155, cy + 110),
    ]
    draw.line(points + [points[0]], fill=WHITE, width=LINE_WIDTH, joint="curve")
    draw.ellipse(
        [cx + 24, cy - 26, cx + 76, cy + 26],
        outline=WHITE,
        width=14,
    )


def draw_wordmark(draw):
    text = "Tagz"
    font = ImageFont.truetype(FONT, WORDMARK_SIZE)
    gap = 7
    widths = []
    for char in text:
        box = draw.textbbox((0, 0), char, font=font)
        widths.append(box[2] - box[0])
    total = sum(widths) + gap * (len(text) - 1)
    x = (S - total) / 2
    for char, width in zip(text, widths):
        draw.text((x, 860), char, font=font, fill=WHITE, anchor="ls")
        x += width + gap


def make_icon():
    image = Image.new("RGB", (S, S), BLACK)
    draw = ImageDraw.Draw(image)
    draw.rectangle([120, 112, S-120, 126], fill=WHITE)
    draw.rectangle([120, S-126, S-120, S-112], fill=WHITE)
    draw_price_tag(draw, S/2, 330)
    draw_wordmark(draw)
    return image


if __name__ == "__main__":
    icon = make_icon()
    icon.resize((512, 512), Image.Resampling.LANCZOS).save("icon-512.png")
    icon.resize((192, 192), Image.Resampling.LANCZOS).save("icon-192.png")
    icon.resize((180, 180), Image.Resampling.LANCZOS).save("icon-180.png")
    print("Tagz icons generated")
