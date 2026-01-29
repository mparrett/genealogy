# Image Generation Prompts

## Location Panel Template (Hand-Watercolored Engraving)

Use this for location/place images. Distinct from bio illustrations (watercolor scenes).

**Reference**: https://mirka-h.blogspot.com/2015/02/imprinting-american-west-engravings.html

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export IMAGE_GEN="$CODEX_HOME/skills/imagegen/scripts/image_gen.py"

uv run --with openai --with pillow python "$IMAGE_GEN" generate \
  --prompt "Hand-watercolored engraving depicting [PLACE], [REGION/COUNTRY] circa [YEAR]" \
  --size 1024x1024 \
  --out images/locations/[filename].png \
  --scene "[Key landmarks: river, bridge, castle, church, buildings, landscape features]" \
  --subject "Location panel, no people" \
  --style "19th century wood engraving with hand-applied watercolor washes; fine black linework using parallel lines, cross-hatching, stippling; subtle color washes over linework; aged paper texture" \
  --composition "square format, title cartouche reading '[PLACE], [Region] — c. [YEAR]'" \
  --lighting "[Appropriate lighting for region/climate]" \
  --palette "muted greens, warm ochres and browns for stone, soft gray-blue sky; colors complement linework without overwhelming" \
  --constraints "engraved linework must remain visible beneath color; no modern elements; cohesive with genealogy collection" \
  --negative "photorealistic, modern elements, bright saturated colors, busy clutter, text other than cartouche"
```

### Completed Location Panels

| Location | File | Year |
|----------|------|------|
| Croom, Co. Limerick, Ireland | `images/locations/croom-limerick-1864.png` | c. 1864 |
| Rathmines, Dublin, Ireland | `images/locations/rathmines-dublin-1870.png` | c. 1870 |

---

## ChatGPT 4o Image Designer Prompts

### Base Template for Genealogy Graphics

Use this template for all genealogy-related graphics to ensure consistency:

```
Create a vintage-style illustration representing [SPECIFIC TOPIC/PERIOD]. The design should be suitable for use as either a background element or icon in genealogy research reports. Include elements like:

- [SPECIFIC ELEMENTS FOR THIS TOPIC/PERIOD]
- [GEOGRAPHIC/HISTORICAL DETAILS]
- [RELEVANT ACTIVITIES/OBJECTS]
- Warm, earthy color palette (browns, golds, muted greens)
- Soft, aged appearance with slight sepia tones

Style: Historical illustration with a clean, not overly detailed approach that works well as a background element. The design should feel authentic to the [TIME PERIOD] but remain legible and not too busy when used behind text.

CONSISTENCY REQUIREMENTS (use for all genealogy graphics):
- Maintain the same vintage illustration style with sepia/aged tones
- Use consistent warm, earthy color palette across all images
- Keep the same level of detail and artistic approach
- All graphics should complement each other as part of a cohesive genealogy research collection
- Ensure typography and decorative elements (if any) match this historical aesthetic

Format: Square aspect ratio, suitable for web use. The design should work both as a subtle background and as a standalone decorative element.
```

---

### Elizabeth "Betsy" Lusby Mowery (c. 1790s-1850s) - Tennessee Native, Pioneer Wife

```
Create a vintage-style illustration representing Tennessee pioneer women and early family life in the 1800s. The design should be suitable for use as either a background element or icon in genealogy research reports. Include elements like:

- Tennessee landscape with rolling hills and early settlements
- A log cabin or simple wooden home with smoke rising from chimney
- Pioneer family life elements: garden plots, washing areas, children playing
- Split-rail fencing and farm animals (chickens, cow, etc.)
- Traditional pioneer women's work: spinning wheel, garden tools, hanging laundry
- Native Tennessee vegetation and wildflowers
- Warm, earthy color palette (browns, golds, muted greens)
- Soft, aged appearance with slight sepia tones

Style: Historical illustration with a clean, not overly detailed approach that works well as a background element. The design should feel authentic to the 1800-1850s Tennessee pioneer family life but remain legible and not too busy when used behind text.

CONSISTENCY REQUIREMENTS (use for all genealogy graphics):
- Maintain the same vintage illustration style with sepia/aged tones
- Use consistent warm, earthy color palette across all images
- Keep the same level of detail and artistic approach
- All graphics should complement each other as part of a cohesive genealogy research collection
- Ensure typography and decorative elements (if any) match this historical aesthetic

Format: Square aspect ratio, suitable for web use. The design should work both as a subtle background and as a standalone decorative element.
```

---

### Lewis R. Mowery (c. 1780s-1850s) - German Immigrant, Tennessee Pioneer

```
Create a vintage-style illustration representing German immigration to early Tennessee in the early 1800s. The design should be suitable for use as either a background element or icon in genealogy research reports. Include elements like:

- Appalachian foothills landscape typical of East Tennessee (Knox/Bradley Counties)
- A simple log cabin or early settler's homestead with German architectural influences
- Perhaps a covered wagon or cart suggesting immigration/migration
- Split-rail fencing and cleared farmland showing frontier settlement
- Distant mountains (Great Smoky Mountains) in the background
- Tools of early farming and homesteading (axe, plow, etc.)
- Warm, earthy color palette (browns, golds, muted greens)
- Soft, aged appearance with slight sepia tones

Style: Historical illustration with a clean, not overly detailed approach that works well as a background element. The design should feel authentic to the 1800-1840s German-American frontier settlement period in Tennessee but remain legible and not too busy when used behind text.

CONSISTENCY REQUIREMENTS (use for all genealogy graphics):
- Maintain the same vintage illustration style with sepia/aged tones
- Use consistent warm, earthy color palette across all images
- Keep the same level of detail and artistic approach
- All graphics should complement each other as part of a cohesive genealogy research collection
- Ensure typography and decorative elements (if any) match this historical aesthetic

Format: Square aspect ratio, suitable for web use. The design should work both as a subtle background and as a standalone decorative element.
```

---

### George Washington Kuthe (1869–1925) - German-American Migration

```
Create a vintage-style illustration representing German-American migration and farming in the late 1800s/early 1900s American West. The design should be suitable for use as either a background element or icon in genealogy research reports. Include elements like:

- Rolling farmland or prairie landscape typical of Missouri/Oregon farming regions
- A modest farmhouse with German-American architectural influences (perhaps steep-roofed barn)
- Horse-drawn farming equipment or a wagon suggesting westward migration
- Railroad tracks or train in the distance (representing late 1800s migration routes)
- Desert elements subtly in the background (representing eventual move to Arizona)
- Warm, earthy color palette (browns, golds, muted greens)
- Soft, aged appearance with slight sepia tones

Style: Historical illustration with a clean, not overly detailed approach that works well as a background element. The design should feel authentic to the 1870s-1920s period of German-American settlement and westward migration but remain legible and not too busy when used behind text.

CONSISTENCY REQUIREMENTS (use for all genealogy graphics):
- Maintain the same vintage illustration style with sepia/aged tones
- Use consistent warm, earthy color palette across all images
- Keep the same level of detail and artistic approach
- All graphics should complement each other as part of a cohesive genealogy research collection
- Ensure typography and decorative elements (if any) match this historical aesthetic

Format: Square aspect ratio, suitable for web use. The design should work both as a subtle background and as a standalone decorative element.
```

---

### Huldah Imogene (Bridgefarmer) Kuthe (1873–1907) - Oregon Trail Pioneer Descendant

```
Create a vintage-style illustration representing Oregon Trail pioneer families and Willamette Valley settlement in the late 1800s. The design should be suitable for use as either a background element or icon in genealogy research reports. Include elements like:

- Willamette Valley landscape with rolling hills and forested mountains in the distance
- A pioneer homestead with log cabin or simple wooden farmhouse
- Split-rail fencing typical of Oregon pioneer settlements
- Perhaps a covered wagon wheel or other Oregon Trail artifacts as subtle background elements
- Native Oregon vegetation (fir trees, wildflowers)
- A sense of established community rather than active migration
- Warm, earthy color palette (browns, golds, muted greens)
- Soft, aged appearance with slight sepia tones

Style: Historical illustration with a clean, not overly detailed approach that works well as a background element. The design should feel authentic to the 1870s-1900s Oregon pioneer settlement period but remain legible and not too busy when used behind text.

CONSISTENCY REQUIREMENTS (use for all genealogy graphics):
- Maintain the same vintage illustration style with sepia/aged tones
- Use consistent warm, earthy color palette across all images
- Keep the same level of detail and artistic approach
- All graphics should complement each other as part of a cohesive genealogy research collection
- Ensure typography and decorative elements (if any) match this historical aesthetic

Format: Square aspect ratio, suitable for web use. The design should work both as a subtle background and as a standalone decorative element.
```

---

### Example: Texas Farming 1820s-1830s

```
Create a vintage-style illustration representing Texas farming in the 1820s-1830s period. The design should be suitable for use as either a background element or icon in genealogy research reports. Include elements like:

- Rolling hills or open prairie landscape typical of 1820s Texas
- A simple wooden farmhouse or cabin with a stone chimney
- Split-rail fencing
- A horse-drawn plow or oxen working the fields
- Perhaps a covered wagon in the distance to represent westward migration
- Warm, earthy color palette (browns, golds, muted greens)
- Soft, aged appearance with slight sepia tones

Style: Historical illustration with a clean, not overly detailed approach that works well as a background element. The design should feel authentic to the 1820s-1830s Texas frontier period but remain legible and not too busy when used behind text.

CONSISTENCY REQUIREMENTS (use for all genealogy graphics):
- Maintain the same vintage illustration style with sepia/aged tones
- Use consistent warm, earthy color palette across all images
- Keep the same level of detail and artistic approach
- All graphics should complement each other as part of a cohesive genealogy research collection
- Ensure typography and decorative elements (if any) match this historical aesthetic

Format: Square aspect ratio, suitable for web use. The design should work both as a subtle background and as a standalone decorative element.
```

---

### Irish Immigrants to Wisconsin Farmland (1850s-1880s)
*For: James Fitzgerald, Maria Ann Fitzgerald, Anne B. Gleeson*

```
Create a vintage-style illustration representing Irish immigrant farming families in Wisconsin during the 1850s-1880s. The design should be suitable for use as either a background element or icon in genealogy research reports. Include elements like:

- Rolling Wisconsin farmland with gentle hills and mixed forest
- A modest wooden farmhouse or small dairy farm
- Elements suggesting Irish Catholic heritage (perhaps a simple cross or church steeple in distance)
- Dairy farming elements typical of Wisconsin (milk cans, small barn, grazing cattle)
- Split-rail or stone fencing
- Wildflowers and native Wisconsin vegetation
- Warm, earthy color palette (browns, golds, muted greens)
- Soft, aged appearance with slight sepia tones

Style: Historical illustration with a clean, not overly detailed approach that works well as a background element. The design should feel authentic to the 1850s-1880s Wisconsin immigrant farming period but remain legible and not too busy when used behind text.

CONSISTENCY REQUIREMENTS (use for all genealogy graphics):
- Maintain the same vintage illustration style with sepia/aged tones
- Use consistent warm, earthy color palette across all images
- Keep the same level of detail and artistic approach
- All graphics should complement each other as part of a cohesive genealogy research collection
- Ensure typography and decorative elements (if any) match this historical aesthetic

Format: Square aspect ratio, suitable for web use. The design should work both as a subtle background and as a standalone decorative element.
```

---

### Irish Immigrants to Urban East Coast (1880s-1900s) — Generic
*Alternative for: Laurence Higgins, Mary Knight (see individual prompts below)*

```
Create a vintage-style illustration representing Irish immigrant life in urban northeastern America during the 1880s-1900s. The design should be suitable for use as either a background element or icon in genealogy research reports. Include elements like:

- Urban row houses or tenement buildings typical of Newark/New York City
- Cobblestone streets with gas lamps
- Perhaps a church steeple suggesting Irish Catholic neighborhood
- Working-class elements: a porter's cart, market stalls, or factory smokestacks in distance
- Horse-drawn streetcar or elevated train suggesting city life
- Period clothing silhouettes (bowler hats, long skirts)
- Warm, earthy color palette (browns, golds, muted greens)
- Soft, aged appearance with slight sepia tones

Style: Historical illustration with a clean, not overly detailed approach that works well as a background element. The design should feel authentic to the 1880s-1900s urban Irish-American immigrant experience but remain legible and not too busy when used behind text.

CONSISTENCY REQUIREMENTS (use for all genealogy graphics):
- Maintain the same vintage illustration style with sepia/aged tones
- Use consistent warm, earthy color palette across all images
- Keep the same level of detail and artistic approach
- All graphics should complement each other as part of a cohesive genealogy research collection
- Ensure typography and decorative elements (if any) match this historical aesthetic

Format: Square aspect ratio, suitable for web use. The design should work both as a subtle background and as a standalone decorative element.
```

---

### Laurence Higgins - Dublin to Newark (1870s-1900s)
*For: Laurence Higgins*

```
Create a vintage-style illustration representing Irish immigrant working-class life, specifically a Dublin-born porter in Newark, New Jersey during the 1870s-1900s. The design should be suitable for use as either a background element or icon in genealogy research reports. Include elements like:

- Newark industrial waterfront or rail yard setting
- Working-class labor elements: cargo, crates, hand trucks, warehouse doorways
- Georgian-style Dublin architecture as a faded background memory element
- Factory smokestacks and brick warehouses typical of Newark
- Horse-drawn freight wagons
- Period working men's clothing (cap, vest, rolled sleeves)
- Warm, earthy color palette (browns, golds, muted greens)
- Soft, aged appearance with slight sepia tones

Style: Historical illustration with a clean, not overly detailed approach that works well as a background element. The design should feel authentic to the 1870s-1900s Newark industrial working-class experience but remain legible and not too busy when used behind text.

CONSISTENCY REQUIREMENTS (use for all genealogy graphics):
- Maintain the same vintage illustration style with sepia/aged tones
- Use consistent warm, earthy color palette across all images
- Keep the same level of detail and artistic approach
- All graphics should complement each other as part of a cohesive genealogy research collection
- Ensure typography and decorative elements (if any) match this historical aesthetic

Format: Square aspect ratio, suitable for web use. The design should work both as a subtle background and as a standalone decorative element.
```

---

### Mary Knight - Sligo to New York (1880s-1900s)
*For: Mary Knight*

```
Create a vintage-style illustration representing an Irish immigrant woman's journey from rural County Sligo to New York City in the 1880s-1900s. The design should be suitable for use as either a background element or icon in genealogy research reports. Include elements like:

- Split composition: rural Irish west (thatched cottage, stone walls, green hills) fading into NYC tenement streetscape
- Atlantic ocean or ship silhouette suggesting emigration journey
- New York row houses or tenement buildings
- Laundry lines, market baskets, domestic life elements
- Church steeple suggesting Irish Catholic community
- Perhaps Ellis Island or Statue of Liberty as distant silhouette
- Warm, earthy color palette (browns, golds, muted greens)
- Soft, aged appearance with slight sepia tones

Style: Historical illustration with a clean, not overly detailed approach that works well as a background element. The design should feel authentic to the 1880s-1900s Irish immigrant woman's experience but remain legible and not too busy when used behind text.

CONSISTENCY REQUIREMENTS (use for all genealogy graphics):
- Maintain the same vintage illustration style with sepia/aged tones
- Use consistent warm, earthy color palette across all images
- Keep the same level of detail and artistic approach
- All graphics should complement each other as part of a cohesive genealogy research collection
- Ensure typography and decorative elements (if any) match this historical aesthetic

Format: Square aspect ratio, suitable for web use. The design should work both as a subtle background and as a standalone decorative element.
```

---

### Early 20th Century American - Railroad & WWI Era (1910s-1930s)
*For: James Everett Higgins*

```
Create a vintage-style illustration representing early 20th century American life, particularly railroad engineering and WWI military service. The design should be suitable for use as either a background element or icon in genealogy research reports. Include elements like:

- Western railroad elements: steam locomotive, rail tracks through mountainous terrain
- Engineering/surveying tools (transit, blueprints, drafting equipment)
- Subtle WWI military elements (perhaps a doughboy helmet or military insignia)
- Western American landscape (Sierra Nevada or Rocky Mountain foothills)
- Early 20th century technology: telephone poles, Model T automobile silhouette
- American flag or patriotic elements suggesting the WWI era
- Warm, earthy color palette (browns, golds, muted greens)
- Soft, aged appearance with slight sepia tones

Style: Historical illustration with a clean, not overly detailed approach that works well as a background element. The design should feel authentic to the 1910s-1930s American West and WWI period but remain legible and not too busy when used behind text.

CONSISTENCY REQUIREMENTS (use for all genealogy graphics):
- Maintain the same vintage illustration style with sepia/aged tones
- Use consistent warm, earthy color palette across all images
- Keep the same level of detail and artistic approach
- All graphics should complement each other as part of a cohesive genealogy research collection
- Ensure typography and decorative elements (if any) match this historical aesthetic

Format: Square aspect ratio, suitable for web use. The design should work both as a subtle background and as a standalone decorative element.
```

---

## Inline Bio Illustrations

These are watercolor-style illustrations embedded within biography reports.

### Laurence Higgins - Dublin Emigration (1880s)
*File: `images/bio/laurence-higgins-01-dublin-emigration.jpg`*

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export IMAGE_GEN="$CODEX_HOME/skills/imagegen/scripts/image_gen.py"

uv run --with openai --with pillow python "$IMAGE_GEN" generate \
  --prompt "Vintage watercolor illustration of Irish emigration from Dublin in the 1880s for genealogy report" \
  --size 1024x1024 \
  --out images/bio/laurence-higgins-01-dublin-emigration.png \
  --scene "1880s Dublin quayside or Rathmines street, young Irish family departing for America, Georgian architecture, horse-drawn cart with belongings" \
  --subject "Emigration scene, working-class Irish family leaving Dublin (no specific portraits)" \
  --style "vintage watercolor illustration, soft washes, warm tones, lightly textured paper, period-appropriate" \
  --composition "wide view showing departure scene, emotional but not overcrowded" \
  --lighting "overcast Dublin daylight, soft diffused light" \
  --palette "muted greens, warm browns, soft grays, touches of ochre" \
  --constraints "no text, no logos, no watermark; cohesive with existing genealogy bio illustrations" \
  --negative "modern elements, bright colors, busy clutter, photorealistic"
```

### Laurence Higgins - Newark Porter (1890s-1900s)
*File: `images/bio/laurence-higgins-02-newark-porter.jpg`*

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export IMAGE_GEN="$CODEX_HOME/skills/imagegen/scripts/image_gen.py"

uv run --with openai --with pillow python "$IMAGE_GEN" generate \
  --prompt "Vintage watercolor illustration of Irish immigrant porter working in Newark NJ in the 1890s-1900s for genealogy report" \
  --size 1024x1024 \
  --out images/bio/laurence-higgins-02-newark-porter.png \
  --scene "1890s Newark industrial waterfront or warehouse district, Irish working-class neighborhood, brick buildings, cobblestone streets" \
  --subject "Porter at work with hand truck and cargo, warehouse doorway, working-class labor scene (no specific portrait)" \
  --style "vintage watercolor illustration, soft washes, warm tones, lightly textured paper, period-appropriate" \
  --composition "focus on labor and urban industrial setting, human figure at work" \
  --lighting "soft morning or afternoon light, industrial atmosphere" \
  --palette "warm browns, brick reds, muted ochres, soft gray-blue shadows" \
  --constraints "no text, no logos, no watermark; cohesive with existing genealogy bio illustrations" \
  --negative "modern elements, bright colors, busy clutter, photorealistic"
```
