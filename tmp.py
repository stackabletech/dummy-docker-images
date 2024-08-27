import sys
import os
sys.path.append(str(os.getcwd()))
import conf

product=os.environ['PRODUCT_NAME']
assert(product)
print(f"Generating version list for {product}")

# get the product config
product_conf = list(filter(lambda x: x["name"] == product, conf.products))[0]
# list the versions, eg: [1.0, 1.1, 2.0]
versions = [v["product"] for k,v in enumerate(product_conf["versions"])]
assert(versions)
output_versions = f"VERSIONS={versions}\n"

github_outputs_file = os.environ['GITHUB_OUTPUT']
f = open(github_outputs_file, "w")
print(f"Writing to $GITHUB_OUTPUT: {output_versions}")
f.write(output_versions)
f.close()