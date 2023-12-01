import subprocess

cmd = 'sudo sh -c echo -n "1-1" > /sys/bus/usb/drivers/usb/unbind'

subprocess.call(cmd, shell=True)