# Changelog

All notable changes to this project will be documented in this file.

## [0.0.9] - 2019-12-28

### Added

- None.

### Changed

- Restructured package a bit. When not installed as a package, rpg can be run with 'python -m rpg' (as opposed to 'python -m rpg.rpg').

### Removed

- None.

## [0.0.8] - 2019-12-27

### Added

- None.

### Changed

- Fixed linter issues.

### Removed

- None.

## [0.0.7] - 2019-12-27

### Added

- Added support for YAML input files, for those that favour YAML over CSV (or vice versa). Input CSV files are still supported.
- Added CHANGELOG.md

### Changed

- The '--axis-labels' and '--axis-arrows' arguments no longer require a value. Specifying the argument by itself suffices now.
- Fixed the donut function.

### Removed

- The '--legend' argument was broken for some time now, was no longer supported, and is now removed.
