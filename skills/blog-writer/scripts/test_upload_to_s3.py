import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from upload_to_s3 import upload_to_s3


class UploadToS3Tests(unittest.TestCase):
    def test_custom_domain_takes_precedence_for_public_urls(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            image_path = Path(tmp_dir) / "ai-efficient-but-work-more_mermaid_1.png"
            image_path.write_bytes(b"png")

            mock_client = MagicMock()

            with patch.dict(
                "os.environ",
                {
                    "S3_PUBLIC_BASE_URL": "https://public-base.example.com",
                    "S3_CUSTOM_DOMAIN": "https://slides.yugasun.com",
                },
                clear=False,
            ), patch("upload_to_s3.boto3.client", return_value=mock_client):
                result = upload_to_s3(
                    tmp_dir,
                    "aislides",
                    s3_prefix="blogs/ai-efficient-but-work-more",
                )

        self.assertEqual(result["public_base_url"], "https://slides.yugasun.com")
        self.assertEqual(
            result["files"][0]["public_url"],
            "https://slides.yugasun.com/blogs/ai-efficient-but-work-more/ai-efficient-but-work-more_mermaid_1.png",
        )


if __name__ == "__main__":
    unittest.main()