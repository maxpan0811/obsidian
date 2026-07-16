---
title: "lukaspustina_Evernote.lbaction"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/lukaspustina_Evernote.lbaction.md
tags: [印象笔记]
---

# lukaspustina_Evernote.lbaction

# lukaspustina/Evernote.lbaction --- "Better" Evernote Integration for Launchbar ===================

---

# lukaspustina/Evernote.lbaction

---

"Better" Evernote Integration for Launchbar
===========================================

[![](.evernote-content/DC292A8A-0469-41C4-96C6-E2DB52283400/B06F2295-E19F-4569-82E3-4DE87282C6EF)](https://travis-ci.org/lukaspustina/Evernote.lbaction)

The current Evernote integration in Launchbar version 6.8 (6140) has a few shortcomings that make it difficult to interact with Evernote through Launchbar. For example, search terms are concatenated with `%20` as in URL encoded space, there is no preview of found notes you could select from, and creating new notes does not work properliy if you are using Evernote 6 or above.

This Launchbar Action mitigates these shortcomings.

[![](.evernote-content/DC292A8A-0469-41C4-96C6-E2DB52283400/03DF5427-182F-4BC9-9D2D-557B492C8647.png)](https://github.com/lukaspustina/Evernote.lbaction/blob/master/assets/Full%20menu.png)

**Table of Contents**

* [Features](https://github.com/lukaspustina/Evernote.lbaction#features)
  + [Open Evernote](https://github.com/lukaspustina/Evernote.lbaction#open-evernote)
  + [Search for Notes](https://github.com/lukaspustina/Evernote.lbaction#search-for-notes)
    - [Open Note](https://github.com/lukaspustina/Evernote.lbaction#open-note)
    - [Copy Note Link](https://github.com/lukaspustina/Evernote.lbaction#copy-note-link)
    - [Open Evernote Window with Search Query](https://github.com/lukaspustina/Evernote.lbaction#open-evernote-window-with-search-query)
  + [Favorite Notes](https://github.com/lukaspustina/Evernote.lbaction#favorite-notes)
  + [Saved Searches](https://github.com/lukaspustina/Evernote.lbaction#saved-searches)
  + [Create new Note](https://github.com/lukaspustina/Evernote.lbaction#create-new-note)
  + [Synchronize Now](https://github.com/lukaspustina/Evernote.lbaction#synchronize-now)
  + [Action Settings](https://github.com/lukaspustina/Evernote.lbaction#action-settings)
* [Installation](https://github.com/lukaspustina/Evernote.lbaction#installation)
* [Configuration](https://github.com/lukaspustina/Evernote.lbaction#configuration)
  + [Configuration Settings](https://github.com/lukaspustina/Evernote.lbaction#configuration-settings)
* [Known Limitations](https://github.com/lukaspustina/Evernote.lbaction#known-limitations)
* [Credits](https://github.com/lukaspustina/Evernote.lbaction#credits)

Features
--------

### Open Evernote

[![](.evernote-content/DC292A8A-0469-41C4-96C6-E2DB52283400/E9605FD9-BADC-46B6-9DCA-FA6C46EE40D7.png)](https://github.com/lukaspustina/Evernote.lbaction/blob/master/assets/Evernote.png)

In case you just want to open Evernote's main window, just press `<Return>` before entering a search query.

### Search for Notes

[![](.evernote-content/DC292A8A-0469-41C4-96C6-E2DB52283400/35ED682D-08A5-4CB5-9604-2BD3095D0C79.png)](https://github.com/lukaspustina/Evernote.lbaction/blob/master/assets/Search.png)

Search queries may make use of the full [Evernote Search Grammar](https://dev.evernote.com/doc/articles/search_grammar.php). For example:

* `search terms` -- matches notes that contain these terms in its full text
* `intitle:"Words in title"` -- maches notes with these words in the title
* `created:day-1` -- matches notes created yesterday or today
* `todo:*` -- matches notes that contain todos

See the link above for more details of Evernote's search grammar.

#### Open Note

You can open any matching note by navigating to the search result and pressing `<Return>`. The search results show the title, the date of the last modification, the tags -- if any --, and the notebook of each matching note.

#### Copy Note Link

You can copy an Evernote link of a note to the clipboard by navigating to the search result and pressing `<Cmd>+<Return>`. This allows you to create references to your notes in other applications as well as in other notes. These references will be opened by Evernote on your desktop; not the browser.

#### Open Evernote Window with Search Query

You can also open the main Evernote window with the executed search query results by pressing `<Shift>+<Cmd>+<Return>`. This allows you to see the result notes in Evernote's main window.

### Favorite Notes

[![](.evernote-content/DC292A8A-0469-41C4-96C6-E2DB52283400/FE349CE7-848D-434A-8A51-E2801725AA39.png)](https://github.com/lukaspustina/Evernote.lbaction/blob/master/assets/Favorites.png)

If you want a shortcut to notes you use frequently, add them as favorites notes in the settings file and open them quickly in the *Favorites* sub menu.

### Saved Searches

[![](.evernote-content/DC292A8A-0469-41C4-96C6-E2DB52283400/17ADAE58-3815-425C-97DE-1A7711CEF579.png)](https://github.com/lukaspustina/Evernote.lbaction/blob/master/assets/Saved%20Searches.png)

If you happen to search for specific queries regularly, you can save these queries as "saved searches" in the settings file and easily activate them in the *Saved Searches* sub menu.

### Create new Note

You can easily create a new note in the default notebook with the *Create new Note* menu item.

### Synchronize Now

You can trigger note synchronization with the *Synchronize Now* menu item.

### Action Settings

In order to change the default settings, add favorite notes, or saved searches, use the *Edit Settings* menu item. It will open the settings configuration file in your default editor application.

Installation
------------

1. Clone this repository
2. Deactivate the build-in Evernote integration in Launchbar's *Settings -> Index -> Show Index -> Applications -> Evernote*.
3. Double click the cloned repository directory in Finder.

Configuration
-------------

Since Launchbar does offer a built in mechanism for Action settings, this Action uses a JSON file called `settings.js` to configure its settings. The format is shown below and easy to use. Here is an example:

```
{
  "debug": true,
  "max_results": 20,
  "favorites": [
    { "name": "A frequently used note", "note_link": "evernote:///view/722304695/s5/1207980e-41aa-8c3a-db9c15c1fef1/120798e0-80e9-41aa-8c3a-db9c15c1fef1/" },
    { "name": "Another regularly used note", "note_link": "evernote:///view/73204695/s5/928ee3f8-40c7-a3d0-7ab971452551/928eef38-9121-40c7-a3d0-7ab971452551/" }
  ],
  "saved_searches": [
    { "name": "Launchbar Actions", "search": "\"Launchbar Actions\"" }
    { "name": "Notes with 'Launchbar' in title", "search": "intitle:\"Launchbar\"" },
    { "name": "Created yesterday or ealier", "search": "created:day-1" },
    { "name": "Note with todos", "search": "todo:*" },
  ]
}
```

### Configuration Settings

* `debug`: If `true` debug messages are logged to the Console `[default = false]`.
* `max_results`: The maximum number of results a search should return. Increasing this setting may have performance impacts `[default = 20]`.
* `favorite`: A list of favorite note `[default = []]`.

  The list elements consist of a name and the Evernote internal note link; cf. [Saved Searches](https://github.com/lukaspustina/Evernote.lbaction#saved-searches) on how to obtain a note link. See above for examples.
* `saved_searches`: A list of saved searches `[default = []]`.

  The list elements consist of a name and search query in Evernote's search grammar; cf. [Saved Searches](https://github.com/lukaspustina/Evernote.lbaction#saved-searches) for how to use the search grammar. It is important to note that every `"` as part of the search query needs to be escaped using `\`, i.e., `\"`. See above for examples.

Known Limitations
-----------------

1. This Action requires Evernote to run. If it is not running, any action will start it automatically, grabbing the focus. Thus, Lauchbar loses the focus and needs to be re-invoked.

Credits
-------

Icons are (C) by [Designerz Base](https://www.iconfinder.com/iconsets/faticons) licensed free for commercial use.

---

[🌐 原始链接](https://github.com/lukaspustina/Evernote.lbaction)

[📎 在印象笔记中打开](evernote:///view/207087/s1/65113b09-6012-438a-b840-d4abbe6dc1f1/65113b09-6012-438a-b840-d4abbe6dc1f1/)