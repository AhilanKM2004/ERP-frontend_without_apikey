import streamlit as st
if "login" not in st.session_state:
    st.session_state.login = False

if st.session_state.login == False:
    st.page_link(label = "please login before the acion", page = "DASHBOARD.py" )


elif st.session_state.login == True:
    st.header("PRODUCT PAGE")
    products = [
    {"id": 101, "name": "fruit basket", "image": "https://i.pinimg.com/736x/9c/d5/bc/9cd5bcd17774460c382d1162840e2735.jpg"},
    {"id": 102, "name": "milk", "image": "https://i.pinimg.com/736x/4f/71/a5/4f71a52e88313fd0dc12664871937838.jpg"},
    {"id": 103, "name": "T shirt", "image": "https://i.pinimg.com/1200x/8b/f6/2e/8bf62edb1c05322a4d74921075c07275.jpg"},]

    if not "x" in st.session_state :
        st.session_state.x = False
   
    for p in products:
        with st.container(border=True):
            c1, c2 , c3 = st.columns(3)
            c1.image(p["image"], caption=p["name"], width=200)
            if c2.button("Select", key=f"select_{p['id']}"):
                st.session_state.x=True
                st.write("Selected product:", st.session_state.get("selected_product"))
                st.session_state.selected_product = p["id"]
    if st.session_state.x == True:
        st.session_state.num = st.number_input("enter the quantity",min_value=0)
        x=st.button("use my profile address for delivery details")
        if x and st.session_state.num!=0:
            st.success("success")
        elif x and st.session_state.num == 0:
            st.write("quantity cannot be zero") 
        button = st.button("reset")
        if button:
            st.rerun()
            
if st.session_state.login == True:
    if st.sidebar.button("LOG-OUT"):
        st.session_state.login = False

