#!/usr/bin/env python
import env_file

data = env_file.load()
print(data)

data = env_file.load([".env", "dev.env"])
print(data)
