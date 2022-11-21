available_proteins = ['chicken', 'steak', 'carnitas', 'barbacoa', 'sofritas']
requested_proteins = ['Garlic Guajillo Steak', 'Chicken']

if requested_proteins:
    for requested_protein in requested_proteins:
        if requested_protein.lower() in available_proteins:
            print(f'Adding {requested_protein}.')
        else:
            print(f'Sorry, {requested_protein} is not available.')
    print('\nFinished making your bowl!')
else:
    print("Are you sure you do not want a protein?")