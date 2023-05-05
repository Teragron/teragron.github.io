import datetime
import gradio as gr
import cv2
import uuid
from github import Github

# replace the placeholder values with your GitHub account information and repository details
github_username = "teragron"
github_password = "<your_github_password>"
repo_name = "teragron.github.io"
repo_branch = "main"

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
    cv2.imwrite(f"blog_assets/{unique_id}.jpg", image)

    # Write the Markdown content to the file with the formatted filename
    with open(filename, "w") as f:
        f.write(markdown_content)

    # Push the generated markdown file and image to the GitHub repository
    g = Github(github_username, github_password)
    repo = g.get_user().get_repo(repo_name)
    with open(filename, "rb") as f:
        repo.create_file(filename, f"Add new blog post '{title}'", f.read(), branch=repo_branch)
    with open(f"blog_assets/{unique_id}.jpg", "rb") as f:
        repo.create_file(f"blog_assets/{unique_id}.jpg", f"Add new image for blog post '{title}'", f.read(), branch=repo_branch)

    return f"Markdown post created at {filename} and pushed to GitHub"

title = "Markdown Blog Post Generator"
description = "This app generates a Markdown blog post with the given title, content, and image and pushes it to your GitHub repository."
inputs = [
    gr.Textbox(label="Enter the blog post title:"),
    gr.Textbox(label="Enter the content:"),
    gr.Image(label="Upload an image")
]
outputs = gr.Textbox()
gr.Interface(fn=generate_markdown_post, inputs=inputs, outputs=outputs, title=title, description=description).launch()
