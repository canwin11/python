# 串列生成基本
symbols = "天氣不錯"
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

print(codes)

# listcomp
codes = [ord(x) for x in symbols]
print(codes)

# map /filter
codes = [ord(x) for x in symbols if ord(x) > 28000]
print(codes)

# lambda

codes = list(filter(lambda c: c > 28000, map(ord, symbols)))
print(codes)

#
colors = ["black", "white"]
sizes = ["s", "m", "l"]
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

# genexp
g = tuple(ord(symbol) for symbol in symbols)
print(g)

for tshirts in (f"{c} {s}" for c in colors for s in sizes):
    print(tshirts)
