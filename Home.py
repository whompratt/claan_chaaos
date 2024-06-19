import pathlib
from pathlib import Path

import streamlit as st
from PIL import Image

# Get relative path
img_path = Path(__file__).parents[0]
# Load images
logo_img = Image.open(f"{img_path}/Images/Logo.png")


def main():
    # Header section
    with st.container():
        # Create columns
        head_l, head_r = st.columns((2.5, 1))

        with head_l:
            # Add a subheader
            st.subheader("Advancing Analytics")
            # Add a title
            st.title("Goodbye from Alex <3")

        with head_r:
            # Add logo
            st.image(logo_img)

        st.divider()

        # Add description
        st.header("The Claans portal has moved to a new domain.")
        st.subheader("https://claans.streamlit.app/")
        st.write("Love you all.")

        st.divider()

        st.image(str(pathlib.Path("./Images/so_long.png")))

        st.divider()

        st.write("So long and thanks for all the fish!")


if __name__ == "__main__":
    main()
