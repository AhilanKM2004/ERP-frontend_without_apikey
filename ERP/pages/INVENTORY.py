import streamlit as st
from groq import Groq
import pandas as pd

if "login" not in st.session_state:
    st.session_state.login = False

if st.session_state.login == False:
    st.page_link(label = "please login before the acion", page = "DASHBOARD.py" )


elif (st.session_state.login == True and st.session_state.role == "admin"):

    st.header("INVENTORY PAGE")
    if "readed" not in st.session_state:
        st.session_state.readed = None
    # file=st.file_uploader("please upload your project report - CSV",type = ["csv"])
    file = "erp_dummy.csv"
    if file:
        with st.expander("RAW CSV file"):
            readed = pd.read_csv(file)
            st.session_state.readed = readed
            st.table(readed)
        if "readed" in st.session_state:
            c1, c2 = st.columns(2)

            with c1:
                chart_options = ["line chart", "area chart", "scatter chart"]

                if "radio" not in st.session_state:
                    st.session_state.radio = chart_options[0]

                st.session_state.radio = st.radio("SELECT DIAGRAM TYPE",chart_options)

            with c2:
        
                df = st.session_state.readed

                numeric_cols = df.select_dtypes(include="number").columns.tolist()

                if st.session_state.radio == "line chart":
                    st.line_chart(df[numeric_cols])

                elif st.session_state.radio == "area chart":
                    st.area_chart(df[numeric_cols])

                elif st.session_state.radio == "scatter chart":
                    st.scatter_chart(
                        df,
                        x=numeric_cols[0],
                        y=numeric_cols[1]
                    )

            client = Groq(api_key="")
            st.header("AI report")
            st.write("i have removed api key - since someone told me to remove all api key before uploading your project into github")
            system_prompt=f"""we will give you an csv file and you have to do analys over the file and make small report about the subjected file , declare the current state , postive , negative all important points , remember it's need not be a bigger report but important point , just for the clarification and finally once again make it very  shorter because longer version will be displayed after this portion so make don't make it over 25 lines, and the csv file is = {st.session_state.readed}"""
            response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "system", "content": system_prompt}])
            st.session_state.result = ( response.choices[0].message.content )
            st.write(st.session_state.result)


    st.write("-----------------------------------------------------------------------------")
    c1,c2 = st.columns(2)
    with c1:
        st.page_link(label = "To check sales details", page = "pages/SALES.py" )
    with c2:
        st.page_link(label = "To check product details", page = "pages/PRODUCTS.py" )

elif (st.session_state.login == True and st.session_state.role == "common"):
    st.subheader("you are restricted")
    st.write("please go to product page or sales page")
    st.write("-----------------------------------------------------------------------------")
    c1,c2 = st.columns(2)
    with c1:
        st.page_link(label = "To explore our sales and service", page = "pages/SALES.py" )
    with c2:
        st.page_link(label = "To purchase our products", page = "pages/PRODUCTS.py" )



if st.session_state.login == True:
    if st.sidebar.button("LOG-OUT"):
        st.session_state.login = False

