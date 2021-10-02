class Song(object):
    def __init__(this,lyrics):
        this.lyrics = lyrics

    def sing_me_a_song(this):
        for line in this.lyrics:
            print(line)

happy_bday = Song(["Happy birth day to you", "I don`t want to get sued",
                    "so, I`ll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

print("\n\n")
seven_years_old = Song(["once I was 7years old.","My mama told me go make yourself some friend or you`ll be lonely.",
                        "I always had that dream like my dady before me."])

seven_years_old.sing_me_a_song()

next = ["so, I started sing them a song I started tell them storeies.","something about that golry....","once I 12 years old my dady told me go get yourself a wife or you`ll be lonely."]

seven_years_old = Song(next)
seven_years_old.sing_me_a_song()
