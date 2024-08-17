import streamlit as st
from views import display_home_content, display_cart_content, display_payment_content, display_settings_content


def apply_theme_and_font_size():
   theme = st.session_state.get("theme", "light")  # Default to light theme
   font_size = st.session_state.get("font_size", 16)  # Default font size

    # Apply theme using inline CSS (adjust as needed)
   if theme == "dark":
        st.markdown("<style>body {background-color: #262730; color: #fff;}</style>", unsafe_allow_html=True)
   elif theme == "blue":
        st.markdown("<style>body {background-color: #007bff; color: #fff;}</style>", unsafe_allow_html=True)

    # Apply font size (adjust as needed)
   st.markdown(f"<style>body {{ font-size: {font_size}px; }}</style>", unsafe_allow_html=True)


def cart():
  st.title("Cart")
  # Content for the Cart page

def payment():
  st.title("Payment")
  # Content for the Purchase page

def settings():
  st.title("Settings")
  # Content for the Settings page (including contact form logic)

function_map = {
  "home": display_home_content,  # Use display_home_content here
  "cart": display_cart_content,
  "payment": display_payment_content,
  "settings": display_settings_content,
}


if "page" not in st.session_state:
  st.session_state.page = "home"

selected = st.selectbox("Navigate", list(function_map.keys()), index=list(function_map.keys()).index(st.session_state.page))
st.session_state.page = selected

try:
  function_map[selected]()
except KeyError:
  st.error("Invalid page selection")


def update_page(new_page):
    st.session_state.page = new_page


def cart_button_clicked():
    st.session_state.page = "cart"  # Update page to "cart" on button click

def payment_button_clicked():
    st.session_state.payment = "payment"


def main():
    """
    Main function for application layout and navigation.
    """
    st.session_state.page = "home"  # Set initial page

    # Initialize cart items
    st.session_state.cart_items = []
    
    # ... (Your product display and button logic from views.py)

    # Register the cart button callback
    st.button("View Cart", on_click=cart_button_clicked)

    st.session_state.payment

    if "page" in st.session_state:
      page_to_show = st.session_state.page
      function_map = {
        "home": display_home_content,
        "cart": display_cart_content,
        "payment": display_payment_content,  # Ensure it's included
        "settings": display_settings_content,
    }
    if page_to_show in function_map:
        function_map[page_to_show]()
    else:
        st.error(f"Invalid page: {page_to_show}")

    if st.button("Go to Payment"):
       st.session_state.page = "payment"  # Update page on button click
