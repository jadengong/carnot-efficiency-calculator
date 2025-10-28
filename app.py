"""
Carnot Efficiency Calculator
An interactive web app demonstrating the Second Law of Thermodynamics
"""

import streamlit as st
from carnot_calculator import (
    calculate_carnot_efficiency,
    celsius_to_kelvin,
    kelvin_to_celsius
)

# Page configuration
st.set_page_config(
    page_title="Carnot Efficiency Calculator",
    page_icon="🔥",
    layout="wide"
)

# Title and header
st.title("🔥 Carnot Efficiency Calculator")
st.subheader("Understanding the Maximum Possible Engine Efficiency")

# Add a brief explanation
st.info("""
💡 **What is Carnot Efficiency?** The Carnot efficiency represents the maximum theoretical 
efficiency that any heat engine can achieve. It's given by: **η = 1 - (T_cold / T_hot)**
""")

# Input section
col1, col2 = st.columns(2)

with col1:
    st.header("🌡️ Temperature Controls")
    
    # Temperature input
    temp_choice = st.radio(
        "Temperature Unit:",
        ["Kelvin", "Celsius"],
        horizontal=True
    )
    
    if temp_choice == "Kelvin":
        t_hot = st.slider(
            "Hot Reservoir Temperature (K)",
            min_value=273,  # 0°C
            max_value=2000,
            value=873,  # ~600°C (typical power plant)
            step=10
        )
        
        t_cold = st.slider(
            "Cold Reservoir Temperature (K)",
            min_value=273,  # 0°C
            max_value=400,
            value=298,  # ~25°C (room temperature)
            step=5
        )
    else:
        t_hot_celsius = st.slider(
            "Hot Reservoir Temperature (°C)",
            min_value=0,
            max_value=1700,
            value=600,
            step=10
        )
        
        t_cold_celsius = st.slider(
            "Cold Reservoir Temperature (°C)",
            min_value=-50,
            max_value=100,
            value=25,
            step=5
        )
        
        t_hot = celsius_to_kelvin(t_hot_celsius)
        t_cold = celsius_to_kelvin(t_cold_celsius)

with col2:
    st.header("📊 Results")
    
    try:
        # Calculate efficiency
        efficiency = calculate_carnot_efficiency(t_hot, t_cold)
        efficiency_percent = efficiency * 100
        
        # Display results
        st.metric(
            label="Carnot Efficiency",
            value=f"{efficiency_percent:.2f}%"
        )
        
        st.metric(
            label="Temperature Ratio (T_cold/T_hot)",
            value=f"{t_cold/t_hot:.3f}"
        )
        
        # Visual gauge using progress bar
        st.subheader("Efficiency Visualization")
        st.progress(efficiency)
        
        # Additional info
        with st.expander("💡 What does this mean?"):
            st.write(f"""
            At these temperatures:
            - Hot reservoir: {t_hot:.1f} K ({t_hot_celsius if temp_choice == "Celsius" else kelvin_to_celsius(t_hot):.1f}°C)
            - Cold reservoir: {t_cold:.1f} K ({t_cold_celsius if temp_choice == "Celsius" else kelvin_to_celsius(t_cold):.1f}°C)
            
            **Maximum possible efficiency:** {efficiency_percent:.2f}%
            
            This means that in the BEST possible scenario, only {efficiency_percent:.2f}% 
            of heat energy can be converted to useful work. The remaining 
            {100-efficiency_percent:.2f}% must be rejected as waste heat.
            """)
    
    except ValueError as e:
        st.error(f"❌ Error: {e}")

# Real-world context
st.divider()
st.subheader("🌍 Real-World Context")

real_world_data = {
    "Car Engine (Gasoline)": {"hot": celsius_to_kelvin(600), "cold": celsius_to_kelvin(60), "actual_eff": 0.25},
    "Power Plant (Steam)": {"hot": celsius_to_kelvin(700), "cold": celsius_to_kelvin(40), "actual_eff": 0.35},
    "Diesel Engine": {"hot": celsius_to_kelvin(650), "cold": celsius_to_kelvin(80), "actual_eff": 0.30},
}

for engine_name, data in real_world_data.items():
    try:
        carnot_eff = calculate_carnot_efficiency(data["hot"], data["cold"])
        actual_eff = data["actual_eff"]
        gap = carnot_eff - actual_eff
        
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.write(f"**{engine_name}**")
        with col_b:
            st.write(f"Carnot: {carnot_eff*100:.1f}% | Actual: {actual_eff*100:.1f}%")
        with col_c:
            st.write(f"Gap: {gap*100:.1f}% due to real-world losses")
    except ValueError:
        continue

st.caption("""
Note: Actual engine efficiencies are always lower than Carnot efficiency due to friction, 
heat losses, and other irreversibilities in real engines.
""")

