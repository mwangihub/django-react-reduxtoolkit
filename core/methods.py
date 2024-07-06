"""
methods.py have simple functions that reduce the code reputation
TODO: get_current_site to be used in deployment
For this case domain was attached to different instances to mimic dynamics of domain name changes
"""

from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


# Sub methods
def get_rendered_html(template_name, context={}):
    """
    The get_rendered_html function accepts a template name and context,
    and returns the rendered HTML of that template.
    :param template_name: Specify the name of the template file to be rendered
    :param context={}: Pass in the dictionary of values that will be available to the template
    :return: The rendered html content of the template
    """
    html_content = render_to_string(template_name, context)
    return html_content


# Exported methods
def send_email(
    subject,
    html_content,
    text_content=None,
    from_email=None,
    recipients=[],
    attachments=[],
    bcc=[],
    cc=[],
):
    """
    The send_email function sends an email to a user with a list of attachments.
    :param subject: Set the subject of the email
    :param html_content: Send html emails
    :param text_content: Specify the plain text version of an email
    :param from_email: Specify the email address that appears in the from: header for this email
    :param recipients: Specify the recipients of the email
    :param attachments: Attach files to the email
    :param bcc: Specify a list of recipients who will receive the email, but not visible to them
    :param cc: Specify any recipients in the &quot;carbon copy&quot; of the email
    :return: None

    """
    # send email to user with attachment
    if not from_email:
        from_email = settings.DEFAULT_FROM_EMAIL
    if not text_content:
        text_content = ""
    email = EmailMultiAlternatives(
        subject, text_content, from_email, recipients, bcc=bcc, cc=cc
    )
    email.attach_alternative(html_content, "text/html")
    for attachment in attachments:
        # Example: email.attach('design.png', img_data, 'image/png')
        email.attach(*attachment)
    email.send()


def send_mass_mail(data_list):
    """
    The send_mass_mail function accepts a list of dictionaries, each containing a template and context.
    The function then loops through the list, rendering HTML from each template using the provided context.
    Finally, it uses the EmailMultiAlternatives function to send each message to its recipient.
    :param data_list: Pass a list of dictionaries to the send_mass_mail function
    :return: A list of the sent email messages

    """
    for data in data_list:
        template = data.pop("template")
        context = data.pop("context")
        html_content = get_rendered_html(template, context)
        data.update({"html_content": html_content})
        send_email(**data)
