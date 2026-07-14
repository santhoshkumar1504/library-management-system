from django import forms


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class UpdateProfileForm(forms.Form):

    first_name = forms.CharField(max_length=100)

    last_name = forms.CharField(max_length=100)

    email = forms.EmailField()

    phone = forms.CharField(max_length=15, required=False)

    address = forms.CharField(
        widget=forms.Textarea,
        required=False
    )

    city = forms.CharField(max_length=100, required=False)

    state = forms.CharField(max_length=100, required=False)

    pincode = forms.CharField(max_length=10, required=False)

    profile_image = forms.ImageField(required=False)


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput)

    new_password = forms.CharField(widget=forms.PasswordInput)


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField()


class ResetPasswordForm(forms.Form):
    username = forms.CharField(max_length=100)

    new_password = forms.CharField(widget=forms.PasswordInput)
    