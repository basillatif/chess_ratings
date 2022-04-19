import lichess.api
import time
from urllib.error import HTTPError

player_list = [
'GutovAndrey',
'Hikaru',
'GMVallejo',
'LevonAronian',
'FabianoCaruana',
'LyonBeast',
'AnishGiri',
'FairChess_on_YouTube',
'iturrizaga',
'TenisMaster',
'GMWSO',
'GM_D85',
'FCChelsea14',
'TampaChess',
'jefferyx',
'Khvicha_Supatashvili',
'Duhless',
'7hanat',
'Beastly99',
'GMALMEIDA',
'mishanick',
'lachesisQ',
'dropstoneDP',
'Grischuk',
'KNVB',
'Parhamov',
'jhonfernadez',
'bakki78',
'Jospem',
'lonelyqueen0',
'ChessWarrior7197',
'Bigfish1995',
'WDCH',
'CyberneticLion',
'unclejambit',
'amintabatabaei',
'viditchess',
'amirrezaemamiii',
'Tesla37',
'Indianlad',
'rednova1729',
'1random',
'Konavets',
'Blitzstream',
'ChristopherYoo',
'BillieKimbah',
'AlexanderL',
'GHANDEEVAM2003',
'LiemLe',
'DJojua']
for i in player_list:
    print("Player Name: ", i)
    #print(user)
    try:
        user = lichess.api.user(i)
        print(user['perfs']['rapid']['rating'])
    except Exception:
        print('No data for this user')
    except requests.HTTPError as exception:
        print(exception)
