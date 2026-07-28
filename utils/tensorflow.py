"""TensorFlow import configured for stable InkSight inference."""

from __future__ import annotations

import importlib
import os
import shlex

_INCOMPATIBLE_XLA_PASSES = (
    "custom-kernel-fusion-rewriter",
    "custom_kernel-fusion-autotuner",
)


def _configure_xla_flags() -> None:
    tokens = shlex.split(os.environ.get("XLA_FLAGS", ""))
    disabled_passes: list[str] = []
    preserved_flags: list[str] = []

    for token in tokens:
        if token.startswith("--xla_disable_hlo_passes="):
            disabled_passes.extend(token.partition("=")[2].split(","))
        elif not token.startswith("--xla_gpu_autotune_level="):
            preserved_flags.append(token)

    for pass_name in _INCOMPATIBLE_XLA_PASSES:
        if pass_name not in disabled_passes:
            disabled_passes.append(pass_name)

    preserved_flags.extend(
        (
            "--xla_gpu_autotune_level=0",
            "--xla_disable_hlo_passes=" + ",".join(filter(None, disabled_passes)),
        )
    )
    os.environ["XLA_FLAGS"] = shlex.join(preserved_flags)


_configure_xla_flags()

# These modules must load after the XLA configuration.
tf = importlib.import_module("tensorflow")
tf_text = importlib.import_module("tensorflow_text")

__all__ = ["tf", "tf_text"]
