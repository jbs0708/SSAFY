from django import forms
from .models import Menu


class MenuForm(forms.ModelForm):
    # name = forms.CharField(
    #     widget = forms.TextInput(
    #         attrs = {
    #             'placeholder' : '메뉴 이름을 작성해 주세요.',
    #         }
    #     )
    # )

    # description = forms.CharField(
    #     widget = forms.TextInput(
    #         attrs = {
    #             'placeholder' : '메뉴 설명을 작성해 주세요.',
    #         }
    #     )
    # )

    class Meta:
        model = Menu
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(
                attrs={
                    # CDN을 이용한 디자인 활용
                    'class': 'form-control',
                    'placeholder': '메뉴 이름을 작성해 주세요.'
                    }
                ),
            'description': forms.Textarea(
                attrs={
                    # CDN을 이용한 디자인 활용
                    'class': 'form-control',
                    'placeholder': '메뉴 설명을 작성해 주세요.'
                    }
                ),
            # CDN을 이용한 디자인 활용
            'is_vegan': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
        }