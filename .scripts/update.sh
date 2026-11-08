#!/usr/bin/env bash
# Re-import the MCB/*.docx study notes into the vault's Appunti/ folders.
#
#   .scripts/update.sh            only the docx changed since the last import
#   .scripts/update.sh FG SATAUMV just these keys (see: python3 .scripts/build.py --list)
#   .scripts/update.sh --all      everything
#
# Works on Linux and on Windows (Git Bash). Needs: Python 3, LibreOffice (soffice) and
# ImageMagick (magick; `convert` on Linux is fine) for EMF images. pandoc >= 3 is used
# from PATH, otherwise pypandoc_binary is installed in a venv under $IMPORT_WORK.
# Hand edits inside Appunti notes are overwritten: put recurring fixes in FIXES (build.py).
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export IMPORT_WORK="${IMPORT_WORK:-$HOME/.cache/bioinformatics-import}"
STAMP="$HERE/last-import.sha256"
mkdir -p "$IMPORT_WORK/conv"

# Python: python3 on Linux; python / py on Windows (Git Bash). The Windows Store
# "python3" alias is a stub that fails, so each candidate is actually run.
PY=""
for c in python3 python py; do
    if command -v "$c" >/dev/null && "$c" -c 'import sys; sys.exit(sys.version_info < (3, 8))' 2>/dev/null; then PY="$c"; break; fi
done
[ -n "$PY" ] || { echo "Python 3 not found" >&2; exit 1; }
export PYTHONIOENCODING=utf-8 PYTHONUTF8=1

case "$(uname -s)" in MINGW*|MSYS*|CYGWIN*) VBIN=Scripts ;; *) VBIN=bin ;; esac
if command -v pandoc >/dev/null && pandoc --version | head -1 | grep -qE ' (3|[4-9])\.'; then
    PANDOC=pandoc
else   # pandoc missing or too old (< 3): private copy via pypandoc_binary
    if [ ! -e "$IMPORT_WORK/venv/$VBIN/python" ] && [ ! -e "$IMPORT_WORK/venv/$VBIN/python.exe" ]; then
        "$PY" -m venv "$IMPORT_WORK/venv"
        "$IMPORT_WORK/venv/$VBIN/python" -m pip -q install pypandoc_binary
    fi
    PANDOC="$("$IMPORT_WORK/venv/$VBIN/python" -c 'import pypandoc; print(pypandoc.get_pandoc_path())')"
fi

declare -A SRC
while IFS=$'\t' read -r key path; do SRC[$key]="$path"; done < <("$PY" "$HERE/build.py" --list | tr -d '\r')

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

"$PY" "$HERE/build.py" "${keys[@]}" | grep -v '^    '
"$PY" "$HERE/links.py" >/dev/null

{ for k in "${!SRC[@]}"; do
    if printf '%s\n' "${keys[@]}" | grep -qx "$k"; then echo "$k $(hash_of "${SRC[$k]}")"; else grep -s "^$k " "$STAMP" || true; fi
  done; } | sort > "$STAMP.tmp" && mv "$STAMP.tmp" "$STAMP"
echo "Done. Review with: git -C \"$(dirname "$HERE")\" status"
