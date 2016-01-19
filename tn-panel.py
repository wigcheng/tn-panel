#!/usr/bin/env python


import pygtk
pygtk.require('2.0')
import gtk
import subprocess
import os


class tn_panel:

    module_name=""

    def set_value(self, widget):
	os.system("alsamixergui")	

    def save_audio(self, widget, combobox,label2):
        model = combobox.get_model()
        index = combobox.get_active()
	proc = subprocess.Popen(['/home/ubuntu/tn/tn_audio_save',module_name,model[index][0]], stdout=subprocess.PIPE)
	(out, err) = proc.communicate()
	proc = subprocess.Popen(['/home/ubuntu/tn/tn_audio',module_name], stdout=subprocess.PIPE)
	(out, err) = proc.communicate()
        label2.set_text("Current:" +out)


    def changed_cb(self, combobox, label):
	global module_name
        model = combobox.get_model()
        index = combobox.get_active()
    	module_name=model[index][0]
	proc = subprocess.Popen(['/home/ubuntu/tn/tn_audio',model[index][0]], stdout=subprocess.PIPE)
	(out, err) = proc.communicate()
        label.set_text("Current:" +out)


    def __init__(self):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.connect("destroy", lambda w: gtk.main_quit())
        window.set_title("Audio")

        main_vbox = gtk.VBox(False, 5)
        main_vbox.set_border_width(1)
        window.add(main_vbox)


        frame = gtk.Frame("Audio Device")
        main_vbox.pack_start(frame, True, True, 0)
        vbox = gtk.VBox(False, 0)
        vbox.set_border_width(5)
        frame.add(vbox)
  
        hbox = gtk.HBox(False, 0)
        vbox.pack_start(hbox, False, True, 5)
  
        vbox2 = gtk.VBox(False, 0)
        hbox.pack_start(vbox2, True, True, 5)
  
	combo_tn_audio = gtk.combo_box_new_text()
	combo_tn_audio.append_text("HDMI-AUDIO")
	combo_tn_audio.append_text("SPDIF")
	combo_tn_audio.append_text("SGTL5000")
	#combo_tn_audio.connect('changed', self.changed_cb)
 	combo_tn_audio.set_active(0)
        vbox2.pack_start(combo_tn_audio, False, True, 0)

        val_label = gtk.Label("")
        btn_audio_save = gtk.Button("Save Setting")
        btn_audio_save.connect("clicked", self.save_audio,combo_tn_audio,val_label)
        vbox2.pack_start(btn_audio_save, True, True, 5)
        vbox2.pack_start(val_label, True, True, 0)


        frame = gtk.Frame("Audio Config")
        main_vbox.pack_start(frame, True, True, 0)
  
        vbox = gtk.VBox(False, 0)
        vbox.set_border_width(5)
        frame.add(vbox)

        hbox = gtk.HBox(False, 0)
        vbox.pack_start(hbox, True, True, 5)
  
        vbox2 = gtk.VBox(False, 0)
        hbox.pack_start(vbox2, True, True, 5)

	combo_tn_cpu = gtk.combo_box_new_text()
	combo_tn_cpu.append_text("WANDBOARD")
	combo_tn_cpu.append_text('EDM1-CF-IMX6')
	combo_tn_cpu.append_text('PICOSOM-IMX6')
	combo_tn_cpu.append_text('EDM1-CF-IMX6SX')
	combo_tn_cpu.append_text('PICOSOM-IMX6UL')
	combo_tn_cpu.append_text('PICOSOM-IMX7')

	combo_tn_cpu.connect('changed', self.changed_cb,val_label)

	proc = subprocess.Popen(['/home/ubuntu/tn/detect_module'], stdout=subprocess.PIPE)
        (out, err) = proc.communicate()
 	combo_tn_cpu.set_active(int(out))
        vbox2.pack_start(combo_tn_cpu, True, True, 0)

        btn_run = gtk.Button("Volume")
        btn_run.connect("clicked", self.set_value)
        vbox2.pack_start(btn_run, True, False, 5)

        #val_label.set_text("0")
  
        hbox = gtk.HBox(False, 0)
        main_vbox.pack_start(hbox, False, True, 0)
  
        button = gtk.Button("Close")
        button.connect("clicked", lambda w: gtk.main_quit())
        hbox.pack_start(button, True, True, 5)
        window.show_all()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    tn_panel()
    main()

