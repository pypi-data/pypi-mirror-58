"""Plotting routines."""

from .colors import (color_char_to_word, get_cmap_safe, hex_to_rgb, hexcolors,
                     string_to_rgb, PARAVIEW_BACKGROUND)
from .export_vtkjs import export_plotter_vtkjs, get_vtkjs_url
from .helpers import plot, plot_arrows, plot_compare_four
from .plotting import BasePlotter, Plotter, close_all
from .qt_plotting import BackgroundPlotter, QtInteractor
from .renderer import CameraPosition, Renderer, scale_point
from .theme import (DEFAULT_THEME, FONT_KEYS, MAX_N_COLOR_BARS,
                    parse_color, parse_font_family, rcParams, set_plot_theme)
from .tools import (create_axes_orientation_box, opacity_transfer_function,
                    system_supports_plotting)
from .widgets import WidgetHelper
