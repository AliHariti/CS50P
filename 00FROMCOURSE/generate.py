from random import choice


gauss = []

for _ in range(100):
    coin = choice(["heads", "tails"])
    gauss.append(coin)
print(gauss)
print(f"Len gauss: {len(gauss)}")
print(f"tails: {gauss.count('tails')}, {gauss.count('tails') / len(gauss):.0%}")
print(f"heads: {gauss.count('heads')}, {gauss.count('heads') / len(gauss):.0%}")