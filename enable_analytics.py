import re

with open("mkdocs.yml", "r") as file:
    lines = file.readlines()

lines = [
    re.sub(r"# property: G-8LCP0TZS4Y", "property: G-8LCP0TZS4Y", line)
    for line in lines
]

with open("mkdocs.yml", "w") as file:
    file.writelines(lines)
