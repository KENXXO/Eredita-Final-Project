import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="About Us",
    page_icon="🌲",
)

st.title("Welcome to Eredità: Branching Into Tomorrow")
st.divider()
st.markdown("At Eredità, our vision is to simplify legacies one contract at a time. Our Mission is to revolutionize "
            "inheritance and legacy planning by leveraging blockchain technology to "
            "provide a secure, transparent, and user-centric platform for individuals to "
            "create, manage, execute, and educate themselves regarding their inheritance plans.")


st.header("Who We Are")
st.markdown("Eredità represents the convergence of financial technology and innovative solutions, offering a progressive"
            " perspective on legacy planning. Our goal is simple: to uncomplicate the inheritance process, "
            "bring transparency to every step, and empower users to craft personalized and secure legacy plans.")

st.header("Our Commitment")
st.markdown("Rooted in transparency, security, and user empowerment, "
            "Eredità is committed to leveraging the latest technologies to "
            "evolutionize how individuals manage their assets and pass on their legacies.")

# Team Section
st.header("Meet our Team")

imagek = Image.open('kenny.JPG')
imagec = Image.open('carlo.jpg')

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image(imagek,caption="Kenneth pictured in 2023 at UCF", width=350)
st.markdown("Kenneth Colón was born and raised in San Juan, Puerto Rico. After moving to "
                "Florida, he quickly shifted his focus on his accounting and finance studies at"
                "the University of Central Florida. After obtaining his undergraduate degree with a double"
                "major in Accounting and Finance, he then proceeded to earn his CPA license and "
                "earn an MS in Financial Technology from his alma mater.")

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image(imagec,caption="Carlo Manfredini in Business Attire", width=350)
st.markdown("Carlo Manfredini is from Modena, Italy and graduated from UCF with a degree in economics in 2021. He is "
            "currently working as a market research intern at TTS Energy Services, promoting hydrogen-based "
            "energy for natural gas turbines.")

#Innovation and Transformation at the Heart
st.header("Innovation and Transformation at the Heart")
st.markdown("Eredita is not just a platform; it's a dedication to innovation. It all started in a Capstone class as an idea, but"
            "By integrating cutting-edge technologies like blockchain, we provide a secure, transparent, and automated approach to legacy planning. "
            "Security, customizable smart contracts, convenience, and our user-centric approach exemplify our commitment to reshaping inheritance planning.")

# Connect with Us

st.divider()
st.header("Want to learn more? Connect with us!")
st.markdown("Embark on this transformative journey with us. Whether you're a user seeking a modernized approach to legacy planning, "
"an investor eager to participate in financial innovation, or a collaborator interested in shaping the future, "
        "Eredità invites you to join our community.")

contact_form = """
<form action="https://formsubmit.co/ke228717@ucf.edu" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Comments/Questions"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")
