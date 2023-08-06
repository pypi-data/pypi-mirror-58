import re
from urllib.parse import urlparse, parse_qs


tags_map = {
    "header": ('<h3 class="rusmarkup-subheader">{}</h3>', "ЗАГОЛОВОК"),
    "video": ('<video class="rusmarkup-video" width="480" controls src="{0}"><a href="{0}">{1}</a></video>', "ССЫЛКА"),
    "youtube": ('<div class="rusmarkup-youtube" data-id="{}"></div>', "ССЫЛКА"),
    "audio": ('<audio class="rusmarkup-audio" width="480" controls src="{0}"><a href="{0}">{1}</a></audio>', "ССЫЛКА"),
    "image": ('<img class="rusmarkup-image" src="{}" alt="{}">', "ССЫЛКА"),
    "link": ('<a class="rusmarkup-link"  href="{}">{}</a>', "ССЫЛКА"),
    "warning": ('<p class="rusmarkup-warning">{}</p>', "ПРЕДУПРЕЖДЕНИЕ"),
    "tip": ('<p class="rusmarkup-tip">{}</p>', "СОВЕТ"),
    "quote": ('<blockquote class="rusmarkup-quote">{}</blockquote>', "ЦИТАТА"),
    "strong": ('<strong class="rusmarkup-strong">{}</strong>', "ЖИРНЫЙ"),
    "emphasized": ('<em class="rusmarkup-emphasized">{}</em>', "КУРСИВ"),
    "sup": ('<sup>{}</sup>', "ВЕРХНИЙРЕГИСТР"),
    "sub": ('<sub>{}</sub>', "НИЖНИЙРЕГИСТР"),
    "list": ('<ol class="rusmarkup-list">{}</ol>', "СПИСОК")
}


class rusmarkup2html:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, tags_map: dict):
        self._tags_map = tags_map
        self._tags = list({tag[1] for _, tag in self._tags_map.items()})
        self._pattern = r'\((?P<tag>{})\)(?P<value>.*?)\((?P=tag)\)'.format(
            "|".join(self._tags)
        )
        self._regex = re.compile(self._pattern, re.IGNORECASE|re.DOTALL)

    def __call__(self, text: str):
        """
        Конвертировать текст, размеченный тэгами, в html.
        """
        text = self.preprocess(text)
        return re.sub(self._regex, self._replacer, text)

    @property
    def description(self):
        """
        Описание разметки
        """
        half = len(self._tags)//2
        tags_1, tags_2 = self._tags[:half], self._tags[half:]
        return f"""Примеры разметки:\n(ссылка)somesite.ru Отображаемое имя ссылки(ссылка)
(ссылка)somesite.ru/video.mp4 Видео, аудио и youtube отобразятся с проигрывателями(ссылка)
(КУРСИВ)тэги можно писать как в нижнем, так и в верхнем регистре(КУРСИВ)\n(список)\nЭлемент 1\n        элемент 1.1
Элемент 2\n(список)\n\nДоступные тэги:\n{", ".join(tags_1)}\n{", ".join(tags_2)}"""

    @property
    def pattern(self):
        """
        Регулярное выражение для поиска тэгированных строк
        """
        return self._pattern

    @property
    def tags_map(self):
        """
        Соответствие тэгов html-тэгам
        """
        return self._tags_map

    def preprocess(self, text):
        """
        Предобработка текста
        """
        return text

    def remove_tags(self, text: str):
        """
        Очистить текст от тэгов
        """
        return re.sub(self._regex, self._remover, text)

    def handle_header(self, tag, value):
        return self._tags_map['header'][0].format(value)

    def handle_link(self, tag, value):
        link, title = value.split(maxsplit=1)
        link = link.strip()
        title = title.strip()
        if link.endswith(('mp4', 'ogv', 'webm')):
            return self._tags_map['video'][0].format(link, title)
        elif link.endswith(('mp3', 'ogg', 'wav', 'aac')):
            return self._tags_map['audio'][0].format(link, title)
        elif link.endswith(('jpg', 'jpeg', 'png', 'gif', 'tiff', 'bmp', 'png', 'heif')):
            return self._tags_map['image'][0].format(link, title)
        elif 'youtube.com' in link:
            u = urlparse(link)
            try:
                video_id = parse_qs(u.query)['v'][0]
            except:
                return self._tags_map['link'][0].format(link, title)
            return self._tags_map['youtube'][0].format(video_id)
        else:
            return self._tags_map['link'][0].format(link, title)

    def handle_warning(self, tag, value):
        return self._tags_map['warning'][0].format(value)

    def handle_tip(self, tag, value):
        return self._tags_map['tip'][0].format(value)

    def handle_quote(self, tag, value):
        return self._tags_map['quote'][0].format(value)

    def handle_strong(self, tag, value):
        return self._tags_map['strong'][0].format(value)

    def handle_emphasized(self, tag, value):
        return self._tags_map['emphasized'][0].format(value)

    def handle_sup(self, tag, value):
        return self._tags_map['sup'][0].format(value)

    def handle_sub(self, tag, value):
        return self._tags_map['sub'][0].format(value)

    def handle_list(self, tag, value):
        tags = []
        items = re.split(r'\n+', value)
        sublist = []
        for item in items:
            if not item:
                continue

            cleaned_item = item.lstrip()
            leading_spaces = len(item) - len(cleaned_item)
            if leading_spaces == 0:
                if sublist:
                    sublist_string = re.sub(self._regex, self._replacer, '(СПИСОК){}(СПИСОК)'.format("\n".join(sublist)))
                    tags.append(sublist_string)
                    sublist = []
                if tags:
                    tags.append('</li>')
                tags.append(f'<li>{cleaned_item}')
            else:
                sublist.append(cleaned_item)
        tags.append('</li>')

        return self._tags_map['list'][0].format("".join(tags))

    def _replacer(self, matchobj):
        tag = matchobj.group('tag').upper()
        value = matchobj.group('value')
        value = re.sub(self._regex, self._replacer, value)
        if tag == 'ЗАГОЛОВОК':
           return self.handle_header(tag, value)
        elif tag == 'ССЫЛКА':
            return self.handle_link(tag, value)
        elif tag == 'ПРЕДУПРЕЖДЕНИЕ':
            return self.handle_warning(tag, value)
        elif tag == 'СОВЕТ':
            return self.handle_tip(tag, value)
        elif tag == 'ЦИТАТА':
            return self.handle_quote(tag, value)
        elif tag == 'ЖИРНЫЙ':
            return self.handle_strong(tag, value)
        elif tag == 'КУРСИВ':
            return self.handle_emphasized(tag, value)
        elif tag == 'ВЕРХНИЙРЕГИСТР':
            return self.handle_sup(tag, value)
        elif tag == 'НИЖНИЙРЕГИСТР':
            return self.handle_sub(tag, value)
        elif tag == 'СПИСОК':
            return self.handle_list(tag, value)

    def _remover(self, matchobj):
        value = matchobj.group('value')
        value = re.sub(self._regex, self._remover, value)
        return value
