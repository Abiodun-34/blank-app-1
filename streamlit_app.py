import streamlit as st

st.title("Welcome To Healthnics")

about_page = st.Page(
    page="views/Welcome.py",
    title="Welcome",
    icon=":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    page="views/Vitals.py",
    title="Vitals",
    icon=":material/thumb_up:",
)
project_2_page = st.Page(
    page="views/Goodbye.py",
    title="Goodbye",
    icon=":material/smart_toy:",
)

pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

pg.run()



