import numpy_financial as npf
import pandas as pd
import math
import pandas as pd
import streamlit as st

# Streamlit app setup
st.title("Collins Amortization Calculator")
st.write("""
This tool helps you calculate the amortization schedule of a loan by providing the details for each monthly payment.
The schedule includes the principal, interest applied, and unpaid principal balance for every month.
""")

# Input fields in Streamlit
st.sidebar.header("Enter Loan Details")
principal = st.sidebar.number_input("Principal Amount ($)", min_value=1000, value=10000, step=500)
rate = st.sidebar.number_input("Annual Interest Rate (%)", min_value=0.1, value=2.0, step=0.1) / 100  # Convert to decimal
term_years = st.sidebar.number_input("Loan Term (Years)", min_value=1, value=2, step=1)

# Display inputs
st.write(f"**Principal:** ${principal}")
st.write(f"**Annual Interest Rate:** {rate * 100:.2f}%")
st.write(f"**Term:** {term_years} years")

# Calculations
monthNo = term_years * 12
fixedPayment = (principal * (rate / 12) * (math.pow(1 + rate / 12, 12 * term_years))) / \
               (math.pow(1 + rate / 12, 12 * term_years) - 1)

# Store the amortization schedule in a list
schedule = []
newPrincipal = principal
tolerance = 0.01  # Tolerance for floating-point precision errors

for i in range(1, monthNo + 1):
    interestApplied = rate / 12 * newPrincipal
    principalToPay = fixedPayment - interestApplied
    unpaidPrincipalBalance = newPrincipal + interestApplied - fixedPayment
    
    # Apply tolerance check for the last month
    if i == monthNo:
        unpaidPrincipalBalance = 0.00
    
    # Append to the schedule
    schedule.append([i, newPrincipal, interestApplied, principalToPay, fixedPayment, unpaidPrincipalBalance])
    
    newPrincipal = unpaidPrincipalBalance

# Create a DataFrame to display the amortization schedule
df_schedule = pd.DataFrame(schedule, columns=[
    'Month Number', 'New Principal', 'Interest Applied', 'Principal Paydown', 'Fixed Payment', 'Unpaid Principal Balance'
])

# Display the schedule
st.write("### Amortization Schedule")
st.dataframe(df_schedule.style.format({
    'New Principal': '${:,.2f}',
    'Interest Applied': '${:,.2f}',
    'Principal Paydown': '${:,.2f}',
    'Fixed Payment': '${:,.2f}',
    'Unpaid Principal Balance': '${:,.2f}'
}), height=300)

# Summary Information
st.write("### Loan Summary")
st.write(f"- **Total Payments:** {int(monthNo)} months")
st.write(f"- **Fixed Monthly Payment:** ${fixedPayment:,.2f}")
st.write(f"- **Total Interest Paid:** ${df_schedule['Interest Applied'].sum():,.2f}")
st.write(f"- **Total Amount Paid:** ${fixedPayment * monthNo:,.2f}")

# Add a plot of the unpaid principal balance over time
st.write("### Unpaid Principal Balance Over Time")
st.line_chart(df_schedule['Unpaid Principal Balance'])

# Add a download button for the amortization schedule as CSV
csv = df_schedule.to_csv(index=False)
st.download_button(
    label="Download Amortization Schedule as CSV",
    data=csv,
    file_name='amortization_schedule.csv',
    mime='text/csv'
)

# Style enhancements for better visualization
st.markdown("""
<style>
    .sidebar .sidebar-content {
        background-color: #f5f5f5;
    }
    .main {
        font-family: 'Arial', sans-serif;
    }
    h1 {
        color: #2c3e50;
    }
    h2, h3 {
        color: #34495e;
    }
</style>
""", unsafe_allow_html=True)
