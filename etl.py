from ckanapi import RemoteCKAN
from json import dumps
from pandas import read_json, read_csv
from os import path, makedirs

covid_data = []

with RemoteCKAN('https://dadesobertes.gva.es') as gva:
    package = gva.action.package_show(id='15810be9-d797-4bf3-b37c-4c922bee8ef8')
    for resource in package['resources']:
        created_date = resource['created']
        last_modified_date = resource['last_modified']
        data_date = resource['name'][-10:]
        data = read_csv(resource['url'], sep=';')
        for _, record in data.iterrows():
            print(record.keys())
            if 'Municipi / Municipio' in record.keys():
                town = record['Municipi / Municipio']
            elif 'Municipio' in record.keys():
                town = record['Municipio']
            else:
                town = record['Municipi']

            if 'Casos PCR+ / Casos PCR+' in record.keys():
                pcr_cases = record['Casos PCR+ / Casos PCR+']
            else:
                pcr_cases = record['Casos PCR+']

            covid_data.append({
                'Fecha y hora creación': created_date,
                'Fecha y hora última modificación': last_modified_date,
                'Fecha datos': data_date,
                'Municipio': town,
                'Casos PCR+': pcr_cases
            })
        break

if not path.exists('dist'):
    makedirs('dist')

with open('dist/historico_covid_19_municipios_comunidad_valenciana.json', 'w', encoding='utf-8') as file:
    json_string = dumps(covid_data, default=lambda o: o.__dict__, sort_keys=True, indent=2, ensure_ascii=False)
    file.write(json_string)

read_json('dist/historico_covid_19_municipios_comunidad_valenciana.json').to_csv(
    'dist/historico_covid_19_municipios_comunidad_valenciana.csv', index=None)
