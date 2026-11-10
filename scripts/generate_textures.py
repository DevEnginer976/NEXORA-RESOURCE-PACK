from PIL import Image, ImageDraw
from pathlib import Path

OUT = Path("assets/nexora/textures")
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "items").mkdir(parents=True, exist_ok=True)
(OUT / "armor").mkdir(parents=True, exist_ok=True)
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


# ---------------------------------------------------------------------------
# NEXORA 50-weapon expansion: unique pixel-art icons + 1.12.2 damage models.
# The damage predicate is the supported pre-1.14 model-selection mechanism.
# ---------------------------------------------------------------------------
import json

ARSENAL = [
("EMBERFANG","SWORD","FUEGO"),("PYRA","SWORD","FUEGO"),("INFERNUS","SWORD","FUEGO"),
("SOLARIS","SWORD","LUZ"),("DAWNBREAKER","SWORD","LUZ"),("FROSTBITE","SWORD","HIELO"),
("PERMAFROST","SWORD","HIELO"),("TIDEBREAK","SWORD","AGUA"),("ABYSSAL","SWORD","AGUA"),
("THUNDERCALL","SWORD","RAYO"),("STORMREND","SWORD","RAYO"),("VOIDEDGE","SWORD","VACIO"),
("NIGHTFALL","SWORD","VACIO"),("SOULREAVER","SWORD","ALMA"),("WRAITH","SWORD","ALMA"),
("VERDANT","SWORD","NATURALEZA"),("THORNHEART","SWORD","NATURALEZA"),("DRAGONFANG","SWORD","DRAGON"),
("WYRMKILLER","SWORD","DRAGON"),("STARFALL","SWORD","ARCANO"),("ASTRALIS","SWORD","ARCANO"),
("RUNIC","SWORD","ARCANO"),("OBLIVION","SWORD","VACIO"),("CROWNFALL","SWORD","SOMBRA"),
("ETERNITY","SWORD","LUZ"),
("TITANBREAKER","AXE","TIERRA"),("DOOMCLEAVER","AXE","SOMBRA"),("MAGMAREND","AXE","FUEGO"),
("GLACIERAXE","AXE","HIELO"),("SKYREND","AXE","RAYO"),("EARTHSHAKER","AXE","TIERRA"),
("BONECLEAVER","AXE","ALMA"),("VOIDCHOPPER","AXE","VACIO"),("SUNSPLITTER","AXE","LUZ"),
("BEASTFELL","AXE","NATURALEZA"),
("ARCANEFOCUS","HOE","ARCANO"),("STORMSTAFF","HOE","RAYO"),("FROSTWAND","HOE","HIELO"),
("PYRESTAFF","HOE","FUEGO"),("VOIDCALLER","HOE","VACIO"),("LIFEBLOOM","HOE","NATURALEZA"),
("SOULWEAVER","HOE","ALMA"),("TIDECALLER","HOE","AGUA"),("STARROD","HOE","LUZ"),
("RUNICSTAFF","HOE","ARCANO"),
("SKYPIERCER","BOW","RAYO"),("MOONBOW","BOW","ARCANO"),("PHOENIXBOW","BOW","FUEGO"),
("VOIDLONGBOW","BOW","VACIO"),("STARHUNTER","BOW","LUZ")
]
PALETTES = {
 "FUEGO":((190,38,28,255),(255,174,62,255),(65,18,24,255),(255,225,145,255)),
 "LUZ":((220,175,65,255),(255,246,180,255),(100,65,125,255),(255,255,235,255)),
 "HIELO":((55,155,220,255),(210,245,255,255),(25,55,110,255),(235,255,255,255)),
 "AGUA":((25,145,165,255),(140,235,230,255),(15,50,95,255),(205,255,250,255)),
 "RAYO":((70,100,205,255),(255,235,95,255),(25,30,85,255),(230,250,255,255)),
 "VACIO":((105,50,165,255),(205,150,255,255),(25,12,50,255),(245,220,255,255)),
 "ALMA":((145,85,175,255),(235,195,255,255),(45,25,70,255),(255,235,255,255)),
 "NATURALEZA":((55,145,75,255),(180,225,105,255),(25,65,40,255),(230,255,175,255)),
 "DRAGON":((155,45,35,255),(245,155,65,255),(55,20,25,255),(255,225,155,255)),
 "ARCANO":((100,75,185,255),(205,175,255,255),(35,25,80,255),(245,230,255,255)),
 "SOMBRA":((65,55,85,255),(175,125,195,255),(15,12,25,255),(225,195,245,255)),
 "TIERRA":((125,90,50,255),(220,185,105,255),(50,35,25,255),(245,225,165,255))
}
ARSENAL_DIR = OUT / "items" / "arsenal"
ARSENAL_DIR.mkdir(parents=True, exist_ok=True)
models_dir = Path("assets/nexora/models/item")
models_dir.mkdir(parents=True, exist_ok=True)
material_counts = {"SWORD":0,"AXE":0,"HOE":0,"BOW":0}
model_overrides = {"SWORD":[],"AXE":[],"HOE":[],"BOW":[]}
for idx,(weapon_id,kind,element) in enumerate(ARSENAL):
    material_counts[kind] += 1
    local_index = material_counts[kind]
    if kind == "SWORD":
        damage = 0.10 + (local_index-1)*0.01
    elif kind == "AXE":
        damage = 0.01 + (local_index-1)*0.01
    elif kind == "HOE":
        damage = 0.10 + (local_index-1)*0.01
    else:
        damage = 0.01 + (local_index-1)*0.01
    main,light,dark,glow = PALETTES[element]
    im = Image.new("RGBA",(64,64),(0,0,0,0)); d = ImageDraw.Draw(im)
    # The same elemental palette is rendered through four distinct silhouettes.
    if kind == "SWORD":
        d.polygon([(8,54),(42,13),(54,3),(49,20),(15,59)],fill=dark,outline=glow)
        d.polygon([(13,51),(43,14),(50,8),(46,20),(17,55)],fill=main)
        d.line([(18,47),(45,16)],fill=light,width=2)
        d.polygon([(7,45),(20,57),(16,62),(3,50)],fill=dark)
        d.line([(5,47),(18,59)],fill=glow,width=2)
        d.rectangle((8,55,14,61),fill=light)
    elif kind == "AXE":
        d.line([(12,58),(43,13)],fill=dark,width=9); d.line([(14,56),(43,14)],fill=main,width=4)
        d.polygon([(29,22),(35,7),(54,4),(61,18),(52,35),(39,31)],fill=dark,outline=glow)
        d.polygon([(34,20),(39,10),(53,9),(56,18),(49,29),(40,27)],fill=main)
        d.line([(39,13),(52,12),(55,18)],fill=light,width=3)
        d.rectangle((9,53,18,61),fill=glow)
    elif kind == "HOE":
        d.line([(13,59),(44,12)],fill=dark,width=9); d.line([(15,57),(44,13)],fill=main,width=4)
        d.polygon([(36,9),(51,5),(59,14),(54,22),(40,20)],fill=dark,outline=glow)
        d.polygon([(40,10),(51,8),(55,14),(51,18),(41,17)],fill=light)
        d.line([(37,18),(49,26)],fill=main,width=5)
        d.ellipse((8,51,19,62),fill=dark,outline=glow)
    else:
        d.arc((7,3,57,61),250,110,fill=dark,width=9)
        d.arc((10,6,54,58),250,110,fill=main,width=5)
        d.line([(18,12),(46,52)],fill=light,width=2)
        d.polygon([(42,45),(53,53),(46,57)],fill=glow)
        d.polygon([(12,7),(20,11),(16,18)],fill=light)
    # Unique rune geometry per ID: no two generated icons are byte-identical.
    rune_x = 23 + (idx % 5) * 3
    rune_y = 25 + (idx % 4) * 3
    if idx % 4 == 0:
        d.polygon([(rune_x,rune_y-7),(rune_x+5,rune_y),(rune_x,rune_y+7),(rune_x-5,rune_y)],fill=glow)
    elif idx % 4 == 1:
        d.line([(rune_x-5,rune_y+5),(rune_x,rune_y-6),(rune_x+5,rune_y+5)],fill=glow,width=3)
    elif idx % 4 == 2:
        d.ellipse((rune_x-5,rune_y-5,rune_x+5,rune_y+5),outline=light,width=2)
    else:
        d.line([(rune_x-5,rune_y-4),(rune_x+5,rune_y+4)],fill=glow,width=2)
        d.line([(rune_x+4,rune_y-5),(rune_x-4,rune_y+5)],fill=light,width=2)
    d.point((4+(idx*7)%56,4+(idx*11)%56),fill=glow)
    im.save(ARSENAL_DIR/(weapon_id.lower()+".png"))
    model_name = "arsenal_" + weapon_id.lower()
    model = {"parent":"item/handheld" if kind != "BOW" else "item/bow",
             "textures":{"layer0":"nexora:items/arsenal/"+weapon_id.lower()}}
    (models_dir/(model_name+".json")).write_text(json.dumps(model,indent=2)+"\n",encoding="utf-8")
    model_overrides[kind].append({"predicate":{"damage":round(damage,4)},"model":"nexora:item/"+model_name})

# 1.12.2 item-model overrides: diamond tools use damage fractions, not CustomModelData.
def write_base_model(filename, texture, parent, overrides):
    model = {"parent":parent,"textures":{"layer0":texture},"overrides":overrides}
    path = Path("assets/minecraft/models/item")/filename
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(model,indent=2)+"\n",encoding="utf-8")

sword_overrides = []
for i,name in enumerate(["divina","glacial","infernal","natural","trueno","vacio","marina","ancestral"]):
    sword_overrides.append({"predicate":{"damage":round(0.01+i*0.01,4)},"model":"nexora:item/spear_"+name})
sword_overrides.extend(model_overrides["SWORD"])
write_base_model("diamond_sword.json","minecraft:items/diamond_sword","item/handheld",sword_overrides)

axe_overrides = model_overrides["AXE"]
write_base_model("diamond_axe.json","minecraft:items/diamond_axe","item/handheld",axe_overrides)

hoe_overrides = []
for i,name in enumerate(["divino","infernal","glacial"]):
    hoe_overrides.append({"predicate":{"damage":round(0.01+i*0.01,4)},"model":"nexora:item/fragment_"+name})
hoe_overrides.extend(model_overrides["HOE"])
write_base_model("diamond_hoe.json","minecraft:items/diamond_hoe","item/handheld",hoe_overrides)

bow_overrides = [{"predicate":{"damage":round(0.01+i*0.01,4)},"model":"nexora:item/arsenal_"+name.lower()}
                 for i,(name,kind,element) in enumerate([x for x in ARSENAL if x[1]=="BOW"])]
bow_overrides.append({"predicate":{"damage":0.06},"model":"nexora:item/astral_bow"})
write_base_model("bow.json","minecraft:items/bow_standby","item/bow",bow_overrides)

# The four armor inventory icons select the correct set by the same damage fraction
# written by NexoraWeapons. Worn armor layers remain vanilla on unmodified 1.12 clients.
for piece in ("helmet","chestplate","leggings","boots"):
    overrides = []
    for i,name in enumerate(("divina","infernal","glacial","vacio")):
        model_name = "armor_"+name+"_"+piece
        model = {"parent":"item/generated","textures":{"layer0":"nexora:armor/"+name+"_"+piece}}
        (models_dir/(model_name+".json")).write_text(json.dumps(model,indent=2)+"\n",encoding="utf-8")
        overrides.append({"predicate":{"damage":round(0.01+i*0.01,4)},"model":"nexora:item/"+model_name})
    vanilla_texture = "minecraft:items/diamond_"+piece
    write_base_model("diamond_"+piece+".json",vanilla_texture,"item/generated",overrides)

# Model for the original Astral bow, used by the BOW_ASTRAL item ID.
astral_model = {"parent":"item/bow","textures":{"layer0":"nexora:items/astral"}}
(models_dir/"astral_bow.json").write_text(json.dumps(astral_model,indent=2)+"\n",encoding="utf-8")

assert len(ARSENAL) == 50, "The NEXORA arsenal must contain exactly 50 weapons"
print("Generated 50 unique arsenal textures and 9 damage-predicate item model files.")


# Dedicated model files for the eight legacy spears and three boss fragments.
for name in ("divina","glacial","infernal","natural","trueno","vacio","marina","ancestral"):
    model = {"parent":"item/handheld","textures":{"layer0":"nexora:items/"+name}}
    (models_dir/("spear_"+name+".json")).write_text(json.dumps(model,indent=2)+"\n",encoding="utf-8")
for name in ("divino","infernal","glacial"):
    model = {"parent":"item/handheld","textures":{"layer0":"nexora:items/fragment_"+name}}
    (models_dir/("fragment_"+name+".json")).write_text(json.dumps(model,indent=2)+"\n",encoding="utf-8")
print("Generated legacy spear and fragment model definitions.")
