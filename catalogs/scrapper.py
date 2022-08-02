from bs4 import *
import requests
import os
from PIL import Image
from .models import ProductImage
from django.core.files.uploadedfile import InMemoryUploadedFile


def create_directory(dir_name):
    """Create directory"""
    media_directory = 'media/'
    try:
        # Directory creation
        os.makedirs(media_directory + dir_name)

    # if directory exists with that name, ask another name
    except Exception as e:
        print("Directory Exist with this name!")

    return media_directory + dir_name


def download_images(images, folder_name):
    image_link = ''
    count = 0

    # Print total number of images found in this url
    print(f"Total {len(images)} images found!")

    # Checking if images is not zero
    if len(images) != 0:
        for i, image in enumerate(images):
            """
            Fetch image Source URL from image tag , like-
                1.data-srcset
                2.data-src
                3.data-fallback-src
                4.src
            """
            try:
                # In image tag ,searching for "data-srcset"
                image_link = image["data-srcset"]

            # then we will be searching for "data-src" in img
            except Exception as e:
                try:
                    # In image tag ,searching for "data-src"
                    image_link = image["data-src"]

                except Exception as e:
                    try:
                        # In image tag ,searching for "data-fallback-src"
                        image_link = image["data-fallback-src"]
                    except Exception as e:
                        try:
                            # In image tag ,searching for "src"
                            image_link = image["src"]

                        # if no Source URL found
                        except Exception as e:
                            print('No source url found :(')

            # After getting Image Source URL
            # We will try to get the content of image
            try:
                response = requests.get(image_link).content
                try:

                    # Possibility of decode
                    response = str(response, 'utf-8')

                except UnicodeDecodeError:

                    # After checking above condition, Image downloading will be started
                    with open(f"{folder_name}/images{i + 1}.jpg", "wb+") as f:
                        f.write(response)
                        img = Image.open(f.name)
                        # Saving image data to corresponding model
                        product_image = ProductImage()
                        product_image.original_image = img.filename[6:]
                        product_image.save()

                    # Counting number of images downloaded
                    count += 1
            except Exception as e:
                pass

        # If all images download
        if count == len(images):
            print("All Images Downloaded!")

        # If all images are not downloaded
        else:
            print(f"Total {count} Images Downloaded Out of {len(images)}")


def main():
    url = "https://applegadgetsbd.com/"
    response = requests.get(url)
    # Parse HTML Code
    soup = BeautifulSoup(response.text, 'html.parser')
    # find all images in URL
    images = soup.findAll('img')

    #  Call this to create directory
    dir_name = create_directory(dir_name='scrapped-images')
    # To download images
    download_images(images, dir_name)
