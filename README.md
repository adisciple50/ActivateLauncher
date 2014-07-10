ActivateLauncher
================

A windows 8 fullscreen launcher
clone, with extra features and 
different launcher shapes
to avoid being sued

Basicly its going to be an artistic spinoff of the windows 8 menu. starting with squares and rectangles,
but with extra shapes coming later to avoid copyright infringement later on.
 
nods to microsoft. well integrate hotmail AND google if you dont sue us. both can be enabled and disabled.
 
its going to be totally open, with the freedom to program your own widgets in pygame,
and to use any data source you want.
 
im doing one for the portfolio rather than for profit.
 
i have no idea what the compiz fusion guys are doing right now but, integration would give some kickass gpu powered effects.
 
 
but
 
__Design Principles__
*design for touch, cause right click is a luxury.
*we can do what we want! thus we can set the launcher to scroll vertically AND horizontally. there. touch vs mouse war, ended.
*make it modular. like dbus? great! youll like this. we can multi-thread the live tiles to be spread across several cores.
*make widgets independent.
* oh yes, don't forget the music visualizer background.. are you seeing this ms? ive wanted this, cause i miss doing so much acid and mushrooms.
 
*in case of bad planning, use a function button instead of right click.
*sidebars; use only to solve the right click button. further discussion needed.
 
__File and Folder List__
 
this is a my first pygame project. so feel free to water this stub.
 
Root(./) .. This contains the menu script, the other folders and resource subfolders.
L Activate.Py .. this is the main lauuncher file, whos job it is to provide a unified look for all the widgets and list programs.
L Widgets .. each one is (at the moment) going to be a standalone pygame package to run on a shape in the launcher
L Resources .. images and sounds for Activate.py that is not given from the user.
    L ThemeInstructions.txt
    L [ResourceFolder] (one folder for every theme.) theme instructions coming soon
L Dev .. Dump of usefull scripts to help you develope apps.
