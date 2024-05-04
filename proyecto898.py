#importamos subprocess
import subprocess

#le decimos al proceso que abra la terminal y ejecute "poweroff"
comando = "systemctl poweroff"

subprocess.run(comando, shell=True)

