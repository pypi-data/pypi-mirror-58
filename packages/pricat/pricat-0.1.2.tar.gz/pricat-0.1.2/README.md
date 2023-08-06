# Python pricat package

This is a Python package for loading and parsing tyre lists in Pricat file format

## Installation

	pip install pricat

## Usage

	import pricat

	p = pricat.File()
	p.validate_file("/path/to/pricatfile.csv")
	p.validate_files("/path/to")
	p.load_file("/path/to/pricatfile.csv")
