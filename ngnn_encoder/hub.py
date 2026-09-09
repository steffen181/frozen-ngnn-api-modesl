"""Verified local and Hugging Face Hub loading for the NGNN encoder."""

from __future__ import annotations

import json
from pathlib import Path
import re
from typing import Any

import torch

from ngnn_general_encoder import (
    ARTIFACT_SHA256,
    MODEL_NAME,
    MODEL_REVISION,
    NgnnGeneralEncoder as _StandaloneEncoder,
    NgnnGeneralEncoderError,
)


MODEL_CONFIG = {
    "schema_version": 1,
    "model_name": MODEL_NAME,
    "model_revision": MODEL_REVISION,
    "artifact_file": "model.npz",
    "artifact_sha256": ARTIFACT_SHA256,
    "base_model": "text-embedding-3-large",
    "input_dim": 3072,
    "output_dim": 512,
    "torch_version": "2.11.0",
    "top_k": 256,
}

_CONFIG_TYPES = {
    "schema_version": int,
    "model_name": str,
    "model_revision": str,
    "artifact_file": str,
    "artifact_sha256": str,
    "base_model": str,
    "input_dim": int,
    "output_dim": int,
    "torch_version": str,
    "top_k": int,
}
_SHA_REVISION = re.compile(r"[0-9a-f]{40}\Z")


def _require_torch_version() -> None:
    installed = torch.__version__.split("+", 1)[0]
    if installed != MODEL_CONFIG["torch_version"]:
        raise NgnnGeneralEncoderError("NGNN inference requires torch==2.11.0")


def _load_config(path: str | Path) -> None:
    try:
        value = json.loads(Path(path).read_text(encoding="utf-8"))
    except Exception:
        raise NgnnGeneralEncoderError("Could not load NGNN model config") from None
    if type(value) is not dict or set(value) != set(MODEL_CONFIG):
        raise NgnnGeneralEncoderError("NGNN model config does not match this release")
    for key, expected in MODEL_CONFIG.items():
        if type(value[key]) is not _CONFIG_TYPES[key] or value[key] != expected:
            raise NgnnGeneralEncoderError("NGNN model config does not match this release")


class NgnnGeneralEncoder(_StandaloneEncoder):
    """Standalone encoder with runtime compatibility and verified Hub loading."""

    def __init__(
        self,
        artifact_path: str | Path,
        *,
        api_key: str | None = None,
        client: Any | None = None,
        provider_batch_size: int = 100,
    ) -> None:
        _require_torch_version()
        super().__init__(
            artifact_path,
            api_key=api_key,
            client=client,
            provider_batch_size=provider_batch_size,
        )

    @classmethod
    def from_pretrained(
        cls,
        repo_id: str,
        *,
        revision: str,
        cache_dir: str | Path | None = None,
        local_files_only: bool = False,
        client: Any | None = None,
        provider_batch_size: int = 100,
    ) -> NgnnGeneralEncoder:
        if type(revision) is not str or _SHA_REVISION.fullmatch(revision) is None:
            raise NgnnGeneralEncoderError(
                "revision must be a 40-character lowercase commit SHA"
            )
        try:
            from huggingface_hub import hf_hub_download

            config_path = hf_hub_download(
                repo_id=repo_id,
                filename="config.json",
                revision=revision,
                cache_dir=cache_dir,
                local_files_only=local_files_only,
                token=False,
            )
        except Exception:
            raise NgnnGeneralEncoderError("Could not download NGNN model config") from None
        _load_config(config_path)
        try:
            artifact_path = hf_hub_download(
                repo_id=repo_id,
                filename=MODEL_CONFIG["artifact_file"],
                revision=revision,
                cache_dir=cache_dir,
                local_files_only=local_files_only,
                token=False,
            )
        except Exception:
            raise NgnnGeneralEncoderError("Could not download NGNN model artifact") from None
        return cls(
            artifact_path,
            client=client,
            provider_batch_size=provider_batch_size,
        )
