rpiconf
=======

A GUI for editing Raspberry Pi config.txt file
Written int Python3 and Gtk+3

This is still a work in progress and cannot generate fail-proof config files.
All of the elements in the video output settings page have been connected to
the code, so changing their values will lead to a change in out config
object which holds the settings.

TODO:    
* Connect the overclocking page elements into the code.  
* Implement code to only allow global gpu freq/voltage or individual ones.  
* Implement file saving to a custom file.
* Implement the filesaving dialogues.
* Try to preload the existing values into their places.  
* Add gettext support and translate into Finnish. Also optimize layout to better fit translated strings.

###CONTRIBUTOR:  
If you want to contribute code to this project, please try to  
avoid super optimized and expert code (if such exist) I want to keep this  
simple so even beginners can easily get a hang of what is going on, it is  
for the RPi after all.

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
