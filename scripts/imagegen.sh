#!/bin/bash
# Wrapper for codex image generation
# Usage: ./scripts/imagegen.sh [image_gen.py arguments...]
#
# This script sets up the environment and calls image_gen.py
# Add to Claude's allowed commands for auto-approval

export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export IMAGE_GEN="$CODEX_HOME/skills/imagegen/scripts/image_gen.py"

exec uv run --with openai --with pillow python "$IMAGE_GEN" "$@"
