import main
import requests


def topLogin(data: list) -> None:
    sendkey = main.webhook_discord_url
    rewards = data[0]
    login = data[1]
    bonus = data[2]
    title = "FGO签到 - Lv." + str(rewards.level)
    desp = "## 每日签到

"
    desp += "- 等级：" + str(rewards.level) + "
"
    desp += "- 圣晶石：" + str(rewards.stone) + "
"
    desp += "- 呼符：" + str(rewards.ticket) + "
"
    desp += "- 连续登录：" + str(login.login_days) + " 天
"
    desp += "- 累计登录：" + str(login.total_days) + " 天
"
    desp += "- 友情点：+" + str(login.add_fp) + "（总计 " + str(login.total_fp) + "）
"
    desp += "- 体力上限：" + str(login.act_max) + "
"
    if bonus != "No Bonus":
        desp += "
### 登录奖励

"
        desp += "**" + bonus.message + "**

"
        for item in bonus.items:
            desp += "- " + item + "
"
        if bonus.bonus_name is not None:
            desp += "
**" + bonus.bonus_name + "**

"
            desp += bonus.bonus_detail + "

"
            for item in bonus.bonus_camp_items:
                desp += "- " + item + "
"
    requests.post("https://sctapi.ftqq.com/" + sendkey + ".send", data={"title": title, "desp": desp})


def drawFP(servants, missions) -> None:
    sendkey = main.webhook_discord_url
    title = "FGO友情点十连"
    desp = "## 友情点召唤结果

"
    if len(servants) > 0:
        servants_atlas = requests.get("https://api.atlasacademy.io/export/JP/basic_svt_lang_en.json").json()
        svt_dict = {svt["id"]: svt for svt in servants_atlas}
        names = []
        for servant in servants:
            svt = svt_dict[servant.objectId]
            names.append(svt["name"])
        desp += "、".join(names)
    if len(missions) > 0:
        desp += "

### 活动任务

"
        for mission in missions:
            desp += "- " + mission.message + ": " + str(mission.progressTo) + "/" + str(mission.condition) + "
"
    requests.post("https://sctapi.ftqq.com/" + sendkey + ".send", data={"title": title, "desp": desp})
