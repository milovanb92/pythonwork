def make_shirt(size='L', text='I Love Python!'):
    print(f"I want a shirt size {size} and text on it: {text}")

def describe_city(city, country='BiH'):
    print(f"{city.title()} is in {country}")



make_shirt('L', 'Jebem vam majkuuu')
make_shirt(text='Ja sam Bog', size='M')

make_shirt()
make_shirt(size='M')
make_shirt(size='S', text='Ja sam malo govno')


describe_city('knezevo')
describe_city(city='banja luka')
describe_city(city='beograd', country='Srbija')

