# 🔥 Carnot Efficiency Calculator

An interactive web application demonstrating the Second Law of Thermodynamics through the Carnot cycle, for my PHYC-202 physics project!

## Project Overview

This Streamlit web app helps visualize and understand:
- **Carnot Efficiency**: The theoretical maximum efficiency of any heat engine
- **Formula**: η = 1 - (T_cold / T_hot)
- **Real-World Applications**: Comparison of ideal vs actual engine efficiencies

## Installation

```bash
pip install -r requirements.txt
```

## Running the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Features

### Core Functionality
- ✅ Interactive temperature sliders (Kelvin/Celsius)
- ✅ Real-time efficiency calculation with live metrics
- ✅ Color-coded efficiency interpretation (Excellent/Good/Moderate/Low ranges)
- ✅ Real-world engine comparisons with visual progress bars
- ✅ CSV export functionality

### Enhanced Visualizations
- ✅ **P-V Diagram**: Interactive visualization with process annotations
  - Shows all four Carnot cycle processes with labels
  - Highlights heat absorption and rejection
  - Educational arrows explaining each step
- ✅ **Energy Flow Diagram**: Sankey diagram showing energy conversion
  - Visual representation of useful work vs waste heat
  - Adjustable energy input with helpful tooltips
- ✅ **Creator's Note**: Comprehensive explanation of the Second Law

### Real-World Context
- ✅ Detailed comparison tables for car engines, power plants, and diesel engines
- ✅ Shows Carnot limit vs actual efficiency percentages
- ✅ Displays how close real engines are to theoretical maximum

## Physics Concept

The Carnot efficiency demonstrates why 100% efficient engines are physically impossible. 
Even an ideal engine must reject waste heat to the cold reservoir, limited by the Second Law of Thermodynamics.

---

**Assignment**: Physics 202 - Creative Application Project