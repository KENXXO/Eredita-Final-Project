import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
)


image = Image.open('eredita.jpg')

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image(image, width=350)

st.divider()

st.write("# Welcome to Eredità! 👋")
#st.sidebar.success("Select a demo above.")

st.write(
    """
    Eredita is a digital B2B and B2C platform that utilizes blockchain and smart contract technologies in order to digitize and modernize the estate planning industry. 

Its goal is to empower individuals to navigate and secure their legacies while providing comprehensive educational resources to foster greater awareness and understanding of this critical aspect of financial planning.
Feel free to explore our various tabs on the left side to learn more!""")
st.markdown("""
        - About Us
- Key Statistics and Information
- Walkthrough
- Contact Us!

You are one step closer to branching into tomorrow and cementing your legacy!
""")

if 'button_pressed' not in st.session_state:
    st.session_state.button_pressed = False
if st.button("Celebrate!"):
    st.session_state.button_pressed = True
if st.session_state.button_pressed:
    st.balloons()
