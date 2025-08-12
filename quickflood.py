import subprocess

ip = "127.0.0.1"
port = "19132"
b = 10
s = "skins"
c = "chat.txt"
i = 1
d = 30
delay = 0

command = [
    "python3", "bedflood.py",
    "-ip", ip,
    "-port", port,
    "-b", str(b),
    "-s", s,
    "-c", c,
    "-i", str(i),
    "-d", str(d),
    "-delay", str(delay)
]

try:
    subprocess.run(command)

except KeyboardInterrupt:
    exit()
