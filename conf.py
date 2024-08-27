"""
Configuration file for the Stackable image-tools: https://github.com/stackabletech/image-tools.

Application images will be created for products and associated versions configured here.
"""

import product1.versions as product1
import product2.versions as product2

products = [
    {
        "name": "product1",
        "versions": product1.versions,
    },
    {
        "name": "product2",
        "versions": product2.versions,
    },
]

# open_shift_projects = {
#     "airflow": {"id": "62613f498ccb9938ba3cfde6"},
#     "druid": {"id": "626140028ccb9938ba3cfde7"},
#     "hadoop": {"id": "6261407f887d6e0b8614660c"},
#     "hbase": {"id": "62614109992bac3f9a4a24b8"},
#     "hive": {"id": "626140806812078a392dceaa"},
#     "kafka": {"id": "625ff25b91bdcd4b49c823a4"},
#     "nifi": {"id": "625586a32e9e14bc8118e203"},
#     "opa": {"id": "6255838bea1feb8bec4aaaa3"},
#     "spark-k8s": {"id": "62613e81f8ce82a2f247dda5"},
#     "superset": {"id": "62557e5fea1feb8bec4aaaa0"},
#     "tools": {"id": "62557cd575ab7e30884aaaa0"},
#     "trino": {"id": "62557c4a0030f6483318e203"},
#     "zookeeper": {"id": "62552b0aadd9d54d56cda11d"},
# }

cache = [
    {
        "type": "registry",
        "ref_prefix": "build-repo.stackable.tech:8083/sandbox/cache",
        "mode": "max",
        "compression": "zstd",
        "ignore-error": "true",
    },
]
