---
name: backend-ai
description: AI features using LiteLLM and Docling
---

# AI Integration

## Dependencies

```bash
uv add litellm docling
```

## LLM Interface (LiteLLM)

Use `litellm` as a unified interface for OpenAI, Anthropic, Azure, etc. This simplifies provider switching and cost tracking.

### Configuration

Ensure `src/core/config.py` loads necessary API keys (e.g., `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `ALIYUN_API_KEY`).

### Aliyun Bailian (Qwen) Support

To use Aliyun's Bailian platform via its OpenAI-compatible interface:

1.  Set `ALIYUN_API_KEY` in your `.env` file.
2.  Use the base URL: `https://dashscope.aliyuncs.com/compatible-mode/v1`.
3.  Use model names prefixed with `openai/` (e.g., `openai/qwen-max`) to force LiteLLM to use the OpenAI client.

```python
async def chat_with_qwen(text: str) -> str:
    response = await completion(
        model="openai/qwen-max",
        messages=[{"role": "user", "content": text}],
        api_key=settings.ALIYUN_API_KEY,
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
    )
    return response.choices[0].message.content
```

### Usage Example

```python
from litellm import completion
from src.core.config import settings

async def generate_summary(text: str) -> str:
    response = await completion(
        model="gpt-4o",
        messages=[{"role": "user", "content": f"Summarize this: {text}"}],
        api_key=settings.OPENAI_API_KEY
    )
    return response.choices[0].message.content
```

## Document Processing (Docling)

Use `docling` for robust document parsing (PDF, DOCX, HTML) into structured Markdown or JSON.

### Usage Example

```python
from docling.document_converter import DocumentConverter

def parse_document(file_path: str) -> str:
    converter = DocumentConverter()
    result = converter.convert(file_path)
    return result.document.export_to_markdown()
```

For async contexts, you might need to run blocking Docling calls in a thread pool:

```python
import asyncio
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor()

async def parse_document_async(file_path: str) -> str:
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(executor, parse_document, file_path)
```
