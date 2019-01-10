
def generate_id(list):
    """ Function to generate ID for collection """

    if len(list) == 0:
        return 1
    else:
        return list[-1]['id']+1
    # If list is empty return 1 else add 1 to id of last object