import streamlit as st
from supabase import create_client, Client

if "SUPABASE_URL" not in st.secrets:
    st.error("SUPABASE_URL missing in Streamlit Cloud Secrets")

if "SUPABASE_KEY" not in st.secrets:
    st.error("SUPABASE_KEY missing in Streamlit Cloud Secrets")

supabase: Client = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
)