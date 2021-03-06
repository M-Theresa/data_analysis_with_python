import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df =pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'], s=6)

    # Create first line of best fit
    linregress_stats = linregress(df['Year'], y=df['CSIRO Adjusted Sea Level'])
    slope = linregress_stats.slope
    intercept = linregress_stats.intercept

    x_predict_2050 = range(1880, 2051)

    plt.plot(
        x_predict_2050,
        intercept + slope * x_predict_2050,
        "r",
        label="first line of best fit",
    )

    # Create second line of best fit
    x_2000_recent = df[df["Year"] >= 2000]["Year"]
    y_2000_recent = df[df["Year"] >= 2000]["CSIRO Adjusted Sea Level"]

    linregress_stats = linregress(x_2000_recent, y_2000_recent)
    slope_2000_recent = linregress_stats.slope
    intercep_2000_recent = linregress_stats.intercept

    x_predict_2000_2050 = range(2000, 2051)

    plt.plot(
        x_predict_2000_2050,
        intercep_2000_recent + slope_2000_recent * x_predict_2000_2050,
        "b",
        label="second line of best fit",
    )

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()

if __name__ == '__main__':
    draw_plot()