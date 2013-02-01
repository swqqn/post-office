from django.core.mail import EmailMultiAlternatives, get_connection
from django.utils.encoding import force_unicode

from .cache import set_cache, get_cache
from .models import Email, PRIORITY, STATUS, EmailTemplate
from .settings import get_email_backend


def send_mail(subject, message, from_email, recipient_list, html_message='',
              priority=PRIORITY.medium):
    """
    Add a new message to the mail queue.

    This is a replacement for Django's ``send_mail`` core email method.

    The `fail_silently``, ``auth_user`` and ``auth_password`` arguments are
    only provided to match the signature of the emulated function. These
    arguments are not used.
    """

    subject = force_unicode(subject)
    # Turn the input to django's email object to check for failures
    msg = EmailMultiAlternatives(subject, message, from_email,
                                 recipient_list)
    status = None if priority == PRIORITY.now else STATUS.queued

    for address in recipient_list:
        email = Email.objects.create(from_email=from_email, to=address, subject=subject,
            message=message, html_message=html_message, status=status, priority=priority)
        if priority == PRIORITY.now:
            email.dispatch()


def send_queued_mail():
    """
    Sends out all queued mails
    """
    sent_count = 0
    failed_count = 0
    queued_emails = Email.objects.filter(status=STATUS.queued).order_by('-priority')

    if queued_emails:

        # Try to open a connection, if we can't just pass in None as connection
        try:
            connection = get_connection(get_email_backend())
            connection.open()
        except Exception, error:
            connection = None

        for mail in queued_emails:
            status = mail.dispatch(connection)
            if status == STATUS.sent:
                sent_count += 1
            else:
                failed_count += 1
        if connection:
            connection.close()
    print '{0} emails attempted, {1} sent, {2} failed'.format(len(queued_emails),
                                                              sent_count, failed_count)


def send_templated_mail(template_name, context, from_address, to_addresses, priority):
    email_template = get_email_template(template_name)
    message = email_template.create_email(from_address, to_addresses, context_instance=context)
    status = None if priority == PRIORITY.now else STATUS.queued

    for address in to_addresses:
        email = Email.objects.create(from_email=from_address, to=address, subject=email_template.subject,
            message=message, html_message=html_message, status=status, priority=priority)
        if priority == PRIORITY.now:
            email.dispatch()
    pass


def get_email_template(name):
    """
    Function to get email template object that checks from cache first
    """
    email_template = get_cache(name)
    if email_template is not None:
        return email_template
    else:
        email_template = EmailTemplate.objects.get(name=name)
        set_cache(name, email_template)
        return email_template
