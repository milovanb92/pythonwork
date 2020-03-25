# def item_list(*items):
#     for item in items:
#         print(f"Your sendwich with {item} is ready")

# item_list('majonez')
# item_list('kecap', 'kupus')
# item_list('krastavci', 'urnebes')

# def build_profile(first='milovan', last='bekic', **info):
#     info['first_name'] = first
#     info['last_name'] = last
#     return info

# my_profile = build_profile(age=27, hair='brown')
# print(my_profile)

def make_car(marka, model, **other_info):
    other_info['marka_auta'] = marka
    other_info['model_auta'] = model
    return other_info

car = make_car('vw', 'golf', boja='crvena', alu='da', siber='da')
print(car)