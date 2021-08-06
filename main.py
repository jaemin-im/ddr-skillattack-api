from fastapi import FastAPI

import requests

app = FastAPI()


@app.get('/api/ddr_skill/{ddrcode}')
async def check_ddr_skill(ddrcode):
    req_score = requests.get(
        f'http://skillattack.com/sa4/dancer_profile.php?ddrcode={ddrcode}')
    html_score = req_score.text
    ddr_skill = html_score.split('sSkill=')[1][1:8].rstrip("';\n")
    ddr_nick = html_score.split("sName='")[1].split("';")[0]
    req_date = requests.get(
        f'http://skillattack.com/sa4/dancer_skillpoint.php?ddrcode={ddrcode}')
    html_date = req_date.text
    try:
        update_date = html_date.split("dsUpdate=new Array('")[1][0:10]
    except:
        try:
            update_date = html_date.split("dsUpdate[0]='")[1][0:10]
        except:
            update_date = None

    return {'ddr_nick': ddr_nick, 'skill_point': ddr_skill, 'update_date': update_date}
