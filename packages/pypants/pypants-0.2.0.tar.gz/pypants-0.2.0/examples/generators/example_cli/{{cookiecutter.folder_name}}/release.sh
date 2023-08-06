#!/bin/bash
# Build and publish Pants binaries and update the registered version

set -e

PANTS_TARGET="{{ cookiecutter.build_dir }}"
BIN_NAME="{{ cookiecutter.binary_name }}"
BIN_VERSION="$(git rev-parse --short HEAD)"
PLATFORMS=({{ cookiecutter.platforms | replace(",", " ") }})

for platform in "${PLATFORMS[@]}"; do
  pexpm --platform "$platform" build "$BIN_NAME" "$PANTS_TARGET"
  pexpm --platform "$platform" publish "$BIN_NAME"
  pexpm --platform "$platform" install "${BIN_NAME}@${BIN_VERSION}" --save
done
