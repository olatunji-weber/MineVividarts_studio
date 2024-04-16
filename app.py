from flask import Flask, render_template, request
import os
import boto3

s3 = boto3.client('s3', aws_access_key_id='AKIAZI2LJE2O4EFLHZ6O',
                  aws_secret_access_key='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',
                  region_name='us-east-1')

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
