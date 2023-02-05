import os
import boto3
from PIL import Image
from io import BytesIO
import numpy as np
import matplotlib.pyplot as plt
import pathlib
from Constants import const

from Scripts.Utility import utils
from Constants import const



class AWS_S3BucketConnection:

    def __init__(self, server):
        # aws_key = utils.configuration["aws_s3_bucket_connection"]["access_key_id"]
        # aws_secret = utils.configuration['aws_s3_bucket_connection']['secret_access_key']
        # bucket_name = utils.configuration['aws_s3_bucket_connection']['bucket_name']
        # region = utils.configuration['aws_s3_bucket_connection']['region']

        self.aws_key = utils.configuration["aws_s3_bucket_connection"][server]["aws_access_key_id"]
        self.aws_secret = utils.configuration['aws_s3_bucket_connection'][server]['aws_secret_access_key']
        self.bucket_name = utils.configuration['aws_s3_bucket_connection'][server]['bucket_name']
        self.region_name = utils.configuration['aws_s3_bucket_connection'][server]['region']


    def download_single_test_image_from_s3Bucket(self, s3_image_key, dest_dir):
        s3_client = boto3.client("s3", aws_access_key_id=self.aws_key, aws_secret_access_key=self.aws_secret)
        bucket_name = self.bucket_name
        #s3_client = boto3.client('s3')
        try:
            # s3_image_url = os.path.join(const.aws_s3Bucket_url, s3_image_key)
            dest_file_name = os.path.join(dest_dir, s3_image_key)

            # If s3_image_key devoid of image file extension then append '.jpg' file extension to "dest_file_name" before downloading to local directory.
            # This appending is required because openCV image resize is possible for valid file image file extension only.
            if not pathlib.Path(dest_file_name).suffix in const.image_file_extention:
                dest_file_name += ".jpg"

            # s3_image_key = "/".join(s3_image_url.rsplit("/")[3:])
            # if s3_image_key.split(".")[-1] in (const.image_file_extention):
            s3_client.download_file(bucket_name, s3_image_key, dest_file_name)
            return dest_file_name, True

        except Exception as e:
            utils.logger.exception("__Error while downloading from S3 Bucket__" + str(e))
            return False, None



    def read_image_from_s3_bucket(self, key):
        """Load image file from s3.

        Parameters
        ----------
        bucket_name: string
            Bucket name
        key : string
            Path in s3

        Returns
        -------
        np array
            Image array
        """
        try:
            region_name = "ap-south-1"
            s3_resource = boto3.resource("s3", aws_access_key_id=self.aws_key, aws_secret_access_key=self.aws_secret, region_name=self.region_name)
            bucket = s3_resource.Bucket(self.bucket_name)
            img_object = bucket.Object(key)
            response = img_object.get()
            file_stream = response["Body"]
            im = Image.open(file_stream)

            # plt.figure(0)
            # plt.imshow(im)

            return np.array(im)
        except Exception as e:
            utils.logger.exception("--ERROR--: read_image_from_s3_bucket" + str(e))


    def write_image_to_s3_bucket(self, img_array, bucket, key):
        """Write an image array into S3 bucket

        Parameters
        ----------
        bucket: string
            Bucket name
        key : string
            Path in s3

        Returns
        -------
        None
        """
        try:

            region_name = "ap-south-1"
            s3 = boto3.resource('s3', region_name=region_name)
            bucket = s3.Bucket(bucket)
            object = bucket.Object(key)
            file_stream = BytesIO()
            im = Image.fromarray(img_array)
            im.save(file_stream, format='jpeg')
        except Exception as e:
            utils.logger.exception("--ERROR--: write_image_to_s3_bucket" + str(e))