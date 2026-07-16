---
title: "HOW-TO_Install XBMC on Apple TV 2 - XBMC"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/HOW-TO_Install XBMC on Apple TV 2 - XBMC.md
tags: [印象笔记]
---

# HOW-TO_Install XBMC on Apple TV 2 - XBMC

# HOW-TO:Install XBMC on Apple TV 2 - XBMC --- HOW-TO:Install XBMC on Apple TV 2 ===================

---

# HOW-TO:Install XBMC on Apple TV 2 - XBMC

---

HOW-TO:Install XBMC on Apple TV 2
=================================

Jump to: [navigation](http://wiki.xbmc.org/index.php?title=HOW-TO:Install_XBMC_on_Apple_TV_2#mw-head),
[search](http://wiki.xbmc.org/index.php?title=HOW-TO:Install_XBMC_on_Apple_TV_2#p-search)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  | [iOS](http://wiki.xbmc.org/index.php?title=IOS "IOS")/[ATV2](http://wiki.xbmc.org/index.php?title=ATV2 "ATV2") | **HOW-TO:Install XBMC on Apple TV 2** |

The current stable release for iOS is XBMC v13 [Gotham](http://wiki.xbmc.org/index.php?title=Gotham "Gotham").

Requirements

* To ****Install XBMC on ATV2**** you must have a [jailbroken](http://forum.xbmc.org/showthread.php?tid=99315 "forum:99315") [Apple TV 2](http://wiki.xbmc.org/index.php?title=Apple_TV_2 "Apple TV 2") running [versions 4.1 to 5.3](http://en.wikipedia.org/wiki/IOS_version_history#Version_history:_Apple_TV_.282nd_generation.29_onwards "w:IOS version history")
* XBMC only works on the second generation Apple TV (ATV2), which is the black version that outputs 720p. XBMC does not work on the newer third generation Apple TV (ATV3) that outputs 1080p (Full HD), because there is no jailbreak for the ATV3.
* If you have any issues, be sure to read the [iOS FAQ](http://wiki.xbmc.org/index.php?title=IOS_FAQ "IOS FAQ")!

|  |
| --- |
| Contents [[hide](http://wiki.xbmc.org/index.php?title=HOW-TO:Install_XBMC_on_Apple_TV_2#)]   * [1 Installing from the command line](http://wiki.xbmc.org/index.php?title=HOW-TO:Install_XBMC_on_Apple_TV_2#Installing_from_the_command_line) * [2 Installing from NitoTV](http://wiki.xbmc.org/index.php?title=HOW-TO:Install_XBMC_on_Apple_TV_2#Installing_from_NitoTV) * [3 Updating](http://wiki.xbmc.org/index.php?title=HOW-TO:Install_XBMC_on_Apple_TV_2#Updating) * [4 Development builds](http://wiki.xbmc.org/index.php?title=HOW-TO:Install_XBMC_on_Apple_TV_2#Development_builds)   + [4.1 Nightly builds](http://wiki.xbmc.org/index.php?title=HOW-TO:Install_XBMC_on_Apple_TV_2#Nightly_builds)   + [4.2 Monthly builds](http://wiki.xbmc.org/index.php?title=HOW-TO:Install_XBMC_on_Apple_TV_2#Monthly_builds) * [5 Uninstalling](http://wiki.xbmc.org/index.php?title=HOW-TO:Install_XBMC_on_Apple_TV_2#Uninstalling)   + [5.1 Uninstalling just XBMC](http://wiki.xbmc.org/index.php?title=HOW-TO:Install_XBMC_on_Apple_TV_2#Uninstalling_just_XBMC)   + [5.2 Removing settings](http://wiki.xbmc.org/index.php?title=HOW-TO:Install_XBMC_on_Apple_TV_2#Removing_settings)   + [5.3 Deleting XBMC dependencies](http://wiki.xbmc.org/index.php?title=HOW-TO:Install_XBMC_on_Apple_TV_2#Deleting_XBMC_dependencies) |

1 Installing from the command line
----------------------------------

1. Open up your [terminal/ssh application](http://wiki.xbmc.org/index.php?title=XBMC_for_iOS_specific_FAQ#SSH "XBMC for iOS specific FAQ") and enter the following command to log in to your ATV2. Note, you need to replace "YOUR.ATV2.IP.ADDRESS" with the IP address of the Apple TV:

   :   ```
       ssh root@YOUR.ATV2.IP.ADDRESS
       ```

       :   **EXAMPLE:** `ssh root@192.168.1.5`
2. You will be asked for a password: *default password is **alpine***
3. Continue to enter the following commands:

   :   ```
       apt-get install wget
       ```
   :   ```
       wget -O- http://apt.awkwardtv.org/awkwardtv.pub | apt-key add -
       ```
   :   ```
       echo "deb http://apt.awkwardtv.org/ stable main" > /etc/apt/sources.list.d/awkwardtv.list
       ```
   :   ```
       echo "deb http://mirrors.xbmc.org/apt/atv2 ./" > /etc/apt/sources.list.d/xbmc.list
       ```
   :   ```
       apt-get update
       ```
   :   ```
       mkdir -p /Applications/AppleTV.app/Appliances
       ```
   :   ```
       apt-get install org.xbmc.xbmc-atv2
       ```
   :   ```
       mkdir -p /Applications/XBMC.frappliance
       ```
   :   ```
       reboot
       ```

And you're done! You should now be running XBMC v13 [Gotham](http://wiki.xbmc.org/index.php?title=Gotham "Gotham") for Apple TV 2. See [here](http://wiki.xbmc.org/index.php?title=IOS_FAQ#XBMC_Version "IOS FAQ") to verify your XBMC version.

2 Installing from NitoTV
------------------------

|  |  |
| --- | --- |
|  | **NOTICE:** While this should work in theory, the official installation method for XBMC is to use the command line instructions. If you have issues with any of the Nito installers then please try the command line instructions to see if that fixes the issue. Nito simply gives a GUI for those command line instructions, so it should work, but Team XBMC has no control over those installers and cannot update them or see any errors from them, or anything like that. |

NitoTV on the Apple TV 2

1. Scroll right to the NitoTV menu on the Apple TV and choose the first option "*Install Software*".
2. Scroll down the list until you see "*XBMC-ATV2*" and click on that.
3. From that menu press "*install*" and your Apple TV will install XBMC and then do a **SOFT** reboot (no tethered boot required).
4. XBMC will now be in your Apple TV menu, scroll right to it, click and enjoy.

And you're done! You should now be running XBMC v13 [Gotham](http://wiki.xbmc.org/index.php?title=Gotham "Gotham") for Apple TV 2. See [here](http://wiki.xbmc.org/index.php?title=IOS_FAQ#XBMC_Version "IOS FAQ") to verify your XBMC version.

3 Updating
----------

Either update through NitoTV or issue the following commands to update:

1. Open up your [terminal/ssh application](http://wiki.xbmc.org/index.php?title=XBMC_for_iOS_specific_FAQ#SSH "XBMC for iOS specific FAQ") and enter the following command to log in to your ATV2:

   :   ```
       ssh root@YOUR.ATV2.IP.ADDRESS
       ```

       :   **EXAMPLE:** `ssh root@192.168.1.5`
2. You will be asked for a password: *default password is **alpine***
3. Continue to enter the following commands:

   :   ```
       apt-get update
       ```
   :   ```
       apt-get install org.xbmc.xbmc-atv2
       ```

4 Development builds
--------------------

Main page: **[Development builds](http://wiki.xbmc.org/index.php?title=Development_builds "Development builds")**

### 4.1 Nightly builds

See also: **[nightly builds](http://wiki.xbmc.org/index.php?title=Nightly_builds "Nightly builds")**

Nightly builds are unstable test builds that have the latest bug fixes and feature additions. Nightly builds work with both ATV2 software version 4.x and 5.x. They are not fully tested, so anticipate issues and be sure to [backup your userdata folder](http://wiki.xbmc.org/index.php?title=IOS_FAQ#Backup "IOS FAQ").

:   *Change history: [commit history](https://github.com/xbmc/xbmc/commits)*

**NOTE: You MUST install the stable version (see above) before you can install a nightly build.** You only need to install the stable version once and you don't need to uninstall previous versions to upgrade (or downgrade) XBMC.

1. Open <http://mirrors.xbmc.org/nightlies/darwin/atv2/> in a web browser and copy the url of the **most recent file** in that listing.

   :   :   **EXAMPLE:** `http://mirrors.xbmc.org/nightlies/darwin/atv2/xbmc-20111202-6729214-master-atv2.deb`
2. Open up your [terminal/ssh application](http://wiki.xbmc.org/index.php?title=XBMC_for_iOS_specific_FAQ#What_is_SSH.3F "XBMC for iOS specific FAQ") and enter the following command to log in to your ATV2:

   :   ```
       ssh root@YOUR.ATV2.IP.ADDRESS
       ```

       :   **EXAMPLE:** `ssh root@192.168.1.5`
3. You will be asked for a password: *default password is **alpine***
4. Continue to enter the following commands:

   :   ```
       rm -f *xbmc*.deb
       ```
   :   ```
       wget URL-FROM-STEP-ONE-HERE
       ```

       :   **EXAMPLE:** `wget http://mirrors.xbmc.org/nightlies/darwin/atv2/xbmc-20111202-6729214-master-atv2.deb`
   :   ```
       dpkg -i *xbmc*.deb
       ```
   :   ```
       rm *xbmc*.deb
       ```

And you're done! You should now have the latest nightly build of XBMC for ATV2. See [here](http://wiki.xbmc.org/index.php?title=IOS_FAQ#XBMC_Version "IOS FAQ") to verify your XBMC version.

### 4.2 Monthly builds

See also: **[monthly builds](http://wiki.xbmc.org/index.php?title=Monthly_builds "Monthly builds")**

Installing a semi-stable monthly build is the same as installing a [nightly build](http://wiki.xbmc.org/index.php?title=HOW-TO:Install_XBMC_on_Apple_TV_2#Nightly_builds) above, but with the url in step 1 replaced with <http://mirrors.xbmc.org/snapshots/darwin/atv2/>

5 Uninstalling
--------------

### 5.1 Uninstalling just XBMC

SSH into your Apple TV (Using the same instructions from above to login). Then run:

```
 apt-get remove org.xbmc.xbmc-atv2
```

It will ask you if you want to continue:

```
The following packages will be REMOVED:
  org.xbmc.xbmc-atv2
0 upgraded, 0 newly installed, 1 to remove and 5 not upgraded.
After this operation, 0B of additional disk space will be used.
Do you want to continue [Y/n]?
```

Just enter "Y" to accept and continue.

### 5.2 Removing settings

XBMC will uninstall from your Apple TV but will leave certain things ([databases](http://wiki.xbmc.org/index.php?title=XBMC_databases "XBMC databases") and everything in your [userdata folder](http://wiki.xbmc.org/index.php?title=Userdata_folder "Userdata folder")) behind to make it easier if you wanted to reinstall. To delete those also run:

```
rm -Rf /private/var/mobile/Library/Preferences/XBMC
```

This will then be completely clear and XBMC will be removed.

### 5.3 Deleting XBMC dependencies

XBMC has three dependencies that it installs along with itself when you first install XBMC (org.xbmc.xbmc-seatbeltunlock, gawk, bsdiff). After uninstalling XBMC you can also uninstall these 3 dependencies by running this command:

```
apt-get remove org.xbmc.xbmc-seatbeltunlock && apt-get remove gawk && apt-get remove bsdiff
```

[Categories](http://wiki.xbmc.org/index.php?title=Special:Categories "Special:Categories"):

* [XBMC Manual](http://wiki.xbmc.org/index.php?title=Category:XBMC_Manual "Category:XBMC Manual")
* [IOS](http://wiki.xbmc.org/index.php?title=Category:IOS "Category:IOS")
* [How-to](http://wiki.xbmc.org/index.php?title=Category:How-to "Category:How-to")
* [Installation](http://wiki.xbmc.org/index.php?title=Category:Installation "Category:Installation")
* [Gotham](http://wiki.xbmc.org/index.php?title=Category:Gotham "Category:Gotham")

---

[🌐 原始链接](http://wiki.xbmc.org/index.php?title=HOW-TO:Install_XBMC_on_Apple_TV_2)

[📎 在印象笔记中打开](evernote:///view/207087/s1/fc332583-8615-49df-ac2b-99cbd5ea43fb/fc332583-8615-49df-ac2b-99cbd5ea43fb/)