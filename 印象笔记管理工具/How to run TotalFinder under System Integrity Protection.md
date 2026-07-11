# How to run TotalFinder under System Integrity Protection

---

How to run TotalFinder under System Integrity Protection
========================================================

Under OS X 10.11 (El Capitan), TotalFinder cannot run on a normally configured machine due to [System Integrity Protection](https://en.wikipedia.org/wiki/System_Integrity_Protection).

System Integrity Protection (SIP) is a new security feature introduced by Apple. That's good, but unfortunately it prevents TotalFinder from augmenting Finder. This article will tell you how to configure your machine, so that you can use TotalFinder. Before you do this, it is important to get informed about [what System Integrity Protection is, and what it means to turn it off](https://en.wikipedia.org/wiki/System_Integrity_Protection). Technical details are well covered in [SIP review on Ars Technica](http://arstechnica.com/apple/2015/09/os-x-10-11-el-capitan-the-ars-technica-review/8). Apple also provided [some information here](https://developer.apple.com/library/prerelease/mac/documentation/Security/Conceptual/System_Integrity_Protection_Guide/Introduction/Introduction.html).

[![](.evernote-content/AC26639B-A0E6-4155-B735-2E2C95FB8DCC/2EED4335-1A56-4F13-8695-E4152FE82690.jpg)](http://binaryage.com/about)At this point I want you to pause and ask yourself a question. Do you really depend on TotalFinder workflows so much that you want to possibly lower your system security? Frankly, I'm going to stop active TotalFinder development because it is not economically viable to continue development for a small group of users who decide to disable SIP. Also it is likely that in the next OS release after El Capitan TotalFinder won't work at all. It is increasingly more difficult to reverse-engineer Finder as new parts are being written in Swift. Also operating system security hardening will probaly continue in future. Those are good things, but you will have to let TotalFinder go at some point anyway. Maybe for you the day is today. Bite the bullet and move on. I have prepared a list of [TotalFinder alternatives here](http://discuss.binaryage.com/t/totalfinder-alternatives).

Anyways, if you decide to modify the setting under El Capitan, you will be able to install and run TotalFinder as before. Just to be clear...

I'm not encouraging you to turn System Integrity Protection off. Your machine may be less secure with it off. It is entirely your decision.

How to partially disable System Integrity Protection
----------------------------------------------------

You must boot into the [Recovery OS](https://support.apple.com/en-us/HT201314). You do this by restarting your machine, and holding `COMMAND + R` until the Apple logo appears.

Then select Terminal from the Utilities menu. It looks like this:

![](.evernote-content/AC26639B-A0E6-4155-B735-2E2C95FB8DCC/016F7385-3653-48D0-957D-941595264410.png)

In the window that opens, type `csrutil enable --without debug` and press return.

![](.evernote-content/AC26639B-A0E6-4155-B735-2E2C95FB8DCC/61F7650B-C558-48CF-834D-DA29333087F1.png)

This turns off the part of SIP that TotalFinder needs to run, and OS X complains that it is an unsupported configuration.

Now type `reboot` and press return to restart your machine. After restart you may install the [latest version of TotalFinder](http://totalfinder.binaryage.com/beta-changes#latest).

Technical details
-----------------

TotalFinder works by changing Finder.app. OS X does not provide any other way to achieve deep Finder modifications, we believe this is the only way the functionality of TotalFinder can be achieved.

In order to add or change some features of Finder, we use a technique called *code injection*. This means we add some additional code to the Finder program whilst it is running to do what we need. This is relatively safe - in fact we do not change any part of OS X on the disk. You only have to force quit Finder via `COMMAND+OPTION+ESC` to relaunch Finder.app cleanly and everything will be as if TotalFinder was never running.

However, in El Capitan new security measures disallow this kind of modification *even if you have administrator access*. In order for TotalFinder to launch, part of System Integrity Protection must be disabled.

You can find some further information [in our blog](http://blog.binaryage.com/el-capitan-update).

Need to enable System Integrity Protection again?
-------------------------------------------------

Please follow [this article](http://totalfinder.binaryage.com/enable-sip).

[📎 在印象笔记中打开](evernote:///view/207087/s1/46d32802-e68b-4443-b8aa-0bc349dc536f/46d32802-e68b-4443-b8aa-0bc349dc536f/)