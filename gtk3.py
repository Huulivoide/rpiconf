#!/usr/bin/python3
#I know most of you still prefer python2 and it is still more widle
#awaiable and installed by default, but I am a python starter. This is
#my fisrt real application ever, and I see no reason to learn something
#old that will wanish completely not in so faar future, instead I want
#to make sure I can put the skill I gain in use in the future easily.
#Same thing applys to the gtk3 too ^_^

#### Imports
### Backend
import sys
import os
import rpiconf
###Gui
##GTK+ 3.x
from gi.repository import Gtk
##What about ncurses and QT variants too? Turn this into a full fledged
##library on handling the config file.
####

##Helper variables
raw_hdmi_mode = ['AUTO', ''] #One for resolution, one for refreshrate
advanced = False
test = False
l2 = False
#When true use the unified gpu chip frequency changing
gpu_freq_uni = True
voltage_uni = True

###Load our dynamic widgets from the glade file to the current namespace
builder = Gtk.Builder()
builder.add_from_file("mainwindow.ui")
##Main and about windows
window = builder.get_object("mainwindow")
about = builder.get_object("aboutwindow")
##video_output
#Comboboxes
combo_analog = builder.get_object("combo_analog_format")
combo_aspectratio = builder.get_object("combo_aspectratio")
combo_digital_resolution = builder.get_object("combo_digital_resolution")
combo_refreshrate = builder.get_object("combo_refreshrate")
combo_power = builder.get_object("combo_power")
#spinbuttons
spin_overscan_top = builder.get_object("spin_overscan_top")
spin_overscan_bottom = builder.get_object("spin_overscan_bottom")
spin_overscan_left = builder.get_object("spin_overscan_left")
spin_overscan_right = builder.get_object("spin_overscan_right")
spin_fb_height = builder.get_object("spin_fb_height")
spin_fb_width = builder.get_object("spin_fb_width")
#Checkbutons
check_use_dvi = builder.get_object("check_use_dvi")
check_refreshrate = builder.get_object("check_refreshrate")
##Performance_tuning
#spinbuttons
spin_cpu = builder.get_object("spin_cpu")
spin_gpu = builder.get_object("spin_gpu")
spin_core = builder.get_object("spin_core")
spin_3d = builder.get_object("spin_3d")
spin_video = builder.get_object("spin_video")
spin_isp = builder.get_object("spin_isp")
spin_sdram = builder.get_object("spin_sdram")
spin_core_voltage = builder.get_object("spin_core_voltage")
spin_sdram_voltage = builder.get_object("spin_sdram_voltage")
spin_sdramc_voltage = builder.get_object("spin_sdramc_voltage")
spin_sdramp_voltage = builder.get_object("spin_sdramp_voltage")
spin_sdrami_voltage = builder.get_object("spin_sdrami_voltage")
#Checkbuttons
check_individual_gpu = builder.get_object("check_individual_gpu")
check_individual_voltage = builder.get_object("check_individual_voltage")
#Again assume only one radio button is needed from the group
check_l2 = builder.get_object ("check_l2")
check_test = builder.get_object("check_test")

config = rpiconf.rpi_config()

#Get the proper filename for our config file.
#Filename must ALWAYS be the last argument.
args = len(sys.argv)
if args > 1:
	config.get_configfile(sys.argv[args - 1])
else:
	config.get_configfile('')

#Read the config file into memory
config.read_config()

def ratelist_name(mode):
	global advanced
	if mode != "AUTO" and mode != "VGA":
		if advanced:
			list_name = "refreshrates_" + mode + "_advanced"
		else:
			list_name = "refreshrates_" + mode
		return list_name
	else:
		return ''

def populate_refreshrates(mode):
	# Set the refreshrate list to that of supported ones
	#Make 1st sure we are clean of the old ones
	combo_refreshrate.remove_all()
	list_name = ratelist_name(mode)
	if list_name != '':
		for rate in rpiconf.refreshrates[list_name]:
			combo_refreshrate.append_text(rate)

def set_refreshrate(resolution, refreshrate):
	list_name = ratelist_name(resolution)
	ratelist = rpiconf.refreshrates[list_name]
	populate_refreshrates(resolution)
	index = ratelist.index(refreshrate)
	combo_refreshrate.set_active(index)

def check_advanced(refreshrate):
	global advanced
	if "H" in refreshrate or "x" in refreshrate or "rb" in refreshrate:
		advanced = True
		check_refreshrate.set_active(True)

#Populate the config with all of the supported
#settings defined in our conf file
for option in rpiconf.options:
	if config.parser.has_option('dummy', option):
		value = int(config.parser.get('dummy', option))
		#I was told to be extreamly carefull with this, so I think it
		#is a bit dangerous way to do stuff. So Im more than happy
		#if someone tells me a more safer way to do this
		setattr(config , option, value)

	if getattr(config, option) != 0:
		if option == 'arm_freq':
			spin_cpu.set_value(value)
		elif option == 'gpu_freq':
			spin_gpu.set_value(value)
		elif option == 'sdram_freq':
			spin_sdram.set_value(value)

		elif option == 'core_freq':
			spin_core.set_value(value)
			check_individual_gpu.set_active(True)
			gpu_freq_uni = False
		elif option == 'h264_freq':
			spin_video.set_value(value)
			check_individual_gpu.set_active(True)
			gpu_freq_uni = False
		elif option == 'isp_freq':
			spin_isp.set_value(value)
			check_individual_gpu.set_active(True)
			gpu_freq_uni = False
		elif option == 'v3d_freq':
			spin_3d.set_value(value)
			check_individual_gpu.set_active(True)
			gpu_freq_uni = False

		elif option == 'over_voltage':
			spin_core_voltage.set_value(value)
		elif option == 'over_voltage_sdram':
			spin_sdram_voltage.set_value(value)

		elif option == 'over_voltage_sdram_c':
			spin_sdramc_voltage.set_value(value)
			check_individual_voltage.set_active(True)
			voltage_uni = False
		elif option == 'over_voltage_sdram_i':
			spin_sdrami_voltage.set_value(value)
			check_individual_voltage.set_active(True)
			voltage_uni = False
		elif option == 'over_voltage_sdram_p':
			spin_sdramp_voltage.set_value(value)
			check_individual_voltage.set_active(True)
			voltage_uni = False

		elif option == 'overscan_left':
			spin_overscan_left.set_value(value)
		elif option == 'overscan_right':
			spin_overscan_right.set_value(value)
		elif option == 'overscan_top':
			spin_overscan_top.set_value(value)
		elif option == 'overscan_bottom':
			spin_overscan_bottom.set_value(value)

		elif option == 'framebuffer_width':
			spin_fb_width.set_value(value)
		elif option == 'framebuffer_height':
			spin_fb_height.set_value(value)

		elif option == 'hdmi_mode':
			#We need to invert/flip the list of HDMI modes so that
			#instead of getting the numerical value of the mode with the
			#text, we can fecth the text/name of the mode with the value
			inverted_hdmi_modes = \
				dict([[v,k] for k,v in rpiconf.hdtv_modes.items()])
			mode_name = inverted_hdmi_modes[value]
			#split the mode_name into resolution and refreshrate.
			#mode_name format is RESO(i/p)REFRESHRATE, reso is 3/4 chars
			#long. See if 4th char is i or p at 1st.
			if mode_name[3:4] == 'i' or mode_name[3:4] == 'p':
				resolution = mode_name[:4]
				refreshrate = mode_name[4:]
				check_advanced(refreshrate)
				set_refreshrate(resolution, refreshrate)
			elif mode_name[4:5] == 'i' or mode_name[4:5] == 'p':
				resolution = mode_name[:5]
				refreshrate = mode_name[5:]
				check_advanced(refreshrate)
				set_refreshrate(resolution, refreshrate)
			else:
				resolution = 'VGA'
				
			index = rpiconf.hdtv_resolutions.index(resolution)
			combo_digital_resolution.set_active(index)
		elif option == 'hdmi_boost':
			combo_power.set_active(value)
		elif option == 'hdmi_drive':
			if value == 1:
				check_use_dvi.set_active(True)

		elif option == 'sdtv_mode':
			combo_analog.set_active(value)
		elif option == 'sdtv_aspect':
			combo_aspectratio.set_active(value -1)
			#aspectratio has values 1/2/3, -1 to make it mach with index

		elif option == 'test_mode':
			check_test.set_active(True)
			test = True
		elif option == 'enable_l2cache':
			check_l2.set_active(True)
			l2 = True
		

##Define what to do, when we get a signal from the main GTK loop
class Handler:
###Video options########################################################
	def on_sdtv_change(self, combo):
		config.sdtv_mode = rpiconf.sdtv_modes[combo.get_active_text()]
	def on_aspectratio_change(self, combo):
		config.sdtv_aspect = \
			rpiconf.aspectratios[combo.get_active_text()]

	def on_resolution_change(self, combo):
		raw_hdmi_mode[0] = combo.get_active_text()
		populate_refreshrates(raw_hdmi_mode[0])
	def on_check_refreshrate_toggled(self, button):
		global advanced
		advanced = not advanced
		populate_refreshrates(raw_hdmi_mode[0])
	def on_refreshrate_change(self, combo):
		raw_hdmi_mode[1] = combo.get_active_text()
	def on_drive_change(self, button):	
		if button.get_active() == True:
			config.hdmi_drive = 2
		else:
			config.hdmi_drive = 1

	def on_top_change(self, spin):
		config.overscan_top = spin.get_value_as_int()
	def on_bottom_change(self, spin):
		config.overscan_bottom = spin.get_value_as_int()
	def on_left_change(self, spin):
		config.overscan_left = spin.get_value_as_int()
	def on_right_change(self, spin):
		config.overscan_right = spin.get_value_as_int()

	def on_height_change(self, spin):
		config.framebuffer_height = spin.get_value_as_int()
	def on_width_change(sefl, spin):
		config.framebuffer_width = spin.get_value_as_int()

	def on_power_change(self, combo):
		if combo.get_active_text() == "DEFAULT":
			config.hdmi_boost = 0
		else:
			# Make sure we get the value as int and not str
			# I think this might not be needed, but to be sure (HELP!)
			config.hdmi_boost = int(combo.get_active_text())
###End Video Options###################################################
###Performance tuning options##########################################
	#Check the sanes of the values just before saving.
	def on_cpu_change(sefl, spin):
		config.arm_freq = spin.get_value_as_int()
	def on_gpu_change(sefl, spin):
		config.gpu_freq = spin.get_value_as_int()
	def on_sdram_change(sefl, spin):
		config.sdram_freq = spin.get_value_as_int()

	def on_core_change(sefl, spin):
		config.core_freq = spin.get_value_as_int()
	def on_video_change(sefl, spin):
		config.h264_freq = spin.get_value_as_int()
	def on_isp_change(sefl, spin):
		config.isp_freq = spin.get_value_as_int()
	def on_3d_change(sefl, spin):
		config.v3d_freq = spin.get_value_as_int()

	def on_individual_gpu_change(self, button):
		global gpu_freq_uni
		gpu_freq_uni = not button.get_active()
	def on_individual_voltage_change(self,button):
		global voltage_uni
		voltage_uni = not button.get_active()

	def on_core_voltage_change(sefl, spin):
		config.over_voltage = spin.get_value_as_int()
	def on_sdram_voltage_change(sefl, spin):
		config.over_voltage_sdram = spin.get_value_as_int()

	def on_sdramc_voltage_change(sefl, spin):
		config.over_voltage_sdram_c = spin.get_value_as_int()
	def on_sdramp_voltage_change(sefl, spin):
		config.over_voltage_sdram_p = spin.get_value_as_int()
	def on_sdrami_voltage_change(sefl, spin):
		config.over_voltage_sdram_i = spin.get_value_as_int()

	def on_test_change(self, button):
		global test
		test = not test
		if test:
			config.test_mode = 1
		else:
			config.test_mode = 0	
	def on_l2_change(self, button):
		global l2
		l2 = not l2
		if l2:
			config.enable_l2cache = 1
		else:
			config.enable_l2cache = 0
###End Performance tuning options######################################
	def onDeleteWindow(self, *args):
		Gtk.main_quit(*args)
	def on_show_about(self, window):
		about.show_all()
	def on_about_close(sefl, window, name):
		about.hide()

	def on_save(self, menu):
		config.overscan_state()
		config.use_unified_freq(gpu_freq_uni)
		config.use_unified_voltages(voltage_uni)

		config.translate_hdmi_mode(raw_hdmi_mode)
		for option in rpiconf.options:
			config.include_option(option)

		file = open(config.configfile, 'w')
		file.write(config.generated_config)
		file.close()


builder.connect_signals(Handler())
window.show_all()
Gtk.main()
