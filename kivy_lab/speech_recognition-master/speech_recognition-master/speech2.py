#:kivy 1.0.9

<Root>:
    orientation: 'vertical'
    RecordButton:
        id: record_button
        text: 'Start'
        on_release: self.record()
        height: '50dp'
        size_hint_y: None

    TextInput:
        text: record_button.output
        readonly: True
    Label:
        id: stopwatch
        text: '00:00.[size=40]00[/size]'




