from telegram.utils.helpers import escape_markdown as es


def start_msg(name):
    msg = f"""*Hey {es(name,version=2)}* \nI am Jiosaavn downloader bot I can download music for you from jio saavn\n
    Just send me a jiosaavn song or album link I will send you the audio file\n
Owned by @Best_Movies_Everr"""
    return msg


def help_msg():
    help = """*How to Use me*\n
*Just send me a jiosaavn song,album or playlist link, I will send you the audio with lyrics*\n\nSee This Video for Help - \n\nContact - @Movies_Thunder_chat_group"""
    return help
