# -*- coding: utf-8 -*-
# author: Ethosa

import requests

from ..utils import browserFake


class PHub:
    RUSSIAN = 99
    FPS60 = 105
    CLOSED_CAPTIONS = 732
    ASIATS = 1
    ANAL = 35
    ARAB = 98
    BDSM = 10
    BSEX = 76
    BLOND = 9
    BIG_TITS = 8
    BIG_COCK = 7
    BRASILIAN = 102
    BRITISH = 96
    SPRAY = 69
    BRUNETTE = 11
    BUKKAKE = 14
    IN_SCHOOL = 88
    WEB_CAM = 61
    PARTY = 53
    GONZO = 41
    RUDE = 67
    GROUP = 80
    DOUBLE_PENETRATION = 72
    GIRLS_SOLO = 492
    WANKS = 20
    EUROPEANS = 55
    FEMALE_ORGASM = 502
    HARD_SEX = 21
    BEHIND_THE_SCENES = 141
    STARS = 12
    GOLD_RAIN = 211
    ADULT = 28
    TOYS = 23
    INDIAN = 101
    ITALIAN = 97
    CASTINGS = 90
    END = 16
    KOREAN = 103
    COSPLAY = 241
    CREMPIE = 15
    CUNNILINGUS = 131
    SMOKED = 91
    LATIN = 26
    LESBIAN = 27
    AMATEUR = 3
    SMALL_TITS = 59
    MOTHERS = 29
    MASSAGE = 78
    MASTURBATION = 22
    INTERRACIAL_SEX = 25
    BLOW_JOB = 13
    MUSIC = 121
    MULATTOS = 17
    CARTOONS = 86
    MUSCULAR_MEN = 512
    PUBLIC = 24
    GERMAN = 95
    LEGS = 93
    BABYSITTERS = 89
    GUYS_SOLO = 92
    PARODY = 201
    PENSIONERS_TEEN = 181
    HD = "hd"
    SFW = "sfw"
    GAY = "gayporn"
    DESCRIBED = "described-video"
    BABE = "categories/babe"
    INTERACTIVE = "interactive"
    COLLEGE = "categories/college"
    TEEN = "categories/teen"
    SCISSORS = 532
    ASS = 4
    PORNSTARS = "categories/pornstar"

    def __init__(self):
        self.url = "https://rt.pornhub.com/"
        self.session = requests.Session()
        self.session.headers = browserFake

    def search(self, q):
        response = PHPage(self.session.get("%svideo/search" % self.url, params={
                "search": q
            }), self.session)
        return response

    def getPage(self, number=1, min_duration=0, c=""):
        if isinstance(c, str):
            response = PHPage(self.session.get("%s%s" % (self.url, c), params={
                    "page": number,
                    "min_duration": min_duration
                }))
        else:
            response = PHPage(self.session.get("%svideo" % self.url, params={
                    "page": number,
                    "min_duration": min_duration,
                    "c": c
                }), self.session)
        return response


class PHPage:
    def __init__(self, page, session):
        self.page = page.text
        self.session = session
        videos = self.page.split('class=" js-pop videoblock videoBox"')
        videos.pop(0)
        self.videos = []
        for video in videos:
            v = {}
            v["id"] = video.split('data-id="', 1)[1].split('"', 1)[0]
            v["title"] = video.split('title="', 1)[1].split('"', 1)[0].replace("&quot;", '"')
            v["url"] = "https://rt.pornhub.com/view_video.php?%s" % video.split('href="/view_video.php?', 1)[1].split('"', 1)[0]
            v["preview"] = video.split('data-thumb_url = "', 1)[1].split('"', 1)[0]
            v["duration"] = video.split('<var class="duration">', 1)[1].split('<', 1)[0]
            v["views"] = video.split('<span class="views"><var>', 1)[1].split('<', 1)[0]
            self.videos.append(v)

    def get(self, num):
        return PHVideo(self.videos[num], self.session)

    def count(self):
        return len(self.videos)


class PHVideo:
    def __init__(self, video, session):
        for key in video:
            exec("self.%s = %s" % (key, repr(video[key])))
        self.video = video
        self.page = session.post(video["url"]).text
        self.views = self.page.split('<div class="views"><span class="count">', 1)[1].split('</span>', 1)[0]
        self.percent = self.page.split('<span class="percent">', 1)[1].split('</span>', 1)[0]
        self.votesUp = self.page.split('<span class="votesUp">', 1)[1].split('</span>', 1)[0]
        self.votesDown = self.page.split('<span class="votesDown">', 1)[1].split('</span>', 1)[0]
