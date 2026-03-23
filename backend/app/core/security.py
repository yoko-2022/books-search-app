from argon2 import PasswordHasher

ph = PasswordHasher()

password = "mysecretpassword"

hashed_password = ph.hash(password)
