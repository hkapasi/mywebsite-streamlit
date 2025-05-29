import streamlit as st
import base64

# Inject custom CSS
st.set_page_config(layout="wide", page_title="Contact Details", page_icon="📬")

st.markdown(
    """
    <style>
    /* Hide the entire top-right toolbar (Deploy + Menu) */
    [data-testid="stToolbar"] {
        display: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Contact Me 📧")

# --- Email Configuration ---
RECIPIENT_EMAIL = "hzf_kapasi@yahoo.com"
EMAIL_SUBJECT = "Hi!! Let's_connect....." # Optional: prefill subject
EMAIL_BODY = "Hello,\n\n....." # Optional: prefill body

# --- Construct the mailto link ---
# Simple mailto link with just the recipient
# mailto_link = f"mailto:{RECIPIENT_EMAIL}"

# Mailto link with recipient, subject, and body
# Note: For subject and body, special characters should be URL encoded.
# Streamlit's markdown with f-strings handles basic encoding for spaces,
# but for more complex characters, consider using urllib.parse.quote_plus.
import urllib.parse
mailto_link_complex = f"mailto:{RECIPIENT_EMAIL}?subject={urllib.parse.quote_plus(EMAIL_SUBJECT)}&body={urllib.parse.quote_plus(EMAIL_BODY)}"

# --- Display the hyperlink in Streamlit ---
st.subheader("📧 Via Email")

st.markdown("Click the link below to send an email:")

# Using the more complex link with subject and body
st.markdown(f'<a href="{mailto_link_complex}" style="text-decoration: none; color: #007BFF; font-weight: bold;">Contact Via Email</a>', unsafe_allow_html=True)

# --- Alternative: Using a simple mailto link (recipient only) ---
# st.markdown(f'<a href="mailto:{RECIPIENT_EMAIL}">Contact Us (Simple)</a>', unsafe_allow_html=True)

st.info("ℹ️ Clicking the link will open your default email client.(Or right click and copy email address)")




st.subheader("📧 Or, Let's Connect on LinkedIn")
# Load and encode image
file_ = open("linkedin_logo.png", "rb")
contents = file_.read()
data_url = f"data:image/png;base64,{base64.b64encode(contents).decode()}"

# Embed image with a link
st.markdown(
    f"""
    <a href="https://www.linkedin.com/in/hozefa-m-kapasi/" target="_blank">
        <img src="{data_url}" width="50">
    </a>
    """,
    unsafe_allow_html=True
)