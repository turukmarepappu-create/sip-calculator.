import streamlit as st

st.set_page_config(page_title="SIP Calculator", page_icon="💰")

st.title("💰 SIP Calculator")

# Inputs
monthly_investment = st.number_input("Monthly Investment (₹)", 1000, 100000, 5000, 500)
annual_rate = st.number_input("Expected Annual Return (%)", 1.0, 30.0, 12.0, 0.5)
years = st.number_input("Investment Duration (Years)", 1, 40, 10)

# Calculation
months = years * 12
monthly_rate = annual_rate / 12 / 100
future_value = monthly_investment * (((1 + monthly_rate)**months - 1) / monthly_rate) * (1 + monthly_rate)
total_invested = monthly_investment * months
returns = future_value - total_invested

# Output
st.subheader("📊 Results")
st.write(f"**Total Invested:** ₹{total_invested:,.2f}")
st.write(f"**Estimated Returns:** ₹{returns:,.2f}")
st.write(f"**Maturity Value:** ₹{future_value:,.2f}")
