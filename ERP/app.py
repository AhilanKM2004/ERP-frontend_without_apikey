import streamlit as st
from groq import Groq
import pandas as pd

user = { "ahilan" :{"username":"ahilan","password":"a","email":"ahilan@gamil","role":"common","picture":"ahil.JPG","education":"ME", "phone" : "655225"},
        "ashik":{"username":"ashik","password":"ashik123","email":"kadayal@gamil","role":"common","picture":"vis.JPG","education":"B.E", "phone" : "76724543"},
        "libin":{"username":"libin","password":"libin123","email": "tiger@gamil","role":"common","picture":"vis.JPG","education":"B.E", "phone" : "464235"},
        "master":{"username":"master","password":"m","email": "mass@gamil","role":"admin","picture":"chriz.JPG","education":"B.E , M.E , Msc , Phd", "phone" : "94573424"},
        "sundar":{"username":"sundar","password":"s","email": "sundar@gamil","role":"admin","picture":"sa.JPG","education":"Msc", "phone" : "34245467"},}
st.session_state.totaluser = user

if "login" not in st.session_state:
    st.session_state.login = False
if st.session_state.login == False:   
    username=st.text_input("please enter your user name")
    password=st.text_input("please enter your password",type="password")
    if st.button("LOGIN into web page"):
        userdup=user.get(username)
        if userdup == None :
            st.write("wrong username bro")
        else :
            role = user[username]["role"]
            if userdup and password == userdup["password"]:
                st.session_state.login=True
                st.session_state.user = userdup
                st.session_state.role = role
                st.rerun()
                
            else:
                st.write("error , wrong password")

elif st.session_state.login == True and st.session_state.role == "admin":
    
    name=st.session_state.user
    actualname=name["username"]
    st.header("ERP DASHBOARD")
    st.subheader(f"""welcome {actualname}""")
    
    st.write("AI-Powered ERP Mini Dashboard")
    cc,cc2,cc3=st.columns(3)
    with cc2:
        st.subheader("OVERVIEW")
    st.write("-----------------------------------------------------------------")
    c1,c2,c3 = st.columns(3)
    with c1:
        st.subheader("INVENTORY")
        st.write("our inventory conisted of ai assissting data analysis and dynamic chart visualizer")
        st.page_link(label = ">>INVENTORY",page = "pages/INVENTORY.py")
    with c2:
        st.subheader("SALES")
        st.write("To check the sales details ,where you can find summarize of perfomance and more, click")
        st.page_link(label = ">>SALES" , page = "pages/SALES.py")
    with c3:
        st.subheader("PRODUCTS")
        st.write("To see the images of the product and details  , just go to product page")
        st.page_link(label = ">>PRODUCTS" , page = "pages/PRODUCTS.py")
    st.write("-----------------------------------------------------------------") 
elif st.session_state.login == True and st.session_state.role == "common":
    name=st.session_state.user
    
    actualname=name["username"]
    st.header("ERP DASHBOARD")
    st.subheader(f"""welcome {actualname}""")
    
    st.page_link(label = ">>PRODUCTS" , page = "pages/PRODUCTS.py")


if st.session_state.login == True:
    if st.sidebar.button("LOG-OUT"):
        st.session_state.login = False
        st.rerun()


