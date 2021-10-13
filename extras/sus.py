#thank https://github.com/LinesGuy/img_sussifier/blob/main/sus.py

        #⠀⠀⠀⡯⡯⡾⠝⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢊⠘⡮⣣⠪⠢⡑⡌
        #⠀⠀⠀⠟⠝⠈⠀⠀⠀⠡⠀⠠⢈⠠⢐⢠⢂⢔⣐⢄⡂⢔⠀⡁⢉⠸⢨⢑⠕⡌
        #⠀⠀⡀⠁⠀⠀⠀⡀⢂⠡⠈⡔⣕⢮⣳⢯⣿⣻⣟⣯⣯⢷⣫⣆⡂⠀⠀⢐⠑⡌
        #⢀⠠⠐⠈⠀⢀⢂⠢⡂⠕⡁⣝⢮⣳⢽⡽⣾⣻⣿⣯⡯⣟⣞⢾⢜⢆⠀⡀⠀⠪
        #⣬⠂⠀⠀⢀⢂⢪⠨⢂⠥⣺⡪⣗⢗⣽⢽⡯⣿⣽⣷⢿⡽⡾⡽⣝⢎⠀⠀⠀⢡
        #⣿⠀⠀⠀⢂⠢⢂⢥⢱⡹⣪⢞⡵⣻⡪⡯⡯⣟⡾⣿⣻⡽⣯⡻⣪⠧⠑⠀⠁⢐
        #⣿⠀⠀⠀⠢⢑⠠⠑⠕⡝⡎⡗⡝⡎⣞⢽⡹⣕⢯⢻⠹⡹⢚⠝⡷⡽⡨⠀⠀⢔
        #⣿⡯⠀⢈⠈⢄⠂⠂⠐⠀⠌⠠⢑⠱⡱⡱⡑⢔⠁⠀⡀⠐⠐⠐⡡⡹⣪⠀⠀⢘
        #⣿⣽⠀⡀⡊⠀⠐⠨⠈⡁⠂⢈⠠⡱⡽⣷⡑⠁⠠⠑⠀⢉⢇⣤⢘⣪⢽⠀⢌⢎
        #⣿⢾⠀⢌⠌⠀⡁⠢⠂⠐⡀⠀⢀⢳⢽⣽⡺⣨⢄⣑⢉⢃⢭⡲⣕⡭⣹⠠⢐⢗
        #⣿⡗⠀⠢⠡⡱⡸⣔⢵⢱⢸⠈⠀⡪⣳⣳⢹⢜⡵⣱⢱⡱⣳⡹⣵⣻⢔⢅⢬⡷
        #⣷⡇⡂⠡⡑⢕⢕⠕⡑⠡⢂⢊⢐⢕⡝⡮⡧⡳⣝⢴⡐⣁⠃⡫⡒⣕⢏⡮⣷⡟
        #⣷⣻⣅⠑⢌⠢⠁⢐⠠⠑⡐⠐⠌⡪⠮⡫⠪⡪⡪⣺⢸⠰⠡⠠⠐⢱⠨⡪⡪⡰
        #⣯⢷⣟⣇⡂⡂⡌⡀⠀⠁⡂⠅⠂⠀⡑⡄⢇⠇⢝⡨⡠⡁⢐⠠⢀⢪⡐⡜⡪⡊
        #⣿⢽⡾⢹⡄⠕⡅⢇⠂⠑⣴⡬⣬⣬⣆⢮⣦⣷⣵⣷⡗⢃⢮⠱⡸⢰⢱⢸⢨⢌
        #⣯⢯⣟⠸⣳⡅⠜⠔⡌⡐⠈⠻⠟⣿⢿⣿⣿⠿⡻⣃⠢⣱⡳⡱⡩⢢⠣⡃⠢⠁
        #⡯⣟⣞⡇⡿⣽⡪⡘⡰⠨⢐⢀⠢⢢⢄⢤⣰⠼⡾⢕⢕⡵⣝⠎⢌⢪⠪⡘⡌⠀
        #⡯⣳⠯⠚⢊⠡⡂⢂⠨⠊⠔⡑⠬⡸⣘⢬⢪⣪⡺⡼⣕⢯⢞⢕⢝⠎⢻⢼⣀⠀
        #⠁⡂⠔⡁⡢⠣⢀⠢⠀⠅⠱⡐⡱⡘⡔⡕⡕⣲⡹⣎⡮⡏⡑⢜⢼⡱⢩⣗⣯⣟
        #⢀⢂⢑⠀⡂⡃⠅⠊⢄⢑⠠⠑⢕⢕⢝⢮⢺⢕⢟⢮⢊⢢⢱⢄⠃⣇⣞⢞⣞⢾
        #⢀⠢⡑⡀⢂⢊⠠⠁⡂⡐⠀⠅⡈⠪⠪⠪⠣⠫⠑⡁⢔⠕⣜⣜⢦⡰⡎⡯⡾⡽

from PIL import Image
import numpy as np
import subprocess
import os
import random
import requests
from io import BytesIO
import discord
import traceback




#output_width = 30  # Width of output gif, measured in sussy crewmates
nearest_neighbour = False  # Enable this for flags
twerk_frame_count = 6  # 0.png to 5.png

# Load twerk frames 🥵
twerk_frames = []
twerk_frames_data = []  # Image as numpy array, pre-calculated for performance

async def sus(ctx,url,output_width=30):

    reply = await ctx.reply("Working on request...")

    #important! inorder to avoid cross-contamination we will take the ctx id and append
    append = ctx.interaction_id #int(random.random()*10000)

    response = requests.get(url)
    IMAGE = Image.open(BytesIO(response.content))

    for i in range(6):
        try:
            img = Image.open(f"extras/twerk_imgs/{i}.png").convert("RGBA")
        except Exception as e:
            print(f"Error loading twerk frames! Filename = {i}_{append}.png")
            print("Probably you renamed the twerk_imgs folder or forgot to set twerk_frame_count. baka")
            print(e)
            exit()
        twerk_frames.append(img)
        twerk_frames_data.append(np.array(img))

    # Get dimensions of first twerk frame. Assume all frames have same dimensions
    twerk_width, twerk_height = twerk_frames[0].size

    # Get image to sussify!
    input_image = IMAGE.convert("RGB") #Image.open(IMAGE).convert("RGB")
    input_width, input_height = input_image.size

    # Height of output gif (in crewmates)
    output_height = int(output_width * (input_height / input_width) * (twerk_width / twerk_height))

    # Width, height of output in pixels
    output_px = (int(output_width * twerk_width), int(output_height * twerk_height))

    # Scale image to number of crewmates, so each crewmate gets one color
    if nearest_neighbour:
        input_image_scaled = input_image.resize((output_width, output_height), Image.NEAREST)
    else:
        input_image_scaled = input_image.resize((output_width, output_height))

    for frame_number in range(twerk_frame_count):
        #print("Sussying frame #", frame_number)

        # Create blank canvas
        background = Image.new(mode="RGBA", size=output_px)

        progress = frame_number
        left = twerk_frame_count-frame_number-1
        # await ctx.send("{}{}".format(progress,left))

        await reply.edit(content="Working... |{}{}|".format("█"*progress,"░"*left))

        for y in range(output_height):
            for x in range(output_width):
                r, g, b = input_image_scaled.getpixel((x, y))

                # Grab that twerk data we calculated earlier
                # (x - y + frame_number) is the animation frame index,
                # we use the position and frame number as offsets to produce the wave-like effect
                sussified_frame_data = np.copy(twerk_frames_data[(x - y + frame_number) % len(twerk_frames)])
                red, green, blue, alpha = sussified_frame_data.T
                # Replace all pixels with colour (214,224,240) with the input image colour at that location
                color_1 = (red == 214) & (green == 224) & (blue == 240)
                sussified_frame_data[..., :-1][color_1.T] = (r, g, b)  # thx stackoverflow
                # Repeat with colour (131,148,191) but use two thirds of the input image colour to get a darker colour
                color_2 = (red == 131) & (green == 148) & (blue == 191)
                sussified_frame_data[..., :-1][color_2.T] = (int(r*2/3), int(g*2/3), int(b*2/3))

                # Convert sussy frame data back to sussy frame
                sussified_frame = Image.fromarray(sussified_frame_data)

                # Slap said frame onto the background 
                background.paste(sussified_frame, (x * twerk_width, y * twerk_height))
        background.save(f"sussified_{frame_number}_{append}.png")

    await reply.edit(content="Frames creating, compiling...")
    print("Converting sussy frames to sussy gif")
    # Convert sussied frames to gif. PIL has a built-in method to save gifs but
    # it has dithering which looks sus, so we use ffmpeg with dither=none
    subprocess.call('ffmpeg.exe -f image2 -i sussified_%d_'+str(append)+'.png -filter_complex "[0:v] scale=sws_dither=none:,split [a][b];[a] palettegen=max_colors=255:stats_mode=single [p];[b][p] paletteuse=dither=none" -r 20 -y -hide_banner -loglevel error sussified_'+str(append)+'.gif')
    await reply.edit(content="Created gif!")
    # Remove temp files
    print("Ejecting temp files from folder")
    for frame_number in range(twerk_frame_count):
        os.remove(f"sussified_{frame_number}_{append}.png")

    try:
        IMAGE = discord.File("sussified_"+str(append)+".gif") 
        await reply.edit(content="",file=IMAGE)
    except Exception as e:
        err = traceback.format_exc()
        # await reply.edit(content=err)
        #await ctx.reply("Failed to send image, probably too big?")

        if "too large" in err:
            await reply.edit(content="**ERROR:** Resultant gif too large to send (blame discord). Try a smaller size, or smaller image.")

    os.remove(f"sussified_"+str(append)+".gif")

