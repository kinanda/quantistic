from django import forms

class ProjectForm(forms.Form):
    project_name = forms.CharField(
        label='Project Name',
        max_length=64,
        widget=forms.TextInput(attrs={'placeholder': 'Untitled Project'})
    )
    project_path = forms.CharField(
        widget=forms.HiddenInput(),
        label='Project Path',
        max_length=64,
        initial='0'
    )


class SamplingProjectForm(forms.Form):
    project_name = forms.CharField(
        label='Project Name',
        max_length=64,
        widget=forms.TextInput(attrs={'placeholder': 'Untitled Project'})
    )
    project_path = forms.CharField(
        widget=forms.HiddenInput(),
        label='Project Path',
        max_length=64,
        initial='0'
    )
