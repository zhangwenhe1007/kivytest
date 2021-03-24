#!/usr/bin/python3

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.dialog import MDDialog
from jnius import autoclass

Environment = autoclass('android.os.Environment')
MediaRecorder = autoclass('android.media.MediaRecorder')
AudioSource = autoclass('android.media.MediaRecorder$AudioSource')
OutputFormat = autoclass('android.media.MediaRecorder$OutputFormat')
AudioEncoder = autoclass('android.media.MediaRecorder$AudioEncoder')
storage_path = (Environment.getExternalStorageDirectory().getAbsolutePath() + '/kivy_recording.mp3')

class Alerte_Anti_Arnaqueurs(MDApp):

    recorder = MediaRecorder()

    def init_recorder(self):
        self.recorder.setAudioSource(AudioSource.VOICE_CALL)
        self.recorder.setOutputFormat(OutputFormat.DEFAULT)
        self.recorder.setAudioEncoder(AudioEncoder.AMR_NB)
        self.recorder.setOutputFile(storage_path)
        self.recorder.prepare()

    def build(self):

        self.isrecording = False

        self.theme_cls.primary_palette = 'Green'
        screen = Screen()
        icon_record = MDFloatingActionButton(icon='microphone',
                                             pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                             size_hint_x=None,
                                             on_press=self.get_voice)

        screen.add_widget(icon_record)
        return screen

    def get_voice(self, obj):
        if self.isrecording:
            self.recorder.stop()
            self.recorder.reset()
            self.isrecording = False
            close1_btn = MDFlatButton(text='Close', on_release=self.close_dialog)
            self.dialog = MDDialog(title='Verification', text='Stop recording', size_hint=(0.7, 1), buttons=[close1_btn])
            self.dialog.open()
        else:
            self.init_recorder()
            self.recorder.start()
            self.isrecording = True
            close1_btn = MDFlatButton(text='Close', on_release=self.close_dialog)
            self.dialog = MDDialog(title='Verification', text='Start recording', size_hint=(0.7, 1),
                                   buttons=[close1_btn])
            self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

Alerte_Anti_Arnaqueurs().run()