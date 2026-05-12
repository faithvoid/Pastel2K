# Pastel2K
A series of Redmond97-based themes for XFCE4. 

Intended to eventually be used as the aesthetic basis of "[9xOS](https://github.com/faithvoid/9xos)", a retro PC gaming OS for the Raspberry Pi, but works for all *nix distros as long as they can run XFCE4!

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/donate/?cmd=_s-xclick&hosted_button_id=8GF4A3XS7ZHFY)

# Installation:
Copy your theme of choice to the ".themes" folder in your local user directory (if the directory does not exist, make it and then move the theme into it!). If using a matching icon & cursor set from "icons", copy the files into the ".icons" folder of your home directory.

If the theme does not exist in the Releases but exists in the "conf" section, you can use "gen_theme.sh" in the "tools" section to build and install it yourself! Make sure to replace the default "theme.conf" with the .conf file of your choosing.

To convert your own Windows 9x/2K themes to Pastel2K standards, you can use "theme2conf.py" in "tools" by running "python theme2conf.py ThemeName.theme" (with ThemeName.theme being your Windows theme), which will automatically output a near 1:1 Pastel2K theme file to apply. Please note that this utility is still very barebones, as I'm hoping to add automatic cursor, wallpaper and sound theme conversion and naming support so installing the entirety of a Windows theme is a simple as possible.

# Recommended:
#### Icons:

- [98SE](https://github.com/nestoris/Win98SE) - Windows 98 style icons

- [NineIcons-Redux](https://www.opencode.net/aitees/nineicons-redux) - macOS 9 style icons (pairs well with Pastel97-Dracula, Pastel97-Lavender & Pastel97-Solaris)

#### Fonts:
- Tahoma / Sans Regular (system-wide)

- Less Perfect DOS VGA / More Perfect DOS VGA (terminal)

# Themes
## Pastel2K-Dracula
A theme based off of the Dracula colour palette. Use "Dracula-Alt" if you want a purple titlebar!
![Dracula](/images/dracula1.png)

## Pastel2K-Dracula-Alt
Alternate Dracula theme, has a purple titlebar!
![Dracula](/images/dracula2.png)

## Pastel2K-Kokoro
A dark lilac theme. 
![Kokoro](/images/kokoro1.png)

## Pastel2K-Lavender
A light lavender theme. 
![Lavender](/images/lavender.png)

## Pastel2K-Zaytun
An Olive-based theme. Named after the Arabic word for "olive tree". 
![Zaytun](/images/zaytun1.png)

## Pastel2K-Alexandria
A Zune-inspired theme. Named after the internal codename for Zune Marketplace. 
![Alexandria](/images/alexandria1.png)

## Pastel2K-PerfectBlue
An Embedded-based theme.
![Perfect Blue](/images/perfectblue1.png)

## Pastel2K-Evanescence
A theme centered around the colourscheme of Evanescence's album "Fallen".
![Evanescence](/images/evanescence.png)

## Pastel2K-CDE
A Common Desktop Environment-based theme. 
![CDE](/images/cde1.png)

## Pastel2K-Solaris
An alternate Common Desktop Environment-based theme. 
![Solaris](/images/solaris1.png)

## Pastel2K-RawrMeansILY
Y2K scene-inspired theme. Don't take this one too seriously.
![Rawr](/images/RawrMeansILY.png)

## Pastel2K-Vaio
Vaio theme, cloned from the Vaio themeset on Internet Archive.
![Vaio](/images/vaio.png)

## Pastel2K-Springfield
Simpsons theme, cloned from the Simpsons theme on Internet Archive.
![Vaio](/images/springfield.png)

## Pastel2K-Reki
Reki theme, cloned from the Haibane Renmei theme on Internet Archive.
![Reki](/images/reki.png)

## Pastel2K-Rakka
Rakka theme, cloned from the Haibane Renmei theme on Internet Archive.
![Rakka](/images/rakka.png)

## Pastel2K-Angel
Angel theme, cloned from the Haibane Renmei theme on Internet Archive.
![Angel](/images/angel.png)




### Roadmap
- [ ] Create Windows 9X / 2000 .theme to .conf conversion utility in Python
- [ ] Create Windows 9X / 2000 .theme icon / sound theme conversion utility in Python
- [ ] Create a basic tool for editing and previewing themes in Tkinter or PyQT(?)
- [ ] Create additional themes, organize theme folders with their original wallpapers, sounds, cursors, etc, all converted to Linux standards.
