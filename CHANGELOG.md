# Changelog

## [2.1.1](https://github.com/ButterCMS/buttercms-python/compare/v2.1.0...v2.1.1) (2024-05-07)


### Bug Fixes

* add permissions for packages and deployments ([291ce2b](https://github.com/ButterCMS/buttercms-python/commit/291ce2b88aed097a96c672cac1969e0ea716da01))
* enable publish workflow ([efda10b](https://github.com/ButterCMS/buttercms-python/commit/efda10b53c1ad250ddbc7af8321d155b0d3fc74d))

## [2.1.0](https://github.com/ButterCMS/buttercms-python/compare/v2.0.0...v2.1.0) (2024-05-07)


### Features

* implement continuous delivery ([1972c84](https://github.com/ButterCMS/buttercms-python/commit/1972c84ba0eb41fd2797b7e5c33fc0b8281f8698))


### Bug Fixes

* add needed requirements file ([1972c84](https://github.com/ButterCMS/buttercms-python/commit/1972c84ba0eb41fd2797b7e5c33fc0b8281f8698))


### Documentation

* add contributing guide ([1972c84](https://github.com/ButterCMS/buttercms-python/commit/1972c84ba0eb41fd2797b7e5c33fc0b8281f8698))

## 2.0.0

### Added
- Add `requirements.txt` for defining required dependencies

### Changed
- Get version from `version.py` file with exec - avoiding initialization of the package prematurely

### Fixed
- Add handling of timeout of 10 seconds to client.py
