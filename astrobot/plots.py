from datetime import datetime
from io import BytesIO

import matplotlib.pyplot as plt
import numpy as np
from constants import BODIES, DIRECTIONS


def plot_polar_sky(
    eph,
    obj,
    date
):
    """
    Plot a polar sky map of the celestial sphere.
    
    Args:
        eph (Ephemeris): The Ephemeris object.
        obj (str): The sky object.
        date (datetime): The date.
    
    Returns:
        BytesIO: The BytesIO image.
    """
    # Compute the daily path and the actual position of the object
    alt, az = eph.compute_daily_path(date, obj)
    actual_alt, actual_az = eph.compute_actual_position(date, obj)

    # Get the color and size of the object
    color, size = BODIES[obj]

    # Plot the polar sky map
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.set_theta_zero_location('N' if eph.latitude >= 0 else 'S', offset=0)
    ax.set_theta_direction(-1)
    ax.set_thetagrids(np.linspace(0, 360, 9), DIRECTIONS)
    ax.set_rgrids(np.linspace(0, 90, 10), [f'{int(i)}°' for i in np.linspace(90, 0, 10)])
    ax.set_rlabel_position(0 if eph.latitude >= 0 else 180)
    ax.tick_params(axis='y', labelsize=8)
    ax.set_ylim([0, 90])

    # Plot a wide circle for the horizon
    ax.plot(np.linspace(0, 2 * np.pi, 100), np.full(100, 90), color='k', linewidth=2.5)

    # Plot the daily path and the actual position of the object
    ax.plot(np.radians(az), [90 - a for a in alt], color='k', linewidth=0.8)
    ax.plot(np.radians(actual_az), 90 - actual_alt, 'o', color=color, markersize=size, markeredgecolor='black')

    # Plot the solstices for the sun
    if obj == 'sun':
        summer_solstice, winter_solstice = eph.get_solstices(date.year)

        solstices = [summer_solstice, winter_solstice]
        solstice_colors = ['gold', 'blue']
        solstice_labels = ['Solstice d\'été', 'Solstice d\'hiver']
        style = {'linestyle': '--', 'linewidth': 0.8}

        for solstice, color, label in zip(solstices, solstice_colors, solstice_labels):
            solstice_alt, solstice_az = eph.compute_daily_path(solstice, obj)
            ax.plot(np.radians(solstice_az), [90 - a for a in solstice_alt], color=color, label=label, **style)

        # ax.legend() # TODO: Move the legend to the bottom of the plot

    ax.grid(True)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)

    return buffer

def plot_xy_path(
    eph,
    obj,
    date
):
    """
    Plot an XY path of the object.

    Args:
        eph (Ephemeris): The Ephemeris object.
        obj (str): The sky object.
        date (datetime): The date.

    Returns:
        BytesIO: The BytesIO image.
    """
    # Compute the daily path and the actual position of the object
    alt, az = eph.compute_daily_path(date, obj)
    actual_alt, actual_az = eph.compute_actual_position(date, obj)
    
    if eph.latitude < 0:
        az_corrected = []
        for value in az:
            if value > 180:
                az_corrected.append(round(value - 180, 2))
            else:
                az_corrected.append(round(value + 180, 2))
        az = az_corrected
        actual_az = round(actual_az - 180, 2) if actual_az > 180 else round(actual_az + 180, 2)
    
    # Get the color and size of the object
    color, size = BODIES[obj]

    # Plot the XY path
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, 360)
    ax.set_ylim(0, 90)
    if eph.latitude < 0:
        numbers = list(range(180, 341, 20)) + list(range(0, 181, 20))
        ax.set_xticks(np.arange(0, 361, 20), [f'{int(i)}°' for i in numbers])
    else:
        ax.set_xticks(np.arange(0, 361, 20), [f'{int(i)}°' for i in np.arange(0, 361, 20)])
    ax.set_yticks(np.arange(0, 91, 10), [f'{int(i)}°' for i in np.arange(0, 91, 10)])
    ax.set_xlabel('Azimuth (°)')
    ax.set_ylabel('Altitude (°)')
    ax.grid(True)

    # Plot the daily path and the actual position of the object
    ax.plot(az, alt, color='k', linewidth=0.8)
    ax.plot(actual_az, actual_alt, 'o', color=color, markersize=size, markeredgecolor='black')
    
    # Plot the solstices for the sun
    if obj == 'sun':
        summer_solstice, winter_solstice = eph.get_solstices(date.year)

        solstices = [summer_solstice, winter_solstice]
        solstice_colors = ['gold', 'blue']
        solstice_labels = ['Solstice d\'été', 'Solstice d\'hiver']
        style = {'linestyle': '--', 'linewidth': 0.8}

        for solstice, color, label in zip(solstices, solstice_colors, solstice_labels):
            solstice_alt, solstice_az = eph.compute_daily_path(solstice, obj)
            if eph.latitude < 0:
                az_corrected = []
                for value in solstice_az:
                    if value > 180:
                        az_corrected.append(round(value - 180, 2))
                    else:
                        az_corrected.append(round(value + 180, 2))
                solstice_az = az_corrected
            ax.plot(solstice_az, solstice_alt, color=color, label=label, **style)

        ax.legend(loc='upper right')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)

    return buffer
