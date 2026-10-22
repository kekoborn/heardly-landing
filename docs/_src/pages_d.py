# -*- coding: utf-8 -*-
"""Разделы «Настройки», «Аккаунт» и «Приватность»."""

PAGES = {}

PAGES["settings"] = {
    "group_ru": "Настройки", "group_en": "Settings",
    "title_ru": "Справочник настроек", "title_en": "Settings reference",
    "lede_ru": "Все настройки Heardly собраны в одном окне из шести разделов. "
               "Открыть его можно из попапа в строке меню или сочетанием ⌘ + запятая.",
    "lede_en": "Every Heardly setting lives in one window with six sections. "
               "Open it from the menu bar panel or with ⌘ + comma.",
    "body": """
    <h2 id="general"><span lang="ru">Основные</span><span lang="en">General</span></h2>
    <figure>
      <img src="img/settings-general.png" alt="Раздел «Основные»: горячая клавиша, активация диктовки, микрофон, язык распознавания">
    </figure>
    <table class="ref">
      <tr><td><span lang="ru">Горячая клавиша</span><span lang="en">Shortcut</span></td>
          <td><span lang="ru">Сочетание, которым начинается диктовка. По умолчанию правый ⌘.</span><span lang="en">The combination that starts dictation. The right ⌘ by default.</span></td></tr>
      <tr><td><span lang="ru">Активация диктовки при</span><span lang="en">Activation</span></td>
          <td><span lang="ru">«Нажатие» — клавиша работает как выключатель, «Удержание» — запись идёт, пока клавиша зажата.</span><span lang="en">“Toggle” makes the key a switch; “Hold” records only while the key is down.</span></td></tr>
      <tr><td><span lang="ru">Микрофон</span><span lang="en">Microphone</span></td>
          <td><span lang="ru">«Авто» выбирает устройство сам, можно задать конкретное или системное по умолчанию.</span><span lang="en">“Auto” picks a device for you; you can also name one, or follow the system default.</span></td></tr>
      <tr><td><span lang="ru">Язык распознавания</span><span lang="en">Recognition language</span></td>
          <td><span lang="ru">Автоопределение или конкретный язык — <a href="model.html">подробнее</a>.</span><span lang="en">Auto-detect or a specific language — <a href="model.html">more on this</a>.</span></td></tr>
    </table>

    <h2 id="dictation"><span lang="ru">Диктовка</span><span lang="en">Dictation</span></h2>
    <figure>
      <img src="img/settings-dictation.png" alt="Раздел «Диктовка»: вид панели, словарь замен, выключение звука других приложений">
    </figure>
    <table class="ref">
      <tr><td><span lang="ru">Вид диктовки</span><span lang="en">Bar style</span></td>
          <td><span lang="ru">Большая панель или мини. У мини выбирается положение: внизу экрана или у значка в строке меню. <a href="dictation-bar.html">Как они выглядят</a>.</span><span lang="en">The large bar or the mini one. The mini bar has a position: bottom of the screen or under the menu bar icon. <a href="dictation-bar.html">How they look</a>.</span></td></tr>
      <tr><td><span lang="ru">Словарь замен</span><span lang="en">Replacement list</span></td>
          <td><span lang="ru">Правила для имён и терминов — <a href="replacements.html">как их писать</a>.</span><span lang="en">Rules for names and terms — <a href="replacements.html">how to write them</a>.</span></td></tr>
      <tr><td><span lang="ru">Выключать звук других приложений</span><span lang="en">Silence other apps</span></td>
          <td><span lang="ru">Приглушает остальные программы на время диктовки — <a href="muffle.html">зачем</a>.</span><span lang="en">Quiets other apps while you dictate — <a href="muffle.html">why</a>.</span></td></tr>
    </table>

    <h2 id="recordings"><span lang="ru">Записи</span><span lang="en">Recordings</span></h2>
    <table class="ref">
      <tr><td><span lang="ru">Папка для расшифровок</span><span lang="en">Transcripts folder</span></td>
          <td><span lang="ru">Где лежат текстовые файлы и как их перенести — <a href="folder.html">подробнее</a>.</span><span lang="en">Where the text files live and how to move them — <a href="folder.html">more on this</a>.</span></td></tr>
      <tr><td><span lang="ru">История транскрипций</span><span lang="en">Transcription history</span></td>
          <td><span lang="ru">Открывает окно <a href="history.html">Истории</a>.</span><span lang="en">Opens the <a href="history.html">History</a> window.</span></td></tr>
    </table>

    <h2 id="system"><span lang="ru">Система</span><span lang="en">System</span></h2>
    <figure>
      <img src="img/settings-system.png" alt="Раздел «Система»: запуск при входе, команда в терминале, язык интерфейса, обновления">
    </figure>
    <table class="ref">
      <tr><td><span lang="ru">Запускать при входе в систему</span><span lang="en">Launch at login</span></td>
          <td><span lang="ru">Heardly стартует вместе с Mac и ждёт в строке меню.</span><span lang="en">Heardly starts with the Mac and waits in the menu bar.</span></td></tr>
      <tr><td><span lang="ru">Команда в терминале</span><span lang="en">Terminal command</span></td>
          <td><span lang="ru">Ставит команду <a href="cli.html"><code>heardly</code></a> (Pro).</span><span lang="en">Installs the <a href="cli.html"><code>heardly</code></a> command (Pro).</span></td></tr>
      <tr><td><span lang="ru">Интерфейс</span><span lang="en">Interface</span></td>
          <td><span lang="ru">Язык меню и окон: русский, английский, испанский, французский. На распознавание не влияет.</span><span lang="en">The language of menus and windows: Russian, English, Spanish, French. It does not affect recognition.</span></td></tr>
      <tr><td><span lang="ru">Обновления</span><span lang="en">Updates</span></td>
          <td><span lang="ru">Показывает установленную версию и проверяет новую — <a href="updates.html">подробнее</a>.</span><span lang="en">Shows the installed version and checks for a new one — <a href="updates.html">more on this</a>.</span></td></tr>
    </table>

    <h2 id="account"><span lang="ru">Статистика и Подписка</span><span lang="en">Statistics and Subscription</span></h2>
    <div lang="ru">
      <p>«Статистика» — сводка по вашим записям, <a href="stats.html">что в ней считается</a>. «Подписка» — состояние доступа, покупка и восстановление, см. <a href="pricing.html">Бесплатно, пробный период и Pro</a> и <a href="license.html">Лицензия и устройства</a>.</p>
    </div>
    <div lang="en">
      <p>“Statistics” is a summary of your own recordings — <a href="stats.html">what it counts</a>. “Subscription” holds the state of your access, the purchase and the restore flow; see <a href="pricing.html">Free, trial and Pro</a> and <a href="license.html">Licence and devices</a>.</p>
    </div>
""",
}

PAGES["model"] = {
    "group_ru": "Настройки", "group_en": "Settings",
    "title_ru": "Модель и языки", "title_en": "Model and languages",
    "lede_ru": "Распознаванием занимается модель Parakeet, которая целиком лежит на вашем компьютере "
               "и считается на Neural Engine.",
    "lede_en": "Recognition is done by the Parakeet model, which lives entirely on your computer "
               "and runs on the Neural Engine.",
    "body": """
    <h2 id="model"><span lang="ru">Модель</span><span lang="en">The model</span></h2>
    <div lang="ru">
      <p>Heardly использует Parakeet Ultra. Модель скачивается один раз при первом запуске, занимает около 600 МБ и лежит в <code>~/Library/Application&nbsp;Support/FluidAudio/Models/</code>.</p>
      <p>Поверх базовой модели Heardly доставляет собственную доработку под русскую речь: она подтягивается отдельным небольшим обновлением и улучшает разбор русского, не трогая остальные языки.</p>
      <p>Выбора между моделями в приложении нет — она одна. Облачных моделей и ключей к чужим API тоже нет.</p>
    </div>
    <div lang="en">
      <p>Heardly uses Parakeet Ultra. The model is downloaded once on first launch, takes about 600 MB and sits in <code>~/Library/Application&nbsp;Support/FluidAudio/Models/</code>.</p>
      <p>On top of the base model Heardly ships its own refinement for Russian speech: it arrives as a separate small update and improves Russian without touching the other languages.</p>
      <p>There is no model picker in the app — there is only one. There are no cloud models and no keys to third-party APIs either.</p>
    </div>

    <h2 id="languages"><span lang="ru">Языки</span><span lang="en">Languages</span></h2>
    <div lang="ru">
      <p>В <a href="settings.html">Настройках → Основные</a>, строка «Язык распознавания», можно оставить автоопределение или выбрать язык из списка:</p>
      <p>русский, английский, украинский, немецкий, французский, испанский, итальянский, португальский, китайский, японский, корейский, арабский, турецкий, польский, нидерландский, шведский, хинди.</p>
    </div>
    <div lang="en">
      <p>In <a href="settings.html">Settings → General</a>, the “Recognition language” row, you can leave auto-detect on or pick a language from the list:</p>
      <p>Russian, English, Ukrainian, German, French, Spanish, Italian, Portuguese, Chinese, Japanese, Korean, Arabic, Turkish, Polish, Dutch, Swedish, Hindi.</p>
    </div>

    <figure>
      <img src="img/language-sheet.png" alt="Список языков распознавания: переключатель автоопределения, поиск по языкам и семнадцать языков карточками">
      <figcaption><span lang="ru">Список языков: автоопределение переключается справа сверху, выбранный язык обведён.</span><span lang="en">The language list: auto-detect switches at the top right, the chosen language is outlined.</span></figcaption>
    </figure>

    <div class="note tip">
      <b><span lang="ru">Говорите всегда на одном языке — выберите его явно</span><span lang="en">Always speaking one language? Name it</span></b>
      <p><span lang="ru">Автоопределение иногда спотыкается на коротких фразах и на русской речи с английскими терминами. Если язык у вас постоянный, явный выбор надёжнее.</span><span lang="en">Auto-detect sometimes stumbles on short phrases, and on speech that mixes a language with English terms. If your language never changes, naming it is more reliable.</span></p>
    </div>

    <h2 id="offline"><span lang="ru">Работа без интернета</span><span lang="en">Working offline</span></h2>
    <div lang="ru">
      <p>После того как модель скачана, интернет для распознавания не нужен совсем: диктовка, звонки и файлы работают в самолёте и в поезде. Что всё-таки обращается в сеть — на странице <a href="privacy.html">Что уходит в интернет</a>.</p>
    </div>
    <div lang="en">
      <p>Once the model is downloaded, recognition needs no internet at all: dictation, calls and files work on a plane or a train. What does still reach the network is on the <a href="privacy.html">What leaves your Mac</a> page.</p>
    </div>
""",
}

PAGES["stats"] = {
    "group_ru": "Настройки", "group_en": "Settings",
    "title_ru": "Статистика", "title_en": "Statistics",
    "lede_ru": "Раздел показывает, сколько вы наговорили и сколько времени это сэкономило по сравнению с печатью. "
               "Считается всё по вашим записям и никуда не отправляется.",
    "lede_en": "This section shows how much you have spoken and how much time that saved compared with typing. "
               "Everything is counted from your own recordings and goes nowhere.",
    "body": """
    <figure>
      <img src="img/settings-statistics.png" alt="Раздел «Статистика»: скорость речи, сэкономленное время, всего слов, разбивка по видам записей и календарь активности">
    </figure>

    <h2 id="cards"><span lang="ru">Что в карточках</span><span lang="en">What the cards mean</span></h2>
    <table class="ref">
      <tr><td><span lang="ru">Скорость</span><span lang="en">Speed</span></td>
          <td><span lang="ru">Сколько слов в минуту вы наговариваете. Рядом — во сколько раз это быстрее печати.</span><span lang="en">How many words a minute you speak. Beside it, how many times faster that is than typing.</span></td></tr>
      <tr><td><span lang="ru">Сэкономлено</span><span lang="en">Saved</span></td>
          <td><span lang="ru">Разница между временем, которое вы наговорили, и временем, которое ушло бы на набор того же текста.</span><span lang="en">The gap between the time you spent speaking and the time the same text would have taken to type.</span></td></tr>
      <tr><td><span lang="ru">Всего слов</span><span lang="en">Total words</span></td>
          <td><span lang="ru">Все слова во всех записях, плюс оценка в страницах и разбивка на микрофон и звук приложений.</span><span lang="en">Every word across every entry, plus a rough page count and the split between microphone and app audio.</span></td></tr>
      <tr><td><span lang="ru">По видам записей</span><span lang="en">By kind</span></td>
          <td><span lang="ru">Сколько слов пришло из диктовки, из живых записей и из файлов.</span><span lang="en">How many words came from dictation, from live recordings and from files.</span></td></tr>
      <tr><td><span lang="ru">Дней подряд</span><span lang="en">Streak</span></td>
          <td><span lang="ru">Сколько дней подряд вы пользуетесь Heardly, и календарь активности рядом.</span><span lang="en">How many days in a row you have used Heardly, with an activity calendar beside it.</span></td></tr>
    </table>

    <div class="note">
      <b><span lang="ru">Это оценка, а не хронометраж</span><span lang="en">An estimate, not a stopwatch</span></b>
      <p><span lang="ru">«Сэкономлено» считается от средней скорости печати, а не от вашей личной. Цифра показывает порядок величины, а не точное время.</span><span lang="en">“Saved” is calculated from an average typing speed, not from your own. The number shows an order of magnitude, not an exact time.</span></p>
    </div>

    <div lang="ru"><p>Статистика строится из файлов в <a href="folder.html">папке расшифровок</a>. Удалите запись — она исчезнет и из статистики.</p></div>
    <div lang="en"><p>The statistics are built from the files in the <a href="folder.html">transcripts folder</a>. Delete an entry and it leaves the statistics too.</p></div>
""",
}

PAGES["pricing"] = {
    "group_ru": "Аккаунт", "group_en": "Account",
    "title_ru": "Бесплатно, пробный период и Pro", "title_en": "Free, trial and Pro",
    "lede_ru": "После установки две недели работают все функции. Дальше остаётся бесплатная версия "
               "с недельным лимитом слов — или подписка Pro без ограничений.",
    "lede_en": "For the first two weeks everything is unlocked. After that you keep a free version "
               "with a weekly word limit — or take a Pro subscription with no limits.",
    "body": """
    <h2 id="states"><span lang="ru">Три состояния</span><span lang="en">Three states</span></h2>
    <table class="ref">
      <tr>
        <th><span lang="ru">Состояние</span><span lang="en">State</span></th>
        <th><span lang="ru">Что доступно</span><span lang="en">What you get</span></th>
      </tr>
      <tr><td><span lang="ru">Пробный период</span><span lang="en">Trial</span></td>
          <td><span lang="ru">14 дней с момента первого запуска. Работает всё, карту вводить не нужно.</span><span lang="en">14 days from first launch. Everything works, and no card is needed.</span></td></tr>
      <tr><td><span lang="ru">Бесплатная версия</span><span lang="en">Free</span></td>
          <td><span lang="ru">Диктовка и живая расшифровка в пределах 2000 слов в неделю. Счётчик обнуляется в понедельник. Экспорт — только в TXT.</span><span lang="en">Dictation and live transcription within 2,000 words a week. The counter resets on Monday. Export is TXT only.</span></td></tr>
      <tr><td>Pro</td>
          <td><span lang="ru">Без лимита слов, расшифровка файлов, все восемь форматов экспорта и команда в терминале.</span><span lang="en">No word limit, file transcription, all eight export formats and the terminal command.</span></td></tr>
    </table>

    <h2 id="price"><span lang="ru">Сколько стоит</span><span lang="en">What it costs</span></h2>
    <table class="ref">
      <tr>
        <th><span lang="ru">Где</span><span lang="en">Where</span></th>
        <th><span lang="ru">Месяц</span><span lang="en">Monthly</span></th>
        <th><span lang="ru">Год</span><span lang="en">Yearly</span></th>
      </tr>
      <tr><td><span lang="ru">Россия и СНГ</span><span lang="en">Russia and CIS</span></td><td>499 ₽</td><td><span lang="ru">3 990 ₽ — это 332 ₽ в месяц</span><span lang="en">3,990 ₽ — that is 332 ₽ a month</span></td></tr>
      <tr><td><span lang="ru">Остальные страны</span><span lang="en">Elsewhere</span></td><td>$9.99</td><td><span lang="ru">$79.99 — это $6.67 в месяц</span><span lang="en">$79.99 — that is $6.67 a month</span></td></tr>
    </table>
    <div lang="ru"><p>Цена определяется по региону вашей системы. Оплата идёт в рублях: для карт вне СНГ сумма показывается в долларах, а списывается рублёвый эквивалент.</p></div>
    <div lang="en"><p>The price follows your system region. Payment is taken in roubles: outside the CIS the amount is shown in dollars and the rouble equivalent is charged.</p></div>

    <figure>
      <img src="img/settings-subscription.png" alt="Раздел «Подписка» в настройках Heardly">
      <figcaption><span lang="ru">Настройки → Подписка: состояние доступа, покупка и восстановление.</span><span lang="en">Settings → Subscription: the state of your access, buying and restoring.</span></figcaption>
    </figure>

    <h2 id="limit"><span lang="ru">Что происходит на лимите</span><span lang="en">What happens at the limit</span></h2>
    <div lang="ru">
      <p>Когда 2000 слов за неделю исчерпаны, в попапе появляется «Недельный лимит слов исчерпан» и подпись «сброс в понедельник». Новые записи до понедельника не начинаются, но всё, что уже расшифровано, остаётся на месте: История, папка и экспорт в TXT работают как обычно.</p>
    </div>
    <div lang="en">
      <p>Once the 2,000 words for the week are used up, the panel shows “Weekly word limit reached” and “resets Monday”. New recordings won’t start until Monday, but everything already transcribed stays put: History, the folder and TXT export keep working as usual.</p>
    </div>

    <h2 id="buy"><span lang="ru">Как оформить</span><span lang="en">How to subscribe</span></h2>
    <div lang="ru">
      <p>Откройте <a href="settings.html">Настройки → Подписка</a> и нажмите кнопку покупки. Понадобится email — на него оформляется подписка, и по нему же она потом восстанавливается на других устройствах, см. <a href="license.html">Лицензия и устройства</a>.</p>
    </div>
    <div lang="en">
      <p>Open <a href="settings.html">Settings → Subscription</a> and press the purchase button. You will need an email address — the subscription is issued to it, and it is also how you restore the subscription on other devices; see <a href="license.html">Licence and devices</a>.</p>
    </div>
""",
}

PAGES["license"] = {
    "group_ru": "Аккаунт", "group_en": "Account",
    "title_ru": "Лицензия и устройства", "title_en": "Licence and devices",
    "lede_ru": "Подписка привязана к email, а не к компьютеру. На скольких своих машинах включить Heardly — "
               "ваше дело, лимита устройств нет.",
    "lede_en": "The subscription is tied to an email address, not to a computer. How many of your own machines "
               "you run Heardly on is up to you — there is no device limit.",
    "body": """
    <h2 id="restore"><span lang="ru">Включить Pro на другом компьютере</span><span lang="en">Turning Pro on elsewhere</span></h2>
    <ol class="steps">
      <li>
        <b><span lang="ru">Откройте «Настройки → Подписка»</span><span lang="en">Open Settings → Subscription</span></b>
      </li>
      <li>
        <b><span lang="ru">Нажмите «Восстановить доступ»</span><span lang="en">Press “Restore access”</span></b>
        <div lang="ru"><p>Введите email, на который оформлена подписка.</p></div>
        <div lang="en"><p>Enter the email the subscription was issued to.</p></div>
      </li>
      <li>
        <b><span lang="ru">Введите код из письма</span><span lang="en">Enter the code from the email</span></b>
        <div lang="ru"><p>Heardly отправит на этот адрес короткий код и включит Pro после его ввода.</p></div>
        <div lang="en"><p>Heardly sends a short code to that address and switches Pro on once you type it in.</p></div>
      </li>
    </ol>

    <h2 id="offline"><span lang="ru">Pro без интернета</span><span lang="en">Pro without the internet</span></h2>
    <div lang="ru">
      <p>Heardly проверяет подписку на сервере не чаще раза в сутки, а результат запоминает. Если интернета нет или сервер недоступен, Pro продолжает работать ещё две недели с последней удачной проверки — поездка без связи доступ не отключит.</p>
    </div>
    <div lang="en">
      <p>Heardly checks the subscription with the server at most once a day and remembers the answer. If there is no internet, or the server is unreachable, Pro keeps working for another two weeks from the last successful check — a trip without a connection will not cut your access off.</p>
    </div>

    <h2 id="expired"><span lang="ru">Когда подписка кончилась</span><span lang="en">When the subscription ends</span></h2>
    <div lang="ru">
      <p>Приложение переходит в бесплатную версию: лимит 2000 слов в неделю, экспорт только в TXT, файлы и команда в терминале отключаются. Ничего из уже расшифрованного не пропадает — записи лежат текстовыми файлами в <a href="folder.html">вашей папке</a> и остаются доступны всегда.</p>
      <p>Продлить можно там же, в «Настройках → Подписка».</p>
    </div>
    <div lang="en">
      <p>The app falls back to the free version: 2,000 words a week, TXT-only export, no file transcription and no terminal command. Nothing you have already transcribed disappears — the entries are text files in <a href="folder.html">your folder</a> and stay available for good.</p>
      <p>You can renew in the same place, Settings → Subscription.</p>
    </div>

    <div class="note warn">
      <b><span lang="ru">Не получается восстановить</span><span lang="en">Restore not working</span></b>
      <p><span lang="ru">Проверьте, что вводите тот самый адрес, на который оформляли подписку, и загляните в папку «Спам». Если письмо так и не пришло — <a href="support.html">напишите нам</a>.</span><span lang="en">Check that you are entering the exact address the subscription was issued to, and look in the spam folder. If the email never arrives, <a href="support.html">get in touch</a>.</span></p>
    </div>
""",
}

PAGES["privacy"] = {
    "group_ru": "Приватность", "group_en": "Privacy",
    "title_ru": "Что уходит в интернет", "title_en": "What leaves your Mac",
    "lede_ru": "Короткий ответ: звук и расшифровки — никогда. Ниже разобрано, какие соединения Heardly всё же открывает и зачем.",
    "lede_en": "The short answer: audio and transcripts, never. Below is an account of the connections Heardly does open, and why.",
    "body": """
    <h2 id="never"><span lang="ru">Что остаётся на компьютере</span><span lang="en">What stays on the computer</span></h2>
    <div lang="ru">
      <ul>
        <li><b>Звук.</b> Ни запись с микрофона, ни звук приложений, ни загруженные файлы никуда не передаются. Распознавание целиком выполняет <a href="model.html">локальная модель</a>.</li>
        <li><b>Текст расшифровок.</b> Лежит обычными файлами в <a href="folder.html">вашей папке</a>. Облака и синхронизации у Heardly нет.</li>
        <li><b>Словарь замен и настройки.</b> Хранятся локально.</li>
      </ul>
    </div>
    <div lang="en">
      <ul>
        <li><b>Audio.</b> Neither the microphone recording, nor app audio, nor the files you drop in are ever transmitted. Recognition is done entirely by the <a href="model.html">local model</a>.</li>
        <li><b>Transcript text.</b> Kept as ordinary files in <a href="folder.html">your folder</a>. Heardly has no cloud and no sync.</li>
        <li><b>The replacement list and your settings.</b> Stored locally.</li>
      </ul>
    </div>

    <h2 id="network"><span lang="ru">Какие соединения всё-таки есть</span><span lang="en">The connections that do exist</span></h2>
    <table class="ref">
      <tr>
        <th><span lang="ru">Когда</span><span lang="en">When</span></th>
        <th><span lang="ru">Что уходит</span><span lang="en">What is sent</span></th>
      </tr>
      <tr><td><span lang="ru">Первый запуск</span><span lang="en">First launch</span></td>
          <td><span lang="ru">Загрузка модели распознавания и её обновлений под русский язык.</span><span lang="en">Downloading the recognition model and its Russian-language updates.</span></td></tr>
      <tr><td><span lang="ru">Проверка подписки</span><span lang="en">Subscription check</span></td>
          <td><span lang="ru">Не чаще раза в сутки: email подписки и признак устройства. Никакого содержимого записей.</span><span lang="en">At most once a day: the subscription email and a device marker. No recording content whatsoever.</span></td></tr>
      <tr><td><span lang="ru">Оплата</span><span lang="en">Payment</span></td>
          <td><span lang="ru">Оформление идёт на стороне платёжного сервиса. Данные карты Heardly не видит и не хранит.</span><span lang="en">The purchase happens on the payment provider’s side. Heardly never sees or stores card details.</span></td></tr>
      <tr><td><span lang="ru">Обновления</span><span lang="en">Updates</span></td>
          <td><span lang="ru">Проверка новой версии приложения и загрузка её файла.</span><span lang="en">Checking for a new version of the app and downloading its file.</span></td></tr>
      <tr><td><span lang="ru">Сбой приложения</span><span lang="en">A crash</span></td>
          <td><span lang="ru">Отчёт о падении или зависании: стек вызовов, версия приложения и macOS. Текст расшифровок и звук в отчёт не попадают.</span><span lang="en">A crash or freeze report: the call stack, the app version and the macOS version. No transcript text and no audio go into it.</span></td></tr>
    </table>

    <h2 id="calls"><span lang="ru">Про запись звонков</span><span lang="en">About recording calls</span></h2>
    <div lang="ru">
      <p>Heardly не подключается к встрече и не виден собеседникам: он слышит их так же, как ваши колонки или наушники. Отсюда простое следствие — никто не узнает о записи, если вы сами не скажете.</p>
      <p>Во многих странах и компаниях запись разговора без предупреждения недопустима. Предупреждайте в начале встречи.</p>
    </div>
    <div lang="en">
      <p>Heardly does not join the meeting and is invisible to the other side: it hears them the same way your speakers or headphones do. Which leads to a simple consequence — nobody learns about the recording unless you say so.</p>
      <p>In many countries and companies recording a conversation without telling people is not acceptable. Say it at the start of the meeting.</p>
    </div>

    <h2 id="airplane"><span lang="ru">Полностью офлайн</span><span lang="en">Fully offline</span></h2>
    <div lang="ru">
      <p>Если после загрузки модели отключить интернет совсем, Heardly продолжит работать: диктовка, звонки и файлы распознаются как обычно. Pro при этом живёт ещё две недели с последней удачной проверки подписки — см. <a href="license.html">Лицензия и устройства</a>.</p>
    </div>
    <div lang="en">
      <p>If you cut the internet off entirely once the model is downloaded, Heardly carries on: dictation, calls and files are recognised as usual. Pro stays alive for two more weeks from the last successful subscription check — see <a href="license.html">Licence and devices</a>.</p>
    </div>
""",
}
