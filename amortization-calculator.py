import numpy_financial as npf
import pandas as pd
import numpy as np
import math
import streamlit as st

# Streamlit app title
st.title('Amortization Calculator')

# Input Variables using Streamlit widgets
principal = st.number_input("Enter the Principal (e.g., 100000 for $100,000): ", min_value=0, value=100000)
rate = st.number_input("Enter the Annual Interest Rate (e.g., 0.02 for 2%): ", min_value=0.0, value=0.04, step=0.01)
years = st.number_input("Enter the Term in Number of Years (e.g., 30 for 30 years): ", min_value=0, value=30)

# Calculate the number of months in the loan
monthNo = years * 12

# Calculate the fixed monthly payment
fixedPayment = (principal * (rate / 12) * (math.pow(1 + rate / 12, monthNo))) / (math.pow(1 + rate / 12, monthNo) - 1)

# Display the fixed payment amount
st.write(f'Your Fixed Monthly Payment: ${fixedPayment:.2f}')

# Initialize data storage for the amortization schedule
amortization_schedule = []

newPrincipal = principal
unpaidPrincipalBalance = principal

# Generate amortization table
for i in range(1, monthNo + 1):
    interestApplied = rate / 12 * newPrincipal
    principalToPay = fixedPayment - interestApplied
    unpaidPrincipalBalance = newPrincipal + interestApplied - fixedPayment
    
    # Append to amortization schedule
    amortization_schedule.append([i, newPrincipal, interestApplied, principalToPay, fixedPayment, unpaidPrincipalBalance])
    
    # Update the new principal for the next month
    newPrincipal = unpaidPrincipalBalance

# Convert the amortization schedule to a DataFrame
amortization_df = pd.DataFrame(amortization_schedule, columns=['Month Number', 'New Principal', 'Interest Applied', 'Principal Paydown', 'Fixed Payment', 'Unpaid Principal Balance'])

# Display the amortization table
st.subheader("Amortization Schedule")
st.dataframe(amortization_df)

# Add download option for the amortization schedule as a CSV
csv = amortization_df.to_csv(index=False)
st.download_button(label="Download Amortization Schedule as CSV", data=csv, file_name='amortization_schedule.csv', mime='text/csv')
