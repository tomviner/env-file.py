#!/usr/bin/env python
import env_file

value = env_file.get("POSTGRES_PASSWORD")
print(value)

value = env_file.get("no-existing")
print(value)
