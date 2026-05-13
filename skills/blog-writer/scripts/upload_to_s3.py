# /// script
# dependencies = [
#   "boto3",
# ]
# ///

import os
import sys
import argparse
import mimetypes
import json
import boto3
from botocore.exceptions import NoCredentialsError
from botocore.config import Config


class S3UploadError(RuntimeError):
    """Raised when an S3/OSS upload cannot be completed."""

def normalize_base_url(raw_url):
    if not raw_url:
        return None
    raw_url = raw_url.rstrip('/')
    if not raw_url.startswith('http://') and not raw_url.startswith('https://'):
        raw_url = f"https://{raw_url}"
    return raw_url


def normalize_endpoint_url(raw_url):
    return normalize_base_url(raw_url)


def build_public_base_url(bucket_name, endpoint_url=None, addressing_style='auto', public_base_url=None, custom_domain=None, region_name=None):
    public_base_url = normalize_base_url(public_base_url)
    if public_base_url:
        return public_base_url

    custom_domain = normalize_base_url(custom_domain)
    if custom_domain:
        return custom_domain

    if endpoint_url:
        base_url = endpoint_url.rstrip('/')
        if addressing_style == 'virtual':
            if '://' in base_url:
                scheme, host = base_url.split('://', 1)
                return f"{scheme}://{bucket_name}.{host}"
            return f"https://{bucket_name}.{base_url}"
        return f"{base_url}/{bucket_name}"

    region_name = region_name or 'us-east-1'
    return f"https://{bucket_name}.s3.{region_name}.amazonaws.com"


def build_public_url(base_url, s3_key):
    return f"{base_url.rstrip('/')}/{s3_key.lstrip('/')}"


def upload_to_s3(
    local_folder,
    bucket_name,
    s3_prefix='',
    endpoint_url=None,
    addressing_style='auto',
    signature_version=None,
    public_base_url=None,
    manifest_path=None,
):
    """
    Uploads a folder to S3 (or S3-compatible service) with correct MIME types.
    """
    # Allow configuration via environment variables or explicit arguments
    endpoint_url = normalize_endpoint_url(endpoint_url or os.getenv('S3_ENDPOINT_URL'))
    access_key = os.getenv('S3_ACCESS_KEY_ID')
    secret_key = os.getenv('S3_SECRET_ACCESS_KEY')
    region_name = os.getenv('S3_REGION')
    bucket_name = bucket_name or os.getenv('S3_BUCKET')
    custom_domain = os.getenv('S3_CUSTOM_DOMAIN')
    public_base_url = public_base_url or custom_domain or os.getenv('S3_PUBLIC_BASE_URL')

    if not bucket_name:
        raise ValueError(
            "Bucket name is required. Provide it as an argument or set S3_BUCKET env var."
        )

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
        if 's3' not in config_kwargs:
            config_kwargs['s3'] = {}
        config_kwargs['s3']['addressing_style'] = addressing_style
    if signature_version:
        config_kwargs['signature_version'] = signature_version
    
    if config_kwargs:
        s3_kwargs['config'] = Config(**config_kwargs)
        
    s3 = boto3.client('s3', **s3_kwargs)

    uploaded_files = []

    try:
        print(f"Starting upload to bucket: {bucket_name}")
        if endpoint_url:
            print(f"Using Endpoint: {endpoint_url}")
            if addressing_style == 'virtual':
                print("(Virtual Hosted Style enabled)")

        resolved_public_base_url = build_public_base_url(
            bucket_name,
            endpoint_url=endpoint_url,
            addressing_style=addressing_style,
            public_base_url=public_base_url,
            custom_domain=custom_domain,
            region_name=region_name,
        )
        print(f"Public Base URL: {resolved_public_base_url}")

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

                extra_args = {'ContentType': content_type}
                s3.upload_file(local_path, bucket_name, s3_path, ExtraArgs=extra_args)
                public_url = build_public_url(resolved_public_base_url, s3_path)
                uploaded_files.append(
                    {
                        'local_path': local_path,
                        'relative_path': relative_path.replace("\\", "/"),
                        's3_key': s3_path,
                        'public_url': public_url,
                    }
                )
                print(f"Public URL: {public_url}")

        print("Upload completed successfully.")

        if manifest_path:
            manifest_dir = os.path.dirname(manifest_path)
            if manifest_dir:
                os.makedirs(manifest_dir, exist_ok=True)
            with open(manifest_path, 'w', encoding='utf-8') as manifest_file:
                json.dump({'files': uploaded_files}, manifest_file, ensure_ascii=False, indent=2)
            print(f"Manifest written to: {manifest_path}")

        if uploaded_files:
            print("Uploaded file URL summary:")
            for item in uploaded_files:
                print(f"- {item['relative_path']} => {item['public_url']}")

        return {
            'bucket_name': bucket_name,
            'public_base_url': resolved_public_base_url,
            'files': uploaded_files,
            'manifest_path': manifest_path,
        }

    except NoCredentialsError as exc:
        raise S3UploadError("AWS credentials not found.") from exc
    except Exception as exc:
        if isinstance(exc, (ValueError, S3UploadError)):
            raise
        raise S3UploadError(f"An error occurred: {exc}") from exc


def build_parser():
    parser = argparse.ArgumentParser(description="Upload a folder to S3")
    parser.add_argument("local_folder", help="Path to the local folder to upload")
    parser.add_argument("bucket_name", nargs='?', help="Name of the S3 bucket")
    parser.add_argument("--prefix", default="", help="S3 prefix (folder) to upload to")
    parser.add_argument("--endpoint", help="S3 Endpoint URL (overrides env var)")
    parser.add_argument("--addressing-style", default="auto", choices=["auto", "virtual", "path"], help="S3 addressing style (auto, virtual, path)")
    parser.add_argument("--signature-version", default=None, help="AWS Signature Version (e.g. s3v4)")
    parser.add_argument("--public-base-url", default=None, help="Public base URL used to build file URLs (overrides S3_PUBLIC_BASE_URL / S3_CUSTOM_DOMAIN)")
    parser.add_argument("--manifest", default=None, help="Optional path to write uploaded file URLs as JSON")
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    try:
        upload_to_s3(
            args.local_folder,
            args.bucket_name,
            args.prefix,
            args.endpoint,
            args.addressing_style,
            args.signature_version,
            args.public_base_url,
            args.manifest,
        )
    except (ValueError, S3UploadError) as exc:
        print(f"Error: {exc}")
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
