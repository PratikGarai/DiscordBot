class HydraModule :

    def __init__(self, prefix:str) :
        self.prefix = prefix

        self.playlists = {
            "chill" : [
                ("Fake Love" , " https://soundcloud.com/l2sharebts2/bts-fake-love-1"),
                ("Story of My Life", "https://soundcloud.com/inti-baker/one-direction-3")
            ]
        }
    

    async def clear_fav(self, count, ctx) :
        for i in range(count) :
            await ctx.send(f"{self.prefix}playlist song delete 1 fav")
            break
    

    async def set_playlist(self, name, ctx) :
        if name in self.playlists :
            await ctx.send(f"```Playlist {name} does not exist```")
        else :
            for i,j in self.playlists[name] :
                await ctx.send(f"{self.prefix}playlist song save {j}")
                break
