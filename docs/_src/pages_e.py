# -*- coding: utf-8 -*-
"""Раздел «Решение проблем»."""

PAGES = {}

PAGES["fix-dictation"] = {
    "group_ru": "Решение проблем", "group_en": "Troubleshooting",
    "title_ru": "Текст не вставляется", "title_en": "Text is not inserted",
    "lede_ru": "Панель появляется, волна двигается, запись идёт — а в поле ничего не приходит. "
               "Почти всегда дело в разрешении «Универсальный доступ».",
    "lede_en": "The bar appears, the waveform moves, recording runs — and nothing arrives in the field. "
               "Almost always this is the Accessibility permission.",
    "body": """
    <h2 id="ax"><span lang="ru">Проверьте универсальный доступ</span><span lang="en">Check Accessibility</span></h2>
    <div lang="ru">
      <p>Откройте «Системные настройки» → «Конфиденциальность и безопасность» → «Универсальный доступ» и убедитесь, что Heardly там есть и переключатель включён.</p>
      <p>Если переключатель уже включён, выключите и включите его снова: macOS иногда держит запись о старой сборке приложения.</p>
    </div>
    <div lang="en">
      <p>Open System Settings → Privacy &amp; Security → Accessibility and make sure Heardly is listed and switched on.</p>
      <p>If the switch is already on, turn it off and on again: macOS sometimes holds on to a record of an older build.</p>
    </div>

    <div class="note warn">
      <b><span lang="ru">После обновления — частый случай</span><span lang="en">Common right after an update</span></b>
      <p><span lang="ru">macOS привязывает разрешение к конкретной сборке, поэтому новая версия Heardly может оказаться без доступа. Переключение тумблера решает вопрос за секунду.</span><span lang="en">macOS ties the permission to a specific build, so a new version of Heardly can end up without access. Toggling the switch fixes it in a second.</span></p>
    </div>

    <h2 id="saved"><span lang="ru">Текст при этом не потерян</span><span lang="en">The text is not lost</span></h2>
    <div lang="ru">
      <p>Даже когда вставка не сработала, расшифровка сохраняется в <a href="history.html">Историю</a>, в раздел «Диктовки». Откройте её и скопируйте текст оттуда.</p>
    </div>
    <div lang="en">
      <p>Even when the insert fails, the transcript is saved to <a href="history.html">History</a>, in the “Dictations” section. Open it and copy the text from there.</p>
    </div>

    <h2 id="other"><span lang="ru">Если дело не в разрешении</span><span lang="en">If it is not the permission</span></h2>
    <table class="ref">
      <tr>
        <th><span lang="ru">Что видно</span><span lang="en">What you see</span></th>
        <th><span lang="ru">Что делать</span><span lang="en">What to do</span></th>
      </tr>
      <tr><td><span lang="ru">Панель не появляется совсем</span><span lang="en">The bar never appears</span></td>
          <td><span lang="ru">Горячую клавишу перехватывает другая программа. Назначьте другое сочетание в <a href="settings.html">Настройках → Основные</a>.</span><span lang="en">Another app is intercepting the shortcut. Assign a different one in <a href="settings.html">Settings → General</a>.</span></td></tr>
      <tr><td><span lang="ru">Текст уходит не в то поле</span><span lang="en">The text lands in the wrong field</span></td>
          <td><span lang="ru">Курсор должен стоять в поле до нажатия клавиши. Щёлкните в нужное место и только потом начинайте диктовать.</span><span lang="en">The cursor has to be in the field before you press the key. Click where you want the text, then start dictating.</span></td></tr>
      <tr><td><span lang="ru">Не работает в одной конкретной программе</span><span lang="en">Broken in one particular app</span></td>
          <td><span lang="ru">Некоторые приложения запрещают вставку извне. Текст всё равно будет в Истории — заберите его оттуда.</span><span lang="en">Some apps refuse pastes from outside. The text is in History regardless — take it from there.</span></td></tr>
    </table>
""",
}

PAGES["fix-audio"] = {
    "group_ru": "Решение проблем", "group_en": "Troubleshooting",
    "title_ru": "Нет звука приложений", "title_en": "No app audio",
    "lede_ru": "В расшифровке звонка есть только ваши реплики, а собеседников нет. "
               "Значит, Heardly не получает звук из программ.",
    "lede_en": "A call transcript has your own lines but nothing from the other side. "
               "That means Heardly is not getting audio out of the apps.",
    "body": """
    <h2 id="permission"><span lang="ru">Разрешение на системный звук</span><span lang="en">The system audio permission</span></h2>
    <div lang="ru">
      <p>Откройте «Системные настройки» → «Конфиденциальность и безопасность» → «Запись экрана и системного звука» и включите Heardly.</p>
      <p>Это тот самый пункт, который macOS называет записью экрана. Heardly берёт оттуда только звук, картинку он не читает — подробнее на странице <a href="permissions.html">Разрешения macOS</a>.</p>
    </div>
    <div lang="en">
      <p>Open System Settings → Privacy &amp; Security → Screen &amp; System Audio Recording and switch Heardly on.</p>
      <p>This is the entry macOS calls screen recording. Heardly takes only the audio from it and never reads the picture — more on the <a href="permissions.html">macOS permissions</a> page.</p>
    </div>

    <h2 id="toggle"><span lang="ru">Проверьте переключатель в попапе</span><span lang="en">Check the switch in the panel</span></h2>
    <div lang="ru">
      <p>«Звук приложений» должен быть включён до начала записи. Его же можно включить и выключить прямо в <a href="live-window.html">окне живой расшифровки</a> — проверьте, что он не выключен с прошлого раза.</p>
    </div>
    <div lang="en">
      <p>“App Audio” has to be on before recording starts. The same switch is available in the <a href="live-window.html">live window</a> — make sure it was not left off from last time.</p>
    </div>

    <h2 id="output"><span lang="ru">Куда идёт звук</span><span lang="en">Where the sound goes</span></h2>
    <div lang="ru">
      <p>Heardly слышит то, что воспроизводит система. Если звонок идёт в наушники, подключённые по Bluetooth, и вы переключаете вывод во время разговора, захват может сорваться — остановите запись и начните заново после переключения.</p>
      <p>Если звука нет вообще ни в наушниках, ни в динамиках, дело не в Heardly: сначала разберитесь с выводом звука в самой системе.</p>
    </div>
    <div lang="en">
      <p>Heardly hears what the system plays. If the call runs into Bluetooth headphones and you switch the output device mid-conversation, the capture can drop — stop the recording and start it again after switching.</p>
      <p>If there is no sound at all, in headphones or speakers, this is not about Heardly: sort the system output out first.</p>
    </div>
""",
}

PAGES["fix-mic"] = {
    "group_ru": "Решение проблем", "group_en": "Troubleshooting",
    "title_ru": "Микрофон и Bluetooth", "title_en": "Microphone and Bluetooth",
    "lede_ru": "Волна на панели диктовки не двигается, или в расшифровке звонка нет ваших реплик — "
               "разбираемся с микрофоном.",
    "lede_en": "The waveform on the dictation bar stays flat, or a call transcript has none of your own lines — "
               "time to look at the microphone.",
    "body": """
    <h2 id="permission"><span lang="ru">Разрешение</span><span lang="en">The permission</span></h2>
    <div lang="ru"><p>«Системные настройки» → «Конфиденциальность и безопасность» → «Микрофон», Heardly должен быть включён.</p></div>
    <div lang="en"><p>System Settings → Privacy &amp; Security → Microphone; Heardly has to be switched on.</p></div>

    <h2 id="device"><span lang="ru">Выбор устройства</span><span lang="en">Choosing the device</span></h2>
    <div lang="ru">
      <p>По умолчанию стоит «Авто»: Heardly сам выбирает подходящий микрофон. Если в системе много устройств — петличка, веб-камера, виртуальные аудиоустройства от программ записи, — выбор может оказаться неудачным. Задайте нужный микрофон явно в <a href="settings.html">Настройках → Основные</a> или прямо в попапе.</p>
    </div>
    <div lang="en">
      <p>The default is “Auto”, where Heardly picks a microphone for you. With many devices around — a lavalier, a webcam, virtual audio devices installed by recording software — that choice can land badly. Name the microphone you want in <a href="settings.html">Settings → General</a> or right in the panel.</p>
    </div>

    <h2 id="bluetooth"><span lang="ru">Bluetooth-наушники</span><span lang="en">Bluetooth headphones</span></h2>
    <div class="note warn">
      <b><span lang="ru">Звук в наушниках станет хуже</span><span lang="en">Your audio quality will drop</span></b>
      <p><span lang="ru">Когда микрофоном выбраны беспроводные наушники, macOS переводит их в режим гарнитуры: музыка и голос собеседника в них звучат заметно тише и глуше. Это особенность Bluetooth, а не Heardly.</span><span lang="en">When wireless headphones are used as the microphone, macOS switches them into headset mode: music and the other person’s voice get noticeably quieter and duller. That is how Bluetooth works, not something Heardly does.</span></p>
    </div>
    <div lang="ru">
      <p>На созвоне это обычно терпимо. Для диктовки лучше оставить микрофон ноутбука: качество записи будет выше, а наушники продолжат звучать нормально.</p>
    </div>
    <div lang="en">
      <p>On a call this is usually acceptable. For dictation, the laptop’s own microphone is the better choice: the recording is cleaner and the headphones keep sounding right.</p>
    </div>

    <h2 id="other"><span lang="ru">Остальное</span><span lang="en">Anything else</span></h2>
    <table class="ref">
      <tr><td><span lang="ru">Микрофон занят другой программой</span><span lang="en">Another app is holding the microphone</span></td>
          <td><span lang="ru">Zoom, Teams и программы записи иногда удерживают устройство. Закройте их и попробуйте снова.</span><span lang="en">Zoom, Teams and recording software sometimes keep the device. Close them and try again.</span></td></tr>
      <tr><td><span lang="ru">Устройство переключилось во время записи</span><span lang="en">The device switched mid-recording</span></td>
          <td><span lang="ru">Подключение наушников посреди диктовки меняет устройство ввода. Начните запись заново.</span><span lang="en">Plugging headphones in mid-dictation changes the input device. Start the recording over.</span></td></tr>
      <tr><td><span lang="ru">Волна двигается, но текст пустой</span><span lang="en">The waveform moves but the text is empty</span></td>
          <td><span lang="ru">Проверьте <a href="model.html">язык распознавания</a>: при явно выбранном не том языке модель почти ничего не разберёт.</span><span lang="en">Check the <a href="model.html">recognition language</a>: with the wrong language explicitly selected the model will barely make anything out.</span></td></tr>
    </table>
""",
}

PAGES["updates"] = {
    "group_ru": "Решение проблем", "group_en": "Troubleshooting",
    "title_ru": "Обновления", "title_en": "Updates",
    "lede_ru": "Heardly проверяет новые версии сам и ставит их по вашему согласию. "
               "Проверить вручную и посмотреть установленную версию можно в настройках.",
    "lede_en": "Heardly checks for new versions by itself and installs them with your consent. "
               "You can check by hand, and see which version you have, in Settings.",
    "body": """
    <h2 id="check"><span lang="ru">Проверить вручную</span><span lang="en">Checking by hand</span></h2>
    <div lang="ru">
      <p><a href="settings.html">Настройки → Система</a>, строка «Обновления». Там же написана установленная версия и номер сборки. Та же кнопка есть внизу бокового меню настроек.</p>
    </div>
    <div lang="en">
      <p><a href="settings.html">Settings → System</a>, the “Updates” row. It also states the installed version and build number. The same button sits at the bottom of the settings sidebar.</p>
    </div>

    <figure>
      <img src="img/settings-system.png" alt="Раздел «Система»: запуск при входе, команда в терминале, язык интерфейса, обновления с номером версии">
    </figure>

    <h2 id="after"><span lang="ru">После обновления</span><span lang="en">After an update</span></h2>
    <div lang="ru">
      <p>Две вещи, которые могут повести себя неожиданно:</p>
      <ul>
        <li><b>Разрешения.</b> macOS привязывает их к сборке, поэтому «Универсальный доступ» иногда приходится включить заново — см. <a href="fix-dictation.html">Текст не вставляется</a>.</li>
        <li><b>Подготовка модели.</b> После крупного обновления macOS модель один раз пересобирается под Neural Engine: первый запуск займёт до пары минут.</li>
      </ul>
      <p>Записи, настройки и словарь замен обновление не трогает.</p>
    </div>
    <div lang="en">
      <p>Two things that can behave unexpectedly:</p>
      <ul>
        <li><b>Permissions.</b> macOS ties them to a build, so Accessibility sometimes has to be switched back on — see <a href="fix-dictation.html">Text is not inserted</a>.</li>
        <li><b>Model preparation.</b> After a major macOS update the model is rebuilt for the Neural Engine once, so the first launch takes up to a couple of minutes.</li>
      </ul>
      <p>Your recordings, settings and replacement list are left alone by an update.</p>
    </div>

    <div class="note warn">
      <b><span lang="ru">Запускайте из «Программ»</span><span lang="en">Run it from Applications</span></b>
      <p><span lang="ru">Если Heardly открыт прямо из скачанного образа <code>.dmg</code>, обновиться он не сможет. Перенесите приложение в «Программы».</span><span lang="en">If Heardly is running straight from the downloaded <code>.dmg</code>, it cannot update itself. Move the app into Applications.</span></p>
    </div>
""",
}

PAGES["support"] = {
    "group_ru": "Решение проблем", "group_en": "Troubleshooting",
    "title_ru": "Сообщить о проблеме", "title_en": "Report a problem",
    "lede_ru": "Если ничего из раздела «Решение проблем» не помогло, напишите нам — "
               "и приложите несколько деталей, по которым проблему будет видно.",
    "lede_en": "If nothing in Troubleshooting helped, get in touch — "
               "and bring a few details that make the problem visible.",
    "body": """
    <h2 id="what"><span lang="ru">Что приложить к письму</span><span lang="en">What to include</span></h2>
    <div lang="ru">
      <ul>
        <li><b>Версию Heardly и macOS.</b> Версия приложения написана внизу бокового меню настроек.</li>
        <li><b>Что именно не работает</b> и в каком месте: диктовка, звонок, файл, оплата.</li>
        <li><b>Что происходит на экране</b> — скриншот или короткая запись экрана.</li>
        <li><b>Повторяется ли это</b> каждый раз или случилось однажды.</li>
      </ul>
      <p>Текст расшифровок присылать не нужно: для разбора он почти никогда не требуется, а это ваши рабочие разговоры.</p>
    </div>
    <div lang="en">
      <ul>
        <li><b>Your Heardly and macOS versions.</b> The app version is at the bottom of the settings sidebar.</li>
        <li><b>What exactly fails</b> and where: dictation, a call, a file, payment.</li>
        <li><b>What you see on screen</b> — a screenshot or a short screen recording.</li>
        <li><b>Whether it repeats</b> every time, or happened once.</li>
      </ul>
      <p>There is no need to send transcript text: it is almost never needed to work the problem out, and those are your work conversations.</p>
    </div>

    <h2 id="where"><span lang="ru">Куда писать</span><span lang="en">Where to write</span></h2>
    <div lang="ru"><p>Пишите на <a href="mailto:support@kekoborn.ru">support@kekoborn.ru</a>.</p></div>
    <div lang="en"><p>Write to <a href="mailto:support@kekoborn.ru">support@kekoborn.ru</a>.</p></div>

    <h2 id="crash"><span lang="ru">Отчёты о сбоях</span><span lang="en">Crash reports</span></h2>
    <div lang="ru">
      <p>Если приложение падает или зависает, Heardly сам отправляет технический отчёт: стек вызовов, версию приложения и macOS. Звук и текст расшифровок в отчёт не попадают — см. <a href="privacy.html">Что уходит в интернет</a>.</p>
      <p>Отчёт не содержит описания того, что вы делали, поэтому письмо с парой строк от вас помогает гораздо больше.</p>
    </div>
    <div lang="en">
      <p>If the app crashes or freezes, Heardly sends a technical report by itself: the call stack, the app version and the macOS version. No audio and no transcript text go into it — see <a href="privacy.html">What leaves your Mac</a>.</p>
      <p>The report says nothing about what you were doing, which is why a couple of lines from you helps far more.</p>
    </div>
""",
}
