import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',parse_dates=['date'])
df.set_index('date', inplace=True)

# Clean data
df = df[(df['value']>df['value'].quantile(0.025)) & (df['value']<df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig=plt.figure(figsize=(15,6))
    plt.plot(df.index.values, 'value',data=df)
    plt.xlabel ('Date')
    plt.ylabel ('Page Views')
    plt.title ('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy(deep=True)
    df_bar['date_year']=df_bar.index.strftime('%Y')
    df_bar['Months']=df_bar.index.strftime('%B')
    df_bar['date_month_n']=df_bar.index.strftime('%m').astype(int)
    df_bar_plot=df_bar.groupby(['date_year','Months'])['value'].mean().to_frame()

    # Draw bar plot
    ho = df_bar.sort_values(by='date_month_n')['Months'].unique()
    fig, ax = plt.subplots(figsize=(8, 7))
    ax.set(xlabel='Years', ylabel='Average Page Views')
    ax.use_sticky_edges=False
    p=sns.barplot(x='date_year', y='value', hue='Months', hue_order=ho,
                data=df_bar_plot, palette='deep', ax=ax)
    plt.xticks(rotation=90)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
