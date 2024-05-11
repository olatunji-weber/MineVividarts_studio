from flask import Flask, render_template, request
import os
import boto3

s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                  region_name=REGION_NAME)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    s3.upload_fileobj(file, 'vividbucket-beanstalk2', file.filename)
    return 'File uploaded successfully'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
