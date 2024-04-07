import os
from yandex_music import Client

client = Client('y0_AgAAAABhwEmWAAG8XgAAAAEBLvoCAADA2xQlSPdLvbeSPbJjauJdOeWc3w').init()
def last_download():

    print("Скачиваю последний послушанный Вами трек...")
    client.users_likes_tracks()[0].fetch_track().download('example.mp3')
    print("Готово!")

def chart_ym():
    CHART_ID = 'world'
    TOKEN = os.environ.get('TOKEN')
    chart = client.chart(CHART_ID).chart

    text = ["\033[0m{}".format(f'🏆 {chart.title}', chart.description, '', 'Треки:')]

    for track_short in chart.tracks:
        track, chart = track_short.track, track_short.chart
        artists = ''
        if track.artists:
            artists = ' - ' + ', '.join(artist.name for artist in track.artists)

        track_text = f'{track.title}{artists}'

        if chart.progress == 'down':
            track_text = '🔻 ' + track_text
        elif chart.progress == 'up':
            track_text = '🔺 ' + track_text
        elif chart.progress == 'new':
            track_text = '🆕 ' + track_text
        elif chart.position == 1:
            track_text = '👑 ' + track_text

        track_text = f'{chart.position} {track_text}'
        text.append(track_text)

    print('\n'.join(text))
def search():
    link=str(input("\033[0m{}".format('\nВведите ссылку на альбом: ')))
    print(' ')
    ALBUM_ID = link[30:]
    album = client.albums_with_tracks(ALBUM_ID)
    tracks = []
    for i, volume in enumerate(album.volumes):
        if len(album.volumes) > 1:
            tracks.append(f'💿 Диск {i + 1}')
        tracks += volume

    text = 'АЛЬБОМ\n\n'
    text += f'{album.title}\n'
    text += f"Исполнитель: {', '.join([artist.name for artist in album.artists])}\n"
    text += f'{album.year} · {album.genre}\n'

    cover = album.cover_uri
    if cover:
        text += f'Обложка: https://{cover.replace("%%", "400x400")}\n\n'

    text += 'Список треков:'

    print(text)

    for track in tracks:
        if isinstance(track, str):
            print(track)
        else:
            artists = ''
            if track.artists:
                artists = ' - ' + ', '.join(artist.name for artist in track.artists)
            print(track.title + artists)

if __name__ == '__main__':
    print('Привет, дорогой пользователь! Я проводник между тобой и', "\033[31m\033[3m{}".format('Яндекс'),'\033[0m{}'.format('Музыкой🎵'))
    while True:
        print("\033[0m{}".format('\nКакую задачу для тебя выполнить?\n1. Скачать полседнюю прослушанную песню\n2. Показать чарт\n3. Показать информацию о любом альбоме'))
        choose=int(input("\033[3m{}".format('\nВаш выбор: ')))
        if choose==1:
            last_download()
        elif choose==2:
            chart_ym()
        elif choose==3:
            search()
        else:
            print('\nТакого номера нет.')
