from factory import extract_data_from


def main():
    json_factory = extract_data_from('assets/movies.json')
    json_data = json_factory.parsed_data
    print(f'* * Encontrados: {len(json_data)} Filmes * *')
    for movie in json_data:
        print(f"Title: {movie['title']}")
        year = movie['year']
        if year:
            print(f"Year: {year}")
        director = movie['director']
        if director:
            print(f"Director: {director}")
        genre = movie['genre']
        if genre:
            print(f"Genre: {genre}")
        print()
  
    print("-" * 25)

    xml_factory = extract_data_from('assets/person.xml')
    xml_data = xml_factory.parsed_data
    clicksigners = xml_data.findall(f".//person[workAt='Clicksign']")
    print(f'* * Encontrados: {len(clicksigners)} Clicksigners * *')
    for clicksigner in clicksigners:
        firstname = clicksigner.find('firstName').text
        print(f'first name: {firstname}')
        [print(f"phone number ({p.attrib['type']}):", p.text)
        for p in clicksigner.find('phoneNumbers')]
        print()

main()
