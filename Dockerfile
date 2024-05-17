FROM public.ecr.aws/lambda/python:3.12

# Copy requirements.txt and install dependencies
# COPY requirements.txt requirements.txt  # You can uncomment this line if you have a requirements.txt file
# RUN pip install requests

# # Install rembg package
# RUN pip install rembg || echo "Failed to install rembg package"

# Copy your Lambda function code

RUN pip install rembg requests
COPY . .

# Set the CMD to your Lambda handler
CMD ["app.lambda_handler"]
