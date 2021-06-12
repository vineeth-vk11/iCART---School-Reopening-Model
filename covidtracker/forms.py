from django import forms


class inputform(forms.Form):
    student_no = forms.IntegerField(widget=forms. NumberInput(
        attrs={'type': 'number', 'class': 'form-control', 'id': 'student', 'placeholder': '1000'}))
    student_age_limit = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'text', 'class': 'js-range-slider', 'id': 'std', 'name': 'my_range', 'value': ''}), max_length=100)
    teacher_no = forms.IntegerField(widget=forms. NumberInput(
        attrs={'type': 'number', 'class': 'form-control', 'id': 'teacher', 'placeholder': '200'}))
    teacher_age_limit = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'text', 'class': 'js-range-slider', 'id': 't', 'name': 'my_range', 'value': ''}),  max_length=100)
    non_teacher_no = forms.IntegerField(widget=forms. NumberInput(
        attrs={'type': 'number', 'class': 'form-control', 'id': 'nonteacher', 'placeholder': '100'}))
    non_teacher_age_limit = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'text', 'class': 'js-range-slider', 'id': 'nt', 'name': 'my_range', 'value': ''}),  max_length=100)
    batch_size = forms.IntegerField(widget=forms. NumberInput(
        attrs={'type': 'number', 'class': 'form-control', 'id': 'batch', 'placeholder': '230'}))
    infection = forms.FloatField(widget=forms. NumberInput(
        attrs={'type': 'number', 'class': 'form-control', 'id': 'infection', 'placeholder': '0.05'}))
    sensitivity = forms.FloatField(widget=forms. NumberInput(
        attrs={'type': 'number', 'class': 'form-control', 'id': 'sensitivity', 'placeholder': '0.6'}))
    specificity = forms.FloatField(widget=forms. NumberInput(
        attrs={'type': 'number', 'class': 'form-control', 'id': 'specificity', 'placeholder': '0.98'}))
