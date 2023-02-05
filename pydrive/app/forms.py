from django import forms

class ScrapForm(forms.Form):
    username = forms.CharField(max_length=50)

class CombinedForm(forms.Form):
    facebook_un= forms.CharField(max_length=50, required=False)
    twitter_un= forms.CharField(max_length=50, required=False)
    github_un= forms.CharField(max_length=50, required=False)
    instagram_un= forms.CharField(max_length=50, required=False)
    linkedin_un= forms.CharField(max_length=50, required=False)
    quora_un= forms.CharField(max_length=50, required=False)
    medium_un= forms.CharField(max_length=50, required=False)
    pinterest_un= forms.CharField(max_length=50,required=False)