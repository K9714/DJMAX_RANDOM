import random
import sqlite3
import pydirectinput
import re
import time

def _level_search_sql(key, levels):
    nm_min, nm_max, sc_min, sc_max = levels
    nm_sql = f"SELECT * FROM levels WHERE key='{key}B' AND type != 'SC' AND level BETWEEN {nm_min} AND {nm_max}"
    sc_sql = f"SELECT * FROM levels WHERE key='{key}B' AND type = 'SC' AND level BETWEEN {sc_min} AND {sc_max}"
    return nm_sql, sc_sql

def _regexp(expr, item):
    reg = re.compile(expr)
    return reg.search(item) is not None

def select_random(keys, levels):
    if not keys:
        return None
    connection = sqlite3.connect("./data/songs.db")
    connection.create_function("REGEXP", 2, _regexp)
    cur = connection.cursor()
    key = random.sample(keys, 1)[0]
    nm_sql, sc_sql = _level_search_sql(key, levels)
    songs = []
    # GET Normal List
    cur.execute(nm_sql)
    rows = cur.fetchall()
    songs += rows
    # GET 
    cur.execute(sc_sql)
    rows = cur.fetchall()
    songs += rows
    if not songs:
        return None
    select = random.sample(songs, 1)
    _send_keys(cur, select)
    connection.close()
    return select
    
def _send_keys(cur: sqlite3.Cursor, select):
    _, title, name, dlc, key, type, level = select
    cur.execute(f"SELECT * FROM songs WHERE title={title}")
    info = cur.fetchone()
    reverse = False
    if re.search("^[a-zA-z]", name):
        # 첫글자 시작점 찾기
        first = name[0]
    else:
        reverse = True
        # A 시작점 찾기
        first = 'a'
    cur.execute(f"SELECT * FROM songs WHERE name REGEXP \'^[{first.lower()}{first.upper()}]\' LIMIT 1")
    first_no = cur.fetchone()[0]
    # 거리 계산
    distnace = abs(first_no - info[0])
    # 난이도 횟수 계산
    count = -1
    index = {'4B': 4, '5B': 8, '6B': 12, '8B': 16}[key]
    pydirectinput.KEYBOARD_MAPPING['4B'] = 0x4B 
    pydirectinput.KEYBOARD_MAPPING['5B'] = 0x4C 
    pydirectinput.KEYBOARD_MAPPING['6B'] = 0x4D 
    pydirectinput.KEYBOARD_MAPPING['8B'] = 0x48 
    level_data = info[index:index+4]
    for ld in level_data:
        if ld != 0:
            count += 1
        if ld == level and type != "SC":
            break
    # 키 설정
    # pydirectinput.press(key[0])
    pydirectinput.keyDown('ctrl')
    pydirectinput.keyDown(key)
    pydirectinput.keyUp(key)
    pydirectinput.keyUp('ctrl')
    # 정렬 초기화
    pydirectinput.press("shift")
    pydirectinput.press("shiftright")
    # 노래 찾기
    pydirectinput.press(first.lower())
    move_key = "up" if reverse else "down"
    for _ in range(distnace):
        pydirectinput.press(move_key)
    time.sleep(0.5)
    # 난이도 설정
    for _ in range(count):
        pydirectinput.press("right")
        time.sleep(0.1)