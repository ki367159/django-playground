from django import forms


class BmiForm(forms.Form):
    h = forms.FloatField(min_value=1, label='身高')
    w = forms.FloatField(min_value=1, label='體重')

class DeleteConfirmForm(forms.Form):
    check = forms.BooleanField(label='你確定要刪除嗎？')