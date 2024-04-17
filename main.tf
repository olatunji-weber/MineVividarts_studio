resource "aws_s3_bucket" "beanstalk_bucket" {
  bucket = "vividbucket-beanstalk2"

  tags = {
    Name        = "Beanstalk bucket"
    Environment = "Dev"
  }
}

resource "aws_s3_bucket" "resized_images_bucket" {
  bucket = "vividbucket-resized-images"

  tags = {
    Name        = "Resized Images bucket"
    Environment = "Dev"
  }
}

# resource "aws_s3_bucket" "vividbucket" {
#   bucket = "vividbucket-beanstalk2"

#   tags = {
#     Name        = "Beanstalk bucket"
#     Environment = "Dev"
#   }
# }
