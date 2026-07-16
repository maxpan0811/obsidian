---
title: "How to enable System Integrity Protection"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/How to enable System Integrity Protection.md
tags: [印象笔记]
---

# How to enable System Integrity Protection

# How to enable System Integrity Protection --- How to enable System Integrity Protection ==========

---

# How to enable System Integrity Protection

---

How to enable System Integrity Protection
=========================================

You must boot into the [Recovery OS](https://support.apple.com/en-us/HT201314). You do this by restarting your machine, and holding `COMMAND + R` until the Apple logo appears.

Then select Terminal from the Utilities menu. It looks like this:

![](.evernote-content/F318B03D-057B-47B3-9DB2-0C09CBED1DB3/334C2B63-F659-4183-A1AB-675F63F6CF8C.png)

In the window that opens, type `csrutil clear` and press return.

This clears existing configuration of System Integrity Protection to default state which is "enabled".

Now type `reboot` and press return to restart your machine.

---

More information about [TotalFinder and System Integrity Protection](http://totalfinder.binaryage.com/system-integrity-protection).

---

[🌐 原始链接](http://totalfinder.binaryage.com/enable-sip)

[📎 在印象笔记中打开](evernote:///view/207087/s1/d9ba8944-f313-44b1-be10-8a34f6cb4e5e/d9ba8944-f313-44b1-be10-8a34f6cb4e5e/)