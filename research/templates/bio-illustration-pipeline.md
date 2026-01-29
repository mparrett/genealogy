# Biography Illustration Pipeline

Templates for generating inline watercolor illustrations for biography pages.

---

## Stage 1: Shared Style Template

Use this foundation for ALL bio inline images to maintain consistency:

```
STYLE FOUNDATION:
- Watercolor painting style with soft, expressive brushstrokes
- Warm, nostalgic palette with subtle color washes
- More vivid and emotive than the sepia background icons
- Evocative rather than photorealistic — suggest mood and place
- Soft edges, visible paper texture, occasional paint bleeds
- Horizontal/landscape orientation (will sit inline with text)
- No text, signatures, or watermarks
- Should feel like an heirloom illustration from a family history book
```

---

## Stage 2: Bio-Specific Context

Create one of these per biography. Include:
- Era/date range
- Geography (origin → destination)
- Themes relevant to this person's story
- Cultural markers (religion, ethnicity, occupation)
- Key figures to potentially depict

### Example: Frederick Kuthe

```
BIO CONTEXT:
- Era: 1845-1900
- Geography: Vöhl, Hesse, Germany → Bremen → New Orleans → Missouri Ozarks
- Themes: German emigration, sailing ship journey, frontier farming, family loss
- Cultural markers: German immigrant community, Lutheran/Reformed faith, rural Ozark landscape
- Key figures: Frederick (young German emigrant, later widowed farmer), Sarah Ann (wife, died young), six children
```

---

## Stage 3: Individual Image Prompts

Create 1-2 of these per biography, focusing on key narrative moments.

### Example: Frederick Kuthe

**Image 1: The Voyage (1845)**
```
A watercolor depicting the emigration journey: a 19th-century sailing ship on the Atlantic, viewed from the deck or at an angle showing the vessel against an expansive sea and sky. Hints of passengers on deck — a young German family looking toward the horizon. The mood is hopeful but uncertain. Bremen harbor fading in the background or New Orleans approaching. Soft morning or evening light.
```

**Image 2: Missouri Homestead (1870s)**
```
A watercolor of a modest Missouri Ozark farmstead in the 1870s. A simple wooden farmhouse with a German immigrant family's character — perhaps a kitchen garden, split-rail fence, a few children in the yard. Rolling Ozark hills with oak and hickory trees in the background. Late afternoon golden light. The mood is quiet, hardworking, rooted.
```

---

## Combining Stages for Generation

When generating, combine all three stages into a single prompt:

```
[Stage 1: Style Foundation]

[Stage 2: Bio Context]

[Stage 3: Specific Image Prompt]
```

The image generation script can then be called with appropriate --prompt and --style flags.

---

## Output Locations

- Generated images (high-res PNG): `output/imagegen/bio/`
- Final images for bios (web JPG): `images/bio/`
- Naming convention: `{person-slug}-{image-number}-{brief-description}.{ext}`
  - Example: `frederick-kuthe-01-voyage.png` (original)
  - Example: `frederick-kuthe-01-voyage.jpg` (web)

---

## Post-Processing Pipeline

### Step 1: Optimize PNG (keep as archive)

```bash
oxipng -o 4 output/imagegen/bio/*.png
```

### Step 2: Convert to web-sized JPG

```bash
# Convert to 800px wide JPG at 85% quality for inline bio use
sips -Z 800 --setProperty format jpeg --setProperty formatOptions 85 \
  output/imagegen/bio/frederick-kuthe-01-voyage.png \
  --out images/bio/frederick-kuthe-01-voyage.jpg
```

Or batch convert all:

```bash
for f in output/imagegen/bio/*.png; do
  name=$(basename "$f" .png)
  sips -Z 800 --setProperty format jpeg --setProperty formatOptions 85 \
    "$f" --out "images/bio/${name}.jpg"
done
```

### Output sizes

| Format | Resolution | Use case |
|--------|------------|----------|
| PNG (original) | 1536x1024 | Archive, print |
| JPG (web) | 800x533 | Inline in bio pages |
