import secrets
import os
import pathlib

# Generate a random 32-byte hex string

directory = pathlib.Path(__file__).parent.resolve()
rpcuser = directory / "secrets/rpcuser.txt"
rpcpassword = directory / "secrets/rpcpassword.txt"

# Write to file
with open(rpcuser, "w") as f:
    f.write(secrets.token_hex(64))

with open(rpcpassword, "w") as f:
    f.write(secrets.token_hex(64))
