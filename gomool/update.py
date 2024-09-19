import json
import sqlite3
import re
from urllib import request

URL = "https://v-archive.net/db/songs.json"
SAVE_PATH = "./data/songs.json"
DB_PATH = "./data/songs.db"

# 곡 리스트를 다운로드 합니다.
# 다운로드 성공 시 DB 형식으로 변환합니다.
# 다운로드 실패 시 False 를 반환합니다.
def song_list() -> bool:
    try:
        request.urlretrieve(URL, SAVE_PATH)
    except Exception:
        return False
    _to_db()
    return True


# 곡을 DB 형식으로 변환
def _to_db() -> None:
    with open(SAVE_PATH, "r", encoding='utf-8') as f:
        jdata = json.load(f)
    # Connect DB
    connection = sqlite3.connect(DB_PATH)
    cur = connection.cursor()
    # Table Check
    cur.execute("Select name From sqlite_master Where type='table' And name='songs'")
    table_exist = cur.fetchall()
    # Drop Table
    if table_exist:
        cur.execute("Drop Table songs;")
    # Create Table
    cur.execute("""Create Table songs(
                no INTEGER PRIMARY KEY AUTOINCREMENT,
                title INTEGER, name TEXT, dlc TEXT,
                _4BNM INTEGER, _4BHD INTEGER, _4BMX INTEGER, _4BSC INTEGER,
                _5BNM INTEGER, _5BHD INTEGER, _5BMX INTEGER, _5BSC INTEGER,
                _6BNM INTEGER, _6BHD INTEGER, _6BMX INTEGER, _6BSC INTEGER,
                _8BNM INTEGER, _8BHD INTEGER, _8BMX INTEGER, _8BSC INTEGER
                )""")
    # Insert Items
    db_items = []
    # Korean First Sort
    sorted_jdata = sorted(sorted(jdata, key=lambda x: x['name'].lower()), key=lambda x: 0 if re.search('^[ㄱ-힣]', x['name']) else 1)
    for data in sorted_jdata:
        title = data['title']
        name = data['name']
        dlc = data['dlc']
        patterns = data['patterns']
        # 4B 
        _4B = patterns['4B']
        _4BNM = _4B.get("NM", {'level':0})['level']
        _4BHD = _4B.get("HD", {'level':0})['level']
        _4BMX = _4B.get("MX", {'level':0})['level']
        _4BSC = _4B.get("SC", {'level':0})['level']
        # 5B
        _5B = patterns['5B']
        _5BNM = _5B.get("NM", {'level':0})['level']
        _5BHD = _5B.get("HD", {'level':0})['level']
        _5BMX = _5B.get("MX", {'level':0})['level']
        _5BSC = _5B.get("SC", {'level':0})['level']
        # 6B
        _6B = patterns['6B']
        _6BNM = _6B.get("NM", {'level':0})['level']
        _6BHD = _6B.get("HD", {'level':0})['level']
        _6BMX = _6B.get("MX", {'level':0})['level']
        _6BSC = _6B.get("SC", {'level':0})['level']
        # 8B
        _8B = patterns['8B']
        _8BNM = _8B.get("NM", {'level':0})['level']
        _8BHD = _8B.get("HD", {'level':0})['level']
        _8BMX = _8B.get("MX", {'level':0})['level']
        _8BSC = _8B.get("SC", {'level':0})['level']
        db_items.append((title, name, dlc,
                         _4BNM, _4BHD, _4BMX, _4BSC,
                         _5BNM, _5BHD, _5BMX, _5BSC,
                         _6BNM, _6BHD, _6BMX, _6BSC,
                         _8BNM, _8BHD, _8BMX, _8BSC,
                         ))

    cur.executemany("""Insert Into songs(title, name, dlc,
                    _4BNM, _4BHD, _4BMX, _4BSC,
                    _5BNM, _5BHD, _5BMX, _5BSC,
                    _6BNM, _6BHD, _6BMX, _6BSC,
                    _8BNM, _8BHD, _8BMX, _8BSC)
                    Values(?, ?, ?,
                    ?, ?, ?, ?,
                    ?, ?, ?, ?,
                    ?, ?, ?, ?,
                    ?, ?, ?, ?
                    )""", db_items)
    connection.commit()
    # Close Connection
    connection.close()