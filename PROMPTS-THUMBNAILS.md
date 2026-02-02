# Thumbnail Icon Prompts (Lines Page)

These prompts generate the small images that appear behind monogram initials on the family lines pages.

**Style requirements:**
- Sepia-toned pencil sketch / engraving style (NOT watercolor)
- Monochromatic warm brown palette with aged paper texture
- NO PEOPLE - landscapes, buildings, and objects only
- Clean composition that works as a background element

---

## Codex Image Generation (Primary Method)

Use the codex `image_gen.py` script for thumbnail generation.

### Base Template

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export IMAGE_GEN="$CODEX_HOME/skills/imagegen/scripts/image_gen.py"

uv run --with openai --with pillow python "$IMAGE_GEN" generate \
  --prompt "Vintage sepia-toned pencil sketch of [TOPIC] for genealogy thumbnail" \
  --size 1024x1024 \
  --out images/thumbs/[filename].jpg \
  --scene "[Key landscape/building elements, NO PEOPLE]" \
  --subject "Thumbnail background, landscape only, no people" \
  --style "sepia-toned pencil sketch on aged paper; fine linework; monochromatic brown/tan palette; vintage book illustration aesthetic" \
  --composition "square format, simple composition suitable as background behind text/initials" \
  --lighting "soft, diffused period-appropriate lighting" \
  --palette "monochromatic sepia, warm browns, tans, aged cream paper tone" \
  --constraints "NO PEOPLE; must work as subtle background; cohesive with genealogy collection" \
  --negative "watercolor, bright colors, people, portraits, faces, figures, busy detail, modern elements"
```

---

### Johann Peter Maurer (1709–1781) - German Immigrant, Pennsylvania Pioneer
*File: `images/thumbs/german-immigrant.jpg`*

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export IMAGE_GEN="$CODEX_HOME/skills/imagegen/scripts/image_gen.py"

uv run --with openai --with pillow python "$IMAGE_GEN" generate \
  --prompt "Vintage sepia-toned pencil sketch of German colonial Pennsylvania settlement 1750s for genealogy thumbnail" \
  --size 1024x1024 \
  --out images/thumbs/german-immigrant.jpg \
  --scene "Colonial Pennsylvania landscape, rolling hills, stone or log farmhouse (Pennsylvania Dutch style), sailing ship silhouette in distance, split-rail fencing, cleared farmland, distant church steeple" \
  --subject "Thumbnail background showing colonial German settlement, landscape only, no people" \
  --style "sepia-toned pencil sketch on aged paper; fine linework; monochromatic brown/tan palette; vintage book illustration aesthetic" \
  --composition "square format, farmstead in middle ground, ship or church in distance, simple composition" \
  --lighting "soft colonial daylight, gentle atmosphere" \
  --palette "monochromatic sepia, warm browns, tans, aged cream paper tone" \
  --constraints "NO PEOPLE; 1740s-1780s period accuracy; must work as subtle background; cohesive with genealogy collection" \
  --negative "watercolor, bright colors, people, portraits, faces, figures, busy detail, modern elements"
```

---

### Peter W. Mowrey (1760–1840) - Revolutionary War Veteran, Virginia Militia
*File: `images/thumbs/revolutionary-war.jpg`*

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export IMAGE_GEN="$CODEX_HOME/skills/imagegen/scripts/image_gen.py"

uv run --with openai --with pillow python "$IMAGE_GEN" generate \
  --prompt "Vintage sepia-toned pencil sketch of Revolutionary War Virginia Shenandoah Valley 1780s for genealogy thumbnail" \
  --size 1024x1024 \
  --out images/thumbs/revolutionary-war.jpg \
  --scene "Shenandoah Valley landscape, Blue Ridge Mountains in background, Revolutionary War militia artifacts (musket, powder horn, tricorn hat as objects on fence or stump), split-rail fencing, frontier homestead, distant battle smoke" \
  --subject "Thumbnail background showing Revolutionary era landscape with military artifacts, NO PEOPLE" \
  --style "sepia-toned pencil sketch on aged paper; fine linework; monochromatic brown/tan palette; vintage book illustration aesthetic" \
  --composition "square format, valley landscape with mountains, artifacts in foreground, homestead in middle ground" \
  --lighting "soft period daylight, atmospheric haze on mountains" \
  --palette "monochromatic sepia, warm browns, tans, aged cream paper tone" \
  --constraints "NO PEOPLE; military items shown as objects only not worn; 1770s-1800s period accuracy; must work as subtle background" \
  --negative "watercolor, bright colors, people, portraits, faces, figures, soldiers, busy detail, modern elements"
```

---

### Tennessee Pioneer (1800s-1850s)
*File: `images/thumbs/tennessee-pioneer.jpg`*
*For: Lewis R. Mowery, Elizabeth "Betsy" Lisbee Mowery*

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export IMAGE_GEN="$CODEX_HOME/skills/imagegen/scripts/image_gen.py"

uv run --with openai --with pillow python "$IMAGE_GEN" generate \
  --prompt "Vintage sepia-toned pencil sketch of Tennessee pioneer homestead 1820s for genealogy thumbnail" \
  --size 1024x1024 \
  --out images/thumbs/tennessee-pioneer.jpg \
  --scene "Tennessee landscape with rolling hills, log cabin with smoke rising from chimney, covered wagon, split-rail fencing, farm animals (chickens, cow), Great Smoky Mountains in distance" \
  --subject "Thumbnail background showing pioneer homestead, landscape only, no people" \
  --style "sepia-toned pencil sketch on aged paper; fine linework; monochromatic brown/tan palette; vintage book illustration aesthetic" \
  --composition "square format, cabin in middle ground, mountains in distance, simple pastoral scene" \
  --lighting "soft morning or afternoon light, gentle Appalachian atmosphere" \
  --palette "monochromatic sepia, warm browns, tans, aged cream paper tone" \
  --constraints "NO PEOPLE; 1800-1850s period accuracy; must work as subtle background; cohesive with genealogy collection" \
  --negative "watercolor, bright colors, people, portraits, faces, figures, busy detail, modern elements"
```

---

### Texas Farming (1820s-1830s)
*File: `images/thumbs/texas-farming-1820-1830.jpg`*
*For: Moses Mansfield Mowery, Samuel S. Mowrey*

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export IMAGE_GEN="$CODEX_HOME/skills/imagegen/scripts/image_gen.py"

uv run --with openai --with pillow python "$IMAGE_GEN" generate \
  --prompt "Vintage sepia-toned pencil sketch of Texas frontier farming 1830s for genealogy thumbnail" \
  --size 1024x1024 \
  --out images/thumbs/texas-farming-1820-1830.jpg \
  --scene "Rolling Texas prairie, simple wooden farmhouse with stone chimney, split-rail fencing, horse-drawn plow, covered wagon in distance, open landscape" \
  --subject "Thumbnail background showing Texas frontier farm, landscape only, no people" \
  --style "sepia-toned pencil sketch on aged paper; fine linework; monochromatic brown/tan palette; vintage book illustration aesthetic" \
  --composition "square format, farmstead in middle ground, expansive prairie, simple composition" \
  --lighting "bright Texas daylight, open sky" \
  --palette "monochromatic sepia, warm browns, tans, aged cream paper tone" \
  --constraints "NO PEOPLE; 1820s-1850s period accuracy; must work as subtle background; cohesive with genealogy collection" \
  --negative "watercolor, bright colors, people, portraits, faces, figures, busy detail, modern elements"
```

---

## ChatGPT 4o / Nanobanana Fallback

Use these prompts when API is constrained. Copy into ChatGPT 4o Image Designer.

### Base Template (ChatGPT)

```
Create a vintage sepia-toned pencil sketch illustration representing [SPECIFIC TOPIC/PERIOD]. The design should be suitable for use as a subtle background element behind text/monogram initials. Include elements like:

- [SPECIFIC LANDSCAPE/BUILDING ELEMENTS]
- [GEOGRAPHIC/HISTORICAL DETAILS]
- [RELEVANT OBJECTS - NO PEOPLE]
- Monochromatic sepia/brown palette only
- Aged paper texture with fine pencil linework

Style: Sepia pencil sketch or engraving, NOT watercolor. Clean linework like a vintage book illustration. Must remain legible when used behind text - avoid busy details.

CRITICAL REQUIREMENTS:
- NO PEOPLE - only landscapes, buildings, objects, and animals
- Sepia/brown monochrome only - no blues, greens, or other colors
- Pencil sketch style - NOT watercolor
- Aged paper texture background

Format: Square aspect ratio.
```

### Johann Peter Maurer - ChatGPT Fallback

```
Create a vintage sepia-toned pencil sketch illustration representing German immigration to colonial Pennsylvania in the mid-1700s. The design should be suitable for use as a subtle background element behind text/monogram initials. Include elements like:

- Colonial Pennsylvania landscape with rolling hills and farmland
- A simple stone or log farmhouse typical of German settlers (Pennsylvania Dutch style)
- Perhaps a sailing ship silhouette in the distance suggesting Atlantic crossing
- Split-rail fencing and cleared farmland showing frontier settlement
- Distant church steeple suggesting Lutheran or Reformed congregation
- Monochromatic sepia/brown palette only
- Aged paper texture with fine pencil linework

Style: Sepia pencil sketch or engraving, NOT watercolor. Clean linework like a vintage book illustration. Must remain legible when used behind text.

CRITICAL REQUIREMENTS:
- NO PEOPLE - only landscapes, buildings, objects
- Sepia/brown monochrome only
- Pencil sketch style - NOT watercolor

Format: Square aspect ratio.
```

### Peter W. Mowrey - ChatGPT Fallback

```
Create a vintage sepia-toned pencil sketch illustration representing Virginia militia service during the Revolutionary War and Shenandoah Valley settlement. The design should be suitable for use as a subtle background element behind text/monogram initials. Include elements like:

- Shenandoah Valley landscape with Blue Ridge Mountains in background
- Revolutionary War militia artifacts: musket, powder horn, tricorn hat shown as objects (on fence post or stump, NOT worn)
- Split-rail fencing and frontier homestead
- Perhaps distant battle smoke or Continental Army encampment
- Valley farmland suggesting post-war settlement
- Monochromatic sepia/brown palette only
- Aged paper texture with fine pencil linework

Style: Sepia pencil sketch or engraving, NOT watercolor. Clean linework like a vintage book illustration. Must remain legible when used behind text.

CRITICAL REQUIREMENTS:
- NO PEOPLE - military items shown as objects only, not worn by anyone
- Sepia/brown monochrome only
- Pencil sketch style - NOT watercolor

Format: Square aspect ratio.
```
