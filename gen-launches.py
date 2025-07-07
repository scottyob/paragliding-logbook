import click
import json
import reverse_geocoder as rg
import pycountry
import geohash2

import xml.etree.ElementTree as ET

@click.command()
@click.argument('launched_db', type=click.Path(exists=True))
def main(launched_db):
    # Parse KML file
    tree = ET.parse(launched_db)
    root = tree.getroot()

    # Remove namespace prefixes for easier access
    for elem in root.iter():
        if '}' in elem.tag:
            elem.tag = elem.tag.split('}', 1)[1]

    placemarks = []
    coords_list = []
    for placemark in root.findall('.//Placemark'):
        name_elem = placemark.find('name')
        point_elem = placemark.find('Point')
        coords_elem = point_elem.find('coordinates') if point_elem is not None else None

        if coords_elem is not None and name_elem is not None:
            coords = coords_elem.text.strip().split(',')
            if len(coords) >= 2:
                latitude = float(coords[1])
                longitude = float(coords[0])
                coords_list.append((latitude, longitude))
                placemarks.append({
                    'name': name_elem.text.strip(),
                    'longitude': longitude,
                    'latitude': latitude,
                     # Precision 7 ≈ ~150m accuracy
                    'geohash': geohash2.encode(latitude, longitude, precision=7)
                })

    # Reverse geocode to get country
    results = rg.search(coords_list, verbose=False)  # returns list of dicts

    for i, result in enumerate(results):
        cc = result['cc']
        country = pycountry.countries.get(alpha_2=cc)
        country_name = country.name if country else cc
        # import pdb; pdb.set_trace()
        placemarks[i]['country'] = f"{country_name} {country.flag if country else ''}"

    print(json.dumps(placemarks, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()