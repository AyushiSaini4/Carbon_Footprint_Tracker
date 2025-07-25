import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="Carbon Footprint Tracker", layout="wide")

# Title and description
st.title("🌱 Personal Carbon Footprint Tracker")
st.markdown("""
This tool helps you estimate your monthly carbon footprint based on your lifestyle choices.
Simply fill in the fields below and you'll see your estimated CO₂ emissions.
""")

# Input form
with st.form("carbon_form"):
    st.subheader("🔧 Lifestyle Inputs")
    
    col1, col2 = st.columns(2)
    
    with col1:
        electricity_kwh = st.number_input("Monthly Electricity Usage (kWh)", min_value=0.0, value=200.0)
        gas_liters = st.number_input("Monthly Cooking Gas Usage (liters)", min_value=0.0, value=15.0)
        car_kms = st.number_input("Monthly Car Travel (km)", min_value=0.0, value=300.0)
    
    with col2:
        flights_per_month = st.number_input("Monthly Flights (short haul)", min_value=0, value=1)
        food_choice = st.selectbox("Food Habit", ["Vegetarian", "Non-Vegetarian", "Vegan"])
        shopping_spending = st.slider("Monthly Shopping Expenses (INR)", 0, 50000, 5000)

    submitted = st.form_submit_button("Calculate Footprint")

if submitted:
    with st.spinner("Calculating your carbon footprint..."):
        time.sleep(1)

        # Basic multipliers (can be updated with real-world accurate factors)
        footprint = {
            "Electricity": electricity_kwh * 0.85,
            "Cooking Gas": gas_liters * 2.95,
            "Car Travel": car_kms * 0.21,
            "Flights": flights_per_month * 250.0,
            "Shopping": shopping_spending * 0.005,
            "Food": {"Vegetarian": 80, "Non-Vegetarian": 220, "Vegan": 60}[food_choice]
        }

        total = sum(footprint.values())

        st.success(f"✅ Your estimated monthly carbon footprint is **{total:.2f} kg CO₂e**")

        st.subheader("🧾 Breakdown")
        df = pd.DataFrame(footprint.items(), columns=["Activity", "CO₂ Emissions (kg/month)"])
        st.dataframe(df.set_index("Activity"))

        st.subheader("📉 Chart")
        st.bar_chart(df.set_index("Activity"))

        st.markdown("---")
        st.markdown("Want to reduce your footprint? Start by minimizing unnecessary travel, eating more plant-based meals, and conserving electricity! 🌍")

