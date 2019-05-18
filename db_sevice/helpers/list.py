def field_in_list(list_of_objects, key, value):
    for obj in list_of_objects:
        if obj.get(key) and obj[key] == value:
            return True
    return False
