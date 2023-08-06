# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

## [0.6.0] - 2019-12-25

### Added

* Add gentls.py (`webserver gentls`) script that gets LetsEncrypt TLS certificate for website

### Removed

* Bash script gen_tls is now removed

## [0.5.0] - 2019-12-25

### Changed

* Command `webserver sites genconf` is now simplified to `webserver genconf`

## [0.4.2] - 2019-12-24

### Added

* Add genconf.py (`webserver sites genconf`) script that generates HTTPS config with examples

### Removed

* Bash script genconf is now removed

## [0.3.1] - 2019-12-23

### Added

* Add -q/--quiet flag to `webserver update` to silence output
* Add --no-pull flag to `webserver update` to skip pulling fresh nginx image

## [0.3.0] - 2019-12-23

### Added

* Add -q/--quiet flag to `webserver run` to silence output
* Add --no-pull flag to `webserver run` to skip pulling fresh nginx image

## [0.2.1] - 2019-12-22

### Changed

* Start using green-colored text by adding click.style() in click.echo()

## [0.2.0] - 2019-12-22

### Added

* Add update.py (`webserver update`) script that updates webserver stack images

### Removed

* Bash script webserver_update is now removed

## [0.1.1] - 2019-12-22

### Added

* Add echo to run script with explanation of what script does at certain moment

### Removed

* Bash script run is now removed

## [0.1.0] - 2019-12-21

### Added

* Add run.py (`webserver run`) script that spins up nginx stack on Docker Swarm

### Removed

* Folders that were used for Bash scripts are now removed
