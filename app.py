import datetime
import gradio as gr
import cv2
import uuid

def generate_markdown_post(title: str, content: str, image: gr.Image):
    # Get the current date and time
    now = datetime.datetime.now()

    # Format the date and time in the required format
    date_string = now.strftime("%Y-%m-%d %H:%M:%S %z")
    subdate_string = now.strftime("%Y-%m-%d")

    # Generate a random unique ID
    unique_id = str(uuid.uuid4().hex)[:6]

    # Format the filename with subdate and unique ID
    filename = f"_posts/{subdate_string}-{unique_id}.markdown"

    # Define the Markdown content with the updated title and date
    markdown_content = f"""---
layout: post
title: "{title}"
date: {date_string}+200
categories: jekyll update
---
<img src="/blog_assets/{unique_id}.jpg">

{content}
"""

    # Save the uploaded image to the file system
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    cv2.imwrite(f"blog_assets/{unique_id}.jpg",image)

    # Write the Markdown content to the file with the formatted filename
    with open(filename, "w") as f:
        f.write(markdown_content)

    return f"Markdown post created at {filename}"

title = "Markdown Blog Post Generator"
description = "This app generates a Markdown blog post with the given title, content, and image."
inputs = [
    gr.Textbox(label="Enter the blog post title:"),
    gr.Textbox(label="Enter the content:"),
    gr.Image(label="Upload an image")
]
outputs = gr.Textbox()
gr.Interface(fn=generate_markdown_post, inputs=inputs, outputs=outputs, title=title, description=description).launch()
