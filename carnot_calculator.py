"""
Carnot Efficiency Calculator Module
Contains the core physics calculations for Carnot cycle efficiency.
"""

import numpy as np


def calculate_carnot_efficiency(t_hot, t_cold):
    """
    Calculate the Carnot efficiency for an ideal heat engine.
    
    Formula: η = 1 - (Tc/Th)
    
    Args:
        t_hot (float): Temperature of hot reservoir in Kelvin
        t_cold (float): Temperature of cold reservoir in Kelvin
    
    Returns:
        float: Carnot efficiency (0 to 1, expressed as decimal)
    
    Raises:
        ValueError: If temperatures are invalid
    """
    # Validate inputs
    if t_hot <= 0 or t_cold < 0:
        raise ValueError("Temperatures must be positive (in Kelvin)")
    
    if t_cold >= t_hot:
        raise ValueError("Cold reservoir temperature must be less than hot reservoir temperature")
    
    # Calculate efficiency
    efficiency = 1 - (t_cold / t_hot)
    
    return efficiency


def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin"""
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius"""
    return kelvin - 273.15


def calculate_waste_energy(total_energy, efficiency):
    """
    Calculate waste energy (heat rejected).
    
    Args:
        total_energy (float): Total input energy
        efficiency (float): Engine efficiency (0 to 1)
    
    Returns:
        float: Waste energy (energy not converted to work)
    """
    return total_energy * (1 - efficiency)


def calculate_work_output(total_energy, efficiency):
    """
    Calculate work output of the engine.
    
    Args:
        total_energy (float): Total input energy
        efficiency (float): Engine efficiency (0 to 1)
    
    Returns:
        float: Useful work output
    """
    return total_energy * efficiency

