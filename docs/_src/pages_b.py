# -*- coding: utf-8 -*-
"""Разделы «Диктовка» и «Звонки и встречи»."""

PAGES = {}

PAGES["dictation"] = {
    "group_ru": "Диктовка", "group_en": "Dictation",
    "title_ru": "Как диктовать", "title_en": "How to dictate",
    "lede_ru": "Диктовка работает в любом приложении, где есть текстовое поле. "
               "Heardly вставляет готовый текст туда, где стоит курсор, и не трогает то, что уже написано.",
    "lede_en": "Dictation works in any app with a text field. "
               "Heardly inserts the finished text where your cursor is and leaves what you already wrote alone.",
    "body": """
    <h2 id="key"><span lang="ru">Горячая клавиша</span><span lang="en">The shortcut</span></h2>
    <div lang="ru">
      <p>По умолчанию это правый <kbd>⌘</kbd> — клавиша, которая в большинстве раскладок ничем не занята. Сменить её можно в <a href="settings.html">Настройках → Основные</a>: нажмите на поле с сочетанием и наберите своё.</p>
      <p>Подойдёт как одиночный модификатор (правый <kbd>⌥</kbd>, правый <kbd>⌃</kbd>), так и сочетание вроде <kbd>⌥</kbd> + <kbd>Space</kbd>.</p>
    </div>
    <div lang="en">
      <p>The default is the right <kbd>⌘</kbd> — a key most layouts leave unused. You can change it in <a href="settings.html">Settings → General</a>: click the shortcut field and press the keys you want.</p>
      <p>A lone modifier works (right <kbd>⌥</kbd>, right <kbd>⌃</kbd>), and so does a combination such as <kbd>⌥</kbd> + <kbd>Space</kbd>.</p>
    </div>

    <h3 id="modes"><span lang="ru">Нажатие или удержание</span><span lang="en">Toggle or hold</span></h3>
    <table class="ref">
      <tr>
        <td><span lang="ru">Нажатие</span><span lang="en">Toggle</span></td>
        <td><span lang="ru">Одно нажатие включает запись, второе выключает. Удобно для длинных мыслей: руки свободны.</span><span lang="en">One press starts recording, another stops it. Good for longer thoughts — your hands stay free.</span></td>
      </tr>
      <tr>
        <td><span lang="ru">Удержание</span><span lang="en">Hold</span></td>
        <td><span lang="ru">Запись идёт, пока клавиша зажата. Удобно для коротких реплик: отпустил — и текст уже на месте.</span><span lang="en">Recording runs while the key is held. Good for short remarks — let go and the text is already there.</span></td>
      </tr>
    </table>
    <div lang="ru"><p>Режим переключается в <a href="settings.html">Настройках → Основные</a>, строка «Активация диктовки при».</p></div>
    <div lang="en"><p>You switch modes in <a href="settings.html">Settings → General</a>, the “Activation” row.</p></div>

    <figure>
      <img src="img/settings-general.png" alt="Раздел «Основные» в настройках Heardly: горячая клавиша, активация диктовки, микрофон, язык распознавания">
      <figcaption><span lang="ru">Горячая клавиша и режим активации — в разделе «Основные».</span><span lang="en">The shortcut and the activation mode live in the General section.</span></figcaption>
    </figure>

    <h2 id="insert"><span lang="ru">Куда попадает текст</span><span lang="en">Where the text goes</span></h2>
    <div lang="ru">
      <p>Heardly вставляет текст в активное поле там, где стоит курсор. Чтобы вставка выглядела как продолжение фразы, а не как кусок из другого письма, приложение смотрит на последние символы перед курсором.</p>
      <ul>
        <li>Если перед курсором конец предложения, новая фраза начнётся с заглавной буквы.</li>
        <li>Если вы остановились посреди фразы, текст продолжится со строчной.</li>
        <li>Если в поле что-то выделено, продиктованное заменит выделенное — так удобно переписывать абзац голосом.</li>
      </ul>
      <p>Для вставки используется буфер обмена, но прежнее содержимое буфера Heardly возвращает сразу после вставки — скопированная ссылка или пароль никуда не денутся.</p>
    </div>
    <div lang="en">
      <p>Heardly inserts the text into the active field at the cursor. So the insert reads as a continuation rather than a fragment from somewhere else, the app looks at the characters just before the cursor.</p>
      <ul>
        <li>If a sentence ended right before the cursor, the new one starts with a capital letter.</li>
        <li>If you stopped mid-sentence, the text continues in lower case.</li>
        <li>If something is selected in the field, the dictated text replaces it — a convenient way to rewrite a paragraph by voice.</li>
      </ul>
      <p>The insert goes through the clipboard, but Heardly puts the previous contents straight back — a link or a password you had copied is not lost.</p>
    </div>

    <h2 id="cancel"><span lang="ru">Отмена</span><span lang="en">Cancelling</span></h2>
    <div lang="ru">
      <p><kbd>esc</kbd> прерывает диктовку в любой момент: панель закрывается, в поле ничего не вставляется. Сама расшифровка при этом сохраняется в <a href="history.html">Историю</a> — если передумаете, текст можно забрать оттуда.</p>
    </div>
    <div lang="en">
      <p><kbd>esc</kbd> stops dictation at any point: the bar closes and nothing is inserted. The transcript is still saved to <a href="history.html">History</a>, so you can pick the text up there if you change your mind.</p>
    </div>

    <h2 id="quality"><span lang="ru">Как получить текст поточнее</span><span lang="en">Getting a cleaner result</span></h2>
    <div lang="ru">
      <ul>
        <li>Говорите обычным темпом. Диктовка по слогам распознаётся хуже, а не лучше.</li>
        <li>Знаки препинания проговаривать не нужно — модель расставляет их сама.</li>
        <li>Имена, названия продуктов и профессиональные сокращения занесите в <a href="replacements.html">словарь замен</a>, иначе они будут всплывать в разных написаниях.</li>
        <li>Если вокруг шумно или играет музыка, включите <a href="muffle.html">выключение звука других приложений</a>.</li>
      </ul>
    </div>
    <div lang="en">
      <ul>
        <li>Speak at your normal pace. Over-articulating makes recognition worse, not better.</li>
        <li>Don’t say the punctuation out loud — the model places it for you.</li>
        <li>Put names, product names and trade abbreviations into the <a href="replacements.html">replacement list</a>, or they will keep coming back spelled differently.</li>
        <li>If the room is noisy or music is playing, turn on <a href="muffle.html">silencing other apps</a>.</li>
      </ul>
    </div>
""",
}

PAGES["dictation-bar"] = {
    "group_ru": "Диктовка", "group_en": "Dictation",
    "title_ru": "Панель диктовки", "title_en": "The dictation bar",
    "lede_ru": "Пока вы говорите, Heardly показывает небольшую панель: по ней видно, что микрофон слышит голос, "
               "сколько идёт запись и какими клавишами остановить или отменить.",
    "lede_en": "While you speak, Heardly shows a small bar: it tells you the microphone hears you, "
               "how long the recording has been running, and which keys stop or cancel it.",
    "body": """
    <h2 id="large"><span lang="ru">Большая панель</span><span lang="en">The large bar</span></h2>
    <figure>
      <img src="img/dictation-bar-large.png" alt="Большая панель диктовки: волна голоса, таймер, подсказки «Стоп» и «Отмена»">
      <figcaption><span lang="ru">Большая панель появляется внизу экрана. Подсказки показывают текущее сочетание клавиш — на снимке выбрано своё, по умолчанию стоит правый ⌘.</span><span lang="en">The large bar appears at the bottom of the screen. The hints show the current shortcut — a custom one in this shot; the default is the right ⌘.</span></figcaption>
    </figure>
    <div lang="ru">
      <p>Волна показывает уровень звука: если она не двигается, пока вы говорите, Heardly вас не слышит — смотрите <a href="fix-mic.html">Микрофон и Bluetooth</a>. Справа идёт таймер записи.</p>
    </div>
    <div lang="en">
      <p>The waveform shows the input level. If it stays flat while you speak, Heardly cannot hear you — see <a href="fix-mic.html">Microphone and Bluetooth</a>. The recording timer runs on the right.</p>
    </div>

    <h2 id="mini"><span lang="ru">Мини-панель</span><span lang="en">The mini bar</span></h2>
    <figure>
      <img src="img/dictation-bar-mini.png" alt="Мини-панель диктовки — небольшая капсула с волной голоса">
      <figcaption><span lang="ru">Мини-панель занимает минимум места и не перекрывает текст, с которым вы работаете.</span><span lang="en">The mini bar takes up almost no space and never covers the text you are working on.</span></figcaption>
    </figure>
    <div lang="ru">
      <p>Мини-панель показывает только волну. Ей можно выбрать место: внизу экрана или прямо под значком Heardly в строке меню — тогда она совсем не мешает.</p>
    </div>
    <div lang="en">
      <p>The mini bar shows only the waveform. You can place it either at the bottom of the screen or right under the Heardly icon in the menu bar, where it is out of the way entirely.</p>
    </div>

    <h2 id="choose"><span lang="ru">Где переключить</span><span lang="en">Where to switch</span></h2>
    <figure>
      <img src="img/settings-dictation.png" alt="Раздел «Диктовка» в настройках: вид панели, словарь замен, выключение звука других приложений">
      <figcaption><span lang="ru">Настройки → Диктовка: вид панели и, для мини-варианта, её положение на экране.</span><span lang="en">Settings → Dictation: the bar style and, for the mini one, where it sits on screen.</span></figcaption>
    </figure>

    <h2 id="keys"><span lang="ru">Клавиши во время записи</span><span lang="en">Keys while recording</span></h2>
    <table class="ref">
      <tr><td><span lang="ru">Горячая клавиша</span><span lang="en">The shortcut</span></td><td><span lang="ru">Останавливает запись и вставляет текст.</span><span lang="en">Stops recording and inserts the text.</span></td></tr>
      <tr><td><kbd>esc</kbd></td><td><span lang="ru">Отменяет: в поле ничего не попадёт, расшифровка останется в <a href="history.html">Истории</a>.</span><span lang="en">Cancels: nothing reaches the field, and the transcript stays in <a href="history.html">History</a>.</span></td></tr>
    </table>
""",
}

PAGES["replacements"] = {
    "group_ru": "Диктовка", "group_en": "Dictation",
    "title_ru": "Словарь замен", "title_en": "Replacement list",
    "lede_ru": "Имена коллег, названия продуктов и профессиональные сокращения модель слышит так, как они звучат. "
               "Словарь замен приводит их к тому виду, в котором вы их пишете.",
    "lede_en": "Colleagues’ names, product names and trade abbreviations come out the way they sound. "
               "The replacement list turns them into the spelling you actually use.",
    "body": """
    <figure>
      <img src="img/replacements.png" alt="Окно «Словарь замен»: правила вида «как слышится → как должно быть», внизу счётчик правил">
      <figcaption><span lang="ru">Одно правило на строку. Счётчик внизу показывает, сколько правил сейчас работает.</span><span lang="en">One rule per line. The counter at the bottom shows how many rules are active.</span></figcaption>
    </figure>

    <h2 id="rules"><span lang="ru">Как писать правила</span><span lang="en">Writing the rules</span></h2>
    <div lang="ru">
      <p>Каждая строка — одно правило: слева то, как слово слышится, справа то, как оно должно выглядеть. Разделитель — стрелка.</p>
      <pre><code>хартли → Heardly
пэ энд эл → P&amp;L
кей пи ай → KPI
джира → Jira</code></pre>
      <p>Замена срабатывает только на целые слова, регистр при поиске не важен. Правила применяются и к диктовке, и к расшифровке звонков, и к файлам.</p>
    </div>
    <div lang="en">
      <p>Each line is one rule: on the left what the word sounds like, on the right how it should look. The separator is an arrow.</p>
      <pre><code>pee and el → P&amp;L
kay pee eye → KPI
jeera → Jira
slack → Slack</code></pre>
      <p>A replacement matches whole words only, and the search ignores case. The rules apply to dictation, to call transcripts and to files alike.</p>
    </div>

    <h2 id="open"><span lang="ru">Где открыть</span><span lang="en">Where to open it</span></h2>
    <div lang="ru"><p><a href="settings.html">Настройки → Диктовка</a>, строка «Словарь замен», кнопка «Изменить». Список сохраняется сам, отдельной кнопки сохранения нет.</p></div>
    <div lang="en"><p><a href="settings.html">Settings → Dictation</a>, the “Replacement list” row, the Edit button. The list saves itself; there is no save button.</p></div>

    <div class="note tip">
      <b><span lang="ru">Начните с десяти слов</span><span lang="en">Start with ten words</span></b>
      <p><span lang="ru">Не пытайтесь описать весь рабочий словарь сразу. Выпишите то, что модель путает чаще всего: фамилии, названия систем, аббревиатуры. Этого обычно хватает.</span><span lang="en">Don’t try to describe your whole working vocabulary at once. Write down what the model gets wrong most often: surnames, system names, abbreviations. That is usually enough.</span></p>
    </div>
""",
}

PAGES["muffle"] = {
    "group_ru": "Диктовка", "group_en": "Dictation",
    "title_ru": "Звук других приложений", "title_en": "Silencing other apps",
    "lede_ru": "Музыка, видео или голос из звонка попадают в микрофон вместе с вашей речью и портят распознавание. "
               "Heardly умеет приглушать другие программы на время диктовки.",
    "lede_en": "Music, video or a voice from a call reaches the microphone together with your own speech and spoils recognition. "
               "Heardly can quiet other apps while you dictate.",
    "body": """
    <h2 id="how"><span lang="ru">Как это работает</span><span lang="en">How it works</span></h2>
    <div lang="ru">
      <p>Когда настройка включена, Heardly на время диктовки приглушает звук остальных приложений, а после вставки текста возвращает его обратно. Трогается только громкость: ничего не ставится на паузу и не перематывается.</p>
    </div>
    <div lang="en">
      <p>With the setting on, Heardly quiets the other apps for the duration of the dictation and restores them once the text is inserted. Only the volume is touched — nothing is paused or rewound.</p>
    </div>

    <h2 id="where"><span lang="ru">Где включить</span><span lang="en">Where to turn it on</span></h2>
    <div lang="ru"><p><a href="settings.html">Настройки → Диктовка</a>, переключатель «Выключать звук других приложений».</p></div>
    <div lang="en"><p><a href="settings.html">Settings → Dictation</a>, the “Silence other apps” switch.</p></div>

    <div class="note warn">
      <b><span lang="ru">Это про диктовку, а не про звонки</span><span lang="en">This is about dictation, not calls</span></b>
      <p><span lang="ru">Во время <a href="live.html">записи звонка</a> звук других приложений не приглушается — иначе Heardly не услышал бы собеседников, ведь именно оттуда идёт их речь.</span><span lang="en">While <a href="live.html">recording a call</a>, other apps are not quieted — that audio is exactly where the other side’s speech comes from.</span></p>
    </div>
""",
}

PAGES["live"] = {
    "group_ru": "Звонки и встречи", "group_en": "Calls and meetings",
    "title_ru": "Запись звонка без бота", "title_en": "Recording a call, no bot",
    "lede_ru": "Heardly слышит и вас, и собеседников: ваш голос берёт с микрофона, их — из звука приложения, "
               "в котором идёт разговор. В саму встречу никто не подключается.",
    "lede_en": "Heardly hears both sides: your voice from the microphone, theirs from the audio of whichever app "
               "the conversation runs in. Nothing joins the meeting itself.",
    "body": """
    <h2 id="start"><span lang="ru">Как начать</span><span lang="en">Getting started</span></h2>
    <ol class="steps">
      <li>
        <b><span lang="ru">Откройте попап Heardly</span><span lang="en">Open the Heardly panel</span></b>
        <div lang="ru"><p>Щелчок по значку в строке меню.</p></div>
        <div lang="en"><p>Click the icon in the menu bar.</p></div>
      </li>
      <li>
        <b><span lang="ru">Проверьте источники</span><span lang="en">Check the sources</span></b>
        <div lang="ru"><p>«Микрофон» — ваш голос, «Звук приложений» — всё, что звучит из программ. Для встречи нужны оба.</p></div>
        <div lang="en"><p>“Microphone” is your voice, “App Audio” is everything coming out of apps. A meeting needs both.</p></div>
      </li>
      <li>
        <b><span lang="ru">Нажмите «Режим реального времени»</span><span lang="en">Press “Real-time mode”</span></b>
        <div lang="ru"><p>Откроется окно живой расшифровки, и текст начнёт появляться по ходу разговора.</p></div>
        <div lang="en"><p>The live window opens and text starts appearing as the conversation goes on.</p></div>
      </li>
      <li>
        <b><span lang="ru">В конце нажмите «Стоп»</span><span lang="en">Press “Stop” at the end</span></b>
        <div lang="ru"><p>Запись сохранится в <a href="history.html">Историю</a>, в раздел «Звонки и встречи».</p></div>
        <div lang="en"><p>The recording is saved to <a href="history.html">History</a>, in the “Calls and meetings” section.</p></div>
      </li>
    </ol>

    <figure>
      <img src="img/menubar-popup.png" alt="Попап Heardly с кнопкой «Режим реального времени» и переключателями источников звука">
      <figcaption><span lang="ru">Оба переключателя включены — значит, в расшифровке будут и ваши реплики, и реплики собеседников.</span><span lang="en">With both switches on, the transcript will carry your lines and the other side’s alike.</span></figcaption>
    </figure>

    <h2 id="sources"><span lang="ru">Кто есть кто в расшифровке</span><span lang="en">Who is who in the transcript</span></h2>
    <div lang="ru">
      <p>Heardly различает два источника и подписывает реплики: «Я» — то, что пришло с микрофона, «Компьютер» — то, что звучало из приложений. Это не распознавание говорящих по голосу: если в переговорной за одним микрофоном сидят трое, все трое будут подписаны как «Я».</p>
    </div>
    <div lang="en">
      <p>Heardly tells the two sources apart and labels the lines: “Me” for what came from the microphone, “Computer” for what played out of apps. This is not speaker recognition by voice: if three people share one microphone in a meeting room, all three are labelled “Me”.</p>
    </div>

    <h2 id="apps"><span lang="ru">С какими приложениями работает</span><span lang="en">Which apps it works with</span></h2>
    <div lang="ru">
      <p>С любыми. Heardly берёт звук на уровне системы, поэтому ему всё равно, идёт звонок в Zoom, Google Meet, Telegram, Discord или в браузере. По той же причине он расшифрует и видео на YouTube, и голосовое сообщение.</p>
    </div>
    <div lang="en">
      <p>All of them. Heardly takes the audio at system level, so it does not care whether the call runs in Zoom, Google Meet, Telegram, Discord or a browser tab. For the same reason it will transcribe a YouTube video or a voice message just as happily.</p>
    </div>

    <div class="note warn">
      <b><span lang="ru">Предупредите собеседников</span><span lang="en">Tell the other side</span></b>
      <p><span lang="ru">Бота в звонке не видно, а значит, никто не узнает о записи сам. Во многих странах и компаниях запись разговора без предупреждения недопустима — скажите об этом вслух в начале встречи.</span><span lang="en">There is no bot to see, so nobody learns about the recording on their own. In many countries and companies recording a conversation without telling people is not acceptable — say it out loud at the start of the meeting.</span></p>
    </div>
""",
}

PAGES["live-window"] = {
    "group_ru": "Звонки и встречи", "group_en": "Calls and meetings",
    "title_ru": "Окно живой расшифровки", "title_en": "The live window",
    "lede_ru": "Пока идёт запись, текст появляется в отдельном окне: с временем, подписями источников "
               "и кнопками, чтобы забрать нужный кусок прямо посреди разговора.",
    "lede_en": "While recording runs, the text appears in a window of its own: with timestamps, source labels "
               "and buttons that let you grab a piece of it in the middle of the conversation.",
    "body": """
    <figure>
      <img src="img/live-window.png" alt="Окно живой расшифровки: источники «Микрофон» и «Приложения», кнопки «Пауза» и «Стоп», реплики с временем и подписью источника">
      <figcaption><span lang="ru">Реплики появляются по мере того, как люди договаривают фразы.</span><span lang="en">Lines appear as people finish their sentences.</span></figcaption>
    </figure>

    <h2 id="controls"><span lang="ru">Что где</span><span lang="en">What is where</span></h2>
    <table class="ref">
      <tr><td><span lang="ru">Микрофон · Приложения</span><span lang="en">Microphone · Apps</span></td>
          <td><span lang="ru">Источники звука. Любой можно выключить прямо во время записи — например, отключить микрофон, пока говорит другая сторона.</span><span lang="en">The audio sources. Either can be switched off mid-recording — say, mute your microphone while the other side talks.</span></td></tr>
      <tr><td><span lang="ru">Пауза</span><span lang="en">Pause</span></td>
          <td><span lang="ru">Останавливает запись, не закрывая сессию. Удобно на перерыве или когда разговор уходит в личное.</span><span lang="en">Stops recording without ending the session. Handy during a break, or when the conversation turns personal.</span></td></tr>
      <tr><td><span lang="ru">Стоп</span><span lang="en">Stop</span></td>
          <td><span lang="ru">Завершает запись и сохраняет её в Историю.</span><span lang="en">Ends the recording and saves it to History.</span></td></tr>
      <tr><td><span lang="ru">Копировать</span><span lang="en">Copy</span></td>
          <td><span lang="ru">Кладёт в буфер весь текст.</span><span lang="en">Puts the whole text on the clipboard.</span></td></tr>
      <tr><td><span lang="ru">Последние</span><span lang="en">Last</span></td>
          <td><span lang="ru">Копирует только последние реплики — когда нужна одна мысль, а не вся встреча.</span><span lang="en">Copies just the last few lines — when you need one thought, not the whole meeting.</span></td></tr>
      <tr><td><span lang="ru">С подписями</span><span lang="en">With labels</span></td>
          <td><span lang="ru">Добавляет к копируемому тексту подписи источников.</span><span lang="en">Adds the source labels to the copied text.</span></td></tr>
      <tr><td><span lang="ru">Очистить</span><span lang="en">Clear</span></td>
          <td><span lang="ru">Стирает текст на экране и начинает ленту заново.</span><span lang="en">Wipes the text on screen and starts the feed over.</span></td></tr>
    </table>

    <h2 id="delay"><span lang="ru">Почему текст появляется не мгновенно</span><span lang="en">Why the text is not instant</span></h2>
    <div lang="ru">
      <p>Heardly ждёт, пока человек договорит фразу, и только потом отдаёт её целиком. Из-за этого между словом и строчкой на экране проходит несколько секунд, зато в расшифровке не остаётся обрывков, которые пришлось бы переписывать.</p>
    </div>
    <div lang="en">
      <p>Heardly waits for a person to finish the sentence and only then hands it over whole. That puts a few seconds between the spoken word and the line on screen, but it keeps the transcript free of fragments you would have to rewrite afterwards.</p>
    </div>
""",
}
