import streamlit as st
from PIL import Image, ImageDraw

from streamlit_option_menu import option_menu
selected =option_menu(menu_title="NLP",
                              options=["Image Segmentation","Contact","about"],
                              orientation="horizontal",)
if selected == "Image Segmentation":
    def create_grid(image_path, grid_size):
    # Open the input image
        image = Image.open(image_path)
        width, height = image.size

        # Calculate the grid cell dimensions
        grid_width = width // grid_size[0]
        grid_height = height // grid_size[1]

        # Create a draw object
        draw = ImageDraw.Draw(image)

        # Draw vertical grid lines and add numbers for each box
        for x in range(0, width, grid_width):
            for y in range(0, height, grid_height):
                draw.rectangle([(x, y), (x + grid_width, y + grid_height)], outline=(25, 0, 0), width=1)
                draw.text((x + 5, y + 5), f"({x // grid_width}, {y // grid_height})", fill=(250, 0, 0))

        # Save timage with grids
        st.image(image)

    # Specify the number of rows and columns for the grid
    row = 5 #desired number of rows
    col = 5 #the desired number of columns

    # input image path
    input_image_path = ("image2.png")  # Replace with your input image path

    # (rows, columns)
    grid_size = (row, col)

    create_grid(input_image_path, grid_size)

    st.write="Name"
if selected == "about":
    st.write="Riya"
if selected == "home":
    st.write="ok"


