import streamlit as st
from main import Bank

bank = Bank()

st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox(
    "Select Option",
    ["Create Account", "Deposit", "Withdraw", "Check Details", "Update Details", "Delete Account"]
)

# ---------- Create ----------
if menu == "Create Account":
    st.header("Create Account")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, step=1)
    email = st.text_input("Email")
    pin = st.text_input("PIN", type="password")

    if st.button("Create"):
        result = bank.create_account(name, age, email, int(pin))
        st.success(result)

# ---------- Deposit ----------
elif menu == "Deposit":
    st.header("Deposit Money")

    acc = st.number_input("Account Number", step=1)
    pin = st.text_input("PIN", type="password")
    amt = st.number_input("Amount", step=1)

    if st.button("Deposit"):
        res = bank.deposit(int(acc), int(pin), amt)
        st.success(res)

# ---------- Withdraw ----------
elif menu == "Withdraw":
    st.header("Withdraw Money")

    acc = st.number_input("Account Number", step=1)
    pin = st.text_input("PIN", type="password")
    amt = st.number_input("Amount", step=1)

    if st.button("Withdraw"):
        res = bank.withdraw(int(acc), int(pin), amt)
        st.success(res)

# ---------- Details ----------
elif menu == "Check Details":
    st.header("Account Details")

    acc = st.number_input("Account Number", step=1)
    pin = st.text_input("PIN", type="password")

    if st.button("Check"):
        user = bank.details(int(acc), int(pin))
        if user:
            st.json(user)
        else:
            st.error("Invalid credentials")

# ---------- Update ----------
elif menu == "Update Details":
    st.header("Update Details")

    acc = st.number_input("Account Number", step=1)
    pin = st.text_input("Old PIN", type="password")
    name = st.text_input("New Name (optional)")
    email = st.text_input("New Email (optional)")
    new_pin = st.text_input("New PIN (optional)", type="password")

    if st.button("Update"):
        res = bank.update_details(acc, int(pin), name, email, new_pin)
        st.success(res)

# ---------- Delete ----------
elif menu == "Delete Account":
    st.header("Delete Account")

    acc = st.number_input("Account Number", step=1)
    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):
        res = bank.delete(acc, int(pin))
        st.warning(res)