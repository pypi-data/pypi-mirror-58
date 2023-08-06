## RUSMARKUP - простой язык разметки для русского языка для конвертации в html


Существующие языки разметки требуют от пользователя запоминать новый синтаксис, 
а также переключать раскладку при наборе русского текста. 
Данная библиотека - простая расширяемая альтернатива распространенным языкам разметки для 
использования, к примеру, в CMS.

Тэги можно переопределить, изменив словарь tags_map и переопределив методы класса rusmarkup2html.
Тэг (список) поддерживает только один уровень вложения. Если нужно больше, то можно переопределить 
своей логикой.


```python
from rusmarkup import rusmarkup2html, tags_map


text = """

Какой-то текст

(ЗАГОЛОВОК)Это заголовок(ЗАГОЛОВОК)


текст дальше.
(ССЫЛКА)https://www.youtube.com/watch?v=UGuqxiKxNDE фонд Кораблик(ССЫЛКА)

(ЦИТАТА)это цитата(ЦИТАТА)

(ССЫЛКА)https://cdn.pixabay.com/photo/2019/12/13/08/27/snow-4692469_960_720.jpg занесло снегом(ссылка)

еще текст (верхнийрегистр) текст в верхнем регистре (верхнийрегистр)

(ПРЕДУПРЕЖДЕНИЕ)это предупреждение(ПРЕДУПРЕЖДЕНИЕ)

(СОВЕТ)это совет(СОВЕТ)

(курсив)это курсивом(курсив)

и снова текст (нижнийрегистр) текст в нижнем регистре(нижнийрегистр)



(жирный)(курсив)это жирным курсивом(курсив)(жирный)

Список
(список)
Позиция 1
    Позиция 1.1
    Позиция 1.2
Позиция 2
(список)

"""

# Для отображения youtube-плеера нужно добавить следующий скрипт в html-страницу
script = """
<script>
      var tag = document.createElement('script');

      tag.src = "https://www.youtube.com/iframe_api";
      var firstScriptTag = document.getElementsByTagName('script')[0];
      firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
      
      var youtubePlayers = document.getElementsByClassName('rusmarkup-youtube');
      for (var i=0; i < youtubePlayers.length; i++) {
        var player = youtubePlayers[i];
          function onYouTubeIframeAPIReady() {
            player = new YT.Player(player, {
              height: '390',
              width: '640',
              videoId: player.dataset.id
            });
          }
      }
</script>
"""

markupper = rusmarkup2html(tags_map)
print(markupper.description)

with open("index.html", 'w') as f:
    f.write(f'<div style="white-space: pre-wrap;">{markupper(text)}</div>{script}')
```

## Запуск тестов
```bash
python3 test.py
```