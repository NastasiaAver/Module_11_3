from pprint import pprint

def introspection_info(obj):

    attributes = []
    metods = []
    for i in dir(obj):
        if callable(getattr(obj, i)):
            metods.append(i)
        else:
            attributes.append(i)
    pprint( {'type': type(obj),
        'attributes': attributes,
        'metods': metods,
        'module': __name__,
        'length': len(obj)})


obj = [100, True, 'Москва']
introspection_info(obj)

