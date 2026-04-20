import importlib.util
import os
import pathlib
import unittest
from unittest import mock


MODULE_PATH = (
    pathlib.Path(__file__).resolve().parents[1] / "scripts" / "aliyun_image_gen.py"
)


def load_module():
    spec = importlib.util.spec_from_file_location("aliyun_image_gen", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class AliyunImageGenScriptTests(unittest.TestCase):
    def test_api_key_falls_back_to_aliyun_env_var(self):
        module = load_module()

        with mock.patch.dict(
            os.environ,
            {"ALIYUN_API_KEY": "sk-from-aliyun-env"},
            clear=True,
        ):
            self.assertEqual(
                module.require_api_key(None),
                "sk-from-aliyun-env",
            )

    def test_sync_payload_uses_multimodal_message_shape(self):
        module = load_module()

        payload = module.build_sync_payload(
            model="qwen-image-2.0-pro",
            prompt="一个极简海报，中心是一只白色纸鹤",
            negative_prompt="低清晰度",
            size="1024*1024",
            image_count=2,
            watermark=False,
            prompt_extend=True,
        )

        self.assertEqual(payload["model"], "qwen-image-2.0-pro")
        self.assertEqual(payload["input"]["messages"][0]["role"], "user")
        self.assertEqual(
            payload["input"]["messages"][0]["content"][0]["text"],
            "一个极简海报，中心是一只白色纸鹤",
        )
        self.assertEqual(payload["parameters"]["negative_prompt"], "低清晰度")
        self.assertEqual(payload["parameters"]["size"], "1024*1024")
        self.assertEqual(payload["parameters"]["n"], 2)
        self.assertFalse(payload["parameters"]["watermark"])
        self.assertTrue(payload["parameters"]["prompt_extend"])

    def test_async_payload_uses_prompt_shape(self):
        module = load_module()

        payload = module.build_async_payload(
            model="qwen-image-plus",
            prompt="一张写实风格的城市夜景",
            negative_prompt=None,
            size="1664*928",
            image_count=1,
            watermark=False,
            prompt_extend=False,
        )

        self.assertEqual(payload["model"], "qwen-image-plus")
        self.assertEqual(payload["input"]["prompt"], "一张写实风格的城市夜景")
        self.assertNotIn("negative_prompt", payload["input"])
        self.assertEqual(payload["parameters"]["size"], "1664*928")
        self.assertEqual(payload["parameters"]["n"], 1)
        self.assertFalse(payload["parameters"]["watermark"])
        self.assertFalse(payload["parameters"]["prompt_extend"])

    def test_extract_sync_image_urls(self):
        module = load_module()

        urls = module.extract_sync_image_urls(
            {
                "output": {
                    "choices": [
                        {
                            "message": {
                                "content": [
                                    {"image": "https://example.com/a.png"},
                                    {"image": "https://example.com/b.png"},
                                ]
                            }
                        }
                    ]
                }
            }
        )

        self.assertEqual(
            urls,
            ["https://example.com/a.png", "https://example.com/b.png"],
        )

    def test_extract_async_image_urls(self):
        module = load_module()

        urls = module.extract_async_image_urls(
            {
                "output": {
                    "results": [
                        {"url": "https://example.com/task-1.png"},
                        {"url": "https://example.com/task-2.png"},
                    ]
                }
            }
        )

        self.assertEqual(
            urls,
            ["https://example.com/task-1.png", "https://example.com/task-2.png"],
        )

    def test_region_urls_match_documented_endpoints(self):
        module = load_module()

        self.assertEqual(
            module.get_base_url("beijing"),
            "https://dashscope.aliyuncs.com/api/v1",
        )
        self.assertEqual(
            module.get_base_url("singapore"),
            "https://dashscope-intl.aliyuncs.com/api/v1",
        )


if __name__ == "__main__":
    unittest.main()