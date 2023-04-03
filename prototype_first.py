import streamlit as st
from PIL import Image
from instagrapi import Client
from pathlib import Path


"""
TODO:
1.     
"""


def insta_crawling(ID, PW):
    cl = Client()
    cl.login(ID, PW)

    user_id = cl.user_id_from_username("flatfist._.selfish")
    medias = cl.user_medias(int(user_id), 10)
    folder = "test-folder"
    createDirectory(folder)
    for m in medias:
        try:
            print(photo_download(cl, m.pk, folder))
        except AssertionError:
            pass
            

def photo_download(c, pk, folder):
    media = c.media_info(pk)
    assert media.media_type == 1, "Must been photo"
    filename = "{username}_{media_pk}".format(
            username=media.user.username, media_pk=pk
        )
    
    p = os.path.join(folder, filename + '.jpg')
    response = requests.get(media.thumbnail_url, stream=True, timeout=c.request_timeout)
    response.raise_for_status()
    with open(p, "wb") as f:
        f.write(response.content)
    
    return p


def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")


def concat_image:


st.title('AI color grader')
st.subheader('Find the filter that best fits your Instagram feed!')
# uploaded_files = st.file_uploader(label="Choose image(s)...",
#                                   type=['jpeg', 'png', 'jpg', 'heic'],
#                                   label_visibility='visible',
#                                   accept_multiple_files=True)


# crawled = []
# # Check if the user has uploaded any files
# if uploaded_files or crawled:
#     # Create an empty list to store the images
#     images = []

#     # Loop through each uploaded file and append the opened image to the list
#     for file in uploaded_files:
#         image = Image.open(file)
#         images.append(image)

#     # Calculate the number of rows and columns needed to display the images in a 3x3 grid
#     num_images = len(images)
#     num_rows = (num_images + 2) // 3
#     num_cols = min(num_images, 3)

#     # Set the desired width and height of the images in the grid
#     image_width = 200

#     # Loop through each row and column to display the images in a grid
#     for i in range(num_rows):
#         cols = st.columns(num_cols)
#         for j in range(num_cols):
#             index = i * 3 + j
#             if index < num_images:
#                 cols[j].image(
#                     images[index],
#                     caption=f"{uploaded_files[index].name}",
#                     width=image_width)
#     # center_button = st.container()
#     # with center_button:
#     #     st.button("Process Images", text_align='center')
#     if st.button("Process Images!"):
#         st.write("Images are processed")


# else:
#     # If no files were uploaded, display a message
#     st.write("Please upload one or more image files.")

insta_id = st.text_input("Put your Instagram ID here!")
insta_pwd = st.text_input('Put your Instagram password here!')
# Instagram crawling button
if st.button("Crawling Instagram"):
    insta_crawling(insta_id, insta_pwd)

#id = "leessunj"
#pwd = "Ilsj08282!"
