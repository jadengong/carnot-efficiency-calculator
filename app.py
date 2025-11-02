"""
Carnot Efficiency Calculator
An interactive web app demonstrating the Second Law of Thermodynamics
"""

import streamlit as st
import numpy as np
import plotly.graph_objects as go
from carnot_calculator import (
    calculate_carnot_efficiency,
    celsius_to_kelvin,
    kelvin_to_celsius,
    calculate_waste_energy,
    calculate_work_output
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
            min_value=0,
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
        
        # Add color-coded efficiency interpretation
        if efficiency >= 0.7:
            st.success("🔥 Excellent efficiency range (≥70%) - requires very high temperatures")
        elif efficiency >= 0.5:
            st.info("⚡ Good efficiency range (50-70%) - typical for modern power plants")
        elif efficiency >= 0.3:
            st.warning("⚠️ Moderate efficiency range (30-50%) - typical for car engines")
        else:
            st.error("📉 Low efficiency range (<30%) - practical limitations")
        
        # Visualizations moved to full-width section below
        
        # Export results
        st.download_button(
            label="Download results as CSV",
            data=(
                f"metric,value\n"
                f"T_hot_K,{t_hot:.2f}\n"
                f"T_cold_K,{t_cold:.2f}\n"
                f"Efficiency_percent,{efficiency_percent:.2f}\n"
            ),
            file_name="carnot_results.csv",
            mime="text/csv"
        )
        
    
    except ValueError as e:
        st.error(f"❌ Error: {e}")

"""
Full-width contextual explanation to avoid stretching the two-column layout
when expanded.
"""
with st.expander("💡 What does this mean?"):
    try:
        efficiency = calculate_carnot_efficiency(t_hot, t_cold)
        efficiency_percent = efficiency * 100
        st.write(f"""
        At these temperatures:
        - Hot reservoir: {t_hot:.1f} K ({t_hot_celsius if temp_choice == "Celsius" else kelvin_to_celsius(t_hot):.1f}°C)
        - Cold reservoir: {t_cold:.1f} K ({t_cold_celsius if temp_choice == "Celsius" else kelvin_to_celsius(t_cold):.1f}°C)
        
        **Maximum possible efficiency:** {efficiency_percent:.2f}%
        
        This means that in the BEST possible scenario, only {efficiency_percent:.2f}% 
        of heat energy can be converted to useful work. The remaining 
        {100-efficiency_percent:.2f}% must be rejected as waste heat.
        """)
    except Exception:
        st.write("Set valid temperatures to see the detailed explanation.")

# Visualizations & Extras (full-width below the two columns)
st.divider()
st.subheader("🧪 Visualizations & Extras")

tab1, tab2, tab3 = st.tabs(["P–V Diagram", "Energy Flow", "Creator's Note"])

with tab1:
    st.markdown("**Idealized Carnot Cycle in the P–V Plane**")

    try:
        # Parameters for the ideal gas model (relative scale)
        n_moles = 1.0
        R = 8.314
        gamma = 1.4  # diatomic-like working fluid

        # Define state 1 on the hot isotherm
        V1 = 1.0
        P1 = (n_moles * R * t_hot) / V1

        # Choose an isothermal expansion ratio on the hot leg
        expansion_ratio = 2.0
        V2 = V1 * expansion_ratio
        P2 = (n_moles * R * t_hot) / V2

        # Adiabatic expansion from state 2 (Th) to state 3 (Tc)
        # T * V^(gamma-1) = const ⇒ V3 = V2 * (Th/Tc)^(1/(gamma-1))
        V3 = V2 * (t_hot / t_cold) ** (1.0 / (gamma - 1.0))
        P3 = (n_moles * R * t_cold) / V3

        # Isothermal compression at Tc from 3 to 4
        # Determine V4 so that the closing adiabatic 4→1 returns to (Th, V1)
        V4 = V1 * (t_hot / t_cold) ** (1.0 / (gamma - 1.0))
        P4 = (n_moles * R * t_cold) / V4

        # Generate curves for each leg
        # 1→2: isothermal at Th
        V_12 = np.linspace(V1, V2, 200)
        P_12 = (n_moles * R * t_hot) / V_12

        # 2→3: adiabatic (P * V^gamma = const)
        C23 = P2 * (V2 ** gamma)
        V_23 = np.linspace(V2, V3, 200)
        P_23 = C23 / (V_23 ** gamma)

        # 3→4: isothermal at Tc
        V_34 = np.linspace(V3, V4, 200)
        P_34 = (n_moles * R * t_cold) / V_34

        # 4→1: adiabatic back to state 1
        C41 = P4 * (V4 ** gamma)
        V_41 = np.linspace(V4, V1, 200)
        P_41 = C41 / (V_41 ** gamma)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=V_12, y=P_12, mode="lines", name="Isothermal (Th)", line=dict(color="#e74c3c")))
        fig.add_trace(go.Scatter(x=V_23, y=P_23, mode="lines", name="Adiabatic (↓T)", line=dict(color="#3498db", dash="dash")))
        fig.add_trace(go.Scatter(x=V_34, y=P_34, mode="lines", name="Isothermal (Tc)", line=dict(color="#2ecc71")))
        fig.add_trace(go.Scatter(x=V_41, y=P_41, mode="lines", name="Adiabatic (↑T)", line=dict(color="#9b59b6", dash="dash")))

        # Mark states
        fig.add_trace(go.Scatter(x=[V1, V2, V3, V4], y=[P1, P2, P3, P4], mode="markers+text",
                                 text=["1", "2", "3", "4"], textposition="top center",
                                 marker=dict(size=8, color="#34495e"), name="States"))

        fig.update_layout(
            xaxis_title="Volume (relative units)",
            yaxis_title="Pressure (relative units)",
            template="plotly_white",
            showlegend=True,
            height=450,
            hovermode='closest'
        )
        
        # Add annotations for each process
        annotations = [
            dict(x=V1*1.05, y=P1, text="1→2: Heat absorbed (Q_in)", showarrow=True, arrowhead=2, ax=0, ay=-30),
            dict(x=V2*1.05, y=P2*0.85, text="2→3: Adiabatic expansion", showarrow=True, arrowhead=2, ax=0, ay=-20),
            dict(x=V3*0.95, y=P3*1.1, text="3→4: Heat rejected (Q_out)", showarrow=True, arrowhead=2, ax=0, ay=30),
            dict(x=V4*0.95, y=P4, text="4→1: Adiabatic compression", showarrow=True, arrowhead=2, ax=0, ay=20)
        ]
        fig.update_layout(annotations=annotations)

        st.plotly_chart(fig, use_container_width=True)

        st.caption("Curve uses relative units; shape illustrates the ideal Carnot sequence: hot isotherm → adiabatic expansion → cold isotherm → adiabatic compression.")
    except Exception as e:
        st.warning(f"Could not render P–V diagram: {e}")

with tab2:
    st.markdown("**Energy Flow for Chosen Temperatures**")

    try:
        col_e1, col_e2 = st.columns([1, 2])
        with col_e1:
            st.markdown("##### Input Configuration")
            total_energy_in = st.number_input(
                "Total heat input Q_hot (J)",
                min_value=0.0,
                value=1000.0,
                step=50.0,
                format="%.2f",
                help="Total thermal energy input to the engine"
            )

        with col_e2:
            efficiency = calculate_carnot_efficiency(t_hot, t_cold)
            work_out = calculate_work_output(total_energy_in, efficiency)
            waste_heat = calculate_waste_energy(total_energy_in, efficiency)

            st.metric("Theoretical Work Output (W)", f"{work_out:.2f} J")
            st.metric("Waste Heat Rejected (Q_cold)", f"{waste_heat:.2f} J")

            sankey_fig = go.Figure(data=[go.Sankey(
                node=dict(
                    pad=15,
                    thickness=20,
                    line=dict(color="black", width=0.5),
                    label=["Heat In (Q_hot)", "Work (W)", "Waste Heat (Q_cold)"]
                ),
                link=dict(
                    source=[0, 0],
                    target=[1, 2],
                    value=[max(work_out, 0.0), max(waste_heat, 0.0)],
                    color=["#27ae60", "#e67e22"]
                )
            )])

            sankey_fig.update_layout(height=320, margin=dict(l=10, r=10, t=10, b=10))
            st.plotly_chart(sankey_fig, use_container_width=True)

        st.caption("At Carnot efficiency, all input heat splits into useful work and unavoidable waste heat.")
    except ValueError as e:
        st.error(f"Energy flow error: {e}")

with tab3:
    st.markdown("""
    **Creator's Note**
    
    **The Physics Concept: Carnot Efficiency and the Second Law of Thermodynamics**
    
    This calculator demonstrates and visualizes the **Carnot efficiency**, a fundamental limit in thermodynamics that 
    governs the maximum possible efficiency of any heat engine. The principle comes from the Second Law 
    of Thermodynamics, which states that entropy, or the measure of disorder in a system, can never decrease 
    in an isolated process. This law creates an absolute upper bound on how efficiently we can convert 
    heat into useful work.
    
    **How This Project Demonstrates It:**
    
    This interactive tool brings the Carnot efficiency formula **η = 1 - (T_cold / T_hot)** to life by 
    allowing you to manipulate the two key variables: the temperatures of the hot and cold reservoirs. 
    Through the P–V diagram, you can visualize the idealized Carnot cycle: a four-step reversible process 
    consisting of isothermal expansion, adiabatic expansion, isothermal compression, and adiabatic 
    compression. The energy flow diagram then shows how even this theoretically perfect engine must reject 
    a portion of its input heat as waste, regardless of engineering improvements. This impossibility of 
    100% efficiency is a fundamental constraint imposed by the universe itself.
    
    
    **Real-World Connection:**
    
    The Carnot efficiency has profound implications for our energy infrastructure. For example, a typical 
    car engine operates at only about 25% efficiency, while its Carnot limit might be around 35–40%. 
    Modern combined-cycle power plants, the most efficient fossil fuel systems, achieve about 55–60% 
    actual efficiency, approaching about 70% of their Carnot limit—but no engine can ever exceed it. 
    This reality drives research into higher operating temperatures (like in gas turbines) and lower 
    rejection temperatures (like in combined heat and power systems), as these are the only ways to 
    improve theoretical efficiency bounds. Understanding these limits helps engineers make informed 
    decisions about energy systems, recognizing when further optimization approaches diminishing returns 
    due to fundamental physics rather than technical limitations.
    
    Have fun exploring how raising the hot reservoir or lowering the cold one changes these absolute limits!
    """)

# Real-world context 
st.divider()
st.subheader("🌍 Real-World Context")

real_world_data = {
    "Car Engine (Gasoline)": {
        "hot": celsius_to_kelvin(600), 
        "cold": celsius_to_kelvin(60), 
        "actual_eff": 0.25,
        "icon": "🚗"
    },
    "Power Plant (Steam)": {
        "hot": celsius_to_kelvin(700), 
        "cold": celsius_to_kelvin(40), 
        "actual_eff": 0.35,
        "icon": "🏭"
    },
    "Diesel Engine": {
        "hot": celsius_to_kelvin(650), 
        "cold": celsius_to_kelvin(80), 
        "actual_eff": 0.30,
        "icon": "🚛"
    },
}

for engine_name, data in real_world_data.items():
    try:
        carnot_eff = calculate_carnot_efficiency(data["hot"], data["cold"])
        actual_eff = data["actual_eff"]
        gap = carnot_eff - actual_eff
        percent_of_carnot = (actual_eff / carnot_eff) * 100 if carnot_eff > 0 else 0
        
        with st.container():
            col_a, col_b, col_c, col_d = st.columns([2, 3, 2, 1.5])
            with col_a:
                st.markdown(f"### {data['icon']}")
                st.write(f"**{engine_name}**")
                st.caption(f"T_hot: {data['hot']:.0f} K | T_cold: {data['cold']:.0f} K")
            with col_b:
                st.write(f"**Carnot Limit:** {carnot_eff*100:.1f}%")
                st.write(f"**Actual Efficiency:** {actual_eff*100:.1f}%")
                st.write(f"**Achieving:** {percent_of_carnot:.1f}% of theoretical max")
            with col_c:
                st.progress(actual_eff / carnot_eff if carnot_eff > 0 else 0)
                st.caption(f"{gap*100:.1f}% gap from ideal")
            with col_d:
                st.write("")  # spacer
            st.divider()
    except ValueError:
        continue

st.info("💡 **Note:** Actual engine efficiencies are always lower than Carnot efficiency due to friction, heat losses, incomplete combustion, and other irreversibilities in real engines.")
