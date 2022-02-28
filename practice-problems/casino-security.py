print("Texts📃 displays a casino🎰, x = space🃏, T = thief🦹, G = guard💂, and $ = money💰")

txt = input('Security String: ')
#xxTxxx$xxxTxxxGxxT ALARM
#xGxx$xxGxxxTTT Safe

x = txt.replace('x', '')
if '$T' in x or 'T$' in x:
    print('The money💰 is not🙅 safe😟!!')
else:
    print('The money💰 is😌 safe👍')