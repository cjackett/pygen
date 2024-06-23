import json
import logging
import os
import time
from typing import Any, Dict

import boto3
from botocore.exceptions import BotoCoreError, ClientError
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class LLMClient:

    def __init__(self) -> None:
        self.logger = logging.getLogger(self.__class__.__name__)
        self.aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
        self.aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")

        if not self.aws_access_key_id or not self.aws_secret_access_key:
            raise EnvironmentError(
                "AWS credentials not found. Please add AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY to your "
                "environment variables or a .env file in the project root."
            )

        # self.model_name = "claude-3-opus"
        self.model_name = "claude-3-5-sonnet"
        self.max_tokens = 200000
        self.region_name = "us-east-1"
        self.model_id = f"anthropic.{self.model_name}-20240620-v1:0"
        self.brt = boto3.client(
            service_name="bedrock-runtime",
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
            region_name=self.region_name,
        )

    def invoke_model(self, prompt: str, retries: int = 5, base_delay: int = 1) -> None:
        for attempt in range(retries):
            try:
                body: str = json.dumps(
                    {
                        "max_tokens": self.max_tokens,
                        "messages": [{"role": "user", "content": prompt}],
                        "anthropic_version": "bedrock-2023-05-31",
                    }
                )

                response = self.brt.invoke_model(
                    body=body, modelId=self.model_id, accept="application/json", contentType="application/json"
                )
                response_body: Dict[str, Any] = json.loads(response.get("body").read())
                content = response_body.get("content")

                if content and isinstance(content, list) and len(content) > 0:
                    text = content[0].get("text")
                    if text and isinstance(text, str):
                        print(text)
                    else:
                        raise RuntimeError("Invalid response format: 'text' field is missing or not a string.")
                else:
                    raise RuntimeError("Invalid response format: 'content' field is missing or not a list.")

                return

            except (BotoCoreError, ClientError) as error:
                self.logger.warning(f"Attempt {attempt + 1} failed with error: {error}")
                if attempt < retries - 1:  # i.e., not last attempt
                    wait_time = base_delay * (2**attempt)
                    self.logger.info(f"Waiting {wait_time} seconds before retry...")
                    time.sleep(wait_time)
                else:
                    self.logger.error("Max retries reached, giving up.")
                    raise RuntimeError("Failed to invoke model after multiple retries")

    def invoke_model_with_response_stream(self, prompt: str) -> None:
        """
        Streams the response for a text prompt.
        Args:
            prompt (str): The prompt text.
        """
        try:
            body = json.dumps(
                {
                    "anthropic_version": "bedrock-2023-05-31",
                    "max_tokens": self.max_tokens,
                    "messages": [{"role": "user", "content": prompt}],
                }
            )

            response = self.brt.invoke_model_with_response_stream(body=body, modelId=self.model_id)

            for event in response.get("body"):
                chunk = json.loads(event["chunk"]["bytes"])

                if chunk["type"] == "content_block_delta" and chunk["delta"]["type"] == "text_delta":
                    print(chunk["delta"]["text"], end="")

                elif chunk["type"] == "message_delta":
                    self.logger.info(f"\nStop reason: {chunk['delta']['stop_reason']}")
                    self.logger.info(f"Stop sequence: {chunk['delta']['stop_sequence']}")
                    self.logger.info(f"Output tokens: {chunk['usage']['output_tokens']}")

        except (BotoCoreError, ClientError) as error:
            self.logger.error(f"Error occurred: {error}")
            raise RuntimeError("Failed to stream prompt")
