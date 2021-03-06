rpiconf
=======

A GUI for editing Raspberry Pi config.txt file
Written int Python3 and Gtk+3

Download from:  
http://huulivoide.pp.fi/public/rpiconf

TODO:  
* Add gettext support and translate into Finnish. Also optimize layout to better fit translated strings.
* Implemet error handling (non writable filesystem...)
* Check tuning options' sanity, display a warning if value is too high/low
* Add the 86 new monitor modes XD
* Add HDMI force hotplug swich
* Add kernel tab for the new boot option settings.
* Add a commandline client too. (ncurses dialog)
* Add launcher to choose between gtk/ncurses, default to GTK is $SCREEN is set
* Add restore defaults button.

###License  
This piece of software is given to you under the following license  
Copyright (c) 2012, Jaara Jesse Juhani
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met: 

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer. 
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution. 

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
