
# mclip.py - A multi-clipboard program

TEXT = {'agree':"""Yes, I agree. That sounds fine to me.""",'busy':'''Sorry, can we do this another time?''','upsell':'''Would you consider making this a monthly donation?'''}
print('olaaa')
import sys, pyperclip, time
if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1] # first command line arg is the keyphrase
input('Say something: ')
if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for '+keyphrase+' copied to clipboard.')
else:
    print('There us no text for '+ keyphrase)

time.sleep(3)
sys.exit()