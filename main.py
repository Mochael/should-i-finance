import streamlit as st

MAX_INT = 1000000000000000

st.title("Should I Finance It?")

loan_amount = st.number_input(
     "How much is your loan for?",
     min_value=0, max_value=MAX_INT, value=100000)

loan_interest_rate = st.number_input(
     "What is the annual interest rate percentage (APR) on the loan (assuming fixed)?",
     min_value=0.0, max_value=100.0, value=8.0)
loan_interest_rate = loan_interest_rate/100

loan_length = st.number_input(
     "How long is the loan for (in years)?",
     min_value=0, max_value=100, value=10)

annual_growth_invest = st.number_input(
     "What is your estimated annual growth percentage by investing your money in the market?",
     min_value=0.0, max_value=100.0, value=5.0)
annual_growth_invest = annual_growth_invest/100

monthly_interest_rate = loan_interest_rate/12
total_cost = (loan_amount*monthly_interest_rate*12*loan_length)/(1-(1+monthly_interest_rate)**(-12*loan_length))

yearly_cost = total_cost/loan_length

gains_from_investing = 0
for t in range(1, loan_length+1):
    print("year", t, "gains", (loan_amount - t*yearly_cost)*((1+annual_growth_invest)**(loan_length-t)-1))
    gains_from_investing += (loan_amount - t*yearly_cost)*((1+annual_growth_invest)**(loan_length-t)-1)

st.title(f"Results")
st.markdown(f"By financing, you would save {'${:,.2f}'.format(gains_from_investing - total_cost)}.")
st.markdown(f"- Total Mortgage Cost: {'${:,.2f}'.format(total_cost)}.")
st.markdown(f"- Gains from Investing: {'${:,.2f}'.format(gains_from_investing)}.")