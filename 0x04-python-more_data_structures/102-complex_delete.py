
#!/usr/bin/python3
def complex_delete(a_dictionary, price):
    list_keys = list(a_dictionary.keys())

    for price_dic in list_keys:
        if price == a_dictionary.get(price_dic):
            del a_dictionary[price_dic]

    return (a_dictionary)
