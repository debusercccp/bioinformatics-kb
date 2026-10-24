#!/usr/bin/env bash
# Re-import the MCB/*.docx study notes into the vault's Appunti/ folders.
#
#   .scripts/update.sh            only the docx changed since the last import
#   .scripts/update.sh FG SATAUMV just these keys (see: python3 .scripts/build.py --list)
#   .scripts/update.sh --all      everything
#
# Needs: python3, soffice + magick (EMF images). pandoc is used from PATH,
# otherwise pypandoc_binary is installed in a venv under $IMPORT_WORK.
# Hand edits inside Appunti notes are overwritten: put recurring fixes in FIXES (build.py).
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export IMPORT_WORK="${IMPORT_WORK:-$HOME/.cache/bioinformatics-import}"
STAMP="$HERE/last-import.sha256"
mkdir -p "$IMPORT_WORK/conv"

if command -v pandoc >/dev/null; then
    PANDOC=pandoc
else
    if [ ! -x "$IMPORT_WORK/venv/bin/python" ]; then
        python3 -m venv "$IMPORT_WORK/venv"
        "$IMPORT_WORK/venv/bin/pip" -q install pypandoc_binary
    fi
    PANDOC="$("$IMPORT_WORK/venv/bin/python" -c 'import pypandoc; print(pypandoc.get_pandoc_path())')"
fi

declare -A SRC
while IFS=$'\t' read -r key path; do SRC[$key]="$path"; done < <(python3 "$HERE/build.py" --list)

hash_of() { sha256sum "$1" | cut -d' ' -f1; }
old_hash() { grep -s "^$1 " "$STAMP" | cut -d' ' -f2 || true; }

keys=()
if [ "${1:-}" = "--all" ]; then
    keys=("${!SRC[@]}")
elif [ $# -gt 0 ]; then
    for k in "$@"; do [ -n "${SRC[$k]:-}" ] || { echo "unknown key: $k" >&2; exit 1; }; done
    keys=("$@")
else
    for k in "${!SRC[@]}"; do
        [ "$(hash_of "${SRC[$k]}")" = "$(old_hash "$k")" ] || keys+=("$k")
    done
fi
if [ ${#keys[@]} -eq 0 ]; then echo "Nothing changed since the last import."; exit 0; fi

for k in "${keys[@]}"; do
    d="$IMPORT_WORK/conv/$k"; rm -rf "$d"; mkdir -p "$d"
    (cd "$d" && "$PANDOC" "${SRC[$k]}" -t gfm+tex_math_dollars --wrap=none \
        --lua-filter="$HERE/tablemath.lua" --extract-media=media -o "$k.md")
done

python3 "$HERE/build.py" "${keys[@]}" | grep -v '^    '
python3 "$HERE/links.py" >/dev/null

{ for k in "${!SRC[@]}"; do
    if printf '%s\n' "${keys[@]}" | grep -qx "$k"; then echo "$k $(hash_of "${SRC[$k]}")"; else grep -s "^$k " "$STAMP" || true; fi
  done; } | sort > "$STAMP.tmp" && mv "$STAMP.tmp" "$STAMP"
echo "Done. Review with: git -C \"$(dirname "$HERE")\" status"
