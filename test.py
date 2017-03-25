# arch.python_theme

import platform, sys
os=platform.platform()
vp= sys.version_info
if 'arch' in  os and vp >=(2,6,0): 
  print('Parabéns, você é foda')
elif 'arch' in os:
  print('Usa Python, galadx!')
elif vp > (2,6,0):
  print('Use Arch Linux!')
else:
  print('Use Arch e Python, obrigado.')
