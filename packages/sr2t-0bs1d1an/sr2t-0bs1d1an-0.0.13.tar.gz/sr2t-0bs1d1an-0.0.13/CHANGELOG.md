# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

- Figure out a way, if at all useful, to print more details (software versions; Nmap script output).
- Add more useful parsers?
- Look into grouping similar observations when outputting to XLSX
- Not sure if useful, but look into adding an optional Nessus column to print each finding details.

## [0.0.13] - 2019-12-25

### Added

- Ho ho ho, added yamllint to pipeline.

### Changed

- All data files are now refactored into pretty YAML files.

### Removed

- None.

## [0.0.12] - 2019-12-24

### Added

- None.

### Changed

- Moved all testssl.sh findings to match for, to a separate file.

### Removed

- None.

## [0.0.11] - 2019-12-23

### Added

- Added a CHANGELOG.md

### Changed

- Updated README.
- Dirble XLSX tab now has a blue color.
- Nessus XLSX SYN, TLS, X.509 and HTTP worksheets no longer contain 'Nessus' in their worksheet names as it's quite obvious, IMHO, and saves space.

### Removed

- None.

## [0.0.10] - 2019-12-23

### Added

- Multiple parsers can now be used in a single run. When outputting to XLSX, separate worksheets will simply be appended to the same XLSX file. When outputting to CSV, you should now specify a basename (i.e. no extension).

### Changed

- Updated README.
- .gitlab-ci.yml now lints al Python scripts it can find with flake8, recursively up to 2 child directories.

### Removed

- None.

## [0.0.9] - 2019-12-23

### Added

- Added more auto classifications.

### Changed

- Moved auto classifications etc. to separate files.
- Make X's visible in Nessus tables for colour blind people.

### Removed

- None.
