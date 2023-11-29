import streamlit as st
st.set_page_config(
    page_title="Contact Us",
    page_icon=":mailbox:",
)


st.header("Want to learn more? Connect with us! :mailbox:")
st.divider()
st.markdown("Embark on this transformative journey with us. Whether you're a user seeking a modernized approach to legacy planning, "
"an investor eager to participate in financial innovation, or a collaborator interested in shaping the future, "
        "Eredità invites you to join our community. Interested in our service for yourself or your business as well? Don't "
            "be afraid to contact us!")
contact_form = """
<form action="https://formsubmit.co/ke228717@ucf.edu" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Type your interest here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")
