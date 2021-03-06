# PySpeckle
A Python Speckle Client

[Speckle.Works](https://www.speckle.works)

> Speckle: open digital infrastructure for designing, making and operating the built environment.
> We reimagine the design process from the Internet up: Speckle is an open source (MIT) initiative for developing an extensible Design & AEC data communication and collaboration platform.

## Updates

### January 15, 2019

Pip distribution updated to version 0.2.5. Remember to `pip install speckle --upgrade` to stay up-to-date.

## Installation
PySpeckle can be installed through `pip`:
`pip install speckle`

## Disclaimer
This code is WIP and as such should be used with caution, on non-sensitive projects.

## Description

PySpeckle is a light Python wrapper / interface for the Speckle framework. It can be used independently through Python scripts, or as a base for building various plug-ins, such as [SpeckleBlender](https://github.com/speckleworks/SpeckleBlender). 

At the moment, it copies the same method names from the .NET `SpeckleApiClient`, for consistency's sake. Although the functions are mostly labelled 'Async', they are not yet. This could eventually be implemented with `requests_futures` or `grequests` or similar.

## Notes
SpeckleBlender is written and maintained by [Tom Svilans](http://tomsvilans.com) ([Github](https://github.com/tsvilans)).
