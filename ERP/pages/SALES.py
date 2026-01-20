import streamlit as st
from groq import Groq
import pandas as pd
import json



if "login" not in st.session_state:
    st.session_state.login = False

if st.session_state.login == False:
    st.page_link(label = "please login before the acion", page = "app.py" )


elif (st.session_state.login == True and st.session_state.role == "admin"):
    st.header("SALES PAGE")
    
    csv = st.session_state.readed
    with st.expander("click to see the subjected csv file"):
        st.write(csv)
    st.subheader("Last week sales performance")
    c1,c2=st.columns(2)
    st.write("i have removed api key - since someone told me to remove all api key before uploading your project into github")
    client = Groq(api_key="")
    system_prompt=f"""now you have to analyse the last week performance of the given csv file , provide a well detailed report within 100 words thats enough but make it point by point, csv file = {csv}"""
    response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": system_prompt}])
    st.session_state.result1 = ( response.choices[0].message.content )

    system_prompt2="""now you have to analyse the last week performance of the given csv file ,Analyze the CSV performance ,You are a data analyzer.
Respond ONLY in valid JSON.
No explanation. No text. No markdown.

Format:
{
  "Good": number,
  "Average": number,
  "Poor": number
} because i have to use your output to print bar chart or pie chart,"""
    system_prompt3=f"""and the csv file is {csv}"""
    response2 = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": system_prompt2},{"role": "system", "content": system_prompt3}])
    st.session_state.result2 = ( response2.choices[0].message.content )
    dd=st.session_state.result2
    data = json.loads(dd)
    df = pd.DataFrame([data])
    numeric_cols = csv.select_dtypes(include="number").columns.tolist()
    with c1:
        st.write(st.session_state.result1)
    with c2:
        numeric_cols = df.select_dtypes(include="number").columns

        if not numeric_cols.empty:
            st.scatter_chart(df[numeric_cols])
        else:
            st.warning("No numeric columns found for scatter chart")

elif (st.session_state.login == True and st.session_state.role == "common"):
    st.header("AI sales and service manager")
    search = st.text_input("search for a product")
    doc = pd.read_csv("erp_dummy.csv")
    bu = st.button("search")

    if bu:
        st.write("i have removed api key - since someone told me to remove all api key before uploading your project into github")
        client = Groq(api_key="")
        system_prompt=f"""user will give you the product name as {search} ,don't expose any sensitive details because your representing the data to user point of view that must only have to know about the simple basic deatils of the product and you have to do search in our csv file {doc} , and mention do have the product or not , if we have that product then say , yes our company do have this products and establish as much as possible about the product and service ..incase if we don't have the product then say we will soon add this product in our service and provide certaine details about that detail , maximum 20 lines and give the details in bullet point order"""
        response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "system", "content": system_prompt}])
        st.session_state.result = ( response.choices[0].message.content )
        st.write(st.session_state.result)
    
    
if st.session_state.login == True:
    if st.sidebar.button("LOG-OUT"):
        st.session_state.login = False
        st.rerun()


