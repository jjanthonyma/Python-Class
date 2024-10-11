def sing_beer_song(n):
    if n > 0:
        print(f"{n} bottles of beer on the wall, {n} bottles of beer.")
        print(f"Take one down, pass it around, {n-1} bottles of beer on the wall.")
        print()
        sing_beer_song(n-1)
    else:
        print("No more bottles of beer on the wall, no more bottles of beer.Go to the store and buy some more, 99 bottles of beer on the wall.")

sing_beer_song(99)
