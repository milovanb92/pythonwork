# # Start with some desings that need to be printed

# unprinted_designs = ['phone case', 'robot pendant', 'pen']
# completed_modes = []

# # Simulate printing each design, until none are left.
# # Move each design to completed_modes after printing

# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_modes.append(current_design)

# # Display all completed models
# print("\nThe following models have been printed: ")
# for completed_model in completed_modes:
#     print(completed_model)

# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)

import printing_functions 
from printing_functions import print_models
from printing_functions import print_models as p_m
import printing_functions as p_f
from printing_functions import *

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['telefon', 'noz', 'kasika']
completed_models = []

printing_functions.print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

p_m(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

p_f.print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)