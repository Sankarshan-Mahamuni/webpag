import streamlit as st
from PIL import Image
import io
from io import BytesIO

def home():
    st.title("Home Page")
    st.write("Welcome to the home page!")
    st.title("E-lab")

    image_path = "dp.jpg"
    image = Image.open(image_path)
    resized_image = image.resize((500,500))

    # Convert PIL Image to BytesIO object
    image_bytes = io.BytesIO()

    resized_image.save(image_bytes, format="PNG")  # Adjust the format based on your image type
    st.image(image_bytes, caption="concept", use_column_width=False)


def Menu():

    st.title("E-lab")

    image_path = "dp.jpg"
    image = Image.open(image_path)
    resized_image = image.resize((100,100))

    # Convert PIL Image to BytesIO object
    image_bytes = io.BytesIO()

    resized_image.save(image_bytes, format="PNG")  # Adjust the format based on your image type
    st.image(image_bytes, caption="concept", use_column_width=False)


    st.header("PCCOE pune,Engineering chemistry")
    st.subheader("click to any of 5 experiments")


# 1
    other_app_url = "https://experiment1aaa.streamlit.app/"
# Create a hyperlink to the other Streamlit app
    st.markdown(f"EXPERIMENT NO 1 [experiment no 1]({other_app_url}).")


# 2
    other_app_url2 = "https://experiment2-arpita.streamlit.app/"
# Create a hyperlink to the other Streamlit app
    st.markdown(f"EXPERIMENT NO 2 [experiment no 2]({other_app_url2}).")



# 3
    other_app_url3 = "https://sankarshanex3tryl1.streamlit.app/"

# Create a hyperlink to the other Streamlit app
    st.markdown(f"EXPERIMENT NO 3 [experiment no 3]({other_app_url3}).")



# 4
    other_app_url4 = "https://sankarshanex3tryl1.streamlit.app/"

# Create a hyperlink to the other Streamlit app
    st.markdown(f"EXPERIMENT NO 4 [experiment no 4]({other_app_url4}).")



# 5
    other_app_url5 = "https://sankarshanex5tryl4.streamlit.app/"

# Create a hyperlink to the other Streamlit app
    st.markdown(f"EXPERIMENT NO 5 [experiment no 5]({other_app_url5}).")





def contact():
    st.title("Contact Page")
    st.markdown("""You can reach us at contact.
    sankarshan.mahamuni@pccoepune.org
    kinjal.heda@23pccoepune.org""")

def main():
    pages = {
        "Home": home,
        "MENU": Menu,
        "Contact": contact,
    }

    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(pages.keys()))

    # Display the selected page
    pages[selection]()

if __name__ == "__main__":
    main()
