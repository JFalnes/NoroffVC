centimeters = 10


def metric_converter(centimeters):
    return centimeters / 2.54

conversion = metric_converter(centimeters=centimeters)
print(f'{centimeters}cm is {conversion} inches')