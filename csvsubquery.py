#!/usr/bin/env python

import csv
import click    # pip install click -- assumes version 5.x

@click.command()
@click.option('--incsv', type=click.File(mode='rU', lazy=True), help='input csv (the larger of the csv files)')
@click.option('--subcsv', type=click.File(mode='rU', lazy=True), help='subquery csv (the smaller of the csv files)')
@click.option('--outcsv', type=click.File(mode='w', lazy=True), help='output csv')
@click.option('--key', help='key variable to be used for the subquery - only supports a single key')

def subquery(incsv, subcsv, outcsv, key):
    """Perform a subquery using CSV files with a common key.

    \b
    Example:
        csvsubquery.py --incsv /dir/to/infile.csv --subcsv /dir/to/subfile.csv --outcsv /dir/to/outfile.csv --key keyvar
    """
    sub_reader = csv.DictReader(subcsv)
    key_subset = {row[key] for row in sub_reader}

    in_reader = csv.DictReader(incsv)
    header = next(in_reader)
    out_writer = csv.DictWriter(outcsv, header, extrasaction='ignore')
    out_writer.writeheader()
    for row in in_reader:
        if row[key] in key_subset:
            out_writer.writerows([dict(zip(header, [row[c] for c in header]))])

if __name__ == '__main__':
    subquery()
