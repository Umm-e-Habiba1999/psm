import re
import streamlit as st

#page styling
st.set_page_config(page_title="Password Streanght Checker By Umm-E-Habiba" , page_icon="🛅" , layout="centered")
#custom css
st.markdown(""" 
<style>
    .main {text-align: center;}
    .stTextInput {width:50%, background-colour #4CAF50; color: white; font-size: 10px;}
    .stButton button:hover {background-color: #45a049;}
 </style>
""" , unsafe_allow_html=True)

#page title and description
st.title("🔐Password Strenght Generator")
st.write("Enter your Password below to check its security level.✇")

#function to check password strenght
def check_password_strenght(password):
    score = 0
    feedback =[]

    if len(password) >= 8:
        score += 1 #increased score by 1
    else:
        feedback.append("❌ Password should be **atleast 8 character long**.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **both uppercase (A-Z) and lowercase (a-z) letters**.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one number (0-9)**.")

    #speacial characters
    if re.sear(r"[!@$$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Includes **at least one special character (!@$$%^&*)**.")

#display password strenght results
    if score == 4:
       st.success("✔️ **Strong Password** - Your password is secure.")
    elif score ==3:
        st.info("🚨 **Moderate Password** - Consider improving security by adding moree feature")
    else:
        st.error("❌ **Week Password** - Follow the suggestion below to strenght it. ")

#feedback
    if feedback:
       with st.expander("**Improve Your Password**"):
        for item in feedback:
            st.write(item)
password = st.text_input("Enter Your Password", type="password" ,help="Ensure your password is strong🔐")


#button Working
if st.button("Check Strength"):
    if password:
        check_password_strenght(password)
    else:
        st.warning("▩Please enter a password first!") #show warning if password empty
