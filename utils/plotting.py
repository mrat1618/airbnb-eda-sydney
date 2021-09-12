import matplotlib as mpl
import seaborn as sns 

def set_plotting_style()->None:
    """Apply matplotlib and sns plotting style/palette
    """
    mpl.style.use('fivethirtyeight')
    sns.set_palette("mako")

    mpl.rcParams['font.size'] = 10  # customise font size of a particular graph title, x-axis ticker and y-axis ticker
    mpl.rcParams['legend.fontsize'] = 10 # customise legend size
    mpl.rcParams['figure.titlesize'] = 15 # customise the size of suptitle
    mpl.rcParams['lines.markersize'] = 10
    mpl.rcParams['legend.markerscale'] = 0.5
    mpl.rcParams['lines.markeredgewidth'] = 4

