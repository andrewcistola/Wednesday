import os
import platform
OS_local = platform.system()
if OS_local == 'Linux': 
    swc = '/'
    shell_local = 'bash'
    copy_local = 'cp'
if OS_local == 'Windows': 
    swc = '\\'
    shell_local = 'powershell'
    copy_local = 'copy'
if OS_local == 'Darwin': 
    swc = '/'
    shell_local = 'bash'

