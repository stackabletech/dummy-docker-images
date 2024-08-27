# Actions

This repository contains various reusable actions which encapsulate series of
commands to run a particular step in a workflow. Currently, the following actions
are available:

## `build`

> 

This action builds a *single* container image using `bake`. It does the
following work:

1. Free disk space to avoid running out of disk space during larger builds.
2. Build the image using `bake` which internally uses `docker buildx`.
3. Extract output values to be used in next steps.

This action is considered to be the **single** source of truth regarding image
index tag and image manifest tag. All subsequent tasks must use these values to
ensure consistency. The action provides the following outputs:

- `image-repository`: Last segment of the path, for example `kafka`.
- `image-manifest-tag`: Human-readable tag (usually the version) with
  architecture information, for example: `3.4.1-stackable0.0.0-dev-amd64`.

docker.stackable.tech/stackable/kafka:3.4.1-stackable0.0.0-dev-amd64
