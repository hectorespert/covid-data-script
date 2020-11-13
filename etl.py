from ckanapi import RemoteCKAN

print("Starting")

covid_data = []

with RemoteCKAN('https://dadesobertes.gva.es') as gva:
    package = gva.action.package_show(id='15810be9-d797-4bf3-b37c-4c922bee8ef8')
    print(package['num_resources'])
    #for resource in sorted(package['resources'], key=lambda item: item['position']):
        #print(resource)
        #covid_data.append({'created': resource['created'], 'last_modified': resource['last_modified']})
        #data = gva.action.datastore_search(id=resource['id'])
        #rint(data)

print(covid_data)