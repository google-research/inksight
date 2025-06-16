# Changelog

<!--

Changelog follow the https://keepachangelog.com/ standard (at least the headers)

This allow to:

* auto-parsing release notes during the automated releases from github-action:
  https://github.com/marketplace/actions/pypi-github-auto-release
* Have clickable headers in the rendered markdown

To release a new version (e.g. from `1.0.0` -> `2.0.0`):

* Create a new `# [2.0.0] - YYYY-MM-DD` header and add the current
  `[Unreleased]` notes.
* At the end of the file:
  * Define the new link url:
  `[2.0.0]: https://github.com/google-research/inksight/compare/v1.0.0...v2.0.0`
  * Update the `[Unreleased]` url: `v1.0.0...HEAD` -> `v2.0.0...HEAD`

-->

## [Unreleased]

## 2025-06-16

### Added
- uv package manager support with `pyproject.toml` configuration and `uv.lock` for faster dependency management
- `.python-version` file for consistent Python version management

### Changed
- Updated README.md with TMLR publication badge and improved badge styling
- Fixed minor issues in Colab notebook for better execution

## 2024-10-23

### Added
- Initial release with InkSight model for offline-to-online handwriting conversion
- Colab notebook for easy experimentation and inference examples
- Support for both word-level and full-page handwriting conversion
- Model weights and dataset on Hugging Face
- Interactive demo on Hugging Face Spaces
- Comprehensive documentation and examples

### Features
- Vision Transformer (ViT) and mT5 encoder-decoder architecture
- Multi-language support with robust background handling
- Vector-based digital ink output for editing and search
- Integration with docTR and Tesseract OCR for text processing

[Unreleased]: https://github.com/google-research/inksight/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/google-research/inksight/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/google-research/inksight/releases/tag/v0.1.0
