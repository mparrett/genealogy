# Image Generation

Guidance for generating vintage-style genealogy images.

## Directory Structure

| Directory | Purpose | Git Status |
|-----------|---------|------------|
| `images/originals/bio/` | High-res PNGs from generation | gitignored |
| `images/originals/locations/` | High-res location panels | gitignored |
| `images/originals/thumbs/` | High-res thumbnails | gitignored |
| `images/bio/` | Web-ready JPGs for bios | tracked |
| `images/locations/` | Web-ready location panels | tracked |
| `images/thumbs/` | Web-ready thumbnails | tracked |

## Workflow

### 1. Generate high-res PNG

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export IMAGE_GEN="$CODEX_HOME/skills/imagegen/scripts/image_gen.py"

uv run --with openai --with pillow python "$IMAGE_GEN" generate \
  --prompt "Vintage-style illustration of..." \
  --size 1024x1024 \
  --out images/originals/bio/person-name-01-scene.png \
  --scene "..." \
  --subject "..." \
  --style "vintage watercolor illustration, soft washes, warm tones, lightly textured paper" \
  --composition "..." \
  --lighting "..." \
  --palette "..." \
  --constraints "no text, no logos, no watermark; cohesive with existing genealogy illustrations" \
  --negative "modern elements, bright colors, busy clutter, photorealistic"
```

### 2. Convert to web-ready JPG

```bash
# Resize and convert to JPG (adjust quality as needed)
sips -s format jpeg -s formatOptions 80 -Z 1024 \
  images/originals/bio/person-name-01-scene.png \
  --out images/bio/person-name-01-scene.jpg
```

Or batch convert all new PNGs:

```bash
for f in images/originals/bio/*.png; do
  base=$(basename "$f" .png)
  sips -s format jpeg -s formatOptions 80 -Z 1024 "$f" \
    --out "images/bio/${base}.jpg"
done
```

### 3. Reference in markdown

```html
<img src="../../../images/bio/person-name-01-scene.jpg" alt="Description" class="float-right-sm">
```

### 4. Commit

Only the JPGs in `images/bio/` (etc.) get committed. The high-res PNGs in `images/originals/` stay local.

## Inputs

- Refer to `PROMPTS.md` for the evergreen prompt style and examples
- `OPENAI_API_KEY` environment variable must be set

## Notes

- Stick with square output (1024x1024) unless different framing is required
- When a new subject prompt is created, copy it into `PROMPTS.md` for reference
- Bio images: ~300KB JPG is a good target size
- Thumbnails: can be smaller (512px or less)
