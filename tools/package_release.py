#!/usr/bin/env python3
"""
Package the built Astro site into a portable zip for GitHub Pages deployment.

Rewrites root-relative paths to dot-relative so the site works under any
subdirectory (e.g., https://pages.enterprise.com/org/repo-name/).

Usage:
    python3 tools/package_release.py
    python3 tools/package_release.py --version 0.2.0
    python3 tools/package_release.py --dist-dir site/dist --output-dir releases/
"""

import argparse
import json
import os
import re
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DIST = PROJECT_ROOT / "site" / "dist"
DEFAULT_OUTPUT = PROJECT_ROOT / "releases"

README_CONTENT = """\
# Agents for Everyone

## Setup (5 minutes, no tools required)

1. **Create a new repository** on your GitHub instance (any name works)
2. On the repo page, click **"uploading an existing file"** (or **Add file > Upload files**)
3. **Drag all the contents** of this folder into the upload area
   - You should see `index.html`, `favicon.svg`, `.nojekyll`, and the `_astro/` and `images/` folders
   - Drag the files and folders themselves, not the outer zip folder
4. Click **Commit changes**
5. Go to **Settings > Pages**
6. Under "Build and deployment", set Source to **Deploy from a branch**
7. Branch: **main**, folder: **/ (root)** > click **Save**
8. Wait 1-2 minutes, then visit the URL shown on the Pages settings page

## Troubleshooting

- **Images not loading?** Make sure the `images/` folder was uploaded with its contents
- **Fonts look wrong?** Make sure the `_astro/` folder was uploaded (it starts with underscore)
- **404 page?** Check that Pages is enabled and pointing to the `main` branch root
- **Still broken?** Verify the `.nojekyll` file is present (it may be hidden — check with "Show hidden files")
"""


def get_version_from_package_json():
    """Read version from site/package.json, fallback to 0.0.0."""
    pkg_path = PROJECT_ROOT / "site" / "package.json"
    if pkg_path.exists():
        with open(pkg_path) as f:
            data = json.load(f)
            return data.get("version", "0.0.0")
    return "0.0.0"


def find_referenced_images(html_path):
    """Parse index.html and return the set of image filenames actually referenced."""
    with open(html_path) as f:
        html = f.read()
    # Match src="/images/<filename>" patterns
    matches = re.findall(r'src="/images/([^"]+)"', html)
    return set(matches)


def rewrite_html(html_path):
    """Rewrite root-relative paths in HTML to dot-relative."""
    with open(html_path) as f:
        content = f.read()

    original = content

    # Rewrite asset paths: /images/, /_astro/, /favicon.svg
    content = content.replace('src="/images/', 'src="./images/')
    content = content.replace('href="/_astro/', 'href="./_astro/')
    content = content.replace('href="/favicon.svg"', 'href="./favicon.svg"')

    # Remove hardcoded OG URL (not meaningful on enterprise)
    content = re.sub(
        r'<meta\s+property="og:url"\s+content="[^"]*"\s*/?>',
        '',
        content
    )

    changes = 0
    if content != original:
        changes = (
            original.count('src="/images/')
            + original.count('href="/_astro/')
            + original.count('href="/favicon.svg"')
            + (1 if 'og:url' in original else 0)
        )

    with open(html_path, 'w') as f:
        f.write(content)

    return changes


def rewrite_css(css_path):
    """Rewrite root-relative font URLs in CSS to relative paths."""
    with open(css_path) as f:
        content = f.read()

    original = content
    # CSS lives in _astro/, fonts are in _astro/ — url(/_astro/font.woff2) -> url(./font.woff2)
    content = content.replace('url(/_astro/', 'url(./')

    changes = original.count('url(/_astro/')

    with open(css_path, 'w') as f:
        f.write(content)

    return changes


def verify_no_root_paths(staging_dir):
    """Scan HTML and CSS for surviving root-relative paths. Returns list of problems."""
    problems = []

    for html_file in staging_dir.rglob("*.html"):
        with open(html_file) as f:
            content = f.read()
        # Find root-relative src/href but exclude anchors (#), external URLs (http), and data URIs
        for match in re.finditer(r'(?:src|href)="(/[^"]*)"', content):
            path = match.group(1)
            if not path.startswith(('#', 'http', 'data:')):
                problems.append(f"{html_file.name}: {match.group(0)}")

    for css_file in staging_dir.rglob("*.css"):
        with open(css_file) as f:
            content = f.read()
        for match in re.finditer(r'url\((/[^)]*)\)', content):
            problems.append(f"{css_file.name}: url({match.group(1)})")

    return problems


def package(dist_dir, output_dir, version):
    """Build the portable release zip."""
    dist_dir = Path(dist_dir)
    output_dir = Path(output_dir)

    if not dist_dir.exists():
        print(f"Error: dist directory not found: {dist_dir}")
        print("Run 'cd site && npm run build' first.")
        sys.exit(1)

    index_html = dist_dir / "index.html"
    if not index_html.exists():
        print(f"Error: index.html not found in {dist_dir}")
        sys.exit(1)

    # Find which images are actually referenced
    referenced = find_referenced_images(index_html)
    print(f"Found {len(referenced)} referenced images in index.html")

    # Create temp staging directory
    with tempfile.TemporaryDirectory() as tmp:
        staging = Path(tmp) / "staging"
        staging.mkdir()

        # Copy index.html
        shutil.copy2(dist_dir / "index.html", staging / "index.html")

        # Copy favicon
        favicon = dist_dir / "favicon.svg"
        if favicon.exists():
            shutil.copy2(favicon, staging / "favicon.svg")

        # Copy _astro/ (CSS + fonts)
        astro_src = dist_dir / "_astro"
        if astro_src.exists():
            shutil.copytree(astro_src, staging / "_astro")

        # Copy only referenced images (skip archive, skip unreferenced)
        images_src = dist_dir / "images"
        if images_src.exists():
            images_dst = staging / "images"
            images_dst.mkdir()
            copied = 0
            skipped = 0
            for img_file in images_src.iterdir():
                if img_file.is_file() and img_file.name in referenced:
                    shutil.copy2(img_file, images_dst / img_file.name)
                    copied += 1
                elif img_file.is_file():
                    skipped += 1
            print(f"Images: {copied} copied, {skipped} skipped (unreferenced)")

        # Add .nojekyll
        (staging / ".nojekyll").touch()

        # Add README
        with open(staging / "README.md", "w") as f:
            f.write(README_CONTENT)

        # Do NOT copy CNAME

        # Rewrite paths
        html_changes = rewrite_html(staging / "index.html")
        print(f"Rewrote {html_changes} paths in index.html")

        css_changes = 0
        for css_file in (staging / "_astro").glob("*.css"):
            css_changes += rewrite_css(css_file)
        print(f"Rewrote {css_changes} font URLs in CSS")

        # Verify no root-relative paths survive
        problems = verify_no_root_paths(staging)
        if problems:
            print("\nWARNING: Found surviving root-relative paths:")
            for p in problems:
                print(f"  {p}")
            print("\nThese will 404 when deployed under a subdirectory.")
            sys.exit(1)
        else:
            print("Verification passed: no root-relative paths remain")

        # Calculate size
        total_bytes = sum(
            f.stat().st_size for f in staging.rglob("*") if f.is_file()
        )
        print(f"Total size: {total_bytes / 1024 / 1024:.1f} MB")

        # Create zip
        output_dir.mkdir(parents=True, exist_ok=True)
        zip_name = f"agents-for-everyone-v{version}.zip"
        zip_path = output_dir / zip_name

        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
            for file_path in sorted(staging.rglob("*")):
                if file_path.is_file():
                    arcname = file_path.relative_to(staging)
                    zf.write(file_path, arcname)

        zip_size = zip_path.stat().st_size
        print(f"\nCreated: {zip_path}")
        print(f"Zip size: {zip_size / 1024 / 1024:.1f} MB")

    return zip_path


def main():
    parser = argparse.ArgumentParser(
        description="Package the built Astro site for portable GitHub Pages deployment."
    )
    parser.add_argument(
        "--version",
        default=None,
        help="Version string for the zip filename (default: from site/package.json)",
    )
    parser.add_argument(
        "--dist-dir",
        default=str(DEFAULT_DIST),
        help=f"Path to the Astro build output (default: {DEFAULT_DIST})",
    )
    parser.add_argument(
        "--output-dir",
        default=str(DEFAULT_OUTPUT),
        help=f"Where to write the zip (default: {DEFAULT_OUTPUT})",
    )

    args = parser.parse_args()

    version = args.version or get_version_from_package_json()
    print(f"Packaging release v{version}")
    print(f"Source: {args.dist_dir}")
    print(f"Output: {args.output_dir}")
    print()

    zip_path = package(args.dist_dir, args.output_dir, version)

    print(f"\nTo create a GitHub release:")
    print(f"  gh release create v{version} {zip_path} \\")
    print(f'    --title "Agents for Everyone v{version}" \\')
    print(f'    --notes "Portable site package for GitHub Pages deployment."')


if __name__ == "__main__":
    main()
