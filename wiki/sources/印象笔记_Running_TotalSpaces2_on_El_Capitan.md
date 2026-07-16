---
title: "Running TotalSpaces2 on El Capitan"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/Running TotalSpaces2 on El Capitan.md
tags: [印象笔记]
---

# Running TotalSpaces2 on El Capitan

# Running TotalSpaces2 on El Capitan --- How to run TotalSpaces2 on El Capitan =====================

---

# Running TotalSpaces2 on El Capitan

---

How to run TotalSpaces2 on El Capitan
=====================================

TotalSpaces2 [versions 2.3.5 and above](http://totalspaces.binaryage.com/changes-beta) have support for OSX 10.11 El Capitan, but cannot run on a normally configured machine due to system integrity protection, a new security feature in El Capitan.

This article will tell you how to configure your machine by modifying the new setting, so that you can run TotalSpaces2.

Before you do this, it is important to get informed about [what System Integrity Protection is, and what it means to turn it off](https://en.wikipedia.org/wiki/System_Integrity_Protection). Technical details are well covered in [the El Capitan review on Ars Technica](http://arstechnica.com/apple/2015/09/os-x-10-11-el-capitan-the-ars-technica-review/8). Apple also provide [some information here](https://developer.apple.com/library/prerelease/mac/documentation/Security/Conceptual/System_Integrity_Protection_Guide/Introduction/Introduction.html).

Anyway, if you decide to modify the setting under El Capitan, you will be able to install and run TotalSpaces2 as before. Just to be clear...

I'm not encouraging you to modify your System Integrity Protection settings. Your machine may be less secure if you do. It is entirely your decision.

How to modify System Integrity Protection
-----------------------------------------

You must boot into the Recovery OS. You do this by restarting your machine, and holding   ![](.evernote-content/77EB767B-ADEC-481C-9441-36442FF8C638/9F690E29-FA0F-476E-AB06-D01CAD696E80.png)   until the Apple logo appears.

Then select Terminal from the Utilities menu. It looks like this:

![](.evernote-content/77EB767B-ADEC-481C-9441-36442FF8C638/FAEA9660-2E15-4994-AC1B-BE01587A9DC7.png)

In the window that opens, type
`csrutil enable --without debug`
and press return. This turns off the part of System Integrity Protection that TotalSpaces2 needs to run, and OSX complains that it is an unsupported configuration.

![](.evernote-content/77EB767B-ADEC-481C-9441-36442FF8C638/CB794194-7A82-457D-BF33-4E3307732E7F.png)

Reboot your machine and you may install or run the [latest version of TotalSpaces2](http://totalspaces.binaryage.com/changes-beta).

Note, you can also use the `csrutil disable` command to completely disable System Integrity Protection. This has the advantage that there is no scary warning about an unsupported configuration, but the disadvantage that the whole of SIP (rather than just part) is disabled.

Technical details
-----------------

TotalSpaces2 works by changing the way the Dock program handles spaces. OSX does not provide any other way to control spaces, this is the only way the functionality of TotalSpaces2 can be achieved.

In order to change some features inside Dock, we use a technique called *code injection*. This means we add some additional code to the Dock program whilst it is running to do what we need. This is relatively safe - in fact we do not change any part of OSX on the disk. You only have to quit TotalSpaces2, and the Dock program will restart and everything will be as if TotalSpaces2 was never running.

However, in El Capitan the OSX developers added a feature that disallows this kind of modification *even if you have administrator access*. It can also disallow other kinds of modifications (such as replacing parts of the system on disk).

In order for TotalSpaces2 to work, part of this new feature must be disabled. And **we don't recommend you do this unless you know what you are doing.**

You can find some further information [in our blog](http://blog.binaryage.com/el-capitan-update/).

---

[🌐 原始链接](http://totalspaces.binaryage.com/elcapitan)

[📎 在印象笔记中打开](evernote:///view/207087/s1/acdd673e-2b93-49da-ba60-e0595e954e3d/acdd673e-2b93-49da-ba60-e0595e954e3d/)