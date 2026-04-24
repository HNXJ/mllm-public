# science-asset-refiner
Automates compression (PNG→WEBP) and link validation for `gravia-slides`. Prevents broken assets in large research presentations.

## Protocol
1.  **Discovery:** Scan `index.html` and `assets/` for all linked media.
2.  **Compression:** Use `ffmpeg` or `magick` (if available) to convert PNG to WEBP (lossless or 80% quality).
3.  **Refactoring:** Update `index.html` references from `.png` to `.webp`.
4.  **Validation:** Run `link_check.sh` to ensure all paths are correct.

## Tooling
- `link_check.sh`: Local script for path validation.
- `magick`: For image conversion.
