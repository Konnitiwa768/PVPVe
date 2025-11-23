import os
from pathlib import Path
from PIL import Image, ImageEnhance

# 元画像フォルダ
SOURCE_DIR = Path("resource_pack/textures/blocks")
# 出力先
DEST_DIR = Path("Cold_RP/textures/blocks")
DEST_DIR.mkdir(parents=True, exist_ok=True)

# 自然系ブロックのファイル名や部分一致リスト
NATURE_BLOCKS = [
    "grass", "dirt", "sand", "gravel", "stone", "cobblestone",
    "oak", "spruce", "birch", "jungle", "acacia", "dark_oak",
    "leaves", "log", "mushroom", "mycelium", "podzol", "fern",
    "tall_grass",
    # 部分一致
    "leaf", "wood", "tree",
]

def is_nature_block(filename: str) -> bool:
    lower_name = filename.lower()
    return any(name in lower_name for name in NATURE_BLOCKS)

def icefy_image(img: Image.Image) -> Image.Image:
    """
    氷・水色系に色を変換して白を少し上乗せ
    """
    img = img.convert("RGB")
    r, g, b = img.split()
    b = ImageEnhance.Brightness(b).enhance(1.2)
    r = ImageEnhance.Brightness(r).enhance(0.7)
    g = ImageEnhance.Brightness(g).enhance(0.9)
    img = Image.merge("RGB", (r, g, b))
    overlay = Image.new("RGB", img.size, (200, 230, 255))
    img = Image.blend(img, overlay, alpha=0.3)
    return img

def main():
    for f in SOURCE_DIR.iterdir():
        if f.is_file() and f.suffix.lower() in [".png"] and is_nature_block(f.name):
            img = Image.open(f)
            new_img = icefy_image(img)
            new_img.save(DEST_DIR / f.name)
            print(f"Converted: {f.name}")

if __name__ == "__main__":
    main()
