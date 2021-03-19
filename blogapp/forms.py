from django import forms


class FileForm(forms.Form):
    source_name = forms.CharField(max_length=20)
    source_file = forms.CharField(max_length=20)

    def __str__(self):
        return f"{self.comment_text} by {self.your_name}"

#
# class SearchForm(forms.Form):
#     title = forms.CharField(max_length=20)
#
