from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.html import escape

from app.models import Client


# Create your views here.
def index(request):
    return render(request, 'index.html')


def user(request, client_nickname):
    client = Client.objects.get(nickname=client_nickname)
    buttons = client.button_set.all()
    context = {
        'client': client,
        'buttons': buttons
    }
    return render(request, 'user.html', context)


def generate_vcard(request, client_nickname):
    client = Client.objects.get(nickname=client_nickname)
    buttons = client.button_set.all()

    # Generate vCard content
    btns = ""

    for btn in buttons:
        btns += f"URL;TYPE={escape(btn.text)}:{escape(btn.link)}\n"

    vcard_content = f"BEGIN:VCARD\n" \
                    f"VERSION:3.0\n" \
                    f"N:{escape(client.fullname)}\n" \
                    f"FN:{escape(client.fullname)}\n" \
                    f"NICKNAME:{escape(client.nickname)}\n" \
                    f"TITLE:{escape(client.title)}\n" \
                    f"ORG:{escape(client.organization)}\n" \
                    f"BDAY:{client.dob}\n" \
                    f"TEL;TYPE=WORK,VOICE:{client.phone}\n" \
                    f"EMAIL;TYPE=PREF,INTERNET:{client.email}\n" \

    if client.avatar:
        # encode image to base64 and add to vcard content
        import base64
        with open(client.avatar.path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            vcard_content += f"PHOTO;ENCODING=b;TYPE=JPEG:{encoded_string.decode('utf-8')}\n"

    if btns:
        vcard_content += f"{btns}"

    vcard_content += f"REV:{datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')}\n"
    vcard_content += f"END:VCARD"

    # Create an HttpResponse with vCard content
    response = HttpResponse(vcard_content, content_type='text/vcard')

    # Set content disposition to trigger download
    response['Content-Disposition'] = f'attachment; filename="{client.nickname}_vcard.vcf"'

    return response
