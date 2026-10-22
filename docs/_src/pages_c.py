# -*- coding: utf-8 -*-
"""Разделы «Файлы», «Записи» и «Терминал»."""

PAGES = {}

PAGES["files"] = {
    "group_ru": "Файлы", "group_en": "Files",
    "title_ru": "Расшифровка аудио и видео", "title_en": "Transcribing audio and video",
    "lede_ru": "Готовую запись — звонок, интервью, вебинар, голосовое сообщение — можно отдать Heardly файлом. "
               "Расшифровка появится в Истории, в разделе «Файлы».",
    "lede_en": "An existing recording — a call, an interview, a webinar, a voice message — can be handed to Heardly as a file. "
               "The transcript shows up in History, in the “Files” section.",
    "body": """
    <div class="note pro">
      <b><span lang="ru">Функция Pro</span><span lang="en">A Pro feature</span></b>
      <p><span lang="ru">Расшифровка файлов входит в <a href="pricing.html">Pro</a> и в 14-дневный пробный период.</span><span lang="en">File transcription is part of <a href="pricing.html">Pro</a> and of the 14-day trial.</span></p>
    </div>

    <h2 id="how"><span lang="ru">Два способа отдать файл</span><span lang="en">Two ways to hand over a file</span></h2>
    <div lang="ru">
      <ul>
        <li><b>Перетащить.</b> Откройте попап Heardly и бросьте файл в зону внизу.</li>
        <li><b>Выбрать.</b> В том же месте нажмите «или выберите файл». Можно отметить сразу несколько — они встанут в очередь.</li>
      </ul>
      <p>Откроется История на разделе «Файлы», и там будет видно, что считается сейчас и что уже готово.</p>
    </div>
    <div lang="en">
      <p>Either way, History opens on the “Files” section, where you can see what is being processed and what is already done.</p>
      <ul>
        <li><b>Drag it in.</b> Open the Heardly panel and drop the file into the zone at the bottom.</li>
        <li><b>Pick it.</b> In the same place, click “or choose file”. You can select several at once — they queue up.</li>
      </ul>
    </div>

    <figure>
      <img src="img/history-files.png" alt="Раздел «Файлы» в Истории: зона для перетаскивания, кнопка «Выбрать файл», список готовых расшифровок и текст с таймкодами">
      <figcaption><span lang="ru">Раздел «Файлы»: зона загрузки сверху, готовые расшифровки под ней.</span><span lang="en">The Files section: the drop zone on top, finished transcripts below.</span></figcaption>
    </figure>

    <h2 id="formats"><span lang="ru">Какие файлы подходят</span><span lang="en">Which files work</span></h2>
    <div lang="ru">
      <p>Любое аудио и видео, которое умеет открывать macOS: <code>m4a</code>, <code>mp3</code>, <code>wav</code>, <code>aac</code>, <code>mp4</code>, <code>mov</code> и прочие. Из видео Heardly берёт звуковую дорожку, картинка не нужна.</p>
    </div>
    <div lang="en">
      <p>Any audio or video macOS can open: <code>m4a</code>, <code>mp3</code>, <code>wav</code>, <code>aac</code>, <code>mp4</code>, <code>mov</code> and the rest. From a video Heardly takes the audio track; the picture is not needed.</p>
    </div>

    <h2 id="result"><span lang="ru">Что получится</span><span lang="en">What you get</span></h2>
    <div lang="ru">
      <p>Текст с таймкодами: у каждой реплики своё время от начала записи, по нему удобно возвращаться к нужному месту в исходнике. Подписей источников здесь нет — в файле нет разделения на микрофон и звук приложений, оно появляется только в <a href="live.html">живой записи</a>.</p>
      <p>Результат можно <a href="export.html">выгрузить</a> в восемь форматов, в том числе в субтитры SRT и VTT.</p>
    </div>
    <div lang="en">
      <p>Text with timecodes: every line carries its time from the start of the recording, which makes it easy to go back to the right spot in the original. There are no source labels here — a file has no split between microphone and app audio; that only exists in a <a href="live.html">live recording</a>.</p>
      <p>The result can be <a href="export.html">exported</a> to eight formats, subtitles in SRT and VTT among them.</p>
    </div>

    <div class="note tip">
      <b><span lang="ru">Много файлов — через терминал</span><span lang="en">Many files — use the terminal</span></b>
      <p><span lang="ru">Если расшифровать нужно десятки записей, удобнее <a href="cli.html">команда <code>heardly</code></a>: её можно запустить в цикле и сразу сложить результат в нужные файлы.</span><span lang="en">If you have dozens of recordings, the <a href="cli.html"><code>heardly</code> command</a> is easier: run it in a loop and write the results straight to the files you want.</span></p>
    </div>
""",
}

PAGES["history"] = {
    "group_ru": "Записи", "group_en": "Recordings",
    "title_ru": "История", "title_en": "History",
    "lede_ru": "Всё, что Heardly расшифровал, остаётся в Истории и разложено по трём разделам: "
               "«Диктовки», «Звонки и встречи» и «Файлы».",
    "lede_en": "Everything Heardly has transcribed stays in History, sorted into three sections: "
               "“Dictations”, “Calls and meetings” and “Files”.",
    "body": """
    <h2 id="sections"><span lang="ru">Три раздела</span><span lang="en">Three sections</span></h2>
    <table class="ref">
      <tr><td><span lang="ru">Диктовки</span><span lang="en">Dictations</span></td>
          <td><span lang="ru">Всё, что вы наговорили в поля ввода. Короткие записи без таймкодов, показываются сразу текстом.</span><span lang="en">Everything you dictated into text fields. Short entries without timecodes, shown as plain text.</span></td></tr>
      <tr><td><span lang="ru">Звонки и встречи</span><span lang="en">Calls and meetings</span></td>
          <td><span lang="ru">Живые записи. У реплик есть время и подпись источника — «Я» или «Компьютер».</span><span lang="en">Live recordings. Lines carry a time and a source label — “Me” or “Computer”.</span></td></tr>
      <tr><td><span lang="ru">Файлы</span><span lang="en">Files</span></td>
          <td><span lang="ru">Расшифровки загруженных аудио и видео, с таймкодами. Здесь же зона для новых файлов.</span><span lang="en">Transcripts of uploaded audio and video, with timecodes. The drop zone for new files is here too.</span></td></tr>
    </table>

    <figure>
      <img src="img/history-dictations.png" alt="Раздел «Диктовки» в Истории: счётчики слов и скорости сверху, записи за сегодня">
      <figcaption><span lang="ru">«Диктовки» показывают текст сразу — заголовок у короткой записи не нужен.</span><span lang="en">“Dictations” show the text straight away — a short entry needs no title.</span></figcaption>
    </figure>

    <figure>
      <img src="img/history-calls.png" alt="Раздел «Звонки и встречи»: список записей слева, расшифровка с таймкодами и подписями источников справа">
      <figcaption><span lang="ru">У звонков слева список, справа расшифровка с временем и подписями.</span><span lang="en">Calls get a list on the left and the transcript, with times and labels, on the right.</span></figcaption>
    </figure>

    <h2 id="find"><span lang="ru">Поиск и порядок</span><span lang="en">Search and order</span></h2>
    <div lang="ru">
      <p>Поле поиска ищет по тексту расшифровок, а не только по названиям, — так проще найти встречу, от которой помнишь одну фразу. Записи сгруппированы по дням: «Сегодня», «Вчера» и дальше по датам.</p>
    </div>
    <div lang="en">
      <p>The search field looks inside the transcripts, not just at the titles — which helps when all you remember of a meeting is one phrase. Entries are grouped by day: “Today”, “Yesterday” and then by date.</p>
    </div>

    <h2 id="storage"><span lang="ru">Где это лежит</span><span lang="en">Where it is kept</span></h2>
    <div lang="ru">
      <p>Внизу окна написано «Хранится только на этом Mac», и это буквально так: каждая запись — обычный текстовый файл в <a href="folder.html">папке расшифровок</a>. Никакого облака и никакой синхронизации у Heardly нет.</p>
      <p>Файлы можно переименовывать и удалять прямо в Finder — История подхватит изменения.</p>
    </div>
    <div lang="en">
      <p>The line at the bottom of the window says “Stored only on this Mac”, and it is literal: every entry is an ordinary text file in the <a href="folder.html">transcripts folder</a>. Heardly has no cloud and no sync.</p>
      <p>You can rename and delete the files in Finder — History picks the changes up.</p>
    </div>
""",
}

PAGES["export"] = {
    "group_ru": "Записи", "group_en": "Recordings",
    "title_ru": "Экспорт", "title_en": "Export",
    "lede_ru": "Любую расшифровку можно выгрузить в восемь форматов — от простого текста до субтитров и документа Word.",
    "lede_en": "Any transcript can be exported to eight formats — from plain text to subtitles and a Word document.",
    "body": """
    <h2 id="how"><span lang="ru">Как выгрузить</span><span lang="en">How to export</span></h2>
    <div lang="ru">
      <p>Откройте запись в <a href="history.html">Истории</a> и нажмите «Экспорт». Выберите формат, при необходимости включите «С таймкодами» и сохраните файл.</p>
      <p>Рядом есть «Копировать» — если текст нужен не файлом, а сразу в письмо или задачу.</p>
    </div>
    <div lang="en">
      <p>Open an entry in <a href="history.html">History</a> and press Export. Pick a format, switch “With timecodes” on if you need them, and save the file.</p>
      <p>Next to it there is Copy — for when you want the text in an email or a task rather than in a file.</p>
    </div>

    <figure>
      <img class="free" src="img/export-panel.png" alt="Окно Истории с открытой панелью экспорта: восемь форматов, переключатели таймкодов и подписей источников, кнопка «Сохранить как TXT»">
      <figcaption><span lang="ru">Панель экспорта открывается кнопкой над расшифровкой. Формат, таймкоды и подписи выбираются здесь же.</span><span lang="en">The Export panel opens with the button above the transcript. Format, timecodes and labels are all chosen there.</span></figcaption>
    </figure>

    <h2 id="formats"><span lang="ru">Форматы</span><span lang="en">Formats</span></h2>
    <table class="ref">
      <tr>
        <th><span lang="ru">Формат</span><span lang="en">Format</span></th>
        <th><span lang="ru">Когда нужен</span><span lang="en">When you need it</span></th>
        <th><span lang="ru">Доступ</span><span lang="en">Access</span></th>
      </tr>
      <tr><td>TXT</td><td><span lang="ru">Просто текст — вставить в заметку, письмо, задачу.</span><span lang="en">Plain text — paste into a note, an email, a task.</span></td><td><span lang="ru">Бесплатно</span><span lang="en">Free</span></td></tr>
      <tr><td>SRT</td><td><span lang="ru">Субтитры для видео. Самый распространённый формат.</span><span lang="en">Video subtitles. The most common format.</span></td><td>Pro</td></tr>
      <tr><td>VTT</td><td><span lang="ru">Субтитры для веба, формат HTML5-плееров.</span><span lang="en">Web subtitles, the HTML5 player format.</span></td><td>Pro</td></tr>
      <tr><td>CSV</td><td><span lang="ru">Таблица: реплики строками, чтобы разобрать в Excel или Google Sheets.</span><span lang="en">A table: one line per entry, to work through in Excel or Google Sheets.</span></td><td>Pro</td></tr>
      <tr><td>Markdown</td><td><span lang="ru">Для Obsidian, Notion и всего, что понимает разметку.</span><span lang="en">For Obsidian, Notion and anything that speaks markup.</span></td><td>Pro</td></tr>
      <tr><td>HTML</td><td><span lang="ru">Готовая страница — отправить ссылкой или открыть в браузере.</span><span lang="en">A ready page — send it as a link or open it in a browser.</span></td><td>Pro</td></tr>
      <tr><td>PDF</td><td><span lang="ru">Когда расшифровку надо отдать «как есть» и без правок.</span><span lang="en">When the transcript goes out as-is and must not be edited.</span></td><td>Pro</td></tr>
      <tr><td>DOCX</td><td><span lang="ru">Word: протокол встречи, который будут дорабатывать руками.</span><span lang="en">Word: a meeting record someone will keep working on.</span></td><td>Pro</td></tr>
    </table>

    <div class="note tip">
      <b><span lang="ru">Текст и так лежит файлом</span><span lang="en">The text is already a file</span></b>
      <p><span lang="ru">Если нужен просто текст, экспорт можно не открывать: расшифровки и без того хранятся как <code>.txt</code> в <a href="folder.html">папке расшифровок</a>.</span><span lang="en">If plain text is all you need, you can skip Export: transcripts are already kept as <code>.txt</code> in the <a href="folder.html">transcripts folder</a>.</span></p>
    </div>
""",
}

PAGES["folder"] = {
    "group_ru": "Записи", "group_en": "Recordings",
    "title_ru": "Папка расшифровок", "title_en": "Transcripts folder",
    "lede_ru": "Heardly не прячет записи в свою базу: каждая расшифровка — текстовый файл в обычной папке, "
               "которую вы можете открыть, перенести в облако или положить под резервное копирование.",
    "lede_en": "Heardly does not hide your recordings in a database: every transcript is a text file in an ordinary folder "
               "you can open, move into a cloud drive or put under backup.",
    "body": """
    <h2 id="where"><span lang="ru">Где она</span><span lang="en">Where it is</span></h2>
    <div lang="ru">
      <p>По умолчанию — <code>~/Documents/Heardly</code>. Путь виден в <a href="settings.html">Настройках → Записи</a>, там же кнопки «Открыть в Finder» и «Изменить…».</p>
    </div>
    <div lang="en">
      <p>By default, <code>~/Documents/Heardly</code>. The path is shown in <a href="settings.html">Settings → Recordings</a>, together with the “Open in Finder” and “Change…” buttons.</p>
    </div>

    <figure>
      <img src="img/settings-recordings.png" alt="Раздел «Записи» в настройках: путь к папке расшифровок и кнопка открытия истории">
      <figcaption><span lang="ru">Путь к папке и кнопки, чтобы открыть её в Finder или перенести в другое место.</span><span lang="en">The folder path, with buttons to open it in Finder or move it somewhere else.</span></figcaption>
    </figure>

    <h2 id="inside"><span lang="ru">Что внутри</span><span lang="en">What is inside</span></h2>
    <div lang="ru">
      <p>Один файл <code>.txt</code> на запись, имя файла — название записи. Внутри обычный текст; у звонков и файлов в начале строки стоит время, у звонков ещё и подпись источника:</p>
      <pre><code>[00:04] [Я] Коллеги, собрались по редизайну лендинга.
[00:12] [Компьютер] Я вчера посмотрел метрики.</code></pre>
      <p>Рядом лежит служебный файл <code>.heardly-index.json</code> — он помнит, к какому разделу Истории относится запись. Удалять его не стоит, но и ничего ценного в нём нет.</p>
    </div>
    <div lang="en">
      <p>One <code>.txt</code> file per entry, named after the entry. Inside is plain text; calls and files start each line with a time, and calls add the source label:</p>
      <pre><code>[00:04] [Me] Right, we’re here about the landing page redesign.
[00:12] [Computer] I looked at the metrics yesterday.</code></pre>
      <p>Alongside them sits a housekeeping file, <code>.heardly-index.json</code>, which remembers which History section an entry belongs to. Don’t delete it, but there is nothing valuable in it either.</p>
    </div>

    <h2 id="move"><span lang="ru">Перенести папку</span><span lang="en">Moving the folder</span></h2>
    <div lang="ru">
      <p>Кнопка «Изменить…» в настройках переносит расшифровки в новое место вместе со служебным файлом. Папку можно положить в iCloud Drive или в другое облако — тогда записи будут доступны на других ваших компьютерах, но имейте в виду: это уже синхронизация облаком, а не Heardly, и текст встреч уедет на чужие серверы.</p>
    </div>
    <div lang="en">
      <p>The “Change…” button in Settings moves the transcripts to a new place together with the housekeeping file. You can put the folder in iCloud Drive or another cloud, and the entries will be available on your other computers — but note that this is the cloud syncing them, not Heardly, and the text of your meetings will travel to someone else’s servers.</p>
    </div>

    <div class="note tip">
      <b><span lang="ru">Правьте прямо в Finder</span><span lang="en">Edit straight in Finder</span></b>
      <p><span lang="ru">Переименовали файл, подправили текст, удалили лишнее — История увидит это сама, перезапускать Heardly не нужно.</span><span lang="en">Rename a file, fix the text, delete what you don’t need — History notices by itself, with no need to restart Heardly.</span></p>
    </div>
""",
}

PAGES["cli"] = {
    "group_ru": "Терминал", "group_en": "Terminal",
    "title_ru": "Команда heardly", "title_en": "The heardly command",
    "lede_ru": "Та же модель, но из терминала: расшифровать файл одной строкой, прогнать папку циклом "
               "или встроить расшифровку в свой скрипт.",
    "lede_en": "The same model, from the terminal: transcribe a file in one line, run a folder through a loop "
               "or wire transcription into a script of your own.",
    "body": """
    <div class="note pro">
      <b><span lang="ru">Функция Pro</span><span lang="en">A Pro feature</span></b>
      <p><span lang="ru">Команда работает при активной подписке <a href="pricing.html">Pro</a> или в пробный период.</span><span lang="en">The command works with an active <a href="pricing.html">Pro</a> subscription or during the trial.</span></p>
    </div>

    <h2 id="install"><span lang="ru">Установка</span><span lang="en">Installing</span></h2>
    <div lang="ru">
      <p>Откройте <a href="settings.html">Настройки → Система</a> и нажмите «Установить» в строке «Команда в терминале». После этого <code>heardly</code> доступна в любом окне терминала.</p>
    </div>
    <div lang="en">
      <p>Open <a href="settings.html">Settings → System</a> and press Install in the “Terminal command” row. After that, <code>heardly</code> is available in any terminal window.</p>
    </div>

    <h2 id="usage"><span lang="ru">Как пользоваться</span><span lang="en">Usage</span></h2>
    <pre lang="ru"><code>heardly &lt;файл&gt; [опции]</code></pre>
    <pre lang="en"><code>heardly &lt;file&gt; [options]</code></pre>
    <table class="ref">
      <tr>
        <th><span lang="ru">Опция</span><span lang="en">Option</span></th>
        <th><span lang="ru">Что делает</span><span lang="en">What it does</span></th>
      </tr>
      <tr><td><code>-s</code>, <code>--speakers</code></td><td><span lang="ru">Размечает говорящих: кто из них произнёс реплику.</span><span lang="en">Labels the speakers: who said which line.</span></td></tr>
      <tr><td><code>-t</code>, <code>--timecodes</code></td><td><span lang="ru">Добавляет таймкоды.</span><span lang="en">Adds timecodes.</span></td></tr>
      <tr><td><code>-f</code>, <code>--format</code></td><td><code>txt</code><span lang="ru"> (по умолчанию), </span><span lang="en"> (default), </span><code>srt</code>, <code>json</code></td></tr>
      <tr><td><code>-o</code>, <code>--output</code></td><td><span lang="ru">Сохранить в файл вместо вывода на экран.</span><span lang="en">Write to a file instead of printing to the screen.</span></td></tr>
      <tr><td><code>-h</code>, <code>--help</code></td><td><span lang="ru">Показать справку.</span><span lang="en">Show the help.</span></td></tr>
    </table>

    <h2 id="examples"><span lang="ru">Примеры</span><span lang="en">Examples</span></h2>
    <div lang="ru"><p>Расшифровать запись и посмотреть текст прямо в терминале:</p></div>
    <div lang="en"><p>Transcribe a recording and read the text right in the terminal:</p></div>
    <pre><code>heardly ~/Downloads/call.m4a</code></pre>

    <div lang="ru"><p>Субтитры к видео с разметкой говорящих:</p></div>
    <div lang="en"><p>Subtitles for a video, with speakers marked:</p></div>
    <pre><code>heardly webinar.mp4 -s -f srt -o webinar.srt</code></pre>

    <div lang="ru"><p>Прогнать всю папку с записями:</p></div>
    <div lang="en"><p>Run a whole folder of recordings:</p></div>
    <pre><code>for f in ~/Calls/*.m4a; do
  heardly "$f" -t -o "${f%.m4a}.txt"
done</code></pre>

    <h2 id="speakers"><span lang="ru">Про разметку говорящих</span><span lang="en">About speaker labels</span></h2>
    <div lang="ru">
      <p>Флаг <code>-s</code> разделяет голоса по звучанию, а не по источнику звука. Это работает только в терминале: в самом приложении разметки говорящих сейчас нет, там реплики делятся на «Я» и «Компьютер» по тому, откуда пришёл звук.</p>
      <p>Модель для разметки скачивается при первом запуске с флагом, дальше работает офлайн. Если разделить голоса не удалось, команда честно скажет об этом и отдаст текст без подписей.</p>
    </div>
    <div lang="en">
      <p>The <code>-s</code> flag separates voices by how they sound, not by where the audio came from. This works in the terminal only: the app itself has no speaker labels at the moment, and splits lines into “Me” and “Computer” by audio source instead.</p>
      <p>The model for this is downloaded the first time you use the flag and works offline afterwards. If the voices cannot be separated, the command says so plainly and returns the text without labels.</p>
    </div>
""",
}
