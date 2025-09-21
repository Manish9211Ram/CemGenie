import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ------------------------------
# Load trained models (mock or replace with your trained models)
# ------------------------------
try:
    quality_model = joblib.load("quality_model.pkl")  # Train separately and save
except:
    quality_model = None

st.set_page_config(page_title="CemGenie", layout="wide")

st.title("🏭 CemGenie")
st.markdown("""
Intelligence in Every Mix
""")

# ================================================
# 1. Energy Optimization
# ================================================
st.header("⚡ Feature 1: Energy Optimization")
st.markdown("Monitoring *energy vs CO₂ emissions* to suggest optimal plant actions.")

energy_kwh = st.number_input("Enter Total Energy Consumption (kWh)", min_value=1000, value=5000)
co2_tonnes = st.number_input("Enter Predicted CO₂ Emissions (tonnes)", min_value=1.0, value=25.0)

if co2_tonnes > 0:
    energy_co2_ratio = energy_kwh / co2_tonnes
    st.metric("Energy to CO₂ Ratio", f"{energy_co2_ratio:.2f}")

    if energy_co2_ratio > 300:
        st.success("✅ Efficient Operation: Maintain current settings.")
    else:
        st.warning("⚠ High Energy per CO₂: AI suggests adjusting blend or reducing kiln temperature.")

# ================================================
# 2. Quality Prediction
# ================================================
st.header("🔬 Feature 2: Quality Prediction")
st.markdown("AI predicts whether a cement batch will *Pass or Fail* quality standards.")

cao = st.slider("Calcium Oxide % (CaO)", 40, 70, 55)
silica = st.slider("Silica % (SiO₂)", 10, 30, 20)
alumina = st.slider("Alumina % (Al₂O₃)", 5, 20, 10)

input_df = pd.DataFrame([[cao, silica, alumina]], columns=["chemical_cao_pct", "silica_pct", "alumina_pct"])

if quality_model:
    pred = quality_model.predict(input_df)[0]
    if pred == 1:
        st.success("✅ Predicted Quality: PASS")
    else:
        st.error("❌ Predicted Quality: FAIL")
else:
    st.info("Demo Mode: If CaO > 50 and Silica > 15 → PASS, else FAIL.")
    if cao > 50 and silica > 15:
        st.success("✅ Predicted Quality: PASS")
    else:
        st.error("❌ Predicted Quality: FAIL")

# ================================================
# 3. Sustainability Insights
# ================================================
st.header("🌱 Feature 3: Sustainability Insights")
st.markdown("Explore kiln & cooling efficiency and their effect on sustainability.")

kiln_temp = st.slider("Kiln Temperature (°C)", 1000, 1600, 1450)
res_time = st.slider("Residence Time (min)", 10, 90, 45)
clinker_temp = st.slider("Clinker Exit Temp (°C)", 200, 900, 400)
cool_time = st.slider("Cooling Time (min)", 5, 60, 20)

temp_res_interaction = kiln_temp * res_time
temp_cooling_ratio = clinker_temp / (cool_time + 1e-9)

st.metric("🔥 Temp-Residence Interaction", f"{temp_res_interaction:.1f}")
st.metric("❄ Cooling Efficiency Ratio", f"{temp_cooling_ratio:.2f}")

if temp_res_interaction > 60000:
    st.warning("⚠ High energy usage in kiln. AI suggests optimizing feed blend.")
else:
    st.success("✅ Kiln efficiency within sustainable limits.")

if temp_cooling_ratio > 25:
    st.warning("⚠ Cooling too fast. May cause cracks in clinker.")
else:
    st.success("✅ Cooling efficiency is sustainable.")

# ================================================
# Footer
# ================================================
st.markdown("---")
st.markdown("🚀 Prototype integrates *Energy, Quality, and Sustainability* for autonomous cement operations.")