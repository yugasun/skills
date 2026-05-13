#!/usr/bin/env python3
"""Aliyun Bailian Qwen-Image text-to-image helper.

Uses the documented HTTP APIs directly so the script works in a clean Python
environment without extra SDK dependencies.
"""

from __future__ import annotations

import argparse
import json
import os
import pathlib
import sys
import time
from typing import Any
from urllib import error, parse, request

from upload_to_s3 import upload_to_s3 as upload_folder_to_s3


REGION_BASE_URLS = {
    "beijing": "https://dashscope.aliyuncs.com/api/v1",
    "singapore": "https://dashscope-intl.aliyuncs.com/api/v1",
}

SYNC_PATH = "/services/aigc/multimodal-generation/generation"
ASYNC_SUBMIT_PATH = "/services/aigc/text2image/image-synthesis"
ASYNC_SUPPORTED_MODELS = {"qwen-image", "qwen-image-plus"}


class DashScopeApiError(RuntimeError):
    def __init__(self, status_code: int, message: str, payload: dict[str, Any] | None = None):
        super().__init__(message)
        self.status_code = status_code
        self.payload = payload or {}


def get_base_url(region: str) -> str:
    normalized = region.strip().lower()
    try:
        return REGION_BASE_URLS[normalized]
    except KeyError as exc:
        supported = ", ".join(sorted(REGION_BASE_URLS))
        raise ValueError(f"Unsupported region '{region}'. Choose one of: {supported}") from exc


def build_sync_payload(
    *,
    model: str,
    prompt: str,
    negative_prompt: str | None,
    size: str | None,
    image_count: int,
    watermark: bool,
    prompt_extend: bool,
) -> dict[str, Any]:
    parameters: dict[str, Any] = {
        "n": image_count,
        "watermark": watermark,
        "prompt_extend": prompt_extend,
    }
    if negative_prompt:
        parameters["negative_prompt"] = negative_prompt
    if size:
        parameters["size"] = size

    return {
        "model": model,
        "input": {
            "messages": [
                {
                    "role": "user",
                    "content": [{"text": prompt}],
                }
            ]
        },
        "parameters": parameters,
    }


def build_async_payload(
    *,
    model: str,
    prompt: str,
    negative_prompt: str | None,
    size: str | None,
    image_count: int,
    watermark: bool,
    prompt_extend: bool,
) -> dict[str, Any]:
    input_data: dict[str, Any] = {"prompt": prompt}
    if negative_prompt:
        input_data["negative_prompt"] = negative_prompt

    parameters: dict[str, Any] = {
        "n": image_count,
        "watermark": watermark,
        "prompt_extend": prompt_extend,
    }
    if size:
        parameters["size"] = size

    return {
        "model": model,
        "input": input_data,
        "parameters": parameters,
    }


def extract_sync_image_urls(response: dict[str, Any]) -> list[str]:
    urls: list[str] = []
    for choice in response.get("output", {}).get("choices", []):
        content = choice.get("message", {}).get("content", [])
        for item in content:
            image_url = item.get("image")
            if image_url:
                urls.append(image_url)
    return urls


def extract_async_image_urls(response: dict[str, Any]) -> list[str]:
    urls: list[str] = []
    for result in response.get("output", {}).get("results", []):
        image_url = result.get("url")
        if image_url:
            urls.append(image_url)
    return urls


def request_json(
    *,
    method: str,
    url: str,
    api_key: str,
    payload: dict[str, Any] | None = None,
    extra_headers: dict[str, str] | None = None,
    timeout: int = 300,
) -> dict[str, Any]:
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    if extra_headers:
        headers.update(extra_headers)

    body = None
    if payload is not None:
        body = json.dumps(payload).encode("utf-8")

    req = request.Request(url, data=body, headers=headers, method=method)
    try:
        with request.urlopen(req, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        parsed: dict[str, Any] | None = None
        message = raw
        try:
            parsed_json = json.loads(raw)
            if isinstance(parsed_json, dict):
                parsed = parsed_json
                message = parsed.get("message") or parsed.get("code") or raw
        except json.JSONDecodeError:
            parsed = None
        raise DashScopeApiError(exc.code, message, parsed) from exc


def require_api_key(cli_value: str | None) -> str:
    api_key = cli_value or os.getenv("ALIYUN_API_KEY") or os.getenv("DASHSCOPE_API_KEY")
    if not api_key:
        raise ValueError(
            "Missing API key. Pass --api-key or set ALIYUN_API_KEY or DASHSCOPE_API_KEY."
        )
    return api_key


def validate_async_model(model: str) -> None:
    if model not in ASYNC_SUPPORTED_MODELS:
        supported = ", ".join(sorted(ASYNC_SUPPORTED_MODELS))
        raise ValueError(
            f"Async mode currently supports only: {supported}. Received: {model}"
        )


def get_task_status(*, region: str, api_key: str, task_id: str) -> dict[str, Any]:
    base_url = get_base_url(region)
    return request_json(
        method="GET",
        url=f"{base_url}/tasks/{task_id}",
        api_key=api_key,
    )


def wait_for_task(
    *,
    region: str,
    api_key: str,
    task_id: str,
    poll_interval: int,
    max_polls: int,
) -> dict[str, Any]:
    for _ in range(max_polls):
        response = get_task_status(region=region, api_key=api_key, task_id=task_id)
        status = response.get("output", {}).get("task_status")
        if status in {"SUCCEEDED", "FAILED", "CANCELED", "UNKNOWN"}:
            return response
        time.sleep(poll_interval)
    raise TimeoutError(
        f"Task {task_id} did not finish after {max_polls} polls with interval {poll_interval}s"
    )


def build_output_path(output_dir: pathlib.Path, prefix: str, index: int, url: str) -> pathlib.Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    url_path = parse.unquote(parse.urlparse(url).path)
    filename = pathlib.PurePosixPath(url_path).name or f"{prefix}-{index}.png"
    if filename in {"", "/"}:
        filename = f"{prefix}-{index}.png"
    if index > 1 and filename == pathlib.PurePosixPath(url_path).name:
        stem = pathlib.Path(filename).stem
        suffix = pathlib.Path(filename).suffix or ".png"
        filename = f"{stem}-{index}{suffix}"
    return output_dir / filename


def download_images(urls: list[str], output_dir: str, prefix: str = "aliyun-image") -> list[str]:
    saved_files: list[str] = []
    target_dir = pathlib.Path(output_dir)
    for index, image_url in enumerate(urls, start=1):
        target_path = build_output_path(target_dir, prefix, index, image_url)
        with request.urlopen(image_url, timeout=300) as response:
            target_path.write_bytes(response.read())
        saved_files.append(str(target_path))
    return saved_files


def format_summary(response: dict[str, Any], urls: list[str], saved_files: list[str] | None = None) -> str:
    output = response.get("output", {})
    usage = response.get("usage", {})
    lines = []

    if output.get("task_id"):
        lines.append(f"task_id: {output['task_id']}")
    if output.get("task_status"):
        lines.append(f"task_status: {output['task_status']}")
    if response.get("request_id"):
        lines.append(f"request_id: {response['request_id']}")
    if usage:
        lines.append(f"usage: {json.dumps(usage, ensure_ascii=False)}")
    if urls:
        lines.append("image_urls:")
        lines.extend(f"- {item}" for item in urls)
    if saved_files:
        lines.append("saved_files:")
        lines.extend(f"- {item}" for item in saved_files)

    return "\n".join(lines)


def validate_upload_args(args: argparse.Namespace) -> None:
    if getattr(args, "upload_to_oss", False) and not getattr(args, "download", False):
        raise ValueError("--upload-to-oss requires --download so local files exist before upload.")


def collect_remote_urls(saved_files: list[str], upload_result: dict[str, Any] | None) -> list[str]:
    if not upload_result:
        return []

    url_by_local_path = {}
    url_by_relative_path = {}
    url_by_basename = {}
    for item in upload_result.get("files", []):
        public_url = item.get("public_url")
        if not public_url:
            continue

        local_path = item.get("local_path")
        relative_path = item.get("relative_path")
        if local_path:
            url_by_local_path[local_path] = public_url
        if relative_path:
            normalized_relative_path = relative_path.replace("\\", "/")
            url_by_relative_path[normalized_relative_path] = public_url
            url_by_basename[pathlib.PurePosixPath(normalized_relative_path).name] = public_url

    remote_urls: list[str] = []
    for saved_file in saved_files:
        normalized_saved_file = saved_file.replace("\\", "/")
        public_url = url_by_local_path.get(saved_file)
        if not public_url:
            public_url = url_by_relative_path.get(pathlib.PurePosixPath(normalized_saved_file).name)
        if not public_url:
            public_url = url_by_basename.get(pathlib.PurePosixPath(normalized_saved_file).name)
        if public_url:
            remote_urls.append(public_url)
    return remote_urls


def upload_generated_images(args: argparse.Namespace, saved_files: list[str]) -> dict[str, Any] | None:
    if not getattr(args, "upload_to_oss", False) or not saved_files:
        return None

    return upload_folder_to_s3(
        local_folder=args.output_dir,
        bucket_name=getattr(args, "upload_bucket", None),
        s3_prefix=getattr(args, "upload_prefix", "") or "",
        endpoint_url=getattr(args, "upload_endpoint", None),
        addressing_style=getattr(args, "upload_addressing_style", "auto"),
        signature_version=getattr(args, "upload_signature_version", None),
        public_base_url=getattr(args, "upload_public_base_url", None),
        manifest_path=getattr(args, "upload_manifest", None),
    )


def run_generate(args: argparse.Namespace) -> dict[str, Any]:
    validate_upload_args(args)
    api_key = require_api_key(args.api_key)
    base_url = get_base_url(args.region)
    prompt_extend = not args.no_prompt_extend

    if args.mode == "sync":
        payload = build_sync_payload(
            model=args.model,
            prompt=args.prompt,
            negative_prompt=args.negative_prompt,
            size=args.size,
            image_count=args.image_count,
            watermark=args.watermark,
            prompt_extend=prompt_extend,
        )
        response = request_json(
            method="POST",
            url=f"{base_url}{SYNC_PATH}",
            api_key=api_key,
            payload=payload,
        )
        urls = extract_sync_image_urls(response)
    else:
        validate_async_model(args.model)
        payload = build_async_payload(
            model=args.model,
            prompt=args.prompt,
            negative_prompt=args.negative_prompt,
            size=args.size,
            image_count=args.image_count,
            watermark=args.watermark,
            prompt_extend=prompt_extend,
        )
        response = request_json(
            method="POST",
            url=f"{base_url}{ASYNC_SUBMIT_PATH}",
            api_key=api_key,
            payload=payload,
            extra_headers={"X-DashScope-Async": "enable"},
        )
        urls = []
        if args.wait:
            task_id = response.get("output", {}).get("task_id")
            if not task_id:
                raise ValueError("Async submit succeeded but no task_id was returned.")
            response = wait_for_task(
                region=args.region,
                api_key=api_key,
                task_id=task_id,
                poll_interval=args.poll_interval,
                max_polls=args.max_polls,
            )
            urls = extract_async_image_urls(response)

    saved_files: list[str] = []
    if args.download and urls:
        saved_files = download_images(urls, args.output_dir)

    upload_result = upload_generated_images(args, saved_files)
    remote_urls = collect_remote_urls(saved_files, upload_result)

    return {
        "response": response,
        "urls": urls,
        "saved_files": saved_files,
        "upload_result": upload_result,
        "remote_urls": remote_urls,
    }


def run_status(args: argparse.Namespace) -> dict[str, Any]:
    validate_upload_args(args)
    api_key = require_api_key(args.api_key)
    response = get_task_status(region=args.region, api_key=api_key, task_id=args.task_id)
    urls = extract_async_image_urls(response)

    saved_files: list[str] = []
    if args.download and urls:
        saved_files = download_images(urls, args.output_dir)

    upload_result = upload_generated_images(args, saved_files)
    remote_urls = collect_remote_urls(saved_files, upload_result)

    return {
        "response": response,
        "urls": urls,
        "saved_files": saved_files,
        "upload_result": upload_result,
        "remote_urls": remote_urls,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Aliyun Bailian Qwen-Image text-to-image helper",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s generate "一张极简白底海报，中间是一只蓝色纸鹤" --download
  %(prog)s generate "一张写实风格的咖啡店照片" --mode async --model qwen-image-plus --wait
  %(prog)s status <task_id> --download

Environment:
    ALIYUN_API_KEY      Preferred Aliyun Bailian API key for the selected region
    DASHSCOPE_API_KEY   Backward-compatible environment variable name
        """,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    generate = subparsers.add_parser("generate", help="Generate image(s) from a prompt")
    generate.add_argument("prompt", help="Text prompt for image generation")
    generate.add_argument("--mode", choices=["sync", "async"], default="sync")
    generate.add_argument("--model", default="qwen-image-2.0-pro")
    generate.add_argument("--region", choices=sorted(REGION_BASE_URLS), default="beijing")
    generate.add_argument("--api-key", help="Aliyun Bailian API key")
    generate.add_argument("--negative-prompt")
    generate.add_argument("--size", help="Image size like 1024*1024 or 1664*928")
    generate.add_argument("--image-count", type=int, default=1)
    generate.add_argument("--watermark", action="store_true")
    generate.add_argument("--no-prompt-extend", action="store_true")
    generate.add_argument("--wait", action="store_true", help="Poll async tasks until completion")
    generate.add_argument("--poll-interval", type=int, default=10)
    generate.add_argument("--max-polls", type=int, default=30)
    generate.add_argument("--download", action="store_true")
    generate.add_argument("--output-dir", default="generated-images")
    generate.add_argument("--upload-to-oss", action="store_true", help="Upload downloaded images to OSS/S3-compatible storage after generation")
    generate.add_argument("--upload-bucket", help="Override S3_BUCKET for OSS upload")
    generate.add_argument("--upload-prefix", default="", help="S3/OSS prefix for uploaded generated images")
    generate.add_argument("--upload-endpoint", help="Override S3_ENDPOINT_URL for OSS upload")
    generate.add_argument("--upload-addressing-style", choices=["auto", "virtual", "path"], default="auto")
    generate.add_argument("--upload-signature-version", help="Override signature version for OSS upload")
    generate.add_argument("--upload-public-base-url", help="Public base URL or CDN domain for final image URLs")
    generate.add_argument("--upload-manifest", help="Optional JSON manifest path for uploaded image URLs")
    generate.add_argument("--json", action="store_true")
    generate.set_defaults(handler=run_generate)

    status = subparsers.add_parser("status", help="Fetch async task status/result by task ID")
    status.add_argument("task_id", help="Aliyun Bailian async task ID")
    status.add_argument("--region", choices=sorted(REGION_BASE_URLS), default="beijing")
    status.add_argument("--api-key", help="Aliyun Bailian API key")
    status.add_argument("--download", action="store_true")
    status.add_argument("--output-dir", default="generated-images")
    status.add_argument("--upload-to-oss", action="store_true", help="Upload downloaded images to OSS/S3-compatible storage after status fetch")
    status.add_argument("--upload-bucket", help="Override S3_BUCKET for OSS upload")
    status.add_argument("--upload-prefix", default="", help="S3/OSS prefix for uploaded generated images")
    status.add_argument("--upload-endpoint", help="Override S3_ENDPOINT_URL for OSS upload")
    status.add_argument("--upload-addressing-style", choices=["auto", "virtual", "path"], default="auto")
    status.add_argument("--upload-signature-version", help="Override signature version for OSS upload")
    status.add_argument("--upload-public-base-url", help="Public base URL or CDN domain for final image URLs")
    status.add_argument("--upload-manifest", help="Optional JSON manifest path for uploaded image URLs")
    status.add_argument("--json", action="store_true")
    status.set_defaults(handler=run_status)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        result = args.handler(args)
    except (ValueError, TimeoutError, DashScopeApiError) as exc:
        if isinstance(exc, DashScopeApiError):
            print(f"HTTP {exc.status_code}: {exc}", file=sys.stderr)
            if exc.payload:
                print(json.dumps(exc.payload, ensure_ascii=False, indent=2), file=sys.stderr)
        else:
            print(str(exc), file=sys.stderr)
        return 1

    response = result["response"]
    urls = result["urls"]
    saved_files = result["saved_files"]
    remote_urls = result.get("remote_urls", [])
    upload_result = result.get("upload_result")

    if getattr(args, "json", False):
        payload = {
            "response": response,
            "image_urls": urls,
            "saved_files": saved_files,
            "remote_urls": remote_urls,
            "upload_result": upload_result,
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(format_summary(response, urls, saved_files or None))
        if remote_urls:
            print("remote_urls:")
            for item in remote_urls:
                print(f"- {item}")

    return 0


if __name__ == "__main__":
    sys.exit(main())