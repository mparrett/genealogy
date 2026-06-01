#!/usr/bin/env bash
# Fetch a parish register page at ~1.5x resolution by assembling
# IIPImage tiles from the NLI server.
#
# Usage:
#   ./nli_fetch_hires.sh <vtls_id> <page> <output_filename> [jtl_zoom]
#
# JTL zoom defaults to 4 → ~2328 wide (1.55× the default CVT=JPG).
# JTL=5 → ~4656 wide but ~285 tiles (much slower).
#
# Reference: research/analysis/nli-parish-register-pipeline.md

set -euo pipefail

if [ $# -lt 3 ]; then
  echo "Usage: $0 <vtls_id> <page> <output_filename> [jtl_zoom]" >&2
  exit 1
fi

vtls_id="$1"
page="$2"
outfile="$3"
jtl_zoom="${4:-4}"

# Map JTL zoom to divaserve d[] index. Empirically JTL=N corresponds to d[N-1].
d_index=$(( jtl_zoom - 1 ))

vtls_num=$(echo "$vtls_id" | sed 's/^0*//')
parent_num=$(( vtls_num - vtls_num % 10000 + 10000 ))
parent_dir=$(printf "%09d" "$parent_num")
page_padded=$(printf "%03d" "$page")
jp2="${parent_dir}/${vtls_id}/vtls${vtls_id}_${page_padded}.jp2"

# Read tile grid dimensions for this page at this zoom from divaserve.php JSON
tile_info=$(curl -s "https://registers.nli.ie/diva/php/divaserve.php?d=${vtls_id}" \
  | python3 -c "
import sys, json
d = json.loads(sys.stdin.read())
p = d['pgs'][$page - 1]
z = p['d'][$d_index]
print(z['c'], z['r'])
")
cols=$(echo "$tile_info" | awk '{print $1}')
rows=$(echo "$tile_info" | awk '{print $2}')
total=$(( cols * rows ))

tmpdir=$(mktemp -d -t nli_tiles_XXXXXX)
trap "rm -rf $tmpdir" EXIT

echo "Fetching $total tiles (${cols}x${rows}) at JTL zoom $jtl_zoom..." >&2

fetch_tile() {
  local tile=$1
  local tile_padded=$(printf "%04d" "$tile")
  local outpath="${tmpdir}/tile_${tile_padded}.jpg"
  for attempt in 1 2 3 4 5; do
    if curl -sf "https://iserver.nli.ie/fcgi-bin/iipsrv.fcgi?FIF=${jp2}&JTL=${jtl_zoom},${tile}" -o "$outpath"; then
      if [ -s "$outpath" ] && magick identify "$outpath" >/dev/null 2>&1; then
        return 0
      fi
    fi
    sleep "$attempt"
  done
  echo "  WARN: tile $tile failed after 5 attempts" >&2
  return 1
}

# Modest parallelism: 2 at a time
for tile in $(seq 0 $(( total - 1 ))); do
  fetch_tile "$tile" &
  if (( (tile + 1) % 2 == 0 )); then wait; fi
done
wait

# Count how many tiles actually succeeded
got=$(ls "${tmpdir}"/tile_*.jpg 2>/dev/null | wc -l | tr -d ' ')
echo "Got $got/$total tiles. Stitching..." >&2

if [ "$got" -lt "$total" ]; then
  echo "  WARN: missing tiles — output will have gaps" >&2
fi

magick montage -tile "${cols}x${rows}" -geometry +0+0 \
  "${tmpdir}"/tile_*.jpg "$outfile" 2>/dev/null || true

if [ -s "$outfile" ]; then
  sz=$(stat -f%z "$outfile" 2>/dev/null || stat -c%s "$outfile")
  dims=$(magick identify -format "%wx%h" "$outfile" 2>/dev/null)
  echo "OK [$dims, $((sz/1024))KB]: $outfile"
else
  echo "FAIL: stitched output empty" >&2
  exit 1
fi
