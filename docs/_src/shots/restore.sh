#!/bin/bash
# Возврат машины в состояние до съёмки документации.
# Значения сняты с com.heardly.app до того, как что-либо менялось.
set -u

echo "=== останавливаю dev-сборку ==="
osascript -e 'tell application id "com.heardly.app" to quit' 2>/dev/null || true
sleep 1.5
pkill -f "DevHeardly.app/Contents/MacOS/Heardly" 2>/dev/null || true
sleep 1

echo "=== возвращаю настройки Heardly ==="
defaults write com.heardly.app hotkeyKeyCode -int 54          # был правый ⌘
defaults write com.heardly.app hotkeyModifiers -int 0
defaults write com.heardly.app dictationBarStyle -int 1        # мини
defaults write com.heardly.app miniBarPosition -int 1          # у значка в меню
defaults write com.heardly.app dictationMode -int 0            # нажатие
defaults write com.heardly.app appLanguage -string ru          # язык интерфейса был русским
defaults delete com.heardly.app selectedMicDeviceID 2>/dev/null || true  # было «Авто», ключа не существовало
defaults delete com.heardly.app transcriptsFolderPath 2>/dev/null || true  # ключа не было — вернуть папку по умолчанию
defaults delete com.heardly.app replacementDictionary 2>/dev/null || true  # словарь замен был пуст, примеры для скриншота убираем

echo "=== возвращаю тёмную тему ==="
osascript -e 'tell application "System Events" to tell appearance preferences to set dark mode to true' 2>/dev/null || true

echo "=== запускаю боевой Heardly ==="
open -a /Applications/Heardly.app
sleep 3

echo "=== проверка ==="
printf "hotkeyKeyCode   = %s\n" "$(defaults read com.heardly.app hotkeyKeyCode 2>&1)"
printf "hotkeyModifiers = %s\n" "$(defaults read com.heardly.app hotkeyModifiers 2>&1)"
printf "dictationBarStyle = %s\n" "$(defaults read com.heardly.app dictationBarStyle 2>&1)"
printf "miniBarPosition = %s\n" "$(defaults read com.heardly.app miniBarPosition 2>&1)"
printf "transcriptsFolderPath = %s\n" "$(defaults read com.heardly.app transcriptsFolderPath 2>&1 | head -1)"
printf "AppleInterfaceStyle = %s\n" "$(defaults read -g AppleInterfaceStyle 2>&1 | head -1)"
printf "running Heardly: %s\n" "$(ps aux | grep -c '[/]Applications/Heardly.app/Contents/MacOS/Heardly')"
echo "Реальные расшифровки всё время лежали в ~/Documents/Heardly и не трогались."
