provider "aws" {
  region = "eu-central-1"
}

data "archive_file" "lambdazip" {
  type        = "zip"
  output_path = var.zip_filename

  source_dir = "src"
}

resource "aws_iam_role" "iam_for_lambda" {
  name = "iam_for_lambda"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_lambda_function" "discordRedirect" {
  filename = var.zip_filename

  function_name = "discordRedirect"
  description   = "redirect function for a discord invite to be used with a vanity url"

  role    = aws_iam_role.iam_for_lambda.arn
  handler = "main.lambda_handler"

  source_code_hash = filebase64sha256(var.zip_filename)

  runtime = "python3.8"

  memory_size = 128
  timeout     = 1

  environment {
    variables = {
      INVITE = var.invite_link
    }
  }

}