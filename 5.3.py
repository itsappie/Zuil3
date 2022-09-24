def lang_genoeg(x):
    if x >= 120:
        print('Je bent lang genoeg voor de attractie!')
    elif x < 120:
        print('Sorry, je bent te klein!')

#test
lang_genoeg(123)
lang_genoeg(119)