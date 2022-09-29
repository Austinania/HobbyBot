#python 3.10

def bot_respond(message) -> str:
    received_message = message.lower()
    
    if received_message == 'hello' or '':
        return 'Hi!'
    
    elif received_message == 'help':
        return '`HobbyBot Help!!!\nh!  is default prefix\njjbaasbr OR jjteam\nGenerates a full team for Jojo\'s Bizarre Adventure All Star Battle R`'
    
    elif received_message == 'jjbaasbr' or 'jjteam':
        import bot_jjbaasbr
        jjteam = str(bot_jjbaasbr.generate(6, True))
        return jjteam
    
    else:
        return 'Try the help command!'