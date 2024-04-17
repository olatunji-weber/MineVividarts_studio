import os
import tempfile
from PIL import Image
import boto3

s3 = boto3.client('s3')


def lambda_handler(event, context):
    # Get the uploaded image details from the S3 event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Download the image from S3 to a temporary file
    with tempfile.TemporaryFile() as temp_file:
        s3.download_fileobj(bucket_name, key, temp_file)
        temp_file.seek(0)

        # Open the image using Pillow
        image = Image.open(temp_file)

        # Resize the image
        image.thumbnail((400, 400))

        # Save the resized image to a new temporary file
        resized_image = tempfile.NamedTemporaryFile(delete=False)
        image.save(resized_image, format='JPEG')
        resized_image.seek(0)

        # Upload the resized image to the "vividbucket-resized-images" S3 bucket
        resized_bucket_name = "vividbucket-resized-images"
        resized_key = os.path.splitext(key)[0] + "-resized.jpg"
        s3.upload_fileobj(resized_image, resized_bucket_name, resized_key)

        # Clean up the temporary files
        resized_image.close()
        temp_file.close()

    return {
        'statusCode': 200,
        'body': f'Resized image saved to {resized_bucket_name}/{resized_key}'
    }
