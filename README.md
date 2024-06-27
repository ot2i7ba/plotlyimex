# plotlyimex

plotlyimex is a Python script that generates interactive maps from CSV files using the Plotly library. The script allows users to choose between different plot types and export the generated maps as HTML files. I personally use this script to display information exported from Cellebrite UFED.

## Features

- Load CSV files with specific columns: `latitude`, `longitude`, `id`, `userId`, `lastSeenAt`, `speed`, `direction`, `source`
- Choose from three plot types: Scatter Plot, Density Plot, Lines Plot
- Option to export all three plot types automatically
- Interactive map visualization using Plotly
- Customizable delimiter for CSV files (comma or semicolon)

## Requirements

- Python 3.6 or higher
- The following Python packages (listed in `requirements.txt`):
  - pandas==1.5.3
  - plotly==5.10.0

## Installation

1. Clone Git:
   ```bash
   git clone https://github.com/ot2i7ba/plotlyimex.git
   cd EASurvival
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the script:
   ```bash
   python plotlyimex.py
   ```

2. Follow the prompts:
- CSV Filename: Enter the name of the CSV file you want to load (default is import.csv).
- Delimiter: Enter the delimiter used in the CSV file (',' for comma, ';' for semicolon, default is ',').
- Plot Type: Choose a plot type from the list:
  - 1: Scatter Plot
  - 2: Density Plot
  - 3: Lines Plot
  - A: All (generate and export all three plot types)
- Output HTML Filename: Enter the name of the output HTML file (default is based on the plot type, e.g., export_scatter.html).

## Compiled Version
A compiled and 7zip-packed version of PlotlyImex for Windows is available as a release. You can download it from the **[Releases](https://github.com/ot2i7ba/plotlyimex/releases)** section on GitHub. This version includes all necessary dependencies and can be run without requiring Python to be installed on your system.

## Example
Here is an example of running the script and its output:

  ```
  $ python plotlyimex.py

   plotlyimex v0.1.0 by ot2i7ba
  ==============================

  Please provide a CSV file with the following columns: latitude, longitude, id, userId, lastSeenAt, speed, direction, source.
  The file should ideally be comma-separated.
  Input csv filename (enter for 'import.csv'): mydata.csv

  Enter the delimiter used in the CSV file (',' for comma, ';' for semicolon, default is ','): ,

  Choose a plot type:
  1. Scatter Plot
  2. Density Plot
  3. Lines Plot
  A. All

  Enter the number of the plot type (default is 1): 1

  Output html filename (enter for 'export_scatter.html'): my_scatter_plot.html
  Plot saved as my_scatter_plot.html
  ```

## Acknowledgments
Special thanks to the Plotly team for their amazing visualization library.

## License
This project is licensed under the **[MIT license](https://github.com/ot2i7ba/plotlyimex/blob/main/LICENSE)**, providing users with flexibility and freedom to use and modify the software according to their needs.

## Disclaimer
This project is provided without warranties. Users are advised to review the accompanying license for more information on the terms of use and limitations of liability.
