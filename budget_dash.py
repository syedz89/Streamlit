import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="Budget Dashboard", layout="wide")

# Initialize session state for monthly data storage
if 'monthly_data' not in st.session_state:
    st.session_state.monthly_data = {}

# Header
st.title("📊 Budget Dashboard")
selected_month = st.selectbox("Select Month", ["January", "February", "March", "April", "May", "June", 
                                       "July", "August", "September", "October", "November", "December"])

# Initialize data for selected month if it doesn't exist
if selected_month not in st.session_state.monthly_data:
    st.session_state.monthly_data[selected_month] = {
        'income_data': [],
        'expenses_data': [],
        'bills_data': [],
        'savings_data': [],
        'debt': 0.0
    }

# Get current month's data
current_data = st.session_state.monthly_data[selected_month]

# Tabs for data entry
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["📈 Dashboard", "💰 Income", "🛒 Expenses", "📄 Bills", "💵 Savings", "💳 Debt"])

# Income Tab
with tab2:
    st.header(f"Income - {selected_month}")
    with st.form("income_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            income_category = st.text_input("Category", key="income_cat")
        with col2:
            income_budgeted = st.number_input("Budgeted Amount", min_value=0.0, step=100.0, key="income_bud")
        with col3:
            income_actual = st.number_input("Actual Amount", min_value=0.0, step=100.0, key="income_act")
        
        if st.form_submit_button("Add Income"):
            if income_category:
                current_data['income_data'].append({
                    'category': income_category,
                    'budgeted': income_budgeted,
                    'actual': income_actual
                })
                st.success(f"Added {income_category}")
                st.rerun()
    
    if current_data['income_data']:
        st.subheader("Current Income Items")
        for idx, item in enumerate(current_data['income_data']):
            col1, col2, col3, col4 = st.columns([3, 2, 2, 1])
            with col1:
                st.write(f"**{item['category']}**")
            with col2:
                st.write(f"Budgeted: ${item['budgeted']:,.2f}")
            with col3:
                st.write(f"Actual: ${item['actual']:,.2f}")
            with col4:
                if st.button("🗑️", key=f"del_income_{idx}"):
                    current_data['income_data'].pop(idx)
                    st.rerun()
        
        st.markdown("---")
        if st.button("Clear All Income Data"):
            current_data['income_data'] = []
            st.rerun()

# Expenses Tab
with tab3:
    st.header(f"Expenses - {selected_month}")
    with st.form("expenses_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            expense_category = st.text_input("Category", key="expense_cat")
        with col2:
            expense_budgeted = st.number_input("Budgeted Amount", min_value=0.0, step=50.0, key="expense_bud")
        with col3:
            expense_actual = st.number_input("Actual Amount", min_value=0.0, step=50.0, key="expense_act")
        
        if st.form_submit_button("Add Expense"):
            if expense_category:
                progress = (expense_actual / expense_budgeted * 100) if expense_budgeted > 0 else 0
                current_data['expenses_data'].append({
                    'category': expense_category,
                    'budgeted': expense_budgeted,
                    'actual': expense_actual,
                    'progress': round(progress, 1)
                })
                st.success(f"Added {expense_category}")
                st.rerun()
    
    if current_data['expenses_data']:
        st.subheader("Current Expense Items")
        for idx, item in enumerate(current_data['expenses_data']):
            col1, col2, col3, col4, col5 = st.columns([3, 2, 2, 1, 1])
            with col1:
                st.write(f"**{item['category']}**")
            with col2:
                st.write(f"Budgeted: ${item['budgeted']:,.2f}")
            with col3:
                st.write(f"Actual: ${item['actual']:,.2f}")
            with col4:
                st.write(f"{item['progress']}%")
            with col5:
                if st.button("🗑️", key=f"del_expense_{idx}"):
                    current_data['expenses_data'].pop(idx)
                    st.rerun()
        
        st.markdown("---")
        if st.button("Clear All Expenses Data"):
            current_data['expenses_data'] = []
            st.rerun()

# Bills Tab
with tab4:
    st.header(f"Bills - {selected_month}")
    with st.form("bills_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            bill_category = st.text_input("Category", key="bill_cat")
        with col2:
            bill_budgeted = st.number_input("Budgeted Amount", min_value=0.0, step=25.0, key="bill_bud")
        with col3:
            bill_actual = st.number_input("Actual Amount", min_value=0.0, step=25.0, key="bill_act")
        
        if st.form_submit_button("Add Bill"):
            if bill_category:
                progress = (bill_actual / bill_budgeted * 100) if bill_budgeted > 0 else 0
                current_data['bills_data'].append({
                    'category': bill_category,
                    'budgeted': bill_budgeted,
                    'actual': bill_actual,
                    'progress': round(progress, 1)
                })
                st.success(f"Added {bill_category}")
                st.rerun()
    
    if current_data['bills_data']:
        st.subheader("Current Bill Items")
        for idx, item in enumerate(current_data['bills_data']):
            col1, col2, col3, col4, col5 = st.columns([3, 2, 2, 1, 1])
            with col1:
                st.write(f"**{item['category']}**")
            with col2:
                st.write(f"Budgeted: ${item['budgeted']:,.2f}")
            with col3:
                st.write(f"Actual: ${item['actual']:,.2f}")
            with col4:
                st.write(f"{item['progress']}%")
            with col5:
                if st.button("🗑️", key=f"del_bill_{idx}"):
                    current_data['bills_data'].pop(idx)
                    st.rerun()
        
        st.markdown("---")
        if st.button("Clear All Bills Data"):
            current_data['bills_data'] = []
            st.rerun()

# Savings Tab
with tab5:
    st.header(f"Savings - {selected_month}")
    with st.form("savings_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            saving_category = st.text_input("Category", key="saving_cat")
        with col2:
            saving_budgeted = st.number_input("Budgeted Amount", min_value=0.0, step=100.0, key="saving_bud")
        with col3:
            saving_actual = st.number_input("Actual Amount", min_value=0.0, step=100.0, key="saving_act")
        
        if st.form_submit_button("Add Savings Goal"):
            if saving_category:
                progress = (saving_actual / saving_budgeted * 100) if saving_budgeted > 0 else 0
                current_data['savings_data'].append({
                    'category': saving_category,
                    'budgeted': saving_budgeted,
                    'actual': saving_actual,
                    'progress': round(progress, 1)
                })
                st.success(f"Added {saving_category}")
                st.rerun()
    
    if current_data['savings_data']:
        st.subheader("Current Savings Items")
        for idx, item in enumerate(current_data['savings_data']):
            col1, col2, col3, col4, col5 = st.columns([3, 2, 2, 1, 1])
            with col1:
                st.write(f"**{item['category']}**")
            with col2:
                st.write(f"Budgeted: ${item['budgeted']:,.2f}")
            with col3:
                st.write(f"Actual: ${item['actual']:,.2f}")
            with col4:
                st.write(f"{item['progress']}%")
            with col5:
                if st.button("🗑️", key=f"del_saving_{idx}"):
                    current_data['savings_data'].pop(idx)
                    st.rerun()
        
        st.markdown("---")
        if st.button("Clear All Savings Data"):
            current_data['savings_data'] = []
            st.rerun()

# Debt Tab
with tab6:
    st.header(f"Debt - {selected_month}")
    debt_amount = st.number_input("Total Debt Payment", min_value=0.0, step=100.0, value=current_data['debt'])
    if st.button("Update Debt"):
        current_data['debt'] = debt_amount
        st.success(f"Debt updated to ${debt_amount:,.2f}")

# Dashboard Tab
with tab1:
    st.header(f"Dashboard - {selected_month}")
    
    # Calculate totals
    total_income = sum(item['actual'] for item in current_data['income_data'])
    total_expenses = sum(item['actual'] for item in current_data['expenses_data'])
    total_bills = sum(item['actual'] for item in current_data['bills_data'])
    total_savings = sum(item['actual'] for item in current_data['savings_data'])
    total_debt = current_data['debt']
    
    left_to_spend = total_income - total_expenses - total_bills - total_savings - total_debt
    
    # Top Summary Cards
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("💰 Income", f"${total_income:,.2f}")
    with col2:
        st.metric("🛒 Expenses", f"${total_expenses:,.2f}")
    with col3:
        st.metric("📄 Bills", f"${total_bills:,.2f}")
    with col4:
        st.metric("💵 Savings", f"${total_savings:,.2f}")
    with col5:
        st.metric("💳 Debt", f"${total_debt:,.2f}")
    
    st.markdown("---")
    
    # Charts Row
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Amount Left to Spend")
        color = "green" if left_to_spend >= 0 else "red"
        st.markdown(f"<h1 style='text-align: center; color: {color};'>${left_to_spend:,.2f}</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Available</p>", unsafe_allow_html=True)
    
    with col2:
        st.subheader("Cash Flow Summary")
        if total_income > 0 or total_expenses > 0:
            cash_flow_data = pd.DataFrame({
                'Category': ['Income', 'Expenses', 'Bills', 'Savings', 'Debt'],
                'Amount': [total_income, total_expenses, total_bills, total_savings, total_debt]
            })
            fig = px.bar(cash_flow_data, y='Category', x='Amount', orientation='h',
                        color_discrete_sequence=['#C5B8E0'])
            fig.update_layout(height=300, showlegend=False)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Add income and expenses to see chart")
    
    with col3:
        st.subheader("Allocation Summary")
        if total_expenses > 0 or total_bills > 0 or total_savings > 0 or total_debt > 0:
            allocation_data = pd.DataFrame({
                'Category': ['Expenses', 'Bills', 'Savings', 'Debt'],
                'Amount': [total_expenses, total_bills, total_savings, total_debt]
            })
            allocation_data = allocation_data[allocation_data['Amount'] > 0]
            fig = px.pie(allocation_data, values='Amount', names='Category',
                        color_discrete_sequence=['#E8D5F2', '#D4C5E8', '#C5B8E0', '#B8A8D8'])
            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Add data to see allocation chart")
    
    st.markdown("---")
    
    # Detailed Tables
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Income Details")
        if current_data['income_data']:
            df_income_display = pd.DataFrame(current_data['income_data'])
            df_income_display['budgeted'] = df_income_display['budgeted'].apply(lambda x: f"${x:,.2f}")
            df_income_display['actual'] = df_income_display['actual'].apply(lambda x: f"${x:,.2f}")
            st.dataframe(df_income_display, use_container_width=True, hide_index=True)
        else:
            st.info("No income data added yet")
        
        st.subheader("Bills Details")
        if current_data['bills_data']:
            df_bills_display = pd.DataFrame(current_data['bills_data'])
            df_bills_display['budgeted'] = df_bills_display['budgeted'].apply(lambda x: f"${x:,.2f}")
            df_bills_display['actual'] = df_bills_display['actual'].apply(lambda x: f"${x:,.2f}")
            df_bills_display['progress'] = df_bills_display['progress'].apply(lambda x: f"{x}%")
            st.dataframe(df_bills_display, use_container_width=True, hide_index=True)
        else:
            st.info("No bills data added yet")
    
    with col2:
        st.subheader("Expenses Details")
        if current_data['expenses_data']:
            df_expenses_display = pd.DataFrame(current_data['expenses_data'])
            df_expenses_display['budgeted'] = df_expenses_display['budgeted'].apply(lambda x: f"${x:,.2f}")
            df_expenses_display['actual'] = df_expenses_display['actual'].apply(lambda x: f"${x:,.2f}")
            df_expenses_display['progress'] = df_expenses_display['progress'].apply(lambda x: f"{x}%")
            st.dataframe(df_expenses_display, use_container_width=True, hide_index=True)
        else:
            st.info("No expenses data added yet")
        
        st.subheader("Savings Details")
        if current_data['savings_data']:
            df_savings_display = pd.DataFrame(current_data['savings_data'])
            df_savings_display['budgeted'] = df_savings_display['budgeted'].apply(lambda x: f"${x:,.2f}")
            df_savings_display['actual'] = df_savings_display['actual'].apply(lambda x: f"${x:,.2f}")
            df_savings_display['progress'] = df_savings_display['progress'].apply(lambda x: f"{x}%")
            st.dataframe(df_savings_display, use_container_width=True, hide_index=True)
        else:
            st.info("No savings data added yet")

# Footer
st.markdown("---")
st.caption("💡 Tip: Switch between months using the dropdown at the top. Each month has its own budget data!")