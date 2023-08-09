# Raspi Controller

This is used to control a raspberry pi

The Servo Motor connections are made to pins:

Motor1 : 8,10
Motor2 : 3,5

A USB camera can be connected to raspberry pi to record the video and upload it into a Minio S3 Bucket.

UI can be accessed using:

````
https://localhost:8000
````
To start with all the required packages use the following command:

````
sh install-dependencies.sh
````


A sample .env file will contain the following params.
````
MINIO_CLIENT_IP="localhost:9000"
MINIO_ACCESS_KEY="some-access-key"
MINIO_SECRET_KEY="some-access-secret"
MINIO_REGION="some-minio-region"
MINIO_BUCKET_NAME="some-raspi-bucket"
MINIO_ACCESS_SECURE=False
VIDEO_PATH="/temp/"
VIDEO_FILENAME="myvideo"
RASPI_FORWARD_MOTOR1=3
RASPI_FORWARD_MOTOR2=5
RASPI_BACKWARD_MOTOR1=8
RASPI_BACKWARD_MOTOR2=10
````

A MinIO server can be started with using the following commands:

https://min.io/docs/minio/container/index.html


TODO: 
1. Get the live feed into UI from the camera