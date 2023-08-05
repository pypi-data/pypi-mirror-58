[![pipeline status](https://gitlab.com/0bs1d1an/rpg/badges/master/pipeline.svg)](https://gitlab.com/0bs1d1an/rpg/commits/master)

# Risk plot generator (rpg)

This tool takes a CSV file with your observations and can output either a grid plot, or a donut ring.
It also accepts a CSV with recommendations to output a recommendations grid.

## Rationale

I was fed-up with having to manually create these graphs for a client and I wanted to make my life easier.
And since I want to increase my Python skills some more, this would be a fun little project to catch two birds with one stone.

## Dependencies

1. argparse (dev-python/argparse);
2. matplotlib (dev-python/matplotlib);
3. python (dev-lang/python).

## Install

Using Pip:

`pip install --user rpg-0bs1d1an`

## Usage

You can use sr2t in two ways:

* When installed as package, call the installed script: `rpg --help`.
* When Git cloned, call the script directly from the root of the Git
repository: `python -m rpg.rpg --help`

```
$ rpg -h
usage: rpg [-h] (-g | -d | -r) -iC INPUT_CSV_FILE [-oP OUTPUT_PNG_FILE]
           [--axis-labels AXIS_LABELS] [--axis-arrows AXIS_ARROWS]
           [--legend LEGEND]

Converting scanning reports to a tabular format

optional arguments:
  -h, --help            show this help message and exit
  -g, --grid            generate a risk grid plot.
  -d, --donut           generate a risk donut.
  -r, --recommendations
                        generate a risk recommendations plot.
  -iC INPUT_CSV_FILE, --input-csv-file INPUT_CSV_FILE
                        specify an input CSV file (e.g. data.csv).
  -oP OUTPUT_PNG_FILE, --output-png-file OUTPUT_PNG_FILE
                        specify an output PNG file (e.g. risk.png).
  --axis-labels AXIS_LABELS
                        specify to print the axis labels
  --axis-arrows AXIS_ARROWS
                        specify to print arrows along the axis
  --legend LEGEND       specify to print the legend
```

## Example

To generate a risk grid plot: `$ rpg -iC example/input/observations.csv -oP example/output/grid.png -g`

![Grid](example/output/grid.png)

To generate a risk donut: `$ rpg -iC example/input/observations.csv -oP example/output/donut.png -d`

![Donut](example/output/donut.png)

To generate a recommendations plot: `$ rpg -iC example/input/recommendations.csv -oP example/output/recommendations.png -r`

![Recommendations](example/output/recommendations.png)

## To do

1. Figure out a way to optionally mark observations as "solved" by shading the marker