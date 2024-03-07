import wget
link = str(input('link: ')).strip()
l2 = f'{link}'
wget.download(link, "teste.mp4")
