from  django import forms
from User.models import UserRegister
class UserRegisterForm(forms.ModelForm):
    Name = forms.CharField(widget=forms.TextInput(attrs={ 'pattern' : '[a-zA-Z]+',
                                                         'class' : 'form-control'}),
                                                          max_length=30, required=True)
    
    User_Name = forms.CharField(widget=forms.TextInput(attrs={'pattern' : '[a-zA-Z]+' ,
                                                              'class': 'formcontrol'})
                                                               , max_length=30 , required=True)
    
    Pass_Word = forms.CharField(widget=forms.PasswordInput(attrs={ 'pattern':'(?=.*\d)(?=.[a-z])(?=.*[A-Z]).{8,}',
                                        'ttitle' : 'Must contain at least one number and one uppercase and lowercase letter,and at least 8 or more characters' ,
                                        'class' :'formcontrol'}), 
                                          max_length=30, required=True )
    Mobile_No = forms.CharField(widget=forms.TextInput(attrs={'pattern' : '[56789][0-9]{9}' ,
                                                              'class' :'formcontrol'}),
                                                               max_length=30 , required=True)
    Maid_Id = forms.CharField(widget=forms.TextInput(attrs={'pattern' : '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$', 
                                                            'class' :'formcontrol'}), 
                                                             max_length=30 , required=True)
    Locality = forms.CharField(widget=forms.TextInput(attrs={'class': 'formcontrol'}),
                                                                max_length=30 , required=True)
    Address = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols': 22,'class':'form-control'}),
                                                              max_length=30 , required=True)
    City =  forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off',
                                                          'class':'form-control',
                                                          'pattern':'[A-Za-z ]+', 
                                                          'title':'Enter Characters Only '}),
                                                           max_length=30 , required=True)
    State = forms.CharField(widget=forms.TextInput(attrs={'autocomplete' :'off' , 
                                                          'class' :'formcontrol'}),
                                                            required=True , max_length=30)
    Status = forms.CharField(widget=forms.HiddenInput({'calss' : 'formcontrol'}),
                                                        initial='waiting' , max_length=30)
    
    class Meta():
        model = UserRegister
        fields = '__all__'
        
