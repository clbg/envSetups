#!/usr/bin/env bash
# @raycast.schemaVersion 1
# @raycast.title Ask Gemini (Chrome)
# @raycast.mode silent
# @raycast.packageName Gemini
# @raycast.argument1 {"type":"text","placeholder":"问 Gemini...", "percentEncoded": false}
# @raycast.icon 🤖

# 说明：把输入作为参数传给 AppleScript，在 Chrome 地址栏触发 @gemini 查询

osascript - "$@" <<'APPLESCRIPT'
on run argv
  set q to (argv as text)
  tell application "Google Chrome"
    activate
    if (count of windows) = 0 then
      make new window
    else
      tell window 1 to make new tab with properties {URL:"chrome://newtab/"}
    end if
  end tell
  delay 0.25
  tell application "System Events"
    -- 需在 系统设置 → 隐私与安全性 → 辅助功能 中勾选 Raycast
    keystroke "l" using {command down} -- 聚焦地址栏
    delay 0.1
    keystroke "@gemini " & q
    key code 36 -- 回车
  end tell
end run
APPLESCRIPT

