#/bin/bash

# Deprecated screenshot approach

alias python=python3

function adb_connect() {
    adb devices # Causes the adb daemon to start automatically.
}

function take_abd_screenshot() {
    adb shell "input keyevent 120"
}

function takeshots() {
    while true; do take_abd_screenshot; done
}

takeshots
