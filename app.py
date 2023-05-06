import datetime
import gradio as gr
import cv2
import uuid

import subprocess

def commit_and_push(file_path: str):
    # Add the file to Git
    subprocess.call(['git', 'add', "."])

    # Commit the changes
    subprocess.call(['git', 'commit', '-m', f'New blog post {unique_id}'])

    # Push the changes to the remote repository
    subprocess.call(['git', 'push'])

    return "Markdown post committed and pushed successfully!"


def generate_markdown_post(title: str, content: str, image: gr.Image):
    # Get the current date and time
    now = datetime.datetime.now()

    # Format the date and time in the required format
    date_string = now.strftime("%Y-%m-%d %H:%M:%S %z")
    subdate_string = now.strftime("%Y-%m-%d")

    # Generate a random unique ID
    global unique_id
    unique_id = str(uuid.uuid4().hex)[:6]
    

    # Format the filename with subdate and unique ID
    filename = f"_posts/{subdate_string}-{unique_id}.markdown"
    
    try:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        cv2.imwrite(f"blog_assets/{unique_id}.jpg",image)
        src = '<img src="/blog_assets/{unique_id}.jpg">'
    except:
        src = ""

    # Define the Markdown content with the updated title and date
    markdown_content = f"""---
layout: post
title: "{title}"
date: {date_string}+200
categories: jekyll update
---
{src}

{content}
"""

    # Write the Markdown content to the file with the formatted filename
    with open(filename, "w") as f:
        f.write(markdown_content)
        
    commit_and_push(filename)

    return f"New Blog: {title}"

title = "Markdown Blog Post Generator"
description = "This app generates a Markdown blog post with the given title, content, and image."
inputs = [
    gr.Textbox(label="Enter the blog post title:"),
    gr.Textbox(label="Enter the content:"),
    gr.Image(label="Upload an image")
]
outputs = gr.Textbox()
gr.Interface(fn=generate_markdown_post, inputs=inputs, outputs=outputs, title=title, description=description).launch()
