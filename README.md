# Vividart Studio Project

This project is to build an image processor utilizing python, lambda, S3 and docker.

I collaborated with Brian Mathenge, Adade Sedom Percy, and Pauline Andege Omondi in doing the project.

Forked the repo from: <https://github.com/olatunji-weber/Vividarts_studio.git>

And here is my personal repository for the project: <https://github.com/olatunji-weber/MineVividarts_studio?tab=readme-ov-file>

Containerized the application using the official Python runtime as the base image, created a function to handle the uploading of images selected via the input form to an S3 bucket on AWS.

And also create a Lambda Function to process the uploaded image by resizing it with a python function invoked by the image upload trigger on an S3 bucket which was created using Terraform.

See Documentation to understand the project: <https://github.com/olatunji-weber/MineVividarts_studio/blob/master/Azubi%20Project%202%20Vividart%20Studio%20-%20Beanstalk2.pdf>
