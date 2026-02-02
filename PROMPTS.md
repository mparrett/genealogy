# Image Generation Prompts

## Post-Generation Optimization

After generating images, always convert to JPEG for better file sizes (watercolor-style images compress poorly as PNG):

```bash
# Convert PNG to JPEG (85% quality, good balance of size/quality)
for f in images/bio/*.png; do
  base="${f%.png}"
  uv run --with pillow python -c "from PIL import Image; img = Image.open('$f'); img = img.convert('RGB'); img.save('${base}.jpg', 'JPEG', quality=85)"
done

# Remove original PNGs
rm images/bio/*.png

# Update markdown references from .png to .jpg
# Then rebuild: just build-reports
```

Typical results: ~2MB PNG → ~300KB JPEG (85% reduction)

---

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
| Feather River Canyon, California | `images/locations/feather-river-canyon-1915.png` | c. 1915 |

---

## Thumbnail Icons (Lines Page)

**See [PROMPTS-THUMBNAILS.md](PROMPTS-THUMBNAILS.md) for thumbnail icon prompts.**

These are the small images that appear behind monogram initials on the family lines pages. Use the codex `image_gen.py` script (primary) or ChatGPT 4o (fallback when API constrained).

**Style:** Sepia pencil sketch (NOT watercolor), no people.

---

## ChatGPT 4o Image Designer Prompts (Legacy)

The prompts below are kept for reference. For new thumbnails, use PROMPTS-THUMBNAILS.md.

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

## Inline Bio Illustrations (Watercolor Style)

These are watercolor-style illustrations embedded within biography reports. They feature color, people, and detailed scenes — **NOT for thumbnail icons**.

**DO NOT use these prompts for thumbnail icons on the lines page.** Thumbnails need sepia sketch style without people. See PROMPTS-THUMBNAILS.md.

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

### James E. Higgins - Orphanage Childhood (1905)
*File: `images/bio/james-e-higgins-01-orphanage.jpg`*

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export IMAGE_GEN="$CODEX_HOME/skills/imagegen/scripts/image_gen.py"

uv run --with openai --with pillow python "$IMAGE_GEN" generate \
  --prompt "Vintage watercolor illustration of a Catholic children's home in early 1900s New York for genealogy report" \
  --size 1024x1024 \
  --out images/bio/james-e-higgins-01-orphanage.png \
  --scene "1905 Catholic orphanage grounds in Rockland County NY, large institutional brick building with cross, children in period clothing, autumn trees" \
  --subject "Children's home exterior with young residents at play or work, nuns supervising in distance (no specific portraits)" \
  --style "vintage watercolor illustration, soft washes, warm tones, lightly textured paper, period-appropriate, gentle and dignified" \
  --composition "wide view of institution grounds, hopeful rather than bleak atmosphere" \
  --lighting "soft autumn afternoon light, golden hour warmth" \
  --palette "warm browns, muted reds, autumn golds, soft blue sky, touches of green" \
  --constraints "no text, no logos, no watermark; dignified portrayal of institutional childhood; cohesive with existing genealogy bio illustrations" \
  --negative "modern elements, bright colors, busy clutter, photorealistic, grim or depressing tone"
```

### James E. Higgins - Railroad Engineer (1910s-1920s)
*File: `images/bio/james-e-higgins-02-railroad.png`*

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export IMAGE_GEN="$CODEX_HOME/skills/imagegen/scripts/image_gen.py"

uv run --with openai --with pillow python "$IMAGE_GEN" generate \
  --prompt "Vintage watercolor illustration of Western Pacific Railroad engineering crew in California mountains 1910s-1920s for genealogy report" \
  --size 1024x1024 \
  --out images/bio/james-e-higgins-02-railroad.png \
  --scene "1910s-1920s Western Pacific Railroad construction or survey site, Sierra Nevada or Feather River Canyon, rail tracks, steam locomotive in distance" \
  --subject "Civil engineering crew at work with surveying equipment, transit on tripod, blueprints, workers in period clothing (no specific portraits)" \
  --style "vintage watercolor illustration, soft washes, warm tones, lightly textured paper, period-appropriate" \
  --composition "engineering work in dramatic mountain landscape, human figures at work against western scenery" \
  --lighting "clear mountain daylight, strong shadows, expansive western sky" \
  --palette "warm earth tones, granite grays, pine greens, golden California light, soft blue sky" \
  --constraints "no text, no logos, no watermark; cohesive with existing genealogy bio illustrations" \
  --negative "modern elements, bright colors, busy clutter, photorealistic"
```

### James E. Higgins - Treasure Island / WPA Legacy (1936-37)
*File: `images/bio/james-e-higgins-03-treasure-island.png`*

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export IMAGE_GEN="$CODEX_HOME/skills/imagegen/scripts/image_gen.py"

uv run --with openai --with pillow python "$IMAGE_GEN" generate \
  --prompt "Vintage watercolor illustration of Treasure Island construction in San Francisco Bay, 1930s WPA engineering project, for genealogy report" \
  --size 1024x1024 \
  --out images/bio/james-e-higgins-03-treasure-island.png \
  --scene "1936-37 Treasure Island construction site in San Francisco Bay, Golden Gate Bridge visible in distance, cranes and dredging equipment, engineers surveying the man-made island" \
  --subject "WPA engineering project at dusk or dawn, workers and engineers silhouetted against the bay, sense of monumental achievement and bittersweet legacy (no specific portraits)" \
  --style "vintage watercolor illustration, soft washes, warm tones mixed with cool bay blues, lightly textured paper, period-appropriate, contemplative mood" \
  --composition "wide view of construction with San Francisco Bay and bridge in background, human figures small against grand engineering scale, hopeful yet melancholic atmosphere" \
  --lighting "golden hour light, sun setting or rising over the bay, long shadows, reflections on water" \
  --palette "warm golds and oranges, soft blues of bay and sky, steel grays of construction, touches of green" \
  --constraints "no text, no logos, no watermark; poignant/contemplative tone; cohesive with existing genealogy bio illustrations" \
  --negative "modern elements, bright colors, busy clutter, photorealistic, cheerful or festive tone"
```

### Peter W. Mowrey - Battle of Guilford Court House (1781)
*File: `images/bio/peter-mowrey-01-guilford.png`*

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export IMAGE_GEN="$CODEX_HOME/skills/imagegen/scripts/image_gen.py"

uv run --with openai --with pillow python "$IMAGE_GEN" generate \
  --prompt "Vintage watercolor illustration of Virginia militia at the Battle of Guilford Court House, 1781, for genealogy report" \
  --size 1024x1024 \
  --out images/bio/peter-mowrey-01-guilford.png \
  --scene "1781 Piedmont North Carolina, rolling wooded hills, bare early spring trees, distant smoke from battle, Continental Army militia position" \
  --subject "Virginia militia soldiers in hunting shirts and tricorn hats, muskets ready, ragged but determined, General Greene's Southern Campaign (no specific portraits)" \
  --style "vintage watercolor illustration, soft washes, warm tones, lightly textured paper, period-appropriate" \
  --composition "small unit of militia in wooded terrain, sense of tension before or during engagement" \
  --lighting "overcast March daylight, diffused light through bare branches, smoke haze" \
  --palette "muted browns, grays, bare tree tans, touches of Continental blue, powder smoke white" \
  --constraints "no text, no logos, no watermark; cohesive with existing genealogy bio illustrations" \
  --negative "modern elements, bright colors, busy clutter, photorealistic, glorified or romantic war scene"
```

### Peter W. Mowrey - Shenandoah Valley Settlement (1770s-1790s)
*File: `images/bio/peter-mowrey-02-shenandoah.png`*

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export IMAGE_GEN="$CODEX_HOME/skills/imagegen/scripts/image_gen.py"

uv run --with openai --with pillow python "$IMAGE_GEN" generate \
  --prompt "Vintage watercolor illustration of Pennsylvania German farmstead in Shenandoah Valley Virginia, late 1700s, for genealogy report" \
  --size 1024x1024 \
  --out images/bio/peter-mowrey-02-shenandoah.png \
  --scene "1770s-1790s Shenandoah Valley, Blue Ridge Mountains in distance, fertile valley farmland, split-rail fencing, grain fields" \
  --subject "Pennsylvania German-style log farmhouse with stone chimney, agricultural prosperity, Conestoga wagon or farm cart (no specific portraits)" \
  --style "vintage watercolor illustration, soft washes, warm tones, lightly textured paper, period-appropriate" \
  --composition "pastoral valley scene with farmstead in middle ground, mountains in background, sense of established settlement" \
  --lighting "golden late afternoon light, long shadows across valley, warm summer atmosphere" \
  --palette "rich greens of valley, blue-gray mountains, warm browns of log construction, golden wheat, soft blue sky" \
  --constraints "no text, no logos, no watermark; cohesive with existing genealogy bio illustrations" \
  --negative "modern elements, bright colors, busy clutter, photorealistic"
```

### Peter W. Mowrey - Knox County Tennessee Homestead (1794-1840)
*File: `images/bio/peter-mowrey-03-knox-county.png`*

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export IMAGE_GEN="$CODEX_HOME/skills/imagegen/scripts/image_gen.py"

uv run --with openai --with pillow python "$IMAGE_GEN" generate \
  --prompt "Vintage watercolor illustration of early 19th century homestead in Knox County Tennessee, for genealogy report" \
  --size 1024x1024 \
  --out images/bio/peter-mowrey-03-knox-county.png \
  --scene "1800-1840 East Tennessee foothills, Great Smoky Mountains in distance, established homestead on Roseberry Creek, mature farm with outbuildings" \
  --subject "Pioneer homestead showing decades of settlement, log house with additions, kitchen garden, fruit trees, livestock, large family atmosphere (no specific portraits)" \
  --style "vintage watercolor illustration, soft washes, warm tones, lightly textured paper, period-appropriate" \
  --composition "prosperous farmstead in middle ground, mountains in misty distance, sense of a life well-lived" \
  --lighting "soft morning light, gentle mist in valley, peaceful domestic atmosphere" \
  --palette "warm earth tones, Appalachian greens, misty blue mountains, autumn golds and oranges" \
  --constraints "no text, no logos, no watermark; cohesive with existing genealogy bio illustrations" \
  --negative "modern elements, bright colors, busy clutter, photorealistic, raw frontier aesthetic"
```
