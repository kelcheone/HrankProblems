
def make_readable(seconds):
    # Do something
    return '{:02}: {:02}:{:02}'.format(seconds // 3600, (seconds//60) % 60, seconds % 60)


# print(make_readable(359999))


def readable(seconds):
    return '{:02}:{:02}:{:02}'.format(seconds // 3600, (seconds // 60) % 60, seconds % 60)


print(readable(359999))
