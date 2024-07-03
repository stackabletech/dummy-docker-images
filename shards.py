import conf

# for product in conf.products:
#     if product["name"] == "product2":
#         versions = [k for k,v in list(enumerate(product["versions"]))]
#         print(versions)

product = list(filter(lambda x: x["name"] == "product2", conf.products))[0]
versions = [k for k,v in list(enumerate(product["versions"]))]
print(versions)
