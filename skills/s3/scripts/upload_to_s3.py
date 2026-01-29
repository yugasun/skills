# /// script
# dependencies = [
#   "boto3",
# ]
# ///

import os
import sys
import argparse
import mimetypes
import boto3
from botocore.exceptions import NoCredentialsError
from botocore.config import Config

def upload_to_s3(local_folder, bucket_name, s3_prefix='', endpoint_url=None, addressing_style='auto', signature_version=None):
    """
    Uploads a folder to S3 (or S3-compatible service) with correct MIME types.
    """
    # Allow configuration via environment variables or explicit arguments
    endpoint_url = endpoint_url or os.getenv('S3_ENDPOINT_URL')
    access_key = os.getenv('S3_ACCESS_KEY_ID')
    secret_key = os.getenv('S3_SECRET_ACCESS_KEY')
    region_name = os.getenv('S3_REGION')
    bucket_name = bucket_name or os.getenv('S3_BUCKET')

    if not bucket_name:
        print("Error: Bucket name is required. Provide it as an argument or set S3_BUCKET env var.")
        sys.exit(1)

    s3_kwargs = {}
    if endpoint_url:
        s3_kwargs['endpoint_url'] = endpoint_url
    if region_name:
        s3_kwargs['region_name'] = region_name
    if access_key and secret_key:
        s3_kwargs['aws_access_key_id'] = access_key
        s3_kwargs['aws_secret_access_key'] = secret_key
    
    config_kwargs = {}
    if addressing_style:
        if 's3' not in config_kwargs: config_kwargs['s3'] = {}
        config_kwargs['s3']['addressing_style'] = addressing_style
    if signature_version:
        config_kwargs['signature_version'] = signature_version
    
    if config_kwargs:
        s3_kwargs['config'] = Config(**config_kwargs)
        
    s3 = boto3.client('s3', **s3_kwargs)

    try:
        print(f"Starting upload to bucket: {bucket_name}")
        if endpoint_url:
            print(f"Using Endpoint: {endpoint_url}")
            if addressing_style == 'virtual':
                 print("(Virtual Hosted Style enabled)")

        for root, dirs, files in os.walk(local_folder):
            for filename in files:
                local_path = os.path.join(root, filename)
                relative_path = os.path.relpath(local_path, local_folder)
                s3_path = os.path.join(s3_prefix, relative_path).replace("\\", "/")
                
                # Remove leading slashes from s3_path if present to avoid empty folders
                s3_path = s3_path.lstrip('/')

                content_type, _ = mimetypes.guess_type(local_path)
                if content_type is None:
                    content_type = 'application/octet-stream'

                print(f"Uploading {local_path} to s3://{bucket_name}/{s3_path} ({content_type})...")
                
                # Extra args for public read or content type
                extra_args = {'ContentType': content_type}
                # Uncomment the following line if the bucket requires explicit ACL for public access
                # extra_args['ACL'] = 'public-read'

                s3.upload_file(local_path, bucket_name, s3_path, ExtraArgs=extra_args)

        print("Upload completed successfully.")
        
        custom_domain = os.getenv('S3_CUSTOM_DOMAIN')

        if custom_domain:
            custom_domain = custom_domain.rstrip('/')
            if not custom_domain.startswith('http'):
                custom_domain = f"https://{custom_domain}"
            print(f"Access your files at: {custom_domain}/{s3_prefix}/index.html")

        # Construct and print the URL
        elif endpoint_url:
            base_url = endpoint_url.rstrip('/')
            if addressing_style == 'virtual':
                # Try to inject bucket into hostname
                if '://' in base_url:
                    parts = base_url.split('://')
                    base_url = f"{parts[0]}://{bucket_name}.{parts[1]}"
                else:
                    base_url = f"https://{bucket_name}.{base_url}"
                print(f"Access your files at: {base_url}/{s3_prefix}/index.html")
            else:
                # S3 Compatible (Path Style fallback: {endpoint}/{bucket}/{key})
                print(f"Access your files at: {base_url}/{bucket_name}/{s3_prefix}/index.html")
        else:
            # AWS Standard
            region = s3.meta.region_name
            if not region:
                 region = 'us-east-1'
            print(f"Access your files at: https://{bucket_name}.s3.{region}.amazonaws.com/{s3_prefix}/index.html")

    except NoCredentialsError:
        print("Error: AWS credentials not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload a folder to S3")
    parser.add_argument("local_folder", help="Path to the local folder to upload")
    parser.add_argument("bucket_name", nargs='?', help="Name of the S3 bucket")
    parser.add_argument("--prefix", default="", help="S3 prefix (folder) to upload to")
    parser.add_argument("--endpoint", help="S3 Endpoint URL (overrides env var)")
    parser.add_argument("--addressing-style", default="auto", choices=["auto", "virtual", "path"], help="S3 addressing style (auto, virtual, path)")
    parser.add_argument("--signature-version", default=None, help="AWS Signature Version (e.g. s3v4)")

    args = parser.parse_args()

    upload_to_s3(args.local_folder, args.bucket_name, args.prefix, args.endpoint, args.addressing_style, args.signature_version)
