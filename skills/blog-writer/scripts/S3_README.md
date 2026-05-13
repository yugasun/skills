# S3 Deployment Skill

## Instructions

This skill handles uploading a local directory (e.g., generated slides) to an AWS S3 bucket or any S3-compatible object storage (e.g., MinIO, Aliyun OSS, Tencent COS) for static website hosting.

1.  **Prerequisites**:
    *   Ensure the user has valid credentials in their environment:
        *   `S3_ACCESS_KEY_ID`
        *   `S3_SECRET_ACCESS_KEY`
        *   `S3_BUCKET` (Optional if provided as an argument)
        *   `S3_REGION` (Optional)
        *   `S3_ENDPOINT_URL` (Required for non-AWS services like MinIO or Aliyun OSS)
        *   `S3_CUSTOM_DOMAIN` (Optional, overrides the generated URL)
    *   Ensure `boto3` is installed in the environment. If not, install it.
    *   Identify the source directory (e.g., `slides/<ppt-name>/dist/`) and the target S3 bucket name.

2.  **Implementation**:
    *   Create a Python script using `boto3` to walk through the source directory.
    *   Configure the S3 client with `endpoint_url` if provided, to support S3-compatible providers.
    *   Upload each file, maintaining the relative path structure.
    *   **Crucial**: specific `ContentType` must be set for each file based on its extension (e.g., `text/html` for `.html`, `text/css` for `.css`, `image/png` for `.png`) so that the browser renders it correctly.
    *   Make the objects public if the bucket policy allows or requires ACL (optional, based on bucket configuration).
    *   Print the final website URL.

## Usage

Use the bundled script to upload files:

```bash
# Explicit bucket name
uv run {baseDir}/scripts/upload_to_s3.py "dist" "my-bucket" --prefix "prefix/for/files"

# Using S3_BUCKET from environment
uv run {baseDir}/scripts/upload_to_s3.py "dist" --prefix "prefix/for/files"
```

## Usage Guidelines

*   **Bucket Name**: Check if `S3_BUCKET` is set in environment. If not, ask the user for the S3 Bucket name.
*   **Endpoint URL**: Check if the user is using a non-AWS provider (like MinIO or Aliyun). If so, request or verify the `endpoint_url`.
