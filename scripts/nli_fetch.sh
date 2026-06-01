#!/usr/bin/env bash
# Fetch a parish register page image from NLI.
#
# Usage:
#   ./nli_fetch.sh <vtls_id> <page> [output_filename]
#
# Examples:
#   ./nli_fetch.sh 000634977 87           # Croom baptisms page 87 → page_087.jpg
#   ./nli_fetch.sh 000634977 87 james.jpg # custom filename
#
# Reference: research/analysis/nli-parish-register-pipeline.md

set -euo pipefail

if [ $# -lt 2 ]; then
  echo "Usage: $0 <vtls_id> <page> [output_filename]" >&2
  echo "  vtls_id: 9-digit zero-padded ID (e.g. 000634977 for Croom baptisms)" >&2
  exit 1
fi

vtls_id="$1"
page="$2"
outfile="${3:-page_$(printf '%03d' "$page").jpg}"

# Compute parent directory bucket
vtls_num=$(echo "$vtls_id" | sed 's/^0*//')
parent_num=$(( vtls_num - vtls_num % 10000 + 10000 ))
parent_dir=$(printf "%09d" "$parent_num")
page_padded=$(printf "%03d" "$page")

url="https://iserver.nli.ie/fcgi-bin/iipsrv.fcgi?FIF=${parent_dir}/${vtls_id}/vtls${vtls_id}_${page_padded}.jp2&CVT=JPG"

echo "Fetching: $url" >&2
curl -s "$url" --max-time 60 -o "$outfile"

if [ -s "$outfile" ]; then
  size=$(stat -f%z "$outfile" 2>/dev/null || stat -c%s "$outfile")
  echo "OK ($size bytes): $outfile"
else
  echo "FAIL: empty response" >&2
  rm -f "$outfile"
  exit 1
fi
