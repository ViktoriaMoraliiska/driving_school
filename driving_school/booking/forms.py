from django import forms
from django.core.mail import send_mail

from driving_school import settings
from driving_school.booking.models import BookingModel


class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingModel
        fields = '__all__'

    def get_info(self):
        cl_data = super().clean()

        f_name = cl_data.get('first_name').strip()
        l_name = cl_data.get('last_name').strip()
        phone = cl_data.get('phone_number')
        from_email = cl_data.get('email')
        text = cl_data.get('text_message')
        week_day = cl_data.get('week_schedule')
        hour = cl_data.get('hour_schedule')

        msg = f'{f_name} {l_name} with email - {from_email} and phone number - {phone} said:'
        msg += f"\n I would like to book an appointment for this week on {week_day} for {hour}"
        msg += f"\n Text message: {text}"
        # msg += cl_data.get('text_message')

        return text, msg, from_email

    def send(self):
        text, msg, from_email = self.get_info()

        send_mail(
            subject=text,
            message=msg,
            from_email=from_email,
            recipient_list=[settings.RECIPIENT_ADDRESS]
        )