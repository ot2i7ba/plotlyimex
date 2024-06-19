# Copyright (c) 2023 ot2i7ba
# https://github.com/ot2i7ba/
# This code is licensed under the MIT License (see LICENSE for details).

"""
Imports a CSV file to generate an interactive map using plotly.
"""

import pandas as pd
import plotly.express as px
import plotly.io as pio
import os
import argparse
from concurrent.futures import ThreadPoolExecutor

def clear_screen():
    # Clear the screen depending on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    # Print the header
    print(" plotlyimex v0.1.0 by ot2i7ba ")
    print("==============================")
    print("")

def print_csv_format_info():
    # Provide information about the required CSV file format
    print("Please provide a CSV file with the following columns:")
    print("latitude, longitude, id, userId, lastSeenAt, speed, direction, source.")
    print("The file should ideally be comma-separated.")
    print("")

def get_csv_filename():
    # Prompt the user to input the CSV filename
    print()
    csv_file = input("Input csv filename (enter for 'import.csv'): ")
    
    # Set default filename if none provided
    if not csv_file:
        csv_file = 'import.csv'
    elif not csv_file.endswith('.csv'):
        csv_file += '.csv'
    return csv_file

def validate_csv_file(csv_file):
    # Validate if the file exists and is a CSV file
    if not os.path.isfile(csv_file):
        raise FileNotFoundError(f"Error: The file '{csv_file}' could not be found.")
    if not csv_file.endswith('.csv'):
        raise ValueError(f"Error: The file '{csv_file}' is not a CSV file.")
    return csv_file

def get_delimiter():
    # Prompt the user to input the delimiter used in the CSV file
    print()
    delimiter = input("Enter the delimiter used in the CSV file (',' for comma, ';' for semicolon, default is ','): ")
    
    # Set default delimiter to comma if none provided
    if delimiter not in [',', ';']:
        delimiter = ','
    return delimiter

def load_csv(csv_file, delimiter):
    # Load the CSV file using pandas with the specified delimiter
    try:
        df = pd.read_csv(csv_file, delimiter=delimiter, usecols=["latitude", "longitude", "id", "userId", "lastSeenAt", "speed", "direction", "source"])
        return df
    except Exception as e:
        raise ValueError(f"Error loading CSV file: {e}")

def choose_plot_type():
    # Print the plot type options
    print()
    print("Choose a plot type:")
    plot_types = {
        "1": "Scatter Plot",
        "2": "Density Plot",
        "3": "Lines Plot",
        "A": "All"
    }
    for key, value in plot_types.items():
        print(f"{key}. {value}")
    
    # Prompt the user to select a plot type
    print()
    choice = input("Enter the number of the plot type (default is 1): ")
    return plot_types.get(choice, "Scatter Plot")

def create_map(df, plot_type):
    # Create the appropriate plot based on the plot type selected
    try:
        if plot_type == "Scatter Plot":
            fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", hover_name="id",
                                    hover_data=["userId", "lastSeenAt", "speed", "direction", "source"],
                                    zoom=3)
        elif plot_type == "Density Plot":
            fig = px.density_mapbox(df, lat="latitude", lon="longitude", hover_name="id",
                                    hover_data=["userId", "lastSeenAt", "speed", "direction", "source"],
                                    zoom=3)
        elif plot_type == "Lines Plot":
            fig = px.line_geo(df, lat="latitude", lon="longitude", hover_name="id",
                              hover_data=["userId", "lastSeenAt", "speed", "direction", "source"],
                              projection="orthographic")
        else:
            raise ValueError(f"Unknown plot type: {plot_type}")

        # Update the layout of the map
        fig.update_layout(mapbox_style="open-street-map", height=1080, width=1920)
        return fig
    except Exception as e:
        raise ValueError(f"Error creating map: {e}")

def export_plot(fig, plot_name):
    # Export the plot to an HTML file
    try:
        html_file = f"export_{plot_name}.html"
        pio.write_html(fig, file=html_file)
        print(f"Plot saved as {html_file}")
    except Exception as e:
        raise ValueError(f"Error exporting plot: {e}")

def get_html_filename(default_name):
    # Prompt the user to input the output HTML filename
    print()
    html_file = input(f"Output html filename (enter for '{default_name}'): ")
    
    # Set default filename if none provided
    if not html_file:
        html_file = default_name
    elif not html_file.endswith('.html'):
        html_file += '.html'
    return html_file

def export_all_plots(df):
    # Export all plot types using parallel processing
    plot_types = ["Scatter Plot", "Density Plot", "Lines Plot"]
    with ThreadPoolExecutor() as executor:
        futures = []
        for plot_type in plot_types:
            futures.append(executor.submit(export_plot, create_map(df, plot_type), plot_type.lower().replace(" ", "_")))
        for future in futures:
            future.result()

def main():
    # Clear the screen and print the header
    clear_screen()
    print_header()
    
    # Provide information about the required CSV file format
    print_csv_format_info()

    # Define argument parser for command-line options
    parser = argparse.ArgumentParser(description='Generate an interactive map from a CSV file.')
    parser.add_argument('--input', type=str, help='Input CSV filename', default='import.csv')
    parser.add_argument('--output', type=str, help='Output HTML filename', default='')
    
    args = parser.parse_args()

    try:
        # Get and validate the input CSV filename
        csv_file = get_csv_filename()
        validate_csv_file(csv_file)
        
        # Get the delimiter used in the CSV file
        delimiter = get_delimiter()
        
        # Load the CSV file into a DataFrame
        df = load_csv(csv_file, delimiter)
        
        # Prompt the user to choose a plot type
        plot_type = choose_plot_type()
        
        # Create and export plots based on the user's choice
        if plot_type == "All":
            export_all_plots(df)
        else:
            fig = create_map(df, plot_type)
            plot_name = plot_type.lower().replace(" ", "_")
            html_file = get_html_filename(f"export_{plot_name}.html")
            
            # Show and export the plot
            pio.show(fig)
            pio.write_html(fig, file=html_file)
            print(f"Plot saved as {html_file}")
    except (FileNotFoundError, ValueError) as e:
        print(e)

if __name__ == "__main__":
    main()
