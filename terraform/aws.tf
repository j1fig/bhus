provider "aws" {
  profile = "personal"
  region  = var.region
  version = "2.42.0"
}


resource "aws_instance" "satori" {
  ami           = "ami-028188d9b49b32a80" # Amazon Linux AMI 2018.03.0
  instance_type = "t2.micro"

  provisioner "local-exec" {
    command = "echo ${aws_instance.satori.public_ip} > ip_address.txt"
  }
}

resource "aws_eip" "ip" {
  vpc      = true
  instance = aws_instance.satori.id
}

resource "aws_s3_bucket" "satori" {
  bucket = "tldx-satori"
  acl    = "private"
  region = var.region
}


output "ip" {
  value = aws_eip.ip.public_ip
}
