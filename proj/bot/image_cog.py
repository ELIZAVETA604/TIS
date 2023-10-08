import discord
from discord.ext import commands

import os, shutil
from google_images_download import google_images_download
import random

class image_cog(commands.Cog):
    def __init__(self, bot):

        self.bot = bot
        self.download_folder = 'downloads'

        self.keywords = "Spongebob"

        self.response = google_images_download.googleimagesdownload()
        self.arguments = {
            "keywords": self.keywords,
            "limit":6,
            "size":"medium",
            "no_directory": True
            }

        self.image_names = []

        self.update_images()

    @commands.command(name="get", help="Показывает рандомные картинки из загруженных")
    async def get(self, ctx):
        img = self.image_names[random.randint(0, len(self.image_names) - 1)]
        await ctx.send(file=discord.File(img))
    
    def update_images(self):
        self.image_names = []
        #store all the names to the files
        for filename in os.listdir(self.download_folder):
            self.image_names.append(os.path.join(self.download_folder, filename))
    