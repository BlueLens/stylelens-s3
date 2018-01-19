import os
from stylelens_s3.s3 import S3

AWS_ACCESS_KEY = os.environ['AWS_ACCESS_KEY']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
RELEASE_MODE = os.environ['RELEASE_MODE']

AWS_BUCKET = 'bluelens-style-model'
AWS_BUCKET_FOLDER = 'object_detection'
MODEL_FILE = 'object_detection_model.pb'

storage = S3(AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY)

file = os.path.join(os.getcwd(), MODEL_FILE)
key = os.path.join(AWS_BUCKET_FOLDER, RELEASE_MODE, MODEL_FILE)

try:
  storage.download_file_from_bucket(AWS_BUCKET, file, key)
except:
  print('download error')
