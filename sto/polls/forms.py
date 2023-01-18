from django import forms

REMO_CHOICES = [
    ("1", "Ремонт подвески"),
    ("2", "Ремонт двигателя"),
    ("3", "Ремонт выхлопной системы"),
    ("4", "Ремонт рулевого управления"),
    ("5", "Ремонт системы охлаждения"),
    ("6", "Ремонт тормозной системы"),
    ("7", "Ремонт электрооборудования"),
    ("8", "Ремонт МКПП"),
    ("9", "Ремонт AКПП")
]

class RemontAvtoForm(forms.Form):
    remont = forms.CharField(max_length=200)
    vid_remonta = forms.CharField(
        max_length=200,
        widget=forms.Select(choices=REMO_CHOICES),
    )
    repair_description_avto = forms.Textarea()