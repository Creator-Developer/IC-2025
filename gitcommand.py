def generate(name:str):
    link = f"https://api.github.com/users/{name}"
    return f'git clone {link}'