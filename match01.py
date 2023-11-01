metro_areas = [
    ("Tokyo", "jp", 36.933, (35.689722, 139.619667)),
    ("Delhi NCR", "IN", 21.935, (28.613889, -77.208889)),
]


# match case的用法
def main():
    print(f'{"":15}|{"latitude":>9}|{"longitude":>9}')
    for record in metro_areas:
        match record:
            case [name, _, _, (lat, lon)] if lon <= 0:
                print(f"{name:15}|{lat:9.4f}|{lon:9.4f}")
            case [name, _, _, (lat, lon)] if lon > 0:
                print(f"{name:15}|{lat:9.4f}|{lon:9.4f}")


main()
