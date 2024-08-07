# This entrypoint file to be used in development. Start by reading README.md
import time_series_visualizer
import sys
from unittest import main

print (sys.argv[1:])

# Test your function by calling it here
#time_series_visualizer.draw_line_plot()
time_series_visualizer.draw_bar_plot()
#time_series_visualizer.draw_box_plot()

# Run unit tests automatically
main(module='test_module', exit=False)


#notes
#replaced numpy 1.24.4 with 1.23
#replaced matplotlib 3.7.5 with 3.7.3