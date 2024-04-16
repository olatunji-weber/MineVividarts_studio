resource "aws_s3_bucket" "vividbucket" {
  bucket = "vividbucket-beanstalk2"

  tags = {
    Name        = "Beanstalk bucket"
    Environment = "Dev"
  }
}
