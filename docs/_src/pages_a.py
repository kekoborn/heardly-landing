# -*- coding: utf-8 -*-
"""Раздел «Начало»."""

PAGES = {}

PAGES["overview"] = {
    "group_ru": "Начало", "group_en": "Get started",
    "title_ru": "Что такое Heardly", "title_en": "What Heardly is",
    "lede_ru": "Heardly живёт в строке меню Mac и превращает речь в текст: диктовку в любое поле ввода, "
               "звонки и встречи целиком, аудио- и видеофайлы. Распознавание идёт на самом компьютере.",
    "lede_en": "Heardly lives in the Mac menu bar and turns speech into text: dictation into any text field, "
               "whole calls and meetings, and audio and video files. Recognition runs on your own computer.",
    "body": """
    <figure>
      <img src="img/menubar-popup.png" alt="Попап Heardly в строке меню: кнопка записи, переключатели микрофона и звука приложений, статистика, зона для файлов">
      <figcaption><span lang="ru">Главное окно Heardly открывается щелчком по значку в строке меню.</span><span lang="en">The Heardly panel opens with a click on the menu bar icon.</span></figcaption>
    </figure>

    <h2 id="modes"><span lang="ru">Три способа получить текст</span><span lang="en">Three ways to get text</span></h2>
    <div lang="ru">
      <p>Heardly делает одно и то же тремя путями, и каждый из них живёт в своём разделе документации.</p>
      <ul>
        <li><b>Диктовка.</b> Нажимаете горячую клавишу в любом приложении, говорите, и текст появляется там, где стоит курсор. Нужна, когда вы пишете письмо, сообщение или комментарий.</li>
        <li><b>Звонки и встречи.</b> Heardly слышит и ваш микрофон, и звук из приложений — Zoom, Meet, Telegram. Бота в звонок приглашать не нужно, собеседники ничего не видят.</li>
        <li><b>Файлы.</b> Перетаскиваете аудио или видео, получаете расшифровку с таймкодами.</li>
      </ul>
      <p>Всё, что получилось, складывается в Историю и лежит обычными текстовыми файлами в папке на вашем компьютере.</p>
    </div>
    <div lang="en">
      <p>Heardly does the same job in three ways, and each one has its own section in these docs.</p>
      <ul>
        <li><b>Dictation.</b> Press a shortcut in any app, speak, and the text appears where your cursor is. This is for writing an email, a message or a comment.</li>
        <li><b>Calls and meetings.</b> Heardly hears both your microphone and the audio coming out of apps — Zoom, Meet, Telegram. No bot joins the call, and the other side sees nothing.</li>
        <li><b>Files.</b> Drop in audio or video and get a transcript with timecodes.</li>
      </ul>
      <p>Everything you produce lands in History and is kept as ordinary text files in a folder on your computer.</p>
    </div>

    <h2 id="local"><span lang="ru">Почему «на самом компьютере»</span><span lang="en">Why “on your own computer”</span></h2>
    <div lang="ru">
      <p>Распознавание речи выполняет локальная модель Parakeet. Звук не уходит на сервер: ни во время диктовки, ни во время звонка, ни при расшифровке файла. Интернет Heardly нужен только для проверки подписки, обновления приложения и первой загрузки модели.</p>
      <p>Подробный разбор, что именно и когда уходит в сеть, — на странице <a href="privacy.html">Что уходит в интернет</a>.</p>
    </div>
    <div lang="en">
      <p>Speech recognition runs on a local Parakeet model. Audio never goes to a server — not while you dictate, not during a call, not when you transcribe a file. Heardly needs the internet only to check your subscription, update itself and download the model the first time.</p>
      <p>A full account of what leaves the Mac and when is on the <a href="privacy.html">What leaves your Mac</a> page.</p>
    </div>

    <h2 id="requirements"><span lang="ru">Что нужно</span><span lang="en">What you need</span></h2>
    <table class="ref">
      <tr><td><span lang="ru">Система</span><span lang="en">System</span></td><td>macOS 14 Sonoma<span lang="ru"> или новее</span><span lang="en"> or newer</span></td></tr>
      <tr><td><span lang="ru">Процессор</span><span lang="en">Chip</span></td><td><span lang="ru">Apple Silicon. Модель считается на Neural Engine, на Intel-машинах Heardly не рассчитан.</span><span lang="en">Apple Silicon. The model runs on the Neural Engine; Heardly is not built for Intel Macs.</span></td></tr>
      <tr><td><span lang="ru">Место</span><span lang="en">Disk</span></td><td><span lang="ru">Около 600 МБ под модель, плюс сами расшифровки — это простой текст, он почти ничего не весит.</span><span lang="en">About 600 MB for the model, plus the transcripts themselves — plain text, which weighs next to nothing.</span></td></tr>
      <tr><td><span lang="ru">Разрешения</span><span lang="en">Permissions</span></td><td><span lang="ru">Микрофон, запись системного звука и универсальный доступ — <a href="permissions.html">разбор каждого</a>.</span><span lang="en">Microphone, system audio recording and accessibility — <a href="permissions.html">each one explained</a>.</span></td></tr>
    </table>

    <h2 id="next"><span lang="ru">С чего начать</span><span lang="en">Where to start</span></h2>
    <div class="cards">
      <a href="install.html"><b><span lang="ru">Установка</span><span lang="en">Install</span></b><span><span lang="ru">Скачать, перенести в Программы, запустить.</span><span lang="en">Download, move to Applications, launch.</span></span></a>
      <a href="quickstart.html"><b><span lang="ru">Первая диктовка</span><span lang="en">First dictation</span></b><span><span lang="ru">Продиктовать первое сообщение за минуту.</span><span lang="en">Dictate your first message in a minute.</span></span></a>
      <a href="live.html"><b><span lang="ru">Запись звонка</span><span lang="en">Record a call</span></b><span><span lang="ru">Расшифровать встречу без бота в комнате.</span><span lang="en">Transcribe a meeting with no bot in the room.</span></span></a>
      <a href="pricing.html"><b><span lang="ru">Пробный период и Pro</span><span lang="en">Trial and Pro</span></b><span><span lang="ru">Что входит в бесплатную версию и сколько стоит Pro.</span><span lang="en">What the free version covers and what Pro costs.</span></span></a>
    </div>
""",
}

PAGES["install"] = {
    "group_ru": "Начало", "group_en": "Get started",
    "title_ru": "Установка и первый запуск", "title_en": "Install and first launch",
    "lede_ru": "Heardly ставится как обычное приложение для Mac: скачать образ, перетащить в «Программы», запустить. "
               "Первый запуск занимает чуть больше времени — приложение готовит модель распознавания.",
    "lede_en": "Heardly installs like any Mac app: download the disk image, drag it to Applications, launch it. "
               "The first launch takes a little longer because the app prepares the recognition model.",
    "body": """
    <h2 id="install"><span lang="ru">Установка</span><span lang="en">Installing</span></h2>
    <ol class="steps">
      <li>
        <b><span lang="ru">Скачайте образ</span><span lang="en">Download the disk image</span></b>
        <div lang="ru"><p>Кнопка «Скачать» наверху этой страницы ведёт на последнюю версию. Файл называется <code>Heardly.dmg</code>.</p></div>
        <div lang="en"><p>The Download button at the top of this page points at the latest version. The file is called <code>Heardly.dmg</code>.</p></div>
      </li>
      <li>
        <b><span lang="ru">Перетащите Heardly в «Программы»</span><span lang="en">Drag Heardly into Applications</span></b>
        <div lang="ru"><p>Откройте скачанный <code>.dmg</code> и перетащите значок в папку «Программы». Запускать приложение прямо из образа не нужно: оттуда не работает автообновление.</p></div>
        <div lang="en"><p>Open the downloaded <code>.dmg</code> and drag the icon into the Applications folder. Don’t run the app straight from the disk image — automatic updates don’t work from there.</p></div>
      </li>
      <li>
        <b><span lang="ru">Запустите приложение</span><span lang="en">Launch the app</span></b>
        <div lang="ru"><p>Значок Heardly появится в строке меню, справа вверху. Окна в Dock у приложения нет — оно всё время живёт в строке меню.</p></div>
        <div lang="en"><p>The Heardly icon appears in the menu bar, top right. The app has no Dock window — it lives in the menu bar.</p></div>
      </li>
      <li>
        <b><span lang="ru">Выдайте разрешения</span><span lang="en">Grant the permissions</span></b>
        <div lang="ru"><p>При первом запуске Heardly попросит доступ к микрофону, а для записи звонков — к системному звуку. Что именно и зачем — на странице <a href="permissions.html">Разрешения macOS</a>.</p></div>
        <div lang="en"><p>On first launch Heardly asks for the microphone, and for system audio if you want to record calls. What each one is for is on the <a href="permissions.html">macOS permissions</a> page.</p></div>
      </li>
    </ol>

    <figure>
      <img src="img/onboarding-welcome.png" alt="Первый экран настройки Heardly: значок приложения, приветствие и кнопка «Начать настройку»">
      <figcaption><span lang="ru">После первого запуска Heardly сам открывает настройку: разрешения, проверка микрофона и короткая проба диктовки.</span><span lang="en">On the first launch Heardly opens the setup by itself: permissions, a microphone check and a short dictation try.</span></figcaption>
    </figure>

    <h2 id="first-run"><span lang="ru">Первый запуск и подготовка модели</span><span lang="en">First launch and model preparation</span></h2>
    <div lang="ru">
      <p>В строке меню Heardly показывает состояние: пока модель грузится и готовится, в попапе стоит соответствующая надпись, а как только всё готово — «Модель готова» с зелёной точкой.</p>
      <p>Подготовка модели под Neural Engine делается один раз после установки и ещё раз после крупного обновления macOS. На M1 это может занять до пары минут, дальше запуск почти мгновенный.</p>
    </div>
    <div lang="en">
      <p>The menu bar panel shows the current state: a line about loading while the model is being downloaded and prepared, and “Model ready” with a green dot once it is done.</p>
      <p>Preparing the model for the Neural Engine happens once after installation, and again after a major macOS update. On an M1 this can take up to a couple of minutes; after that, startup is close to instant.</p>
    </div>
    <div class="note warn">
      <b><span lang="ru">Не закрывайте приложение в это время</span><span lang="en">Don’t quit during this step</span></b>
      <p><span lang="ru">Если прервать подготовку модели, при следующем запуске она начнётся заново.</span><span lang="en">If you interrupt the preparation, it starts again from scratch on the next launch.</span></p>
    </div>

    <h2 id="login"><span lang="ru">Запуск вместе с системой</span><span lang="en">Starting with the Mac</span></h2>
    <div lang="ru">
      <p>Чтобы Heardly был под рукой сразу после включения компьютера, включите «Запускать при входе в систему» в разделе <a href="settings.html">Настройки → Система</a>.</p>
      <p>Если macOS не даёт включить, разрешите Heardly в «Системных настройках» → «Основные» → «Объекты входа».</p>
    </div>
    <div lang="en">
      <p>To have Heardly ready as soon as the Mac starts, turn on “Launch at login” in <a href="settings.html">Settings → System</a>.</p>
      <p>If macOS refuses, approve Heardly in System Settings → General → Login Items.</p>
    </div>

    <h2 id="update"><span lang="ru">Обновления</span><span lang="en">Updates</span></h2>
    <div lang="ru"><p>Heardly обновляется сам и показывает окно с описанием версии. Проверить вручную можно кнопкой «Проверить обновления» в <a href="updates.html">настройках</a>.</p></div>
    <div lang="en"><p>Heardly updates itself and shows a window describing the new version. You can also check by hand with the “Check for updates” button in <a href="updates.html">Settings</a>.</p></div>
""",
}

PAGES["permissions"] = {
    "group_ru": "Начало", "group_en": "Get started",
    "title_ru": "Разрешения macOS", "title_en": "macOS permissions",
    "lede_ru": "Heardly просит три разрешения, и каждое отвечает за свою часть работы. "
               "Без микрофона не будет диктовки, без системного звука — записи звонков, без универсального доступа текст не вставится в поле.",
    "lede_en": "Heardly asks for three permissions, each covering a different part of the job. "
               "Without the microphone there is no dictation, without system audio there are no calls, and without accessibility the text cannot be inserted into a field.",
    "body": """
    <h2 id="list"><span lang="ru">Что именно просит Heardly</span><span lang="en">What Heardly asks for</span></h2>
    <table class="ref">
      <tr>
        <th><span lang="ru">Разрешение</span><span lang="en">Permission</span></th>
        <th><span lang="ru">Для чего</span><span lang="en">What it does</span></th>
        <th><span lang="ru">Без него</span><span lang="en">Without it</span></th>
      </tr>
      <tr>
        <td><span lang="ru">Микрофон</span><span lang="en">Microphone</span></td>
        <td><span lang="ru">Слышит ваш голос — и в диктовке, и в звонке.</span><span lang="en">Hears your voice, both in dictation and in a call.</span></td>
        <td><span lang="ru">Диктовка не стартует, в звонке записана только другая сторона.</span><span lang="en">Dictation won’t start; in a call only the other side is recorded.</span></td>
      </tr>
      <tr>
        <td><span lang="ru">Запись системного звука</span><span lang="en">System audio recording</span></td>
        <td><span lang="ru">Слышит, что звучит из приложений: собеседников в Zoom, Meet, Telegram.</span><span lang="en">Hears what comes out of apps: the people on the other side of Zoom, Meet or Telegram.</span></td>
        <td><span lang="ru">В расшифровке звонка будет только ваша речь.</span><span lang="en">A call transcript will contain only your own speech.</span></td>
      </tr>
      <tr>
        <td><span lang="ru">Универсальный доступ</span><span lang="en">Accessibility</span></td>
        <td><span lang="ru">Вставляет продиктованный текст туда, где стоит курсор.</span><span lang="en">Inserts dictated text where your cursor is.</span></td>
        <td><span lang="ru">Текст распознается и сохранится в Историю, но в поле не попадёт.</span><span lang="en">The text is still recognised and saved to History, but never reaches the field.</span></td>
      </tr>
    </table>

    <figure>
      <img src="img/onboarding-permissions.png" alt="Шаг разрешений в настройке Heardly: микрофон, звук приложений и вставка текста, у каждого своя кнопка «Разрешить»">
      <figcaption><span lang="ru">При первом запуске Heardly просит все три разрешения подряд — каждое отдельной кнопкой.</span><span lang="en">On the first launch Heardly asks for all three permissions in a row, each with its own button.</span></figcaption>
    </figure>

    <h2 id="grant"><span lang="ru">Где их выдать</span><span lang="en">Where to grant them</span></h2>
    <div lang="ru">
      <p>Heardly спрашивает разрешения сам, когда они впервые нужны. Если вы отказали или случайно закрыли окно, всё включается вручную в «Системных настройках» → «Конфиденциальность и безопасность»:</p>
      <ul>
        <li><b>Микрофон</b> — найдите Heardly в списке и включите переключатель.</li>
        <li><b>Запись экрана и системного звука</b> — здесь же живёт доступ к звуку приложений. macOS объединяет их в один пункт.</li>
        <li><b>Универсальный доступ</b> — отдельный пункт, в нём тоже нужно включить Heardly.</li>
      </ul>
    </div>
    <div lang="en">
      <p>Heardly asks for each permission the first time it needs it. If you declined, or closed the dialog by accident, you can switch them on by hand in System Settings → Privacy &amp; Security:</p>
      <ul>
        <li><b>Microphone</b> — find Heardly in the list and turn the switch on.</li>
        <li><b>Screen &amp; System Audio Recording</b> — app audio access lives here; macOS keeps the two together in one entry.</li>
        <li><b>Accessibility</b> — a separate entry, where Heardly also needs to be enabled.</li>
      </ul>
    </div>

    <div class="note warn">
      <b><span lang="ru">После обновления разрешение может слететь</span><span lang="en">An update can reset a permission</span></b>
      <p><span lang="ru">macOS привязывает разрешение к конкретной сборке приложения. Если после обновления диктовка перестала вставлять текст, загляните в «Универсальный доступ» и включите Heardly заново — подробности на странице <a href="fix-dictation.html">Текст не вставляется</a>.</span><span lang="en">macOS ties a permission to a specific build. If dictation stops inserting text after an update, open Accessibility and switch Heardly back on — details on the <a href="fix-dictation.html">Text is not inserted</a> page.</span></p>
    </div>

    <h2 id="why-screen"><span lang="ru">Почему просят «запись экрана»</span><span lang="en">Why it says “screen recording”</span></h2>
    <div lang="ru">
      <p>Это формулировка macOS, а не намерение приложения. Доступ к звуку других программ система выдаёт в том же пункте, что и к изображению экрана, отдельного переключателя под звук в ней нет.</p>
      <p>Heardly записывает только звук. Изображение экрана не читается и никуда не передаётся.</p>
    </div>
    <div lang="en">
      <p>That wording comes from macOS, not from the app. The system grants access to other apps’ audio in the same entry as the screen image; it has no separate switch for audio alone.</p>
      <p>Heardly records audio only. The screen image is never read and never sent anywhere.</p>
    </div>
""",
}

PAGES["quickstart"] = {
    "group_ru": "Начало", "group_en": "Get started",
    "title_ru": "Первая диктовка", "title_en": "Your first dictation",
    "lede_ru": "Самый короткий путь познакомиться с Heardly: открыть любое поле ввода, нажать горячую клавишу и сказать пару фраз.",
    "lede_en": "The shortest way to get to know Heardly: open any text field, press the shortcut and say a couple of sentences.",
    "body": """
    <ol class="steps">
      <li>
        <b><span lang="ru">Поставьте курсор туда, где нужен текст</span><span lang="en">Put the cursor where you want the text</span></b>
        <div lang="ru"><p>Подойдёт что угодно: окно сообщения, письмо, поле поиска, редактор кода.</p></div>
        <div lang="en"><p>Anything will do: a message box, an email, a search field, a code editor.</p></div>
      </li>
      <li>
        <b><span lang="ru">Нажмите правый <kbd>⌘</kbd></span><span lang="en">Press the right <kbd>⌘</kbd></span></b>
        <div lang="ru"><p>Это горячая клавиша по умолчанию. Внизу экрана появится панель диктовки с волной — значит, Heardly слышит вас.</p></div>
        <div lang="en"><p>That’s the default shortcut. The dictation bar with a waveform appears — that means Heardly can hear you.</p></div>
      </li>
      <li>
        <b><span lang="ru">Говорите обычным голосом</span><span lang="en">Speak normally</span></b>
        <div lang="ru"><p>Не нужно диктовать по слогам и проговаривать знаки препинания — точки и запятые модель ставит сама.</p></div>
        <div lang="en"><p>No need to over-articulate or say the punctuation out loud — the model adds full stops and commas itself.</p></div>
      </li>
      <li>
        <b><span lang="ru">Нажмите клавишу ещё раз</span><span lang="en">Press the key again</span></b>
        <div lang="ru"><p>Heardly дослушает фразу и вставит текст туда, где стоял курсор. Если передумали — <kbd>esc</kbd> отменяет вставку.</p></div>
        <div lang="en"><p>Heardly finishes the sentence and inserts the text where the cursor was. Changed your mind? <kbd>esc</kbd> cancels the insert.</p></div>
      </li>
    </ol>

    <figure>
      <img src="img/dictation-bar-large.png" alt="Панель диктовки: волна голоса, таймер и подсказки — «Стоп» и «Отмена»">
      <figcaption><span lang="ru">Панель диктовки во время записи. Подсказки показывают текущее сочетание клавиш: на снимке выбрано своё, по умолчанию стоит правый ⌘.</span><span lang="en">The dictation bar while recording. The hints show the current shortcut — a custom one in this shot; the default is the right ⌘.</span></figcaption>
    </figure>

    <div class="note tip">
      <b><span lang="ru">Клавишу можно поменять</span><span lang="en">The key can be changed</span></b>
      <p><span lang="ru">Если правый <kbd>⌘</kbd> у вас занят, назначьте другое сочетание в <a href="settings.html">Настройках → Основные</a>. Там же выбирается, работает клавиша как выключатель или как кнопка, которую надо держать.</span><span lang="en">If the right <kbd>⌘</kbd> is already taken, assign another shortcut in <a href="settings.html">Settings → General</a>. The same place lets you choose whether the key toggles recording or records only while held.</span></p>
    </div>

    <h2 id="next"><span lang="ru">Что дальше</span><span lang="en">What next</span></h2>
    <div class="cards">
      <a href="dictation.html"><b><span lang="ru">Как диктовать</span><span lang="en">How to dictate</span></b><span><span lang="ru">Режимы клавиши, выделенный текст, буфер обмена.</span><span lang="en">Key modes, selected text, the clipboard.</span></span></a>
      <a href="replacements.html"><b><span lang="ru">Словарь замен</span><span lang="en">Replacement list</span></b><span><span lang="ru">Научить Heardly именам и терминам вашей работы.</span><span lang="en">Teach Heardly the names and terms you use at work.</span></span></a>
      <a href="live.html"><b><span lang="ru">Запись звонка</span><span lang="en">Record a call</span></b><span><span lang="ru">Расшифровка встречи целиком, без бота.</span><span lang="en">A whole meeting transcribed, with no bot.</span></span></a>
    </div>
""",
}
