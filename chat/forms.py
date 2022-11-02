from django import forms


class MessageForm(forms.Form):
    pesan = forms.CharField(label="message", max_length=256, min_length=1)
    cid = forms.IntegerField()
