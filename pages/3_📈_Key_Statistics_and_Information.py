import streamlit as st
import time
st.set_page_config(
    page_title="Key Statistics",
    page_icon="📈",
)


def type_script(message, delay=0.1):
    container = st.empty()
    typed_text = "Report: "
    for char in message:
        typed_text += char
        container.caption(typed_text)
        time.sleep(delay)
    return container



st.title("Key Statistics and Information",)
st.divider()
st.markdown("In this section, we unveil the key statistics and pivotal information that underscore "
            "the impact and significance of our platform. Here, transparency isn't just a concept "
            "– it's a commitment. Dive into the numbers, trends, and milestones that define "
            "Eredita's journey in reshaping the future of legacy planning.")

st.write("# Start Here: ")
#st.sidebar.success("Select a demo above.")
st.markdown(
    """
    Here you can find some key concepts that are important to know before you start your
    inheritance journey. After that, feel free to explore the statistics that shaped our inspiration 
    for Eredità, as well as an **interactive user experience** to learn more about this outdated process.
    
    ### Want to learn more regarding the process?
    - Check out [Investopedia](https://www.investopedia.com/terms/e/estateplanning.asp) for more on Estate Planning.
    - Jump into the [Probate](https://www.americanbar.org/groups/real_property_trust_estate/resources/estate_planning/the_probate_process/) process to see how it works and why it can be so costly.
    - Explore the [importance of estate planning](https://www.investopedia.com/articles/wealth-management/122915/4-reasons-estate-planning-so-important.asp).
    ### See Key Statistics for Estate Planning
    - [LegalZoom](https://www.legalzoom.com/articles/estate-planning-statistics) has a fantastic breakdown of many key stats. Can you try to answer the question below?""")
# Create a slider for age input
selected_age = st.slider("What's the most common age to have a will?", 0, 100, step=1, value=25)

answers = {
    (18, 34): "Not quite. Only 24% of people in this age group of 18-34 have a will.",
    (35, 54): "Not quite. Only 27% of people in this age group of 33-54have a will.",
    (55, 71): "Not quite. Only 45% of people in this age group  of 55-71 have a will.",
    (72, 105): "Correct! 81% of people in this age group of 72+ have a will. ",
}

generate_report_button = st.button("Submit answer")

if generate_report_button:
    found_answer = False
    for age_range, answer in answers.items():
        if age_range[0] <= selected_age <= age_range[1]:
            type_script(answer, delay=0.03)
            found_answer = True
            break

    if not found_answer:
        st.warning("No answer found for the selected age.")

st.markdown("""
- Analyze key numbers provided by [SeniorLiving](https://www.seniorliving.org/finance/estate-settlement-annual-report/) in this insightful report.
- Dive in to some more [interesting/fun facts](https://www.plannedgiving.com/legacy-box/wills-and-estate-planning-statistics/) about estate planning.
## Blockchain, Smart Contracts, and More In The Estate Planning Industry
- [Smart Contracts](https://susqublockchain.medium.com/smart-contracts-for-estate-planning-and-administratio-c400114e8a58) in Estate Planning.
- How [E-Wills](https://trustandwill.com/learn/how-ewills-are-changing-the-industry) Pave the Way for Tomorrow's Estate Planning Landscape.
- The [Three Ways](https://zus.network/blog/posts/three-ways-estate-planning-is-revolutionized-by-smart-contracts/) Estate Planning is Revolutionized by Smart Contracts.
- Revolutionizing wills and asset transfer: [How blockchain could transform](https://www.thestreet.com/crypto/finance/revolutionizing-wills-and-asset-transfer-how-blockchain-could-transform-estate-planning) estate planning.
            """)

st.title("Have questions of your own? Try out our EstateBot!🤖")

selected_text = st.text_input("Enter your question:")
st.write("For demo purposes, the bot can only answer 3 questions phrased as: Key Issues, What is Eredità? and Give me fun facts about estate planning.")
answers = {
    "key issues": """
Inheritance planning has long been steeped in tradition, often relying on conventional methods. Eredita disrupts this tradition by introducing a modern, technology-driven approach, leveraging blockchain to provide transparency, security, and efficiency. The platform addresses the digital divide by offering an inclusive, user-friendly interface, aiming to bridge gaps in accessing financial services. Education is at the forefront of Eredita, empowering users with insights into legal aspects, blockchain benefits, and the intricacies of inheritance planning. We go beyond being a platform; we're an educational resource fostering informed decision-making. Perception plays a pivotal role in how individuals approach estate planning. Eredita aims to reshape perceptions by showcasing the benefits of blockchain technology—ensuring transparency, reducing friction in asset distribution, and providing a user-centric experience. Together, we strive to redefine how people perceive and engage with legacy planning.
""",
    "what is eredità?": "Eredità is a digital B2B and B2C platform that utilizes blockchain and smart contract technologies in order to digitize and modernize the estate planning industry. Its goal is to empower individuals to navigate and secure their legacies while providing comprehensive educational resources to foster greater awareness and understanding of this critical aspect of financial planning."
,
    "give me fun facts about estate planning": """
Shortest will written: “All to son.”
Second shortest will: “All to wife.” (January of 1967, Herr Karl Hausch)
Largest inheritance to a pet: $80 million (1991, Carlotta Leibenstein)
Oldest Power of Attorney: 561 BC, Mesopotamia
Longest will: 1066 pages (Frederica Evelyn Stilwell Cook, British)
Famous people who died without a will: Abraham Lincoln, Picasso, Martin Luther King, among others.
"""
    # Add more text entries and corresponding answers as needed
}

generate_report_button = st.button("Find Out!")

if generate_report_button:
    selected_text_lower = selected_text.lower()  # Convert input to lowercase for case-insensitive matching

    found_answer = False
    for text_entry, answer in answers.items():
        if selected_text_lower == text_entry:
            type_script(answer, delay=0.01)
            found_answer = True
            break

    if not found_answer:
        st.warning("No answer found for the entered text.")
