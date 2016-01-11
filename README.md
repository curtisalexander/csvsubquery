# csvsubquery

## Usage
```
csvsubquery.py [OPTIONS]

Options:
  --incsv FILENAME   input csv (the larger of the csv files)
  --subcsv FILENAME  subquery csv (the smaller of the csv files)
  --outcsv FILENAME  output csv
  --key TEXT         key variable to be used for the subquery - must be same key name on incsv and subcsv
  --help             Show this message and exit.
```

## Assumptions
Assumes the input CSV file has a header.

## Example
```
csvsubquery.py --incsv /dir/to/infile.csv --subcsv /dir/to/subfile.csv --outcsv /dir/to/outfile.csv --key keyvar
```

## Requirements
[click](http://click.pocoo.org) - command line library for Python

```pip install click``` 

## Related
[csvkit](https://github.com/onyxfish/csvkit) - a suite of utilities for converting to and working with CSV
