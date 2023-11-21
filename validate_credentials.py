import streamlit as st
import snowflake.connector

conn = st.connection("snowflake")
df = conn.query("select current_warehouse()")
st.write(df)