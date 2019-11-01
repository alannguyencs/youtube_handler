import codecs
import pafy
from datetime import datetime
from pydub import AudioSegment
import os
from ytcc.download import Download
from constants import *


class Youtube():
    def __init__(self, url):
        self.url = url
        self.name = None
        self.video = None
        self.audio = None

        self.set_up()
        self.download_audio()
        self.download_script()

    def set_up(self):
        self.video = pafy.new(self.url)
        self.audio = self.video.getbestaudio()
        self.name = self.get_name(self.video.title)

    def download_audio(self):
        audio_path = AUDIO_PATH + self.name + self.audio.extension
        self.audio.download(audio_path)

        print (audio_path)
        sound = AudioSegment.from_file(audio_path)
        mp3_path = AUDIO_PATH + self.name + 'mp3'

        sound.export(mp3_path, format="mp3", bitrate="128k")
        os.remove(audio_path)

    def download_script(self):
        download = Download()
        script = download.get_captions(self.url[-11:], 'en')

        script_file = open(SCRIPT_PATH + self.name + '.txt', 'w')
        script_file.write(script)

    def get_name(self, video_title):
        video_title = self.remove_non_alpha_characters(video_title)
        timestamp = datetime.today().strftime('%y%m%d')

        return "{}_{}.".format(timestamp, video_title)

    def remove_non_alpha_characters(self, text):
        return ''.join(c for c in text if (c.isalpha() or c.isdigit()))

class Processor():
    def __init__(self):
        self.procedure()

    def procedure(self):
        urls = self.parse_data_file(URL_PATH)
        parsed_urls = self.parse_data_file(PARSED_URL_PATH)

        for url in urls:
            if url not in parsed_urls:
                Youtube(url)
                self.save_url(url)

    def save_url(self, url):
        parsed_urls_file = open(PARSED_URL_PATH, 'a')
        parsed_urls_file.write(url + '\n')
        parsed_urls_file.close()

    def parse_data_file(self, file_path):
        urls = []
        data_file = codecs.open(file_path, 'r', 'utf8')
        for line in data_file:
            line = line.strip()
            if len(line) == 0: continue
            urls.append(line)

        return urls






