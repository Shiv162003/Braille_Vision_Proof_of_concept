import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image, ImageDraw
import cv2
import numpy as np



# Set page title
st.set_page_config(page_title="Braille Vision", page_icon="asset/logo.png")

# functions grid

def create_grid(image, grid_size):
    # Open the input image
    img = Image.open(image)
    width, height = img.size

    # Calculate the grid cell dimensions
    grid_width = width // grid_size[0]
    grid_height = height // grid_size[1]

    # Create a draw object
    draw = ImageDraw.Draw(img)

    # Draw vertical grid lines and add numbers for each box
    for x in range(0, width, grid_width):
        for y in range(0, height, grid_height):
            draw.rectangle([(x, y), (x + grid_width, y + grid_height)], outline=(25, 0, 0), width=1)
            draw.text((x + 5, y + 5), f"({x // grid_width}, {y // grid_height})", fill=(250, 0, 0))

    # Display image with grids
    st.image(img, caption='Image with Grids', use_column_width=True)
selected =option_menu(menu_title="NLP",
                              options=["xyz","Image Segmentation","Video Segmentation","about"],
                              orientation="horizontal",)
# function for video

def calculate_noise(frame):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return np.std(gray_frame)

def find_frame_with_least_noise(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return None
    
    least_noise_frame = None
    min_noise = float('inf')
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        noise = calculate_noise(frame)
        if noise < min_noise:
            min_noise = noise
            least_noise_frame = frame
    
    cap.release()
    
    return least_noise_frame



# Display content based on the selected option
if selected == "Image Segmentation":
    st.write("Welcome to the Image Segmentation section!")
    # Streamlit app
    st.title('Image Grid Creator')

    # File uploader for image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    # Input fields for grid dimensions
    row = st.number_input('Enter number of rows:', min_value=1, value=5)
    col = st.number_input('Enter number of columns:', min_value=1, value=5)

    # Create grid upon button click
    if uploaded_file is not None and st.button('Create Grid'):
        # (rows, columns)
        grid_size = (row, col)
        create_grid(uploaded_file, grid_size)

    #create submit button
    if st.button('submit'):
        st.write('hello world')
        

elif selected == "Video Segmentation":
    st.write("Here you can find our contact information.")
    # Add more content related to Contact
    video_path = "video.mp4"                            
    least_noise_frame = find_frame_with_least_noise(video_path)

    if least_noise_frame is not None:
        st.image(least_noise_frame)
    else:
        st.write("No frames in the video.")
    
if selected == "About":
    st.write("Learn about the Braille Vision project.")

