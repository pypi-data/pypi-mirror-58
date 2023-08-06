# Lucidic Python Dictionary Utility Package Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.2] - 2019-12-27

### Added

- Getters and Setters for self._results, self._keyword, and self._strict by [@rnason](https://github.com/rnason).
- Internal reset instance method to clear previously set values for self._results, self._strict, and self._keyword by [@rnason](https://github.com/rnason)
- Unit tests for Getters and Setters by [@rnason](https://github.com/rnason).
- Added Replace None, Null, Nil, empty string method by [@rnason](https://github.com/rnason).
- Added Method logic to find and replace a key or it's cooresponding value by [@rnason](https://github.com/rnason).
- Unit test for find and replace key and value methods by [@rnason](https://github.com/rnason).

### Changed

- Few internal method names, and access to self internal attributes via Getters and Setters by [@rnason](https://github.com/rnason).
- Docstring updates by [@rnason](https://github.com/rnason).

### Removed

<!-- markdownlint-disable MD024 -->
## [0.1.1] - 2019-12-27

### Added

- Functional Unit tests for all methods by [@rnason](https://github.com/rnason).
- Readme updated to document currently available methods by [@rnason](https://github.com/rnason).

### Changed

- Logic refactored to ensure recursive search through list objects by [@rnason](https://github.com/rnason).
- Main search divided into smaller methods to match, recursively search nested dicts objects, and recursively search nested lists. by [@rnason](https://github.com/rnason).

### Removed

<!-- markdownlint-disable MD024 -->
## ['0.1.0'] - 2019-12-23

### Added

- Dictionary Search, loose or exact search for keyword through entire dict including dict and list values by [@rnason](https://github.com/rnason).
- Docstrings for all internal and public class methods by [@rnason](https://github.com/rnason).

### Changed

### Removed
