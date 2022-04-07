# Imports
import os

# Main Code
print('Please make sure I am running as a sudo!')
os.system('sudo airmon-ng stop wlan0mon')
os.system('sudo service NetworkManager start')