from PIL import Image, ImageDraw
from pathlib import Path

OUT = Path("assets/nexora/textures")
OUT.mkdir(parents=True, exist_ok=True)
SPEARS = {
 "divina": ((255,205,75,255),(255,246,190,255),(110,70,180,255),(255,255,235,255)),
 "glacial": ((80,210,255,255),(220,250,255,255),(35,105,190,255),(180,245,255,255)),
 "infernal": ((225,65,35,255),(255,190,65,255),(105,25,35,255),(255,235,145,255)),
 "natural": ((75,190,90,255),(195,235,125,255),(80,95,45,255),(240,225,150,255)),
 "trueno": ((245,220,65,255),(255,255,190,255),(65,85,185,255),(180,220,255,255)),
 "vacio": ((135,70,210,255),(225,175,255,255),(35,20,65,255),(245,220,255,255)),
 "marina": ((35,175,190,255),(150,245,235,255),(20,65,115,255),(210,255,250,255)),
 "ancestral": ((165,115,65,255),(235,205,145,255),(75,45,35,255),(255,235,190,255)),
}
def line(d, pts, fill, width=4):
    d.line(pts, fill=fill, width=width)
for name, (main, light, dark, glow) in SPEARS.items():
    im=Image.new("RGBA",(64,64),(0,0,0,0)); d=ImageDraw.Draw(im)
    # diagonal haft, dark outline and bright core
    line(d,[(10,56),(49,17)],dark,8); line(d,[(10,55),(48,17)],main,4)
    line(d,[(13,53),(46,20)],light,1)
    # crossguard
    line(d,[(35,22),(51,36)],dark,7); line(d,[(36,22),(51,35)],main,3)
    # spearhead silhouette, distinct stylized leaf/diamond
    d.polygon([(43,19),(50,2),(55,14),(51,23),(47,26)],fill=dark)
    d.polygon([(46,17),(51,5),(53,15),(49,22)],fill=main)
    d.polygon([(49,14),(51,7),(52,14)],fill=light)
    # rune/elemental accent and pommel
    d.rectangle((7,52,14,59),fill=dark); d.rectangle((9,53,12,57),fill=glow)
    d.point((42,27),fill=glow); d.point((39,30),fill=light)
    if name=="infernal":
        d.polygon([(52,3),(57,0),(55,8)],fill=glow)
        d.point((45,24),fill=(255,80,20,255))
    elif name=="glacial":
        d.point((55,18),fill=glow); d.point((43,12),fill=glow)
    elif name=="trueno":
        d.line([(54,5),(59,10),(55,11),(60,16)],fill=glow,width=2)
    elif name=="natural":
        d.point((33,32),fill=(130,225,85,255)); d.point((29,36),fill=glow)
    elif name=="vacio":
        d.point((55,7),fill=(40,10,75,255)); d.point((48,12),fill=glow)
    elif name=="marina":
        d.point((55,18),fill=glow); d.point((34,34),fill=(80,220,235,255))
    elif name=="ancestral":
        d.rectangle((36,28,38,30),fill=glow); d.point((54,13),fill=light)
    else:
        d.point((54,10),fill=glow); d.point((38,28),fill=light)
    im.save(OUT/"items"/(name+".png"))
# Astral bow: recognizable curved bow with luminous string.
im=Image.new("RGBA",(64,64),(0,0,0,0)); d=ImageDraw.Draw(im)
d.arc((8,3,56,61),250,110,fill=(80,35,145,255),width=8)
d.arc((11,6,53,58),250,110,fill=(210,170,255,255),width=3)
line(d,[(18,12),(46,52)],(245,235,255,255),1)
for p in [(19,13),(24,21),(29,29),(34,37),(40,45),(46,52)]: d.rectangle((p[0]-1,p[1]-1,p[0]+1,p[1]+1),fill=(125,225,255,255))
im.save(OUT/"items"/"astral.png")
# Four visibly distinct chestplate inventory icons.
ARMORS={
 "divina":((245,190,55,255),(255,245,175,255),(105,65,155,255)),
 "infernal":((190,45,30,255),(255,150,45,255),(65,20,30,255)),
 "glacial":((70,175,230,255),(205,245,255,255),(35,75,135,255)),
 "vacio":((105,55,170,255),(210,155,255,255),(30,15,55,255)),
}
for name,(a,b,c) in ARMORS.items():
    im=Image.new("RGBA",(64,64),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.polygon([(16,10),(25,14),(39,14),(48,10),(59,20),(51,34),(46,29),(46,56),(18,56),(18,29),(13,34),(5,20)],fill=c)
    d.polygon([(17,13),(25,17),(39,17),(47,13),(54,21),(47,29),(42,24),(42,51),(22,51),(22,24),(17,29),(10,21)],fill=a)
    d.polygon([(27,18),(37,18),(40,30),(32,39),(24,30)],fill=b)
    d.rectangle((29,42,35,48),fill=b)
    if name=="divina":
        d.polygon([(32,5),(35,14),(32,20),(29,14)],fill=(255,255,225,255))
    elif name=="infernal":
        d.polygon([(22,8),(27,14),(23,20),(18,14)],fill=(255,95,25,255))
    elif name=="glacial":
        d.polygon([(32,5),(36,13),(32,19),(28,13)],fill=(225,255,255,255))
    else:
        d.ellipse((27,21,37,31),outline=(235,190,255,255),width=2)
    im.save(OUT/"armor"/(name+"_chestplate.png"))
print("Generated 13 distinct NEXORA item textures.")

# Three boss fragments use diamond-hoe damage predicates supported by 1.12.2.
FRAGMENTS = {
 "DIVINO": ((250,205,75,255),(255,248,190,255),(110,65,160,255)),
 "INFERNAL": ((210,55,30,255),(255,175,55,255),(75,18,25,255)),
 "GLACIAL": ((70,190,245,255),(225,250,255,255),(30,75,145,255)),
}
for name,(a,b,c) in FRAGMENTS.items():
    im=Image.new("RGBA",(64,64),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.ellipse((8,8,56,56),fill=c,outline=b,width=3)
    d.polygon([(32,5),(43,23),(39,32),(50,43),(32,58),(14,43),(25,32),(21,23)],fill=a,outline=b)
    d.polygon([(32,12),(37,27),(32,35),(27,27)],fill=b)
    d.rectangle((29,36,35,47),fill=c)
    im.save(OUT/"items"/("fragment_"+name.lower()+".png"))
# Individual inventory icons for every armor piece in all four sets.
for name,(a,b,c) in ARMORS.items():
    for piece in ("helmet","leggings","boots"):
        im=Image.new("RGBA",(64,64),(0,0,0,0)); d=ImageDraw.Draw(im)
        if piece=="helmet":
            d.polygon([(13,17),(22,7),(42,7),(51,17),(55,43),(9,43)],fill=c,outline=b)
            d.polygon([(18,18),(25,12),(39,12),(46,18),(49,37),(15,37)],fill=a)
            d.rectangle((23,24,41,30),fill=b)
        elif piece=="leggings":
            d.polygon([(12,7),(52,7),(48,57),(35,57),(32,32),(29,57),(16,57)],fill=c,outline=b)
            d.polygon([(17,12),(47,12),(43,52),(37,52),(32,28),(27,52),(21,52)],fill=a)
            d.rectangle((28,15,36,26),fill=b)
        else:
            d.polygon([(10,13),(30,20),(34,20),(54,13),(58,38),(43,42),(39,58),(25,58),(21,42),(6,38)],fill=c,outline=b)
            d.polygon([(15,18),(29,25),(35,25),(49,18),(51,34),(39,38),(35,53),(29,53),(25,38),(13,34)],fill=a)
            d.rectangle((27,28,37,37),fill=b)
        im.save(OUT/"armor"/(name+"_"+piece+".png"))


# Compatibility fallback for clients that load vanilla PNG overrides but do not
# implement 1.12 item-model predicate overrides (common in browser clients).
# These make the pack visibly change vanilla items even without custom-model support.
VANILLA_ITEMS = Path("assets/minecraft/textures/items")
VANILLA_ITEMS.mkdir(parents=True, exist_ok=True)
# Base diamond sword: dark steel blade with a gold/purple NEXORA core.
im = Image.new("RGBA", (64, 64), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
line(d, [(13, 53), (49, 9)], (35, 25, 55, 255), 10)
line(d, [(15, 51), (48, 10)], (120, 75, 185, 255), 6)
line(d, [(17, 48), (46, 13)], (245, 220, 255, 255), 2)
d.polygon([(45, 7), (55, 2), (51, 14), (47, 17)], fill=(255, 215, 95, 255))
line(d, [(8, 47), (22, 59)], (65, 35, 90, 255), 7)
line(d, [(10, 47), (21, 57)], (235, 185, 75, 255), 3)
d.rectangle((5, 53, 14, 61), fill=(45, 25, 65, 255))
d.rectangle((7, 54, 11, 58), fill=(255, 215, 95, 255))
im.save(VANILLA_ITEMS / "diamond_sword.png")
# Base diamond hoe: visible crystalline NEXORA shard.
im = Image.new("RGBA", (64, 64), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
line(d, [(15, 54), (48, 10)], (40, 25, 65, 255), 7)
line(d, [(17, 52), (47, 11)], (160, 105, 220, 255), 3)
d.polygon([(36, 8), (51, 3), (57, 17), (43, 25), (33, 19)], fill=(75, 40, 120, 255), outline=(245, 220, 255, 255))
d.polygon([(43, 8), (51, 6), (53, 15), (43, 20)], fill=(210, 170, 255, 255))
im.save(VANILLA_ITEMS / "diamond_hoe.png")
# Vanilla armor inventory icons use the NEXORA Divine palette as a visible fallback.
# Per-set icons still depend on the custom model predicates above.
for piece in ("helmet", "chestplate", "leggings", "boots"):
    src = OUT / "armor" / ("divina_" + piece + ".png")
    if src.exists():
        im = Image.open(src).convert("RGBA")
        im.save(VANILLA_ITEMS / ("diamond_" + piece + ".png"))
print("Generated vanilla-path compatibility fallback textures.")
